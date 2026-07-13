#!/usr/bin/env python3
"""make_analysis.py — exp-001 analysis generator (LB-077).  [CS-authored]

Turns the LONG scorecard (one row per coded-answer x dimension x scorer) + the unblinding key into the
submission-grade analysis the operator asked for: EVERY score sliceable by
    category (cat-1/2/3)  x  judge (cs | operator | combined)  x  scoring axis (5 rubric dims)  x  arm (B|L).

Inputs
  scorecard_long.csv  : code,question_id,category,arm,run,dimension,scorer,score,weight,is_cs_only
                        (arm may be blank pre-unblind; this script is POST-unblind so arm is filled)
  blinding_key_FULL   : optional {code: {"arm":..,"question_id":..,"category":..}} to backfill arm/category
Outputs (into out_dir, default ../../05_analysis/)
  analysis_tables.csv                         every aggregated number (tidy, reproducible)
  fig_dim_<dim>_by_scorer.png     (x5)        per-dimension arm bars, 3 panels {CS,the operator,combined}
  fig_per_question_composite.png              per-question composite L vs B (combined)
  fig_endpoint_meanDelta_k.png                headline: mean-Δ across questions + win-count k/3
  fig_cs_vs_human_agreement.png                scatter cs vs operator per answer x dim (calibration)
  fig_by_category.png                         composite by category x arm x scorer (the category view)
This is pure analysis code — no host.* — so it runs offline and is fully reproducible for the submission.
"""
import argparse, csv, json, os, statistics as st
from collections import defaultdict

DIMS = ["grounding", "reasoning", "completeness", "usefulness", "creativity"]
DIM_LABEL = {"grounding": "Grounding & integrity", "reasoning": "Reasoning & soundness",
             "completeness": "Completeness", "usefulness": "Usefulness", "creativity": "Creativity"}
SCORERS = ["cs", "operator", "combined"]
CAT_LABEL = {1: "Cat-1 day-in-lab", 2: "Cat-2 big-think", 3: "Cat-3 translational"}


def load_long(path, key_full=None):
    rows = list(csv.DictReader(open(path)))
    for r in rows:
        r["score"] = float(r["score"]) if r["score"] not in ("", None) else None
        r["weight"] = float(r["weight"]) if r["weight"] not in ("", None) else 0.2
        # backfill arm/category from the full key if the long csv was written pre-unblind
        if key_full and (not r.get("arm") or not r.get("category")):
            k = key_full.get(r["code"], {})
            r["arm"] = r.get("arm") or k.get("arm")
            r["category"] = r.get("category") or k.get("category")
        if r.get("category") not in (None, ""):
            r["category"] = int(float(r["category"]))
    return rows


def _mean(xs):
    xs = [x for x in xs if x is not None]
    return round(st.mean(xs), 3) if xs else None


def aggregate(rows):
    """Return tidy aggregates: by (scorer,dim,arm), by (scorer,dim,arm,category),
    per-question composite, and the endpoint (mean-Δ + k/3)."""
    agg = {"by_dim_scorer_arm": [], "by_dim_scorer_arm_cat": [], "per_question": [], "endpoint": {}}
    grp = defaultdict(list)
    for r in rows:
        if r["score"] is None:
            continue
        grp[(r["scorer"], r["dimension"], r["arm"])].append(r["score"])
    for (sc, dim, arm), xs in sorted(grp.items()):
        agg["by_dim_scorer_arm"].append({"scorer": sc, "dimension": dim, "arm": arm,
                                          "mean_score": _mean(xs), "n": len(xs)})
    gc = defaultdict(list)
    for r in rows:
        if r["score"] is None or r.get("category") in (None, ""):
            continue
        gc[(r["scorer"], r["dimension"], r["arm"], r["category"])].append(r["score"])
    for (sc, dim, arm, cat), xs in sorted(gc.items()):
        agg["by_dim_scorer_arm_cat"].append({"scorer": sc, "dimension": dim, "arm": arm,
                                             "category": cat, "mean_score": _mean(xs), "n": len(xs)})
    # per-question weighted composite per (scorer, arm) = sum(dim_mean * weight)
    perq = defaultdict(lambda: defaultdict(list))
    for r in rows:
        if r["score"] is None:
            continue
        perq[(r["scorer"], r["question_id"], r["arm"])][r["dimension"]].append((r["score"], r["weight"]))
    comp = {}
    for (sc, qid, arm), dimmap in perq.items():
        c = 0.0
        for dim in DIMS:
            vals = dimmap.get(dim)
            if vals:
                c += _mean([v for v, _ in vals]) * vals[0][1]
        comp[(sc, qid, arm)] = round(c, 3)
        agg["per_question"].append({"scorer": sc, "question_id": qid, "arm": arm, "composite": round(c, 3)})
    # endpoint on the composite: mean-Δ across questions + k/3.
    # Prefer the COMBINED composite (mean of CS+the operator, the headline); fall back to CS-only when
    # the operator's scores have not been merged yet (interim endpoint right after Key-1). The scorer used
    # is recorded so the reader never mistakes an interim CS-only delta for the final combined one.
    endpoint_scorer = "combined" if any(sc == "combined" for (sc, _, _) in comp) else "cs"
    qids = sorted({qid for (sc, qid, arm) in comp if sc == endpoint_scorer})
    deltas, wins = [], 0
    for qid in qids:
        L = comp.get((endpoint_scorer, qid, "L")); B = comp.get((endpoint_scorer, qid, "B"))
        if L is not None and B is not None:
            d = round(L - B, 3); deltas.append({"question_id": qid, "delta": d})
            wins += 1 if d > 0 else 0
    agg["endpoint"] = {"scorer": endpoint_scorer,
                       "is_interim_cs_only": endpoint_scorer == "cs",
                       "per_question_delta": deltas,
                       "mean_delta": round(st.mean([d["delta"] for d in deltas]), 3) if deltas else None,
                       "delta_min": min([d["delta"] for d in deltas]) if deltas else None,
                       "delta_max": max([d["delta"] for d in deltas]) if deltas else None,
                       "k_wins": wins, "k_total": len(deltas),
                       "verdict": _verdict(deltas, wins)}
    return agg, comp


def _verdict(deltas, wins):
    if not deltas:
        return "no-data"
    md = st.mean([d["delta"] for d in deltas]); k = wins; n = len(deltas)
    if md > 0 and k == n:
        return "strong (mean-Δ>0 and won all)"
    if md > 0 and k >= max(2, n - 1):
        return "positive (won most; inspect the loss)"
    return "null/negative (mean-Δ≈0 or won ≤ half) — a real, reportable finding"


def write_tables(agg, out_dir):
    p = os.path.join(out_dir, "analysis_tables.csv")
    with open(p, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["#", "by_dimension_scorer_arm"])
        w.writerow(["scorer", "dimension", "arm", "mean_score", "n"])
        for r in agg["by_dim_scorer_arm"]:
            w.writerow([r["scorer"], r["dimension"], r["arm"], r["mean_score"], r["n"]])
        w.writerow([]); w.writerow(["#", "by_dimension_scorer_arm_category"])
        w.writerow(["scorer", "dimension", "arm", "category", "mean_score", "n"])
        for r in agg["by_dim_scorer_arm_cat"]:
            w.writerow([r["scorer"], r["dimension"], r["arm"], r["category"], r["mean_score"], r["n"]])
        w.writerow([]); w.writerow(["#", "per_question_composite"])
        w.writerow(["scorer", "question_id", "arm", "composite"])
        for r in agg["per_question"]:
            w.writerow([r["scorer"], r["question_id"], r["arm"], r["composite"]])
        e = agg["endpoint"]
        # header + scorer flag reflect the ACTUAL scorer used (combined once the operator merges, else CS-only
        # interim) — never hardcode "combined", or an interim CS-only delta would be mislabeled as final.
        _sc = e.get("scorer", "combined")
        _hdr = ("endpoint (CS-only INTERIM — the operator not yet merged)" if e.get("is_interim_cs_only")
                else f"endpoint ({_sc} composite)")
        w.writerow([]); w.writerow(["#", _hdr])
        w.writerow(["scorer", _sc, "is_interim_cs_only", e.get("is_interim_cs_only", False)])
        w.writerow(["mean_delta", e["mean_delta"], "k_wins", e["k_wins"], "k_total", e["k_total"],
                    "verdict", e["verdict"]])
        for d in e["per_question_delta"]:
            w.writerow(["delta", d["question_id"], d["delta"]])
    return p


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--long", required=True)
    ap.add_argument("--key", default=None, help="blinding_key_FULL.json (optional backfill)")
    ap.add_argument("--out", default="../../05_analysis")
    ap.add_argument("--tables-only", action="store_true", help="skip figures (no matplotlib)")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    key = json.load(open(a.key)) if a.key and os.path.exists(a.key) else None
    rows = load_long(a.long, key)
    agg, comp = aggregate(rows)
    tp = write_tables(agg, a.out)
    print("tables ->", tp)
    print("endpoint:", json.dumps(agg["endpoint"]))
    if not a.tables_only:
        import make_analysis_figs as F  # figures live in a sibling module (keeps this file import-light)
        F.render_all(rows, agg, comp, a.out)
