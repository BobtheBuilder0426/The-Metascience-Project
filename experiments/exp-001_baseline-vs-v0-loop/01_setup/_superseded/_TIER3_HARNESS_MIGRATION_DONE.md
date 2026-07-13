# TIER-3 HARNESS MIGRATION — DONE (LB-077, 2026-07-11)

The harness portion of this checklist is COMPLETE: rubric.json is v2 (5x0.20), composite.py + judge.py + adapters.py renamed correctness->reasoning, trace_verify + dataset-resolution wired into the grounding-integrity cap, scorecard_long.csv (per code x dim x scorer) + merge_human_scores added, dry-run 13/13 PASS.

REMAINING (eval-site + final-report code) is tracked in the same LB-077 entry. Original marker preserved below.

---

# ⚠ TIER-3 PENDING — harness/eval/report NOT yet migrated to rubric v2 (LB-075)

Canonical `loop-design/current/rubric.json` is **v2** (LB-075): 5 dims **equal 0.20**,
`correctness` **renamed** `reasoning`, grounding widened to **grounding & integrity**
(+ dataset resolution + trace_verify action-check), test clause **conditional**.

**This harness copy + the eval-site + the final-report code still run v1** (key `correctness`,
weights 0.25/0.25/0.20/0.15/0.15). Do NOT score a real run until this migration lands, or the
scorecard will be split-brain.

## Atomic migration checklist (do ALL in one pass, then delete this file)
- [ ] `harness/rubric.json` ← copy canonical v2
- [ ] `scoring/composite.py` : `RUBRIC_DIMS` correctness→reasoning; weights now loaded (equal) — verify sum==1
- [ ] `scoring/judge.py` : `RUBRIC_DIMS` + form string + system prompt ("correctness"→"reasoning & soundness")
- [ ] `adapters.py` : stub JSON keys correctness→reasoning (lines ~77/86/87) + R1 hard-marker comment
- [ ] wire `trace_verify.py` rate + dataset-resolution rate INTO the grounding score/cap (composite.py)
- [ ] `for-the operator/make_eval_site.py` : dimension keys/labels correctness→reasoning; keep process_trace EXCLUDED from site
- [ ] `for-the operator/make_final_report.py` + `final-report-spec.md` : dimension labels
- [ ] re-run the demo scorer end-to-end; confirm scorecard.csv has `reasoning` col + 5×0.20 weights
- [ ] leave the dated DEMO html/_demo_* snapshots UNTOUCHED (historical record)

Spec of record for v2 dimensions: `loop-design/current/rubric.json` + `quantification.md` §1.
