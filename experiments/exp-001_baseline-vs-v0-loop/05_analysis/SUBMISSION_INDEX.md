# exp-001 — Submission Package Index (paper-ready)

**Purpose:** single map from the exp-001 story → the evidence artifact backing each claim, structured as the skeleton for the paper-style final report. Every row is a saved, versioned artifact. Status: **exp-001 COMPLETE (LB-087).**

## The result in one line
The Metascience Project scoring method run end-to-end: a naive question → 2 arms (raw baseline vs v7 loop) → blind presentation folders → dual blind scoring (gated automated panel + human expert) → two-key unblinding → arm-level endpoint. **v7 loop beats baseline: combined mean-Δ = +0.48, k=2/3; the operator's own verdict favoured the loop on all 3 questions.** n=3×1, descriptive (no p-value claimed).

## Paper skeleton → evidence map

| § | Paper section | Backing artifact(s) |
|---|---|---|
| 1 | **Headline result + endpoint** | [FINAL_RESULT.md]({{artifact:93f42cf7-ce27-466d-ab6a-47f09b6ff613}}) §1; [fig_endpoint_meanDelta_k.png]({{artifact:bdd54415-db62-46dd-85d7-26ba03b58f90}}) |
| 2 | **Method: two-key double-blind** | `loop-design/current/blinding-protocol.md`; keys: [key2_eval_to_R.json]({{artifact:451fc86e-4cec-4faa-9dd8-71c43e7faa47}}) + [blinding_key_FULL.json]({{artifact:ab4df0a5-00b0-4515-8b17-229bc2cbce2a}}) |
| 3 | **Method: dual scoring (panel + expert)** | [BLIND_ANALYSIS.md]({{artifact:1c1542c3-ea42-4a1d-91b0-8067ec2cb0a0}}) (blind, pre-unblind); harness modules [composite.py]({{artifact:074bd6a5-4240-4ec6-b1b0-3ebdd225b685}}), [citations.py]({{artifact:7b8b0c51-5e3d-451a-809d-abc1db2b4d87}}) |
| 4 | **Method: gated creativity metric** | `creativity_index` in [composite.py]({{artifact:074bd6a5-4240-4ec6-b1b0-3ebdd225b685}}); decomposition figure in BLIND_ANALYSIS.md §3.2 |
| 5 | **Per-dimension / per-scorer results** | [analysis_tables.csv]({{artifact:6b3ded61-3941-4730-9c5b-babd9e2239a0}}); [fig_cs_vs_human_agreement.png]({{artifact:da4ce80a-85e8-474e-95b3-39498b694c5d}}); [fig_per_question_composite.png]({{artifact:c47578e9-4188-4ac8-b7e5-2289fdc91a46}}) |
| 6 | **Per-question narrative (expert read)** | [FINAL_RESULT.md]({{artifact:93f42cf7-ce27-466d-ab6a-47f09b6ff613}}) §4; [human_eval.json]({{artifact:f2d86977-4940-4480-9fec-18774c7e615a}}) (verbatim) |
| 7 | **Key finding: effect lives in expert layer** | FINAL_RESULT.md §2; the CS-only Δ=+0.02 vs combined Δ=+0.48 contrast |
| 8 | **Full unblinded scorecard (raw data)** | [scorecard_long_unblind.csv]({{artifact:72819fe2-4354-48f4-9990-037a9fa60393}}) (code×dim×scorer×arm) |
| 9 | **Reproducible pipeline** | [unblind_and_analyze.py]({{artifact:e4698f3f-395b-46a7-82f7-f03005f60420}}) + [make_analysis.py]({{artifact:bd536d6e-239c-41b7-8d59-51833fc1f861}}); operator-facing eval site [eval_site.html]({{artifact:3f40e5d0-cc9f-448b-b92e-0943c469d269}}) |
| 10 | **Limitations + next steps** | FINAL_RESULT.md §7; `exp002_planning/v8_exp002_improvements.md` |

## Data integrity notes (for methods/limitations section)
- **Grounding cap correction (LB-083):** two cap bugs flattened grounding to 2; fixed within the locked rubric anchors, anti-hallucination preserved (13/13 dry-run). Grounding now spans 2–4.
- **Creativity metric verified (LB-082b):** full novelty→panel→gate chain recomputes exactly; boundary behaviour (novel-but-no-reasoning → 0) confirmed.
- **Honest power caveat:** n=3 questions × 1 run/arm; descriptive, directional; contribution is the method + effect direction, not a powered test.
- **Scorer disagreement disclosed:** Q2 is the one combined loss, but the operator picked the loop there too (low confidence) — the CS panel flipped it. Documented in FINAL_RESULT.md §2 + §4.

## What still needs doing to become "the paper"
1. Assemble the paper-style report (intro → method → results → discussion) — this index is the skeleton; FINAL_RESULT.md is ~80% of the body.
2. Fold exp-002 results in once run (the 3-way baseline/v7/v8 comparison — the actual "does optimisation help" test).
3. Decide format: single HTML/PDF report vs the repo as-is. (Operator call.)
