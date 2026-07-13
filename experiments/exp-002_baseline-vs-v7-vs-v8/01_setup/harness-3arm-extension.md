# exp-002 — 3-arm harness extension  [CS-authored]

**Why this exists.** exp-001 was 2-arm (B vs L); its shared harness (`../../exp-001_baseline-vs-v0-loop/01_setup/harness/`)
computes ONE pairwise delta (L−B). exp-002 is 3-arm (B / L7 / L8) and needs the three pairwise deltas. This doc records
how the extension is built — **by reuse, not by forking** the shared harness (protocol §"What CS does with the runs").

## What is reused UNCHANGED (already arm-generic)
The shared `make_analysis.py` groups by whatever `arm` values appear in the `arm` column:
- `load_long()` — reads scorecard_long, backfills arm from the FULL blinding key (Key-1 ∘ Key-2).
- `aggregate()` upstream blocks — `by_dim_scorer_arm`, `by_dim_scorer_arm_cat`, `per_question` composite — all iterate
  over the arms present, so B/L7/L8 flow through with no change.
- `write_tables()` — writes those arm-generic tables.
- `run_scoring.merge_human_scores()` — keyed by code, arm-agnostic.
- The two-key unblinding runner (`unblind_and_analyze.py`) — composes Key-1 ∘ Key-2 over the 9 runs (was 6); mechanism identical.
Only ONE thing in the shared harness is 2-arm-specific: the `endpoint` block hardcodes `comp[...,"L"]` − `comp[...,"B"]`.

## What the extension ADDS (this folder)
- **`make_analysis_3arm.py`** — imports the shared functions, reuses `aggregate()`'s upstream output, and REPLACES the
  endpoint with `three_arm_endpoint()` → the three pairwise deltas, PRIMARY first:
  - **Δ(L8−L7)** = the v8-upgrade-bundle effect (did optimizing the loop help? — the experiment's primary question).
  - **Δ(L8−B)** = full v8 loop vs raw baseline.
  - **Δ(L7−B)** = v7 loop vs raw baseline (reproduces exp-001's finding on the new questions — a sanity anchor).
  Each carries per-question deltas + mean-Δ + k/3. Also emits `arm_mean_composite` (the level each arm sits at).
  Prefers the COMBINED (CS+the operator) composite; falls back to a CS-only interim (flagged `is_interim_cs_only`) right after
  Key-1 before the operator is merged — same discipline as the 2-arm endpoint.
- **`make_3arm_figs.py`** — the exp-001 figure module hardcodes the pair ("B","L") and cannot draw 3 arms, so this
  renders the 3-arm deliverables with `figure-style`: per-question composite (3 grouped bars), per-dimension × 3 arms,
  and the endpoint 3-bar pairwise-Δ figure. Colours B muted / L7 mid / L8 focal (colour-blind-safe).

## Run order (post-unblind, operator stage)
1. `unblind_and_analyze.py` (shared) → backfills arm B/L7/L8 into `scorecard_long_unblind.csv` + merges the operator.
2. `make_analysis_3arm.py --long <unblind csv> --harness <exp-001 harness> --out 05_analysis` → tables + `endpoint_3arm.json`.
3. `make_3arm_figs.py --tables 05_analysis/analysis_tables.csv --endpoint 05_analysis/endpoint_3arm.json --out 05_analysis`.

## Verified
Smoke-tested on a synthetic 9-run scorecard (B<L7<L8): endpoint returns Δ(L8−L7)=+0.4, Δ(L8−B)=+0.8, Δ(L7−B)=+0.4,
each k=3/3; arm means B/L7/L8 = 3.1/3.5/3.9; all 3 figures render. No edit to the shared exp-001 harness.

## Honest caveats carried from the design
- n = 3 questions × 1 run/arm — DESCRIPTIVE, not powered; no p-value. Report the three deltas + per-question detail + k/3.
- **L8 is cumulative** (OPT-1 composed context + Codex panel bundled) — Δ(L8−L7) is the whole-bundle effect, not a
  single-variable isolate (operator ruling, protocol §⚠). Per-upgrade attribution is a named follow-up.
- The scoring harness recalibration (harsher panel anchors + overclaim cap, exp-002 C-improvements) means exp-002
  ABSOLUTE scores are not comparable to exp-001's — only within-exp-002 deltas are. State this in any write-up.
