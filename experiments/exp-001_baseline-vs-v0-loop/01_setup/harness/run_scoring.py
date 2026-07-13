"""run_scoring.py — orchestrate scoring of an experiment (quantification.md §4).

Consumes a run-manifest (questions × arms × runs, each an answer text), scores every
answer through the pure core, runs an Elo tournament across arms per question, and
emits a scorecard (JSON + CSV rows). Works in --dry-run (offline stubs) or real mode.

Usage (dry-run, offline):
    python run_scoring.py --dry-run --answers answers.example.json --rubric rubric.json --out out/

Real mode is invoked from inside a CS session where `host` is available (see README).
"""
import argparse
import csv
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scoring import novelty as novmod, citations as citmod, judge as judgemod, composite as compmod, elo as elomod
from scoring import citation_quality as cqmod
from scoring import trace_verify as tvmod
from scoring.extract import extract_entities, extract_dataset_ids


def resolve_datasets(text, resolver_fn):
    """LB-075 grounding-integrity: extract dataset/DB accessions, resolve each (does it exist?),
    and check it was actually USED (a number/result derived from it), not just name-dropped.
    resolver_fn(id, db)->{'exists':bool,'used':bool} (injected; dry-run stubs it). Returns a
    summary dict or None when no dataset IDs are present."""
    ids = extract_dataset_ids(text)
    if not ids:
        return None
    recs, used_ok = [], 0
    for d in ids:
        r = (resolver_fn(d["id"], d["db"]) if resolver_fn else {"exists": True, "used": True}) or {}
        ok = bool(r.get("exists")) and bool(r.get("used"))
        used_ok += 1 if ok else 0
        recs.append({**d, "exists": bool(r.get("exists")), "used": bool(r.get("used"))})
    n = len(ids)
    return {"n_dataset_ids": n, "used_and_resolved": used_ok,
            "used_and_resolved_rate": round(used_ok / n, 3), "records": recs}


def nearest_sentence_claims_map(answer_text):
    """Return a fn: citation_raw -> the sentence it sits in (for entailment)."""
    sents = re.split(r"(?<=[.!?])\s+", answer_text)
    def m(raw):
        for s in sents:
            if raw in s:
                return s.strip()
        return None
    return m


def score_one_answer(answer_text, question, adapters, weights, tight_query=None, process_trace=None):
    """Full pipeline for a single answer."""
    ents = extract_entities(answer_text)
    nov = novmod.novelty_score(answer_text, adapters.retrieval_fn, tight_query=tight_query or question)
    cver = citmod.verify_citations(answer_text, nearest_sentence_claims_map(answer_text),
                                   adapters.resolver_fn, adapters.entailment_fn)
    # LB-075 grounding-integrity feeds: dataset-ID resolution + process_trace action verification
    dsres = resolve_datasets(answer_text, getattr(adapters, "dataset_resolver_fn", None))
    tvres = tvmod.verify_trace(process_trace, getattr(adapters, "trace_recheck_fn", None)) if process_trace else None
    cqual = None
    if hasattr(adapters, "metadata_fn"):
        cqual = cqmod.score_citation_quality(cver["records"], adapters.metadata_fn,
                                             n_major_claims=ents["counts"]["total"] or None)
    judge_fn = adapters.make_judge_fn()
    rub = judgemod.run_rubric_panel(answer_text, question, judge_fn)
    crea = judgemod.run_creativity_panel(answer_text, judge_fn)
    row = compmod.score_answer(question=question, rubric_result=rub, citation_result=cver,
                               entity_result=ents, novelty_result=nov, creativity_panel=crea,
                               weights=weights, dataset_result=dsres, trace_result=tvres)
    row["_novelty"] = nov
    if cqual is not None:
        row["citation_quality"] = {k: v for k, v in cqual.items() if k != "per_citation"}
        row["_citation_quality_detail"] = cqual
    return row


def run_experiment(manifest, adapters, rubric_path, out_dir):
    """manifest: {"questions":[{"id","text","tight_query"?}],
                  "answers":[{"question_id","arm","run","text"}]}"""
    os.makedirs(out_dir, exist_ok=True)
    weights = compmod.load_weights(rubric_path)
    qmap = {q["id"]: q for q in manifest["questions"]}
    rows = []
    for ans in manifest["answers"]:
        q = qmap[ans["question_id"]]
        row = score_one_answer(ans["text"], q["text"], adapters, weights,
                               tight_query=q.get("tight_query"),
                               process_trace=ans.get("process_trace"))
        row.update({"question_id": ans["question_id"], "arm": ans["arm"], "run": ans.get("run", 1),
                    "category": q.get("category"), "code": ans.get("code")})
        rows.append(row)

    # Elo per question across arms (use run 1 of each arm)
    elo_by_q = {}
    for qid, q in qmap.items():
        entries = {f"{a['arm']}#{a.get('run',1)}": a["text"]
                   for a in manifest["answers"] if a["question_id"] == qid}
        if len(entries) >= 2:
            elo_by_q[qid] = elomod.run_tournament(entries, adapters.make_compare_fn(), q["text"], rounds=2)

    # aggregate arm means per question
    summary = _summarize(rows)
    out = {"rows": rows, "elo": elo_by_q, "summary": summary,
           "weights": weights, "n_answers": len(rows)}
    with open(os.path.join(out_dir, "scorecard.json"), "w") as f:
        json.dump(out, f, indent=2)
    _write_csv(rows, os.path.join(out_dir, "scorecard.csv"))
    _write_long_csv(rows, os.path.join(out_dir, "scorecard_long.csv"), weights)
    return out


def _write_long_csv(rows, path, weights):
    """LONG format — one row per (coded answer x dimension x scorer). This is THE analysis-grade
    table the operator asked for: every score sliceable by category / question / arm / dimension /
    scorer (cs | operator | combined). CS fills `cs`; the operator's per-dim scores are merged later
    (merge_human_scores) which appends `operator` rows + recomputes `combined` = mean(cs,operator).
    The `weight` column reads the ACTUAL per-dimension weight from rubric.json (via the passed
    `weights` dict) — never a hardcoded value — so it stays correct if the rubric is ever reweighted."""
    dims = compmod.RUBRIC_DIMS
    cols = ["code", "question_id", "category", "arm", "run", "dimension", "scorer", "score",
            "weight", "is_cs_only"]
    # CS-only dims (no the operator science score to average): grounding is citation/integrity-driven.
    CS_ONLY = {"grounding"}
    wmap = {d: weights[d] for d in dims}
    with open(path, "w", newline="") as f:
        w = csv.writer(f); w.writerow(cols)
        for r in rows:
            for d in dims:
                w.writerow([r.get("code"), r["question_id"], r.get("category"), r["arm"], r["run"],
                            d, "cs", r["dimensions"][d], wmap[d], int(d in CS_ONLY)])
    return path


def merge_human_scores(long_csv_path, human_scores, out_path=None):
    """human_scores: {code: {dimension: 1..5}} (the operator judges the SCIENCE dims, not grounding/citations).
    Appends a `operator` row per (code x dim) the operator scored, and a `combined` row = mean(cs, operator) for
    dims with both; CS-only dims get combined=cs. Writes back (or to out_path). Blind-safe: keyed to
    the coded answer, never the arm."""
    out_path = out_path or long_csv_path
    with open(long_csv_path, newline="") as f:
        rd = list(csv.DictReader(f))
    cs_by = {(row["code"], row["dimension"]): row for row in rd if row["scorer"] == "cs"}
    extra = []
    for (code, dim), csrow in cs_by.items():
        fab = (human_scores.get(code) or {}).get(dim)
        base = {k: csrow[k] for k in ("code", "question_id", "category", "arm", "run", "dimension", "weight", "is_cs_only")}
        if fab is not None and csrow["is_cs_only"] != "1":
            extra.append({**base, "scorer": "operator", "score": fab})
            extra.append({**base, "scorer": "combined", "score": round((float(csrow["score"]) + float(fab)) / 2.0, 3)})
        else:
            extra.append({**base, "scorer": "combined", "score": csrow["score"]})
    allrows = rd + extra
    with open(out_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["code", "question_id", "category", "arm", "run",
                                          "dimension", "scorer", "score", "weight", "is_cs_only"])
        w.writeheader()
        for row in allrows:
            w.writerow(row)
    return out_path


def _summarize(rows):
    from statistics import mean, pstdev
    by = {}
    for r in rows:
        by.setdefault((r["question_id"], r["arm"]), []).append(r["weighted_composite"])
    summ = {}
    for (qid, arm), vals in by.items():
        summ.setdefault(qid, {})[arm] = {"mean_composite": round(mean(vals), 3),
                                         "spread": round(pstdev(vals), 3) if len(vals) > 1 else 0.0,
                                         "n": len(vals)}
    # delta L-B per question when both present
    for qid, arms in summ.items():
        if "L" in arms and "B" in arms:
            arms["delta_L_minus_B"] = round(arms["L"]["mean_composite"] - arms["B"]["mean_composite"], 3)
    return summ


def _write_csv(rows, path):
    dims = compmod.RUBRIC_DIMS
    cols = (["code", "question_id", "category", "arm", "run", "weighted_composite"] + [f"dim_{d}" for d in dims]
            + ["citation_verification_rate", "n_citations", "creativity_index", "hallucination_flag",
               "effective_grounding_cap", "integrity_cap", "dataset_used_resolved_rate", "trace_verified_fraction"])
    with open(path, "w", newline="") as f:
        w = csv.writer(f); w.writerow(cols)
        for r in rows:
            ds = r.get("dataset_resolution") or {}
            tv = r.get("trace_verification") or {}
            w.writerow([r.get("code"), r["question_id"], r.get("category"), r["arm"], r["run"], r["weighted_composite"]]
                       + [r["dimensions"][d] for d in dims]
                       + [r["citation_verification_rate"], r["n_citations"],
                          r["creativity_detail"]["creativity_index"],
                          r["creativity_detail"]["hallucination_flag"],
                          r.get("effective_grounding_cap"), r.get("integrity_cap"),
                          ds.get("used_and_resolved_rate"), tv.get("verified_fraction")])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--answers", required=True)
    ap.add_argument("--rubric", required=True)
    ap.add_argument("--out", default="out")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    manifest = json.load(open(args.answers))
    if args.dry_run:
        from adapters import DryRunAdapters
        adapters = DryRunAdapters()
    else:
        raise SystemExit("Real mode runs inside a CS session where `host` is available; import "
                         "run_experiment + RealAdapters(host, ...) directly (see README).")
    out = run_experiment(manifest, adapters, args.rubric, args.out)
    print(json.dumps(out["summary"], indent=2))


if __name__ == "__main__":
    main()
