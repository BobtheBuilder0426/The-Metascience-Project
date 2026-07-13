<!-- Authored by [CS] for exp-002. Operator-facing run protocol. Loop under test: v8_cc-bootstrap. -->

# exp-002 — Run Protocol (operator-facing)  [CS-authored]

**Loop-optimization experiment.** Three arms on the same 3 locked questions: **B** (baseline blank CS), **L7** (v7
loop), **L8** (v8 loop = v7 + **the v8 upgrade bundle**: per-question composed CS context **and** the Codex multi-lens
review panel). See `../00_hypothesis.md`.

> **⚠ L8 is CUMULATIVE, not a single-variable isolate (operator ruling 2026-07-12, LB-081).** v8 bundles two upgrades
> rather than proceeding one-variable-at-a-time (time-box). So the **L7→L8 delta measures the whole v8 loop vs v7**, not
> any single optimization — a deliberate, documented trade. Any write-up must state this; per-upgrade attribution is a
> named follow-up, not this experiment's claim.

## The three arms — how each is run
- **Arm B (baseline).** Open a blank CS project; set its Agent Context to the **safety preamble only** (from
  `v8_cc-bootstrap/bootstrap/CS_PROJECT_PREAMBLE.md`, i.e. `context-composer` dose `safety_only`); paste the
  word-identical question (+ attach identical inputs). Take the single response. No loop.
- **Arm L7 (v7 loop).** Run the **`../../exp-001_baseline-vs-v0-loop/01_setup/v7_cc-bootstrap`** loop (or the exp-000
  maintained source — byte-identical) exactly as in exp-001. Its CS project context = safety preamble only.
- **Arm L8 (v8 loop).** Run the **`v8_cc-bootstrap`** loop in THIS folder. Same shared machinery as L7, plus the v8
  bundle: **(1)** at project creation (PART B step 10) the bootstrap runs the `context-composer` skill → composes
  `[safety preamble] + [task-sharpened performance block]` (dose `auto`), asserts the fairness firewall clean, pastes it
  as the Agent Context; **(2)** the driver runs the Codex multi-lens panel at Gate 1 (plan) + Gate 2 (result) with a CS
  Re-Act triage (see `codex-multilens-panel-design.md`; degrades to self-review if Codex is unavailable — logged).

**Everything else is held constant across arms:** the word-identical question, identical attached inputs, the
presentation-folder output instruction (appended byte-identical — output format is NOT engineered into the loop), the
dedicated-per-run-folder isolation, and the two-key double-blind.

## Output — the PRESENTATION FOLDER (identical shape for all arms)
Each answer-run produces the locked presentation folder: `result.md` + `reasoning.md` + `figures/` + `sources.md` +
`process_trace.json`. `process_trace.json` is excluded from the human eval site (blind-safety); it is scored by the CS
harness only. (Same contract as exp-001 — see `loop-design/current/output-format-instruction.md`.)

## Running the arms + collecting results
- **9 answer-runs** = 3 questions × 3 arms × 1 run. Collect each into
  `02_results/<QID>_arm_<B|L7|L8>_run01/presentation/`.
- For L7/L8, the driver writes its run under `driver/AL-<name>/OUTPUT/run-01/presentation/`; copy it into
  `02_results/` under the arm-labelled name above.
- Record which `context-composer` dose + `sections_used` each L8 run used (the driver logs this in its `run_log/`) so
  the analysis can attribute L8's score to the composed context.

## Blinding — the operator's two-key duty (unchanged from exp-001)
Two-key double-blind exactly as `loop-design/current/blinding-protocol.md`: operator holds Key-1 (R-codes over the 9
runs), CS holds Key-2 (E-codes). Unblinding needs both keys. Now 9 runs instead of 6; the mechanism is identical.

## What CS does with the runs (the contract)
- Score every answer through the harness (`../../exp-001_baseline-vs-v0-loop/01_setup/harness/`, shared): 5 rubric
  dimensions (equal 0.20), CS 3-persona panel + citation agent, mean(CS,the operator) composite. The scoring core is
  arm-generic (reads the `arm` field; emits `scorecard_long.csv` with an `arm` column) — B/L7/L8 all flow through it.
- **Analysis extension (documented NEXT build step — see STATUS):** the summary/delta logic and figures currently
  compute one pairwise delta (L−B). For 3 arms they need the three pairwise deltas **Δ(L8−L7)**, **Δ(L8−B)**,
  **Δ(L7−B)** and 3-bar figures. Tracked in `01_setup/harness-3arm-extension.md` (to be written when we wire scoring).
- Endpoint: mean composite across the 3 questions per arm; the three pairwise deltas; per-dimension deltas plotted
  individually; win-count k/3 for L8>L7 (secondary). Honest n=3×1 power caveat.

## Fairness (both v8 upgrades, enforced)
- **Composed context (OPT-1):** Arm L8's composed context sharpens **how** CS works, never **what** to conclude — the
  `context-composer` fairness firewall (question-content-overlap) is asserted clean before the context is used. Arm B's
  context (safety-only) is a strict subset of L8's, so the guardrails are byte-identical across all arms.
- **Codex panel:** the external critique also sharpens **how** (ambition, rigor, grounding, logic), never **what** —
  the chairman drops any answer-priming recommendation (Gate 1) and the driver strips the specific WHAT before relaying
  the Gate-2 review; the question stays byte-identical across arms; and that a panel ran (with what lenses / what it
  changed) is recorded in the run bundle, so any "L8 beat L7/B" claim honestly accounts for the advantage the baseline
  never receives. Both advantages are legitimate loop features, documented as part of the method.
