# exp-002 harness  [CS-authored]

exp-002 REUSES the exp-001 scoring harness (`../../exp-001_baseline-vs-v0-loop/01_setup/harness/`) — it is arm-generic
and now carries the exp-002 scoring improvements (harsher panel calibration C1 + overclaim grounding penalty C2, applied
to ALL arms equally). This folder holds ONLY the exp-002-specific 3-arm ADDITIONS; it does not fork the shared core.

## Files here
- `make_analysis_3arm.py` — replaces the shared 2-arm endpoint with the three pairwise deltas Δ(L8−L7)/Δ(L8−B)/Δ(L7−B).
- `make_3arm_figs.py` — 3-arm deliverable figures (the shared fig module hardcodes 2 arms; this draws B/L7/L8).
- See `../harness-3arm-extension.md` for the full design + run order + verification.

## Shared core (used from exp-001, NOT copied)
scoring/{composite,judge,citations,novelty,trace_verify,elo,extract}.py, run_scoring.py, make_analysis.py,
make_analysis_figs.py, adapters.py, test_dryrun.py, unblind_and_analyze.py. Point `--harness` at the exp-001 path.

## Scoring improvements now live in the shared core (exp-002 C1+C2)
- **C1 (judge.py):** the panel is instructed to use the FULL 1–5 range (3 = competent/typical default; 4–5 earned only),
  fixing the exp-001 bunching that made the automated endpoint under-detect the loop effect.
- **C2 (citations.py + composite.py):** an overclaim/scope-inflation signal — a real source whose claim is overstated
  caps grounding (1 overclaim → ≤4, ≥2 → ≤3), distinct from fabrication (→1). Dry-run: 16/16 checks pass (was 13, +3 new).
Because these live in the shared core, exp-001's record reflects them too; exp-001's FROZEN scores are the saved
artifacts (BLIND_ANALYSIS.md + 05_analysis), not a re-run — so the exp-001 result is unaffected.
