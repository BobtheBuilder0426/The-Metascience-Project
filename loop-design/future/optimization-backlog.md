# Loop-optimization backlog — research points parked for LATER versions

These are **loop-optimization ideas** deliberately held out of the currently-tested bootstrap. Each is to be picked up
in a dedicated **loop-optimization research phase** (after the first clean end-to-end run), researched against
cutting-edge literature, designed, and then introduced as a **measured improvement category** against the working
baseline — the experiment-loop pattern (add one enhancement, measure the delta). None of these are bugs; they are
enhancements. Bugs/safety go straight into the current version instead.

Every item names the LABBOOK entry that parked it, so the decision trail is traceable.

## OPT-1 — Optimized CS project context (performance part of the Agent Context)
- **What:** the loop arm (Arm L) writes an **optimized** Claude Science project context (Agent Context) that raises CS
  output quality on general, question-agnostic axes — capability activation (use featured connectors / compute / skills),
  evidence & citation discipline, reasoning transparency, rigor & self-critique, completeness & actionability,
  uncertainty & anti-hallucination. Explicitly authorized by the operator as a **measured loop gain** (LB-065).
- **Hard line (keeps fairness):** GENERAL scientist-sharpening only. NEVER anything about the specific question's domain,
  the expected answer, or hints toward it — that would smuggle WHAT past the byte-identical-question rule.
- **How (decided direction, LB-065):** the driver COMPOSES it per run (Option 2), disciplined by a research-backed
  context-design guide CS will write; 6 candidate axes proposed for operator inspection.
- **Status:** RESEARCH ON HOLD (operator, LB-067). The *safety-only* isolation preamble is NOT part of this — that ships
  now (see the current bootstrap); only the performance-optimization context is parked here.
- **Parked by:** LB-065 (ruling), LB-067 (research deferred).

## OPT-2 — Driver CC literature-context research (question + inputs → sharpened driver context)
- **What:** after INTAKE captures the research question and the human's publication/file inputs, the driver CC runs a
  literature-context step — pulling related publications / background and digesting them — to sharpen ITS OWN context
  before it reframes and drives CS. Goal: the driver enters STEP 0 (reframe) already grounded in the surrounding
  literature, not just the handed-in files.
- **Open design questions for the research phase:** which sources (the CC's own tools vs asking CS to search); how much
  is fair vs. research advantage the baseline lacks; how to keep it question-general and avoid answer-priming; cost/time
  budget; overlap with OPT-1 and with the shelved multi-model synthesis module.
- **Status:** RESEARCH ON HOLD (operator, LB-067).
- **Parked by:** LB-067.

## OPT-3 — Multi-model literature-synthesis context module (already prepared)
- **What:** Claude + Codex → grounded, concise, quality-filtered topic report handed to the driver. Fully designed.
- **Status:** shelved in `multimodel-context-module/` until the first successful loop run.
- **Parked by:** LB-052.

---
When any item is activated: move its design into `loop-design/current/`, add it as an improvement category in the
experiment design, and cite the new LABBOOK entry here.
