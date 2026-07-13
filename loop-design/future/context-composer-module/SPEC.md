# context-composer module — OPT-1, staged for v8 (NOT in the running v7)

**Status:** built + offline-tested, **shelved for v8**. Like the multimodel-context-module, this stays in
`loop-design/future/` until the v8 bootstrap is cut. The running **v7_cc-bootstrap is not modified.** When v8 is
built (promotion ritual: copy v7 → archive → make v8), drop `skill/` into `v8_cc-bootstrap/bootstrap/skills/context-composer/`
and wire the two bootstrap edits below.

## What it is (operator instruction, 2026-07-11)
A **skill the bootstrap CC owns** that, per question, generates the **perfect CS project Agent Context** for exactly
that task — guardrails **plus** a task-sharpened performance block. It sharpens *how CS works as a scientist* (the
WIE); it never prescribes how to solve the task or reveals the domain/answer (the WAS). Every question → the bootstrap
runs the skill → a bespoke context for that run's CS project.

## Design (the fairness invariant, enforced not promised)
- Context = **[safety preamble, verbatim] + [performance block]**. Guardrails intact by construction.
- The blank CC only sets **general task-shape flags** (supplies_inputs / involves_data / asks_experiment /
  asks_hypothesis / asks_novelty / asks_prediction) — none reveal the subject. It writes **no prose** about the task.
- The performance block is assembled from a **frozen, fairness-checked block library** (`blocks.json`), each block a
  general scientist-virtue traceable to OPT-1 research (P1–P12 / S-054..S-070).
- A **fairness firewall** (`firewall_scan`, question-content-overlap) fails the composition if any distinctive
  question content-word appears in the block. Clean = []; negative control (injected "ergothioneine…") is caught.
- **Dose** = auto (backbone + triggered conditionals) / lean / full / safety_only. auto is the shipped default;
  safety_only == the baseline arm's context (control reproducibility).

## Evidence it works (offline subagent A/B, n=2 self-contained questions)
Composed vs baseline (no performance block), blind judge, 5 rubric dims: **higher on all 5**, overall **+0.060**;
largest gains grounding (+0.085) and usefulness (+0.075) — where the targeted blocks predict. The fairness firewall was
run at composition time on all three locked questions (Q_ERGO, Q2, Q3) and returned clean; the A/B answer-generation +
judging used the two self-contained questions (Q2, Q3 — Q_ERGO needs its attached PDFs, validated in the real loop).
Full evidence: `loop-design/current/opt1-context-composer-test/`. Directional, not powered — the real test
is the in-loop 3-way (baseline / v7 / v8).

## Research lineage
- `loop-design/current/opt1-context-axes.md` — 7 axes → rubric dims (operator gate).
- `loop-design/current/opt1-annotated-bibliography.md` — S-054..S-070, per-axis, evidence strength.
- `loop-design/current/opt1-evidence-synthesis.md` — P1–P12 principles + verdicts (Adopt / Use-with-care / Cut).
- `loop-design/current/opt1-context-design-guide.md` — how an optimal context is built, element→principle.

## The two v8 bootstrap wiring edits (when v8 is cut)
1. **CLAUDE.md, PART B, the "create CS project" step (project + paste Agent Context):** replace "paste the safety
   preamble" with: load the `context-composer` skill → set the 6 task-shape flags from the question → `compose_context(...)`
   with dose="auto" → **assert firewall_hits == []** → paste `res["context"]` as the project's Agent Context →
   log `res["sections_used"]` + `res["dose"]` in the run's `run_log/`.
2. **skills/README.md:** add the `context-composer` row (see this module's `skills_README_row.md`).

## Files
- `skill/SKILL.md`, `skill/blocks.json`, `skill/kernel.py` — the ready-to-drop skill.
- `skills_README_row.md` — the row to add to the bootstrap skills README.
- `SPEC.md` — this file.
