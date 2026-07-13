<!-- Authored by [CS] for exp-002. The v8 iteration hypothesis. -->

# exp-002 — Hypothesis: does the v8 loop (per-question composed CS context) beat v7 — and both beat baseline?  [CS]

## The experiment in one sentence
exp-002 is the **first loop-optimization experiment**: on real aging-biology questions, does adding a **per-question
composed CS project Agent Context** (the OPT-1 `context-composer` skill, shipped in `v8_cc-bootstrap`) make the loop
**measurably better than the v7 loop** — while both loops beat **raw Claude Science** answering the same word-identical
question cold?

## The three arms
- **Arm B — baseline.** Blank Claude Science, given ONLY the word-identical question (+ any attached inputs), one
  response, no loop. Its CS project context = the **safety preamble only** (= `context-composer` dose `safety_only`).
- **Arm L7 — v7 loop.** Blank Claude Code running the `v7_cc-bootstrap` Agentic Loop to drive CS. CS project context =
  the **safety preamble only** (v7 does not optimize the context).
- **Arm L8 — v8 loop.** Identical to v7 in the shared machinery (dedicated per-run folders, bridge, PDF digest,
  isolation, cadence, blinding) but carrying **the v8 upgrade bundle** (two changes): (1) **OPT-1 composed context** —
  at project creation the bootstrap runs the `context-composer` skill to set a composed Agent Context = safety preamble
  + a task-sharpened performance block (dose `auto`); and (2) **the Codex multi-lens review panel** — the driver runs
  external GPT-5.6-sol critique at two gates (plan-stage 4-lens panel + chairman; result-stage journal reviewer) with a
  CS Re-Act triage. See `01_setup/codex-multilens-panel-design.md` and `LOOP_VERSION.md`.

> **⚠ CAVEAT — L8 is CUMULATIVE, not a single-variable isolate (operator ruling 2026-07-12, LB-081; amended by [CS2]).**
> The original design isolated OPT-1 as the single changed variable. Under the time-box, the operator ruled that v8
> would carry several upgrades at once rather than proceed one-variable-at-a-time. **So the L7→L8 delta measures the
> whole v8 loop (composed context + Codex panel together) vs v7 — it does NOT isolate any single optimization.** This is
> a deliberate, documented trade (breadth of gain over attributability); any write-up must state it. Attributing the L8
> gain to a specific upgrade would require a later one-variable follow-up (e.g. a v8-context-only vs v8-panel-only arm).

## Hypotheses
- **H1 (loop vs baseline):** L8 > B and L7 > B on the weighted combined mean(CS,the operator) composite (rubric.json v2,
  **5 dimensions at equal 0.20**: grounding-&-integrity · reasoning-&-soundness · completeness · usefulness ·
  creativity), across the 3 test questions.
- **H2 (the v8-bundle gain — primary for this experiment):** **L8 > L7** on the same composite. Because L8 now carries
  the whole v8 bundle, H2 tests the **combined** effect of (1) the composed context and (2) the Codex panel, not OPT-1
  alone. Pre-registered mechanisms: **(1) composed context** sharpens CS on general scientist-virtues (real-tool use +
  citation discipline → grounding; reasoning transparency → reasoning; completeness/decomposition →
  completeness+usefulness; anchored self-critique → grounding+reasoning; novelty-paired-with-plausibility → creativity);
  **(2) Codex panel** adds external, cross-vendor critique at plan + result stages (ambition + rigor + anti-hallucination
  + red-team lenses → creativity + reasoning + grounding; journal-reviewer + Re-Act → completeness + usefulness). The
  offline subagent A/B for the context piece alone (n=2, `loop-design/current/opt1-context-composer-test/`) showed
  **+0.060 overall, all 5 dimensions positive** — a directional prior for one component, not the bundle.
- **H0 (honest null):** L8 ≈ L7 (the v8 bundle adds nothing measurable in the real loop, or gains from one upgrade are
  cancelled by cost/context-rot from another). A null is a real, publishable result — it says the v7 loop structure
  already carries the value, and this bundle of additions does not move the composite.

## Endpoint (same machinery as exp-001, extended to 3 arms)
- Per question, per arm: the 5 dimension scores + weighted composite (mean of CS panel and the operator).
- **Primary:** mean composite across the 3 questions per arm, and the pairwise deltas **Δ(L8−L7)**, **Δ(L8−B)**,
  **Δ(L7−B)**. Also the per-dimension deltas (plotted individually) so we see which dimension the context moved.
- **Win-count:** k/3 questions where L8 > L7 (secondary to the mean, per the operator's "means decide" ruling).
- **Honest power caveat:** n=3 questions × 1 run/arm. This is a directional, mechanism-illustrating result, not a
  powered superiority test. Reported as such.

## Fairness invariants (unchanged from exp-001, plus the OPT-1 line)
- All three arms receive the **exact same word-identical question** (+ identical attached inputs). Output format is NOT
  engineered into the question (it travels in the question's presentation-folder instruction, byte-identical to all).
- The L8 composed context sharpens **HOW** CS works, **never WHAT** to conclude — enforced by the fairness firewall
  (question-content-overlap asserted clean before use), not left to judgement. Baseline's context = the same safety
  preamble embedded in L8's context (dose `safety_only` is a strict subset of dose `auto`).
- **Two-key double-blind** scoring (operator-held Key-1 R-codes, CS-held Key-2 E-codes) exactly as locked in exp-001;
  now over 9 answer-runs (3 questions × 3 arms) instead of 6.

## What is being demonstrated for the submission
The **method of measuring a loop upgrade**: a blinded A/B/C with pre-registered mechanisms and an honest null, showing
whether (and how) a bundle of loop optimizations improves scientific output. **Note the attributability trade:** because
v8 bundles two upgrades (composed context + Codex panel), this experiment measures the *combined* loop gain, not a
single-variable isolate — a deliberate, documented choice under the time-box (LB-081). The single-variable method is
still the ideal; isolating each upgrade is a named follow-up, not this experiment's claim.
