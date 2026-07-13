# exp-000 — PILOT: how far does one blank CC get? (ergothioneine → best disease target)

**A feasibility smoke-test of the whole Agentic-Loop machinery before the controlled exp-001.**
One blank Claude Code, one simple question, one loop run, **no baseline, no scoring** — we just want to see
the plumbing work end to end and learn where it needs a human.

## What to read / hand over
- `00_hypothesis.md` — what this pilot tests + graded success criteria.
- `01_setup/cc-bootstrap/` — **THE folder you hand to a blank Claude Code.** Self-contained. Start with
  `cc-bootstrap/START_HERE.md` (2-step human instructions).
- `01_setup/project-naming-convention.md` — how loop-driven CS projects (`AL-…`) are named so they never
  collide with our real the Metascience Project project.
- `01_setup/bootstrap-design-notes.md` — the literature/best-practice research (S-022..S-026) that grounds the
  bootstrap design.
- `02_results/` — where the returned run bundle + blackbox report land after the run.

## The one-liner the human types to the blank CC
> Read CLAUDE.md and bootstrap your workspace.

Then, when prompted, paste the question:
> Which disease is the best target for treating it with ergothioneine?

## After the run
Hand the whole `cc-bootstrap/OUTPUT/` folder (plus `run_log.md` + `RUN_REPORT.md`) back to CS, or have
the assistant/the operator write a short blackbox report. CS folds the findings into `agentic-loop-v0.md` + the
bootstrap, then exp-001 (the controlled, scored comparison) goes live.
