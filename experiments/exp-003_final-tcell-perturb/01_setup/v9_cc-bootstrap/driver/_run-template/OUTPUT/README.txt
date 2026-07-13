TEMPLATE (shape only — not a live run). Each prepared run gets its OWN copy of this folder at
driver/AL-<name>/OUTPUT/, where that run's driver writes run-01/ with TWO sibling areas:
  run-01/presentation/  ← the evaluated folder: result.md, reasoning.md, figures/, sources.md, process_trace.json
  run-01/run_log/       ← loop machinery (NOT evaluated): reframed_brief.md, run_log.md, meta.json, RUN_REPORT.md
Collect presentation/ for evaluation. See driver/CLAUDE.md (substitute your ⟨RUN⟩).
