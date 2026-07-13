# loop-design/future/ — prepared but NOT-YET-ACTIVE loop optimizations

Modules here are fully designed and ready, but deliberately **held out of the currently-tested bootstrap**. They are
optimizations to add as measured improvement categories **after** one clean end-to-end loop run succeeds (the
experiment-loop pattern: introduce each enhancement against a working baseline and measure the delta).

## Contents
- `multimodel-context-module/` — multi-model literature-synthesis context brief (Claude + Codex → grounded, concise,
  quality-filtered topic report handed to the driver). Deferred per LB-052 (operator decision 2026-07-10). Excluded from
  the v6 driver handoff package until the first successful loop run.
- `optimization-backlog.md` — parked loop-optimization RESEARCH points to revisit later: OPT-1 optimized CS project
  context (perf part of Agent Context, LB-065), OPT-2 driver CC literature-context step (LB-067), OPT-3 = the
  multi-model module below. Safety-only context preamble is NOT here — it ships in the current bootstrap.
