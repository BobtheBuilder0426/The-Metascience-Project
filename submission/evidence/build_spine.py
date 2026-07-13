#!/usr/bin/env python3
"""
build_spine.py -- the reproducible evidence spine for the submission.

WHAT THIS DOES
  1. Checksums every authoritative input (SHA-256) -> checksums.sha256
  2. Recomputes the headline numbers for exp-001 and exp-002 FROM THE RAW
     per-answer scores, and asserts each recomputed value equals the frozen
     value in the committed analysis tables (fail-loud on drift).
  3. Recomputes the Friedman omnibus (exp-002) with scipy.
  4. Writes derived_numbers.json (machine-readable) that every downstream
     number/label/caption/figure inherits from.

ESTIMANDS / UNITS / FORMULAS
  - Scores are on a 1-5 ordinal rubric scale (higher = better), per dimension.
  - CS panel dimensions: grounding, reasoning, completeness, usefulness, creativity.
    * cs_composite = unweighted mean of all 5 CS dims (each 1/5). [1-5]
    * cs_mean4     = unweighted mean of the 4 *shared science* dims
                     (reasoning, completeness, usefulness, creativity);
                     grounding excluded because the human expert did not score it. [1-5]
  - Human-expert dimensions: reasoning, completeness, usefulness, creativity.
    * human_mean4  = unweighted mean of those 4 dims. [1-5]
  - Combined (DERIVED SUMMARY, *not* a third scorer or an independent replicate):
    per shared dimension d, combined_d = (cs_d + human_d)/2; then
    combined_mean4 = mean over the 4 shared dims. [1-5]
    (exp-001's "combined composite" additionally carries grounding as a CS-only
    term in a 5-dim mean; documented per-experiment below.)
  - Experimental unit = one question-level answer per arm. Design = randomized
    complete block, block = question. exp-001 n=3 questions x 2 arms;
    exp-002 n=3 questions x 3 arms. One answer per (question,arm) cell (no
    within-cell replication).
  - Primary endpoint exp-002 = within-question delta Delta(L8-L7); reported as
    mean delta and sign-count (n_positive of 3). Inference is confined to
    sign-consistency; the Friedman p-values are reported for completeness only
    (underpowered by construction, n=3 blocks).
"""
import csv, json, hashlib, pathlib, sys
from statistics import mean

REPO = pathlib.Path(__file__).resolve().parents[2]
OUT  = pathlib.Path(__file__).resolve().parent

# ---- tier-labelled authoritative inputs (conflict-precedence: 1 > 2 > 3 > 4) ----
INPUTS = {
  "tier1_labbook": ["LABBOOK.md"],
  # exp-001/002 numeric inputs are read from name-normalized copies under evidence/inputs/
  # (operator name -> "human"; values byte-identical to the experiment record). This keeps the
  # evidence spine self-contained and free of the operator's name while preserving every number.
  "tier2_exp001": [
    "experiments/exp-001_baseline-vs-v0-loop/05_analysis/FINAL_RESULT.md",
    "experiments/exp-001_baseline-vs-v0-loop/05_analysis/analysis_tables.csv",
    "submission/evidence/inputs/exp001_scorecard_long_unblind.csv",
    "experiments/exp-001_baseline-vs-v0-loop/05_analysis/blinding_key_FULL.json",
    "submission/evidence/inputs/exp001_human_eval.json",
  ],
  "tier2_exp002": [
    "experiments/exp-002_baseline-vs-v7-vs-v8/FINAL_RESULT.md",
    "submission/evidence/inputs/exp002_master_3arm.csv",
    "submission/evidence/inputs/exp002_final_3arm_summary.json",
    "experiments/exp-002_baseline-vs-v7-vs-v8/05_analysis/table_total_by_arm.csv",
    "experiments/exp-002_baseline-vs-v7-vs-v8/05_analysis/table_deltas.csv",
    "experiments/exp-002_baseline-vs-v7-vs-v8/05_analysis/table_per_question_by_arm.csv",
    "experiments/exp-002_baseline-vs-v7-vs-v8/05_analysis/table_per_dimension_by_arm.csv",
    "experiments/exp-002_baseline-vs-v7-vs-v8/04_evaluation/blinding_key_FULL.json",
    "submission/evidence/inputs/exp002_human_eval.json",
  ],
  "tier3_sources_loopver": [
    "SOURCES.md",
    "experiments/exp-001_baseline-vs-v0-loop/01_setup/v7_cc-bootstrap/LOOP_VERSION.md",
    "experiments/exp-002_baseline-vs-v7-vs-v8/01_setup/v8_cc-bootstrap/LOOP_VERSION.md",
    "experiments/exp-003_final-tcell-perturb/01_setup/v9_cc-bootstrap/LOOP_VERSION.md",
  ],
  "tier2_exp003_reports": [
    "experiments/exp-003_final-tcell-perturb/02_results/presentation CS blank T-cell perturb/report.pdf",
    "experiments/exp-003_final-tcell-perturb/02_results/presentation v9 loop T-cell perturb/report.pdf",
    "experiments/exp-003_final-tcell-perturb/02_results/presentation v9 loop T-cell perturb/result.md",
  ],
}

def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1<<16), b""):
            h.update(chunk)
    return h.hexdigest()

def approx(a, b, tol=0.01):
    return abs(a-b) <= tol

# ---------------- checksums ----------------
def write_checksums():
    lines, missing = [], []
    for tier, files in INPUTS.items():
        lines.append(f"# {tier}")
        for rel in files:
            fp = REPO/rel
            if fp.exists():
                lines.append(f"{sha256(fp)}  {rel}")
            else:
                missing.append(rel); lines.append(f"MISSING  {rel}")
    (OUT/"checksums.sha256").write_text("\n".join(lines)+"\n")
    assert not missing, f"authoritative inputs missing: {missing}"
    return len([r for fs in INPUTS.values() for r in fs])

# ---------------- exp-002 recompute from raw ----------------
def load_master():
    rows = list(csv.DictReader(open(REPO/"submission/evidence/inputs/exp002_master_3arm.csv")))
    for r in rows:
        for k,v in list(r.items()):
            try: r[k] = float(v)
            except (ValueError, TypeError): pass
    return rows

def exp002():
    rows = load_master()
    arms = ["B","L7","L8"]; qs = ["Q1","Q2","Q3"]
    by = {(r["arm"], r["question"]): r for r in rows}
    # recompute per-answer aggregates from the raw dimension columns
    for r in rows:
        cs5 = mean([r["cs_grounding"],r["cs_reasoning"],r["cs_completeness"],r["cs_usefulness"],r["cs_creativity"]])
        cs4 = mean([r["cs_reasoning"],r["cs_completeness"],r["cs_usefulness"],r["cs_creativity"]])
        fa4 = mean([r["human_reasoning"],r["human_completeness"],r["human_usefulness"],r["human_creativity"]])
        cb4 = mean([(r["cs_reasoning"]+r["human_reasoning"])/2,
                    (r["cs_completeness"]+r["human_completeness"])/2,
                    (r["cs_usefulness"]+r["human_usefulness"])/2,
                    (r["cs_creativity"]+r["human_creativity"])/2])
        assert approx(cs5, r["cs_composite"]), (r["R"],"cs_composite",cs5,r["cs_composite"])
        assert approx(cs4, r["cs_mean4"]),    (r["R"],"cs_mean4",cs4,r["cs_mean4"])
        assert approx(fa4, r["human_mean4"]),  (r["R"],"human_mean4",fa4,r["human_mean4"])
        assert approx(cb4, r["comb_mean4_raw"]), (r["R"],"combined",cb4,r["comb_mean4_raw"])
    # NOTE: dict VALUES ("human_mean4", etc.) are the (name-normalized) source-data column names —
    # the single human expert's scorer columns, read verbatim; dict KEYS are our reporting labels.
    metrics = {"cs_composite":"cs_composite","cs_mean4":"cs_mean4",
               "human_mean4":"human_mean4","combined_raw4":"comb_mean4_raw"}
    arm_means = {a:{} for a in arms}
    for mlabel,col in metrics.items():
        for a in arms:
            arm_means[a][mlabel] = round(mean([by[(a,q)][col] for q in qs]), 4)
    # within-question deltas
    def deltas(hi,lo,col):
        d = {q: round(by[(hi,q)][col]-by[(lo,q)][col],4) for q in qs}
        return {"per_question":d, "mean":round(mean(d.values()),4),
                "n_positive": sum(1 for v in d.values() if v>0)}
    contrasts = {"L8-L7":("L8","L7"),"L8-B":("L8","B"),"L7-B":("L7","B")}
    delta_tbl = {ml:{c:deltas(hi,lo,col) for c,(hi,lo) in contrasts.items()}
                 for ml,col in metrics.items()}
    # per-dimension arm means (CS-harness + human-expert)
    dims_cs = ["grounding","reasoning","completeness","usefulness","creativity"]
    dims_fa = ["reasoning","completeness","usefulness","creativity"]
    perdim = {"CS_harness":{}, "human_expert":{}}
    for d in dims_cs:
        perdim["CS_harness"][d] = {a: round(mean([by[(a,q)][f"cs_{d}"] for q in qs]),3) for a in arms}
    for d in dims_fa:
        perdim["human_expert"][d] = {a: round(mean([by[(a,q)][f"human_{d}"] for q in qs]),3) for a in arms}
    # head-to-head winner per question (by cs_composite / human_mean4 / combined)
    def winner(q, col):
        best = max(arms, key=lambda a: by[(a,q)][col]); return best
    h2h = {q: {"CS_composite":winner(q,"cs_composite"),
               "human_mean4":winner(q,"human_mean4"),
               "Combined":winner(q,"comb_mean4_raw")} for q in qs}
    # Friedman omnibus (blocks=questions)
    from scipy.stats import friedmanchisquare
    fried = {}
    for ml,col in {"cs_mean4":"cs_mean4","human_mean4":"human_mean4","combined_raw4":"comb_mean4_raw"}.items():
        B  = [by[("B",q)][col] for q in qs]
        L7 = [by[("L7",q)][col] for q in qs]
        L8 = [by[("L8",q)][col] for q in qs]
        chi,p = friedmanchisquare(B,L7,L8)
        fried[ml] = {"chi2":round(chi,3),"p":round(p,3),"n_blocks":3,"k_arms":3}
    # cross-check against frozen summary (name-normalized copy)
    frozen = json.load(open(REPO/"submission/evidence/inputs/exp002_final_3arm_summary.json"))
    for a in arms:
        assert approx(arm_means[a]["cs_composite"], frozen["arm_means"][a]["cs_composite"]), a
        assert approx(arm_means[a]["human_mean4"],  frozen["arm_means"][a]["human_mean4"]), a
    for ml in ["cs_composite","cs_mean4","human_mean4"]:
        assert delta_tbl[ml]["L8-L7"]["n_positive"] == 3, ml
    return {"design":"randomized complete block; block=question; n=3 questions; arms B/L7/L8; 1 answer per cell",
            "arms":{"B":"baseline (blank Claude Science)","L7":"v7 agentic loop","L8":"v8 agentic loop"},
            "arm_means":arm_means, "deltas":delta_tbl, "per_dimension":perdim,
            "head_to_head":h2h, "friedman":fried,
            "primary_endpoint":"within-question Delta(L8-L7); mean + sign-count of 3",
            "arm_to_Rcode":{"B":["R8","R1","R4"],"L7":["R9","R5","R2"],"L8":["R3","R7","R6"]}}

# ---------------- exp-001 recompute from raw ----------------
def exp001():
    rows = list(csv.DictReader(open(REPO/"submission/evidence/inputs/exp001_scorecard_long_unblind.csv")))
    for r in rows: r["score"]=float(r["score"])
    qs = ["Q_ERGO","Q2","Q3"]; arms=["B","L"]
    # combined composite = 5-dim mean (grounding CS-only; other 4 = combined values)
    def comp(scorer, arm, q):
        sel = [r for r in rows if r["scorer"]==scorer and r["arm"]==arm and r["question_id"]==q]
        d = {r["dimension"]:r["score"] for r in sel}
        return d
    comb = {}
    for q in qs:
        for a in arms:
            d = comp("combined",a,q)
            comb[(a,q)] = round(mean([d["grounding"],d["reasoning"],d["completeness"],d["usefulness"],d["creativity"]]),3)
    per_q_delta = {q: round(comb[("L",q)]-comb[("B",q)],3) for q in qs}
    endpoint = {"per_question":per_q_delta,
                "mean_delta":round(mean(per_q_delta.values()),3),
                "k_wins":sum(1 for v in per_q_delta.values() if v>0),"k_total":3}
    # cs-only composite arm means
    cs_arm = {a: round(mean([mean([comp("cs",a,q)[dd] for dd in ["grounding","reasoning","completeness","usefulness","creativity"]]) for q in qs]),3) for a in arms}
    # human-expert mean4 arm means (4 dims)
    fa_arm = {a: round(mean([mean([comp("human",a,q)[dd] for dd in ["reasoning","completeness","usefulness","creativity"]]) for q in qs]),3) for a in arms}
    # cross-check the frozen endpoint values
    assert approx(endpoint["mean_delta"],0.476), endpoint
    assert endpoint["k_wins"]==2, endpoint
    assert approx(per_q_delta["Q3"],1.24) and approx(per_q_delta["Q_ERGO"],0.421) and approx(per_q_delta["Q2"],-0.232), per_q_delta
    return {"design":"randomized complete block; block=question; n=3 questions; arms B/L (loop=v7); 1 answer per cell",
            "note":"folder slug says 'v0-loop' but the loop under test was v7_cc-bootstrap (hash 6bbd94a13d13e462)",
            "arms":{"B":"baseline (blank Claude Science)","L":"v7 agentic loop"},
            "endpoint_combined_composite":endpoint,
            "cs_composite_arm_means":cs_arm, "human_mean4_arm_means":fa_arm,
            "questions":{"Q_ERGO":"ergothioneine exercise-performance mechanism (+wet-lab protocol)",
                         "Q2":"exercise-mimetic drug repurposing","Q3":"complex-I / mito compound"},
            "head_to_head_human":{"Q_ERGO":"L (loop) preferred (medium confidence)"}}

def main():
    n = write_checksums()
    derived = {
      "_meta":{"generated_by":"submission/evidence/build_spine.py",
               "inputs_checksummed":n,
               "estimand":"per-dimension 1-5 ordinal rubric; unit=one answer per (question,arm) cell; RCB design, block=question",
               "combined_is":"DERIVED per-dimension mean of CS-panel and human-expert; NOT a third scorer or independent replicate",
               "inference_scope":"sign-consistency of within-question deltas; Friedman p reported for completeness only (n=3 blocks, underpowered)"},
      "exp001":exp001(),
      "exp002":exp002(),
      "exp003":{"design":"showcase comparison (NOT scored); n=1 answer per arm; 2 arms B vs L9(v9 loop); 1 question",
                "arms":{"B":"baseline (blank Claude Science, safety-only guardrail)","L9":"v9 agentic loop"},
                "question":"from the genome-scale CD4+ T-cell Perturb-seq dataset, identify a natural metabolite/nutraceutical to treat an autoimmune disease of your choice; give methodology, rationale, and an optimal pilot",
                "arm_B_answer":{"target":"IMPDH2","metabolite":"mycophenolic acid (Penicillium metabolite; prodrug mycophenolate mofetil)","disease":"type-2/eosinophilic asthma"},
                "arm_L9_answer":{"target":"PKM2","metabolite":"micheliolide (feverfew guaianolide; covalent PKM2-Cys424 stabiliser; prodrug DMAMCL/ACT001)","disease":"multiple sclerosis",
                                 "key_stats_as_reported":{"GM-CSF_z":-3.66,"GM-CSF_FDR":0.005,"IFNg_z":-3.30,"IL2_z":-0.05}},
                "verification":"arm scientific claims NOT re-verified (documentation only, LB-104). Accessions recorded verified during the original run (SOURCES.md S-084, LB-106, NCBI E-utilities 2026-07-13); INDEPENDENT live re-confirmation is pending in this submission's Verification track -> verification_ledger.csv",
                "caveat":"n=1 per arm, single question; showcase not measured win"},
      "loop_versions":{
        "v7":{"hash":"6bbd94a13d13e462","files":23,"desc":"bootstrap-once -> drive-many; dedicated isolated per-run CS workspaces"},
        "v8":{"hash":"331d802b219b4e69","files":27,"base":"v7","desc":"v7 + OPT-1 per-question context-composer skill + Codex cross-vendor multi-lens critique panel (2 gates) + Gate-2 figure-quality add-on",
              "caveat":"operator ruling LB-081: >1 upgrade at once; L7->L8 delta is the cumulative v8 bundle, NOT single-variable isolation"},
        "v9":{"hash":"c92973d8a3bbc5e9","files":28,"base":"v8","desc":"v8 + Codex effort high/xhigh + hard multimodal Gate-2 precondition + CS-reconnect doc; inherits v8 cumulative caveat"}},
    }
    (OUT/"derived_numbers.json").write_text(json.dumps(derived, indent=2))
    print("OK: checksummed", n, "inputs; recomputed exp-001 + exp-002 == frozen tables; Friedman recomputed.")
    print("exp002 arm means (combined_raw4):", {a:derived['exp002']['arm_means'][a]['combined_raw4'] for a in ['B','L7','L8']})
    print("exp002 Delta(L8-L7) n_positive:", {m:derived['exp002']['deltas'][m]['L8-L7']['n_positive'] for m in derived['exp002']['deltas']})
    print("exp002 Friedman:", derived['exp002']['friedman'])
    print("exp001 endpoint:", derived['exp001']['endpoint_combined_composite'])

if __name__ == "__main__":
    main()
