<!-- CS's analysis of exp-001. The figures + tables live in the 05_analysis/ FOLDER; this file is the narrative that
     ties them together + the next-hypothesis reasoning. Authored by [CS], post-unblind. STATUS: pending run. -->

# exp-001 — Analysis + next hypothesis (CS)  →  figures in `05_analysis/`

Post-unblind, CS produces (all from `02_results/scoring/scorecard_long.csv`, every score documented + plotted):
- **Per-dimension arm comparison, plotted individually** — each of the 5 dims (grounding & integrity, reasoning &
  soundness, completeness, usefulness, creativity), Arm L vs Arm B, **three ways: CS / the operator / combined**.
- **Per-category breakdown** — the same, split by question category (cat-1 day-in-lab / cat-2 big-think / cat-3
  translational) so we see where the loop helps most.
- **Per-question composite** (combined mean) + per-question Δ.
- **Headline endpoint panel** — mean-Δ across questions + win-count k/3 + per-question Δ spread.
- **CS-vs-the operator agreement** — scatter + per-dimension deltas (instrument-calibration; submission data).
- **Creativity cross-check** (mechanical index vs the operator) + **citation-quality panel** (existence/support/primary-vs-review/
  venue/retractions).
- **`analysis_tables.csv`** — every underlying number, reproducible.

Then: did Arm L beat Arm B (mean-Δ + k/3)? If the loop improved, **promote** to `loop-design/current/` + log
`loop-design/CHANGELOG.md`; append one row to `../../RESULTS-LOG.md`; form the exp-002 hypothesis.
