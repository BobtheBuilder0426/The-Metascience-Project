# exp-000 (PILOT) — 00_hypothesis

**Type:** feasibility pilot / smoke test (NOT a controlled comparison).
**Date:** 2026-07-09 · **Author:** [CS] · **Status:** ready to run (awaiting a blank CC + operator).

## Purpose
Before running the controlled exp-001 (baseline vs. loop, 8 answer-runs, scored), we do **one** end-to-end
dry run of the whole machinery: hand a **blank Claude Code** the self-contained bootstrap folder, let it
**create a fresh Claude Science project and drive it through the v0 loop** on a simple question, and see
**how far one blank CC gets on the first attempt**. No baseline, no scoring — we are testing the *plumbing*,
not measuring the effect.

## Question (deliberately simple, for the pilot)
> **Which disease is the best target for treating it with ergothioneine?**
(Question id `QDIS`. The two operator-provided ergothioneine papers, S-015 + S-016, are supplied as starting
material.)

## What we are actually testing (feasibility, not effect)
- **H-pilot:** a blank CC, given only the bootstrap folder, can (a) bootstrap itself with a simple human
  trigger, (b) create + name an isolated `AL-…` CS project, (c) drive CS through the full loop via the Chrome
  extension, and (d) produce a complete **run bundle** (`answer.md` + trace + citations + meta) — with **at
  most light human help** (card approvals, and any `NEEDS_HUMAN.md` prompts).

## Success criteria (graded, not pass/fail — it's a pilot)
1. **Bootstrap works** — CC reads `CLAUDE.md`, sets up, hands back a clean START PROMPT with a simple trigger.
2. **Isolation holds** — the run happens in a new `AL-exp000-QDIS-L1` project; the shared repo/labbook and any
   parallel project are untouched.
3. **Loop executes** — the phases run in order; CS actually queries connectors (not memory).
4. **Run bundle produced** — `OUTPUT/QDIS_arm_L_run1/` exists with the required files.
5. **Honest degradation** — if it stalls, we get a `NEEDS_HUMAN.md` + a `RUN_REPORT.md` blackbox report rather
   than a fabricated answer.

## What we will learn (feeds exp-001 + the loop design D2/D3)
- Where the CC stalls or needs a human (drive-channel friction, permission cards, "is CS done?" detection).
- Whether the bootstrap instructions are clear enough for "any future user" to trigger.
- How long one run takes end-to-end (budget/cadence calibration).
- Whether the run-bundle format captures what the scoring harness + eval site need.
Findings → a short blackbox report from the assistant/operator → CS updates `agentic-loop-v0.md`, the bootstrap, and
`STATUS.md` before exp-001 goes live.

## Explicitly out of scope for the pilot
Baseline (Arm B); the 3-persona scoring; the blinded the operator eval; the unblinded results HTML. Those are exp-001.
The pilot only has to prove the loop **runs** end-to-end and produces a bundle.
