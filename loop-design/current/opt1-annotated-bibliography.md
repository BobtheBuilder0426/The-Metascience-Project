<!-- [CS-authored] OPT-1 step 2 — annotated bibliography from the grounded literature harvest.
     Every entry is a REAL paper retrieved via the literature connector (arXiv + OpenAlex), registered in SOURCES.md
     (S-054+). Citation counts from OpenAlex where indexed; N/A where the work is a recent preprint OpenAlex hadn't
     cleanly indexed at harvest time (2026-07-11) — flagged, never guessed. Tagged by axis + finding + evidence strength. -->

# OPT-1 — Annotated bibliography (grounded harvest, 2026-07-11)

**Method.** Harvested via the `literature` connector: arXiv full-text search across 10 tracks (general
harness/system-prompt guidelines first, per the v8 GO), then OpenAlex for citation counts / venue to grade evidence
strength. Anchor abstracts read before annotating. Evidence-strength scale: **Established** (widely cited + replicated),
**Emerging** (peer-reviewed or well-cited but recent), **Single-study** (one paper, not yet replicated), **Contested**
(direct counter-evidence exists). No claim below is stated more strongly than its source supports.

## Track 1 — General agent-harness + system-prompt design (the "perfect prompt for this situation" track)
- **S-054 · The Interplay of Harness Design and Post-Training in LLM Agents** (arXiv 2606.25447, 2026). The *harness*
  — which tools are exposed, how they're described, what accompanies each observation — is usually treated as a fixed
  engineering detail, yet it materially shapes agent behavior. **Directly grounds axis A1**: naming/describing CS's
  connectors + compute in the context is a harness-design lever, not decoration. *Evidence: Emerging.*
- **S-055 · SePO: Self-Evolving Prompt Agent for System Prompt Optimization** (arXiv 2606.04465, 2026). System-prompt
  optimization improves agent behavior *without* touching the model, yielding human-readable, model-agnostic
  instructions. **Grounds the whole OPT-1 premise** — that a better CS project context is a real, measurable lever —
  and the dose-response idea (prompts are an optimization target with an optimum, not "more = better"). *Emerging.*
- **S-005 (already registered) · Agent-harness survey** — reused: harness > model, outer-loop scaffolding. Our own
  method-foundations anchor; applies here as the general-scaffolding backbone.

## Track 2 — Reasoning elicitation (targets rubric: reasoning)
- **S-056 · Self-Consistency Improves Chain-of-Thought Reasoning** (arXiv 2203.11171; OpenAlex cit≈702). Sample
  multiple reasoning paths, marginalize to the most consistent answer — one of the most-replicated reasoning gains.
  **Grounds A3** (elicit + expose reasoning). *Established.*
- **S-057 · Tree of Thoughts: Deliberate Problem Solving** (arXiv 2305.10601; OpenAlex cit≈566). Generalizes CoT to
  search over reasoning branches with lookahead/backtracking. **Grounds A3/A4** (deliberate, self-evaluating reasoning).
  *Established.* Caveat: heavier inference cost — a context can *encourage* deliberateness without mandating full ToT.
- **S-058 · Chain-of-Thought Reasoning Without Prompting** (arXiv 2402.10200, 2024). CoT paths can be elicited by
  altering decoding, not just prompt wording — implies a context nudge toward "show your working" is low-cost and need
  not be elaborate. *Emerging.* Keeps A3 lean.

## Track 3 — Self-critique / reflection (targets: reasoning, grounding)
- **S-059 · Self-Refine: Iterative Refinement with Self-Feedback** (arXiv 2303.17651; OpenAlex cit≈214). The same model
  critiques then refines its own output, no extra training. **Grounds A4** (a self-critique pass before finishing).
  *Established.* Caveat below (self-correction limits).
- **S-060 · Reflexion: Language Agents with Verbal Reinforcement Learning** (arXiv 2303.11366; OpenAlex cit≈271).
  Verbal self-reflection on failed attempts improves subsequent tries. **Grounds A4** in the loop/iterative setting.
  *Established.*
- **S-061 · Diversity of Thought Elicits Stronger Reasoning in Multi-Agent Debate** (arXiv 2410.12853, 2024). Debate
  helps at any scale, and *diversity of thought* is the active ingredient. **Grounds A4** (self-critique from varied
  angles) and connects to our loop's own multi-lens moves — but see the contested entry. *Emerging.*

## Track 4 — Creativity / novelty (targets: creativity — the focal, hardest axis A7)
- **S-062 · Can LLMs Generate Novel Research Ideas? A Large-Scale Human Study with 100+ NLP Researchers** (Si et al.,
  arXiv 2409.04109; OpenAlex cit≈41). The key empirical result: LLM-generated ideas were judged **more novel** than
  expert human ideas, but **slightly weaker on feasibility** — the exact novelty↔plausibility tension our creativity
  gate encodes. **Directly grounds A7** and the design target "lift novelty without collapsing plausibility."
  *Emerging (landmark but recent).*
- **S-063 · The Ideation-Execution Gap** (arXiv 2506.20803, 2025; OpenAlex cit≈5). Follow-up: when LLM ideas judged
  *more novel* were actually **executed**, they did **not** produce better research than human ideas. **Critical
  caveat for A7** — apparent novelty ≠ downstream value; this is exactly our plausibility × reasoning-trace gate's job.
  *Single-study — but a direct, sobering counterweight; cited prominently so A7 doesn't over-claim.*
- **S-064 · Measuring LLM Novelty as the Frontier of Original AND High-Quality Output** (arXiv 2504.09389, 2025).
  Novelty must be measured jointly with quality — originality alone can be low-quality. **Validates our multiplicative
  gate** (novelty × plausibility) over a novelty-only score. *Emerging.*
- **S-065 · Can LLMs Unlock Novel Scientific Research Ideas?** (arXiv 2409.06185, 2024). Examines idea generation from
  papers; manual evaluation the default. Corroborates A7 feasibility but methodologically lighter than Si et al.
  *Single-study.*

## Track 4.5 — Task decomposition / completeness (targets: completeness, usefulness — axis A5)
- **S-070 · Least-to-Most Prompting Enables Complex Reasoning** (arXiv 2205.10625, 2022). Decompose a task into ordered
  sub-problems and solve them in sequence; improves easy-to-hard generalization over flat CoT. **Grounds A5** — the
  "address every part / decompose a large problem / finish with concrete next steps" instruction. *Established.*

## Track 5 — Anti-hallucination / verification / calibration (targets: grounding)
- **S-051 (already registered) · Chain-of-Verification (CoVe)** — reused: draft → plan verification questions → answer
  them independently → revise. **Grounds A6** (self-verification pass) and reinforces A2. *Established* (OpenAlex cit≈182).
- **S-066 · Calibrated Language Models Must Hallucinate** (arXiv 2311.14648, 2023). A theoretical result: calibration
  and zero-hallucination are in tension — so A6 must aim for *honest uncertainty flagging*, not an impossible "never
  hallucinate." **Keeps A6 realistic.** *Emerging.*
- **S-052 (already registered) · SelfCheckGPT** — reused: sample-consistency hallucination detection. A cheap A6 guard.

## Track 6 — Scientific-discovery agents (whole-loop context, cross-axis)
- **S-067 · Agentic AI Scientists Are Not Built for Autonomous Scientific Discovery** (arXiv 2605.08956, 2026).
  Position paper: current systems function as **co-scientists**, not autonomous discoverers (problem-selection bias,
  missing tacit/failure knowledge). **Frames scope honestly** — OPT-1 sharpens a co-scientist, and we shouldn't sell
  the loop as more. *Emerging (position).*
- **S-068 · The AI Scientist-v2: Workshop-Level Automated Discovery via Agentic Tree Search** (arXiv 2504.08066, 2025).
  End-to-end agentic system; hypothesize → experiment → analyze → write, via tree search. **Cross-axis reference** for
  what a strong scaffold + context looks like in practice. *Emerging.*
- **S-002/S-004 (already registered)** — reused: ERA (idea injection/recombination) and Co-Scientist (tournament +
  hypothesis evolution). The loop's *own* idea-generation structure; A7 primes CS to meet it.

## Contested / counter-evidence (kept in view so the design isn't folklore)
- **S-069 · Stop Overvaluing Multi-Agent Debate — Rethink Evaluation and Embrace Model Heterogeneity** (arXiv
  2502.08788, 2025). Systematic re-evaluation across 9 benchmarks / 4 models finds MAD's reported gains fragile under
  fair baselines. **Contested.** Consequence for us: do **not** bake multi-agent-debate assumptions into the CS context
  as if settled; keep A4 to single-model self-critique (well-supported) and leave debate to the separately-tested,
  operator-shelved multi-model module (OPT-3), not OPT-1.
- **Self-correction limits (noted, tracked for step 3):** several 2024 works report that unaided self-correction can
  *degrade* reasoning when the model has no external signal. Consequence: A4's self-critique should be anchored to
  concrete checks (verify citations, check internal consistency), not a vague "review yourself."

## Coverage note
All 7 axes now have ≥1 grounded source — A1 (Track 1), A2 (S-050/S-051), A3 (Track 2), A4 (Track 3), A5 (S-070,
Track 4.5), A6 (Track 5), A7 (Track 4); the two highest-value/hardest (A7 novelty, A4 self-critique) have both
supporting AND counter-evidence, which is the honest state of the field. Weak spots to resolve in step 3's synthesis:
whether A4 survives as single-model-only, and how hard A7 can push before the plausibility gate should hold it back.