<!-- [CS-authored] OPT-1 context-optimization — AXES + RUBRIC MAP. Operator inspection gate (LB-065 process:
     propose axes -> operator inspects -> THEN research). Activated from optimization-backlog.md OPT-1 for v8. -->

# OPT-1 — Optimized CS project context: candidate axes + rubric map (v8 research gate)

**Status:** proposed for operator inspection (this is the LB-065 gate — you approve/adjust the axes *before* the
literature harvest spends effort). **Scope:** the *performance* part of the CS project Agent Context that Arm L (the
loop) may write — explicitly authorized as a measured loop gain (LB-065). **Not** exp-001/v7 (v7 ships the safety
preamble only); this is the **v8 improvement category**.

## The one invariant everything obeys (fairness hard-line)
The optimized context may contain **only GENERAL scientist-sharpening** — how to work well as a scientist, question-
agnostic. It must **NEVER** contain anything about the specific question's domain, the expected answer, or any hint
toward it. General "use primary sources / show your reasoning / use your connectors" = fair. Anything that smuggles
*WHAT* is being asked past the byte-identical-question rule = forbidden. This is the boundary the whole experiment's
validity rests on; every axis below is written to stay inside it, and the evidence synthesis will re-check each drafted
line against it.

## Structure of the final context (guardrails stay intact)
Per LB-065 and the operator's v8 instruction, the optimized Agent Context is **two blocks**:
```
[ SAFETY PREAMBLE  — CS_PROJECT_PREAMBLE.md, VERBATIM, unchanged ]   ← required, both arms, fairness-neutral
[ PERFORMANCE BLOCK — the OPT-1 optimized scaffolding (Arm L only) ]  ← general scientist-sharpening only
```
The safety/guardrail preamble (2,145 B, ships in v7) is preserved **byte-for-byte** as the opening of the context — the
performance block is added *after* it, never in place of it. Arm B (baseline) gets the safety preamble alone.

## The candidate axes (6 from LB-067 + 1 new) mapped to the scored rubric
Every axis names the rubric dimension(s) it is *hypothesized* to move, so the harness can later **measure** whether it
did (per-dimension deltas already come out of `scorecard_long.csv`). Rubric dims (all weight 0.20): **grounding**
"Grounding & integrity", **reasoning** "Reasoning & soundness", **completeness** "Completeness & specificity",
**usefulness** "Usefulness & actionability", **creativity** "Creativity (novelty × plausibility)".

| # | Axis (general, fair) | Targets dimension(s) | Mechanism hypothesis (why the context should move it) |
|---|---|---|---|
| A1 | **Capability activation** — use featured connectors (Ensembl/UniProt/PDB/GEO/…), compute, skills | grounding, usefulness | CS under-uses its tools by default; naming them + "reach for real data/compute" raises real-evidence use and actionable, data-backed outputs |
| A2 | **Evidence & citation discipline** — primary sources, verify each citation, quote support | grounding | explicit source-quality + verification instructions reduce fabricated/weak citations, which our grounding cap already penalizes |
| A3 | **Reasoning transparency** — show the working, expose the chain | reasoning | eliciting an explicit chain improves and exposes reasoning soundness (and feeds the creativity reasoning-trace gate) |
| A4 | **Rigor & self-critique** — find your own errors before finishing | reasoning, grounding | a self-check/refine pass catches internal contradictions + unsupported steps before they reach the answer |
| A5 | **Completeness & actionability** — cover the ask fully, end with usable next steps | completeness, usefulness | structure/decomposition instructions reduce partial answers and raise concrete actionability |
| A6 | **Uncertainty & anti-hallucination** — calibrate, flag unknowns, don't over-claim | grounding | calibration/abstention guidance trades fabricated confidence for honest uncertainty (grounding-positive) |
| **A7** | **Novelty elicitation (NEW — your headline ask)** — push for genuinely new, non-obvious, recombinative hypotheses **while keeping them plausible** | **creativity**, reasoning | our creativity = novelty × plausibility × reasoning-trace (multiplicative gate); the context must lift *novelty without collapsing plausibility* — the precise "scientific-breakthrough" lever, and the hardest to get right |

## Two validity guards baked in from the start
1. **Context-rot / dose.** More context is not strictly better — over-long or over-stuffed system prompts dilute
   instruction-following and can *lower* quality. So v8 tests a **dose-response** (safety-only control → lean → full),
   to find the optimal amount, not merely on/off. (This is why step 5 drafts 3 variants, not 1.)
2. **No overfitting to the 3 test questions.** The context must be question-general and is frozen before the run; the
   submission's final question is deliberately distinct from the test set (standing threat-to-validity control). The
   subagent pre-screen (step 6) will watch for a variant that helps our 3 questions suspiciously more than it generalizes.

## Operator refinements folded into this research (v8 GO instruction)
- **General agent-harness + system-prompt guidelines** get their own first-class harvest track (step 2), alongside the
  per-axis technique papers — including vendor-specific Claude/Anthropic prompting guidance (CS *is* Claude, so it
  applies directly) and our own S-005 harness survey. The question "what is a perfect system prompt for *this* situation"
  is answered from that track, not from prompt-craft folklore.
- **Subagent testing after drafting** (step 5→6): the drafted candidate contexts are run as real system prompts on our
  actual questions via subagents and scored by the existing harness, iterating to an optimized final version — evidence,
  not taste, picks the winner.
- **Guardrails intact:** the safety preamble is a required, verbatim section of every candidate (above).

## What is NOT decided here (for the research + your inspection)
- Final wording of any axis (that's steps 3–5, evidence-first).
- Whether all 7 axes survive — a weak-evidence axis (see step 3) may be dropped rather than shipped on folklore.
- The exact dose split (lean vs full boundary) — set after the pre-screen.
- Relationship of A7 to the loop's *own* idea-generation moves (ERA-style injection/recombination, S-002; Co-Scientist
  hypothesis evolution, S-004) — the context primes CS; the loop structure is a separate lever (kept distinct).