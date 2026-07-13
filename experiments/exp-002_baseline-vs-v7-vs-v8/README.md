# exp-002 — baseline vs v7 loop vs v8 loop

**The first loop-optimization experiment.** Tests whether **OPT-1** (a per-question composed CS project Agent Context,
via the `context-composer` skill) makes the loop measurably better. Three arms, same 3 locked aging-biology questions:

| Arm | What it is | CS project context |
|-----|-----------|--------------------|
| **B**  | baseline — blank Claude Science, one cold response, no loop | safety preamble only |
| **L7** | the v7 Agentic Loop (`../exp-001…/01_setup/v7_cc-bootstrap`) driving CS | safety preamble only |
| **L8** | the v8 loop (`01_setup/v8_cc-bootstrap`) — v7 **+** composed context | safety preamble **+** task-sharpened performance block |

**The single changed variable (L7 → L8) is the CS project context.** All other loop machinery is byte-identical, so
this is a clean A/B/C isolating the one optimization.

## Folder map
- `00_hypothesis.md` — the H1/H2/H0 hypotheses + endpoint + fairness invariants.
- `01_setup/protocol.md` — how each arm is run + the scoring contract.
- `01_setup/v8_cc-bootstrap/` — **the loop under test** (Arm L8). Built from v7 (clean 23-file copy) + the
  `context-composer` skill (+3 files) + 2 wiring edits. `LOOP_VERSION.md` records the version name, content hash
  (`92ea3b4abcae5794`), and exactly what v8 adds over v7.
- `02_results/` — the 9 collected presentation folders (`<QID>_arm_<B|L7|L8>_run01/`).
- `04_evaluation/` — the operator's blind HTML eval outputs. `05_analysis/` — CS scoring + analysis.

## Shared infrastructure (not duplicated here)
- **Questions:** the 3 locked questions live in `../exp-001…/01_setup/test-set/` — same set, same categories.
- **Harness:** scoring reuses `../exp-001…/01_setup/harness/` (arm-generic core). The 3-arm delta+figure extension is
  the documented next build step (see STATUS + `01_setup/protocol.md`).
- **v7 loop (Arm L7):** run from `../exp-001…/01_setup/v7_cc-bootstrap/` (or the exp-000 maintained source) — **not
  copied or modified here**; v7 is locked.

## Provenance
Loop version: **v8_cc-bootstrap** (content hash `92ea3b4abcae5794`; base v7 `6bbd94a13d13e462`). Built + documented in
**LB-080**; the OPT-1 skill it ships was built + subagent-tested in **LB-079**.
