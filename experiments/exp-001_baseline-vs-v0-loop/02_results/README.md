<!-- WHAT THIS IS: where the 6 coded answer folders land. HOW IT'S FILLED (operator): after both arms finish, the
     operator renames the 6 presentation folders to a PRIVATE shuffle R1…R6 (keeping {Rn→question,arm} = Key-1,
     operator-held) and copies the ARM-STRIPPED folders here. CS then scores from them, blind. -->

# exp-001 — 02_results/  [operator copies coded answers R1…R6 here; CS scores blind]

## What lands here (HANDOFF ②, Key-1 applied)
Six folders `R1/ … R6/` (one per question×arm, arm-stripped), each a **presentation folder**:
```
R<n>/
├── result.md          the final answer + the case for it
├── reasoning.md       the line of thought
├── figures/           plots / tables / artefacts produced
├── sources.md         every source, with identifiers
└── process_trace.json action-labelled record of what was actually done (CS scores this; NOT shown to the operator)
```
The operator holds Key-1 (`{Rn → question, arm}`) and does **not** give it to CS until unblinding. CS therefore scores
without knowing which arm any `Rn` is.

## Then (CS, HANDOFF ③ onward)
CS runs `../01_setup/harness/run_scoring.py` over `R1…R6` → `scoring/scorecard.csv` + `scoring/scorecard_long.csv`
(one row per code × dimension × scorer) + `scoring/scorecard.json`. Blinded, idempotent, re-runnable from these folders.

*(the assistant is NOT involved unless a run crashed — then he writes a blackbox forensic report, per LB-032.)*
