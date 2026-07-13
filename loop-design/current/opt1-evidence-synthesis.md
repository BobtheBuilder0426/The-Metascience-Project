<!-- [CS-authored] OPT-1 step 3 — evidence synthesis. Turns the annotated bibliography (S-054..S-070 + reused
     S-002/004/005/051/052) into design principles, each tagged by rubric dimension + effect direction + evidence
     strength + whether Claude-specific. Weak/contested levers are flagged and CUT, not shipped on folklore. -->

# OPT-1 — Evidence synthesis → design principles (honest edition)

**Purpose.** Distill the harvest into the *defensible* levers only. Each principle names: the axis, the rubric
dimension it should move, the effect direction, the evidence strength, and whether it's Claude-specific. The design
guide (step 4) may use only **Adopt** principles; **Use-with-care** principles ship in reduced/anchored form;
**Cut** items are explicitly excluded so we don't build on folklore.

## Principle table

| P | Principle (context lever) | Axis | Rubric dim | Effect | Evidence | Verdict |
|---|---|---|---|---|---|---|
| P1 | Name CS's real capabilities (connectors, compute, skills) + instruct to reach for real data | A1 | grounding, usefulness | ↑ real-evidence use, ↑ actionability | S-054 harness-design (Emerging) + our S-005 | **Adopt** |
| P2 | Instruct: prefer primary sources, verify every citation, quote the supporting span | A2 | grounding | ↑ citation validity, ↓ fabrication | S-050 attribute-first + S-051 CoVe (Established) | **Adopt** |
| P3 | Elicit an explicit reasoning chain ("show your working") | A3 | reasoning | ↑ reasoning soundness (+ feeds creativity trace-gate) | S-056 self-consistency (Established), S-058 (keeps it lean) | **Adopt (lean)** |
| P4 | Encourage deliberate, branch-and-evaluate thinking on hard sub-problems | A3 | reasoning | ↑ on exploration-heavy tasks | S-057 ToT (Established) — but inference-cost heavy | **Use-with-care** (encourage, don't mandate full ToT) |
| P5 | A self-critique/refine pass **anchored to concrete checks** (verify citations, check internal consistency) before finishing | A4 | reasoning, grounding | ↑ when anchored; ↓ if unaided/vague | S-059 self-refine, S-060 Reflexion (Established) **but** self-correction-limits caveat | **Use-with-care** (must be anchored, not "review yourself") |
| P6 | Multi-agent **debate** baked into the context as a settled reasoning win | A4 | reasoning | fragile under fair baselines | S-069 (Contested), S-061 mixed | **Cut** from OPT-1 (belongs to shelved OPT-3 multi-model module) |
| P7 | Cover the ask fully + decompose + end with concrete next steps | A5 | completeness, usefulness | ↑ completeness, ↑ actionability | S-070 least-to-most decomposition (Established) | **Adopt** |
| P8 | Calibrate confidence, flag unknowns, state assumptions — honest uncertainty, not false confidence | A6 | grounding | ↑ honesty; note calibration≠zero-hallucination | S-066 calibrated-must-hallucinate (Emerging), S-052 SelfCheckGPT | **Adopt (framed as honest-uncertainty)** |
| P9 | Push for genuinely novel, non-obvious, **recombinative** hypotheses — explicitly *paired* with a plausibility + reasoning-line requirement | A7 | creativity | ↑ novelty; risk ↓ plausibility if unpaired | S-062 (novel>experts but ↓feasibility), S-064 (measure novelty×quality) | **Use-with-care (paired)** |
| P10 | Trust apparent novelty as end-value | A7 | creativity | apparent novelty ≠ executed value | S-063 ideation-execution gap (decisive caveat) | **Cut** the "novelty alone" framing — gate stays multiplicative |
| P11 | Persona/role-play prompting ("you are a Nobel laureate") | A7/A3 | — | mixed/unreliable effect | broad mixed evidence, no strong anchor in harvest | **Cut** (folklore; not shipped) |
| P12 | Maximal, exhaustive context ("more instructions = better") | all | all | dilutes instruction-following | S-045 lost-in-the-middle, S-046 power-of-noise, S-055 (prompts have an optimum) | **Cut** — motivates the dose-response test instead |

## The honest headline
- **Strongly supported, ship confidently:** P1, P2, P3, P7, P8 — capability activation, citation discipline, lean
  reasoning-transparency, completeness/actionability, honest uncertainty. These are the backbone of the optimized context.
- **Supported but conditional, ship carefully:** P4 (encourage deliberateness, don't mandate expensive search), P5
  (self-critique **must** be anchored to concrete checks — unaided self-correction can backfire), P9 (novelty **paired**
  with plausibility + a reasoning line, never solo).
- **Cut so we don't build on sand:** P6 multi-agent-debate-as-settled (contested — kept for the separate OPT-3 module),
  P10 novelty-as-end-value (execution gap), P11 persona prompting (folklore), P12 max-context (context rot).

## Why this shape is fair (re-checked against the invariant)
Every Adopt/Use-with-care principle is **question-agnostic scientist-sharpening** — "verify citations", "show reasoning",
"flag uncertainty", "seek novel-but-plausible hypotheses". None encodes the domain, the expected answer, or a hint.
The fairness hard-line holds. (Verified line-by-line again when the guide is drafted in step 4.)

## The dose-response falls out of the evidence
P12 + S-055 (prompts have an optimum) say directly: test **safety-only (C0) → lean (C1) → full (C2)**, don't assume
full is best. C1 = the strongly-supported backbone (P1,P2,P3,P7,P8). C2 = backbone + the conditional levers (P4,P5,P9)
in their anchored/paired form. If C2 ≤ C1 on the harness, that is the context-rot signal and we ship C1.

## Claude-specific note
CS is Claude, so vendor prompting conventions apply directly (structured sections, explicit-instruction-following,
tool-use framing). The levers above are model-general; the *wording* in step 4 will follow Claude conventions, which is
a wording choice, not a new lever — so it needs no separate evidence claim.