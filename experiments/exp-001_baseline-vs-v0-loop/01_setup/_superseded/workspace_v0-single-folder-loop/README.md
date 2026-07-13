<!-- Authored by [CS] for exp-001. This is the blank CC's SCRATCH SPACE — the only place it writes. -->

# exp-001 — workspace (the blank CC's only writable area)

This folder **IS the blank CC's start package**: a context-less Claude Code started here auto-reads `CLAUDE.md` and runs
the loop from it. It ships with `CLAUDE.md` + this README + `materials/` + the `harness/` package; the CC writes all run
outputs here and nowhere else.

**Ships in the package (present before any run):**
| File | What it is |
|---|---|
| `CLAUDE.md` | the CC's auto-loaded operating manual — identity, fairness rule, and the runnable v0 loop (STEP 0 REFRAME → … → INTEGRATE) |
| `README.md` | this file map |
| `materials/` | the two Q_ERGO PDFs (attached to CS for every Q_ERGO run, both arms) |
| `harness/` | the Metascience Project scoring harness (CS-side scoring, NOT run by the CC) |

**Produced by the CC during a run:**
| File / folder | What it is |
|---|---|
| `run_log.md` | timestamped line per action (see `../protocol.md`) |
| `OUTPUT/` | holds the 8 **run bundles** (one folder per answer-run) — this is the whole deliverable the operator copies into `02_results/` |
| `OUTPUT/<QID>_arm_<B\|L>_run<N>/` | one run bundle: `answer.md` + `figures/` + `process_trace.json` + `citations.json` + `meta.json` (+ `reframed_brief.md` for Arm L). Full layout in `CLAUDE.md` → "OUTPUT". |
| `RUN_REPORT.md` | the structured self-report CS analyses (sections fixed in `../protocol.md`) |
| `NEEDS_HUMAN.md` | (only if stuck) what a human must click/paste if autonomy breaks |

(8 run bundles total = 2 questions × 2 arms × 2 runs; each bundle = one answer-run.)

## `harness/` — the scoring harness (CS-side, NOT run by the blank CC)
`harness/` holds the Metascience Project scoring harness that CS's research side uses to score the two answers AFTER the run. The
blank CC does **not** run it (the CC only produces the answer files). It ships here so the experiment is self-contained
and reproducible. Quick check that it's intact (optional, offline):
```
cd harness && python test_dryrun.py     # expect: 13 checks, 0 failures, ALL PASS
```
Real scoring (CS-side, inside a CS session with `host`): see `harness/README.md` → "Real mode".

## Isolation reminder
The blank CC writes ONLY inside this `workspace/`. It never touches the shared research repo or labbook — that
isolation is what keeps it a *blank* driver and the experiment clean.
