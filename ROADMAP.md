# the Metascience Project ROADMAP -- [FINAL]

<!-- WHAT THIS FILE IS: the phase plan from setup to submission. Each phase states its goal, what must be documented,
     and what CLOSES it / opens the next. HOW TO USE: read it to see the whole path; STATUS.md tells you which phase we
     are in right now + the immediate next action. Update THIS file only if the plan itself changes; update STATUS.md
     after every step. The LABBOOK is the full ground-truth history. -->

**Deadline:** Mon 2026-07-13 21:00 ET (= Tue 2026-07-14 03:00 CEST). Target + success criteria: `GOAL.md`.

**How the three docs work together:** `ROADMAP.md` = the plan (phases + gates) - `STATUS.md` = where we are right now
(updated after every step) - `LABBOOK.md` = the full, append-only history (the ground truth). A phase advances only
when its **Done-when** gate is met; every step is logged in the labbook and reflected in STATUS.

---

## Phase 0 -- Setup & GOAL  [DONE]
- **Goal:** a self-contained repo + bridge + structure + resources + a locked GOAL.
- **Document:** LB-001..008 (structure, review fixes, resources, handbook, papers, GOAL, roadmap+status).
- **Done when:** GOAL final + resources in place + repo self-contained + roadmap/status live. **[met]**

## Phase 1 -- CS designs the Experiment Loop  [NEXT]
- **Environment pre-check (first):** CS self-checks its reachable environment; then CS hands a short pre-check prompt to a blank Claude Code, which verifies the CC-side environment CS depends on (Chrome control + Codex -- both CC-side -- + the local runtime) and reports back to CS. Confirm before building the runnable core.
- **Goal:** Claude Science works out HOW it will run the experiments -- its experimental design, the **quantification
  methods** that make "better" measurable, and the **test/baseline strategy** -- and produces the first setup.
- **Document:** a labbook entry for the design decision; `experiments/exp-001_<slug>/00_hypothesis.md` + `01_setup/`.
- **Done when:** exp-001 setup exists (bootstrap + workspace + protocol + test-set + for-the operator specs) AND the
  quantification + test/baseline strategy are written down.

## Phase 2 -- Run the Experiment Loop (iterate)
- **Goal:** run exp-NNN cycles, testing improvement categories, until the Agentic Loop stops improving materially.
- **Cycle:** CS setup -> blank CC runs it independently -> the assistant analyses + reports + pulls data back -> the operator evaluates
  -> CS analyses + next hypothesis (+ promote to `loop-design/` if improved).
- **Document:** per experiment `00..05` + a `experiments/RESULTS-LOG.md` row + `loop-design/CHANGELOG.md` on each
  promotion; a labbook entry each step.
- **Target scale:** aim for **>=3 iterations, 2 tests each** as the go-to; adjust as it goes (bounded by compute + time).
- **Done when:** improvements plateau (or the time-box is hit) AND the improvement report (GOAL D2) is written.

## Phase 3 -- Lock the final Agentic Loop
- **Goal:** promote the best loop to `loop-design/current/`, made downloadable + self-bootstrapping.
- **Document:** `loop-design/CHANGELOG.md` final version + a labbook entry.
- **Done when:** a fresh download + a blank Claude Code bootstraps the working loop (verified).

## Phase 4 -- Final run (the real question)
- **Goal:** the operator's real question -> raw blank Claude Science baseline vs. blank Claude Code + final loop (word-identical)
  -> the finding.
- **Document:** `final-run/` (question + both arms + results + report); labbook.
- **Done when:** the finding is produced AND the controlled comparison is documented.

## Phase 5 -- Report + submit
- **Goal:** one publication-style report (= basis for the demo + summary) -> 3-min video + 100-200w summary -> submit repo.
- **Document:** the report; `submission/` filled (checklist all green); README + LICENSE finalized.
- **Done when:** submitted via the CV platform before the deadline.
