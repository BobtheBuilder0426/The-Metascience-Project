<!-- [CS-authored] OPT-1 step 4 — the research-backed context-design guide (the guide LB-065 committed to).
     Defines the STRUCTURE + section-by-section content of an optimal CS Agent Context (Arm L only), every element
     traceable to a cited principle (P1..P12 in opt1-evidence-synthesis.md; S-054..S-069 in opt1-annotated-bibliography.md).
     Fairness hard-line + anti-overfitting are non-negotiable constraints. Includes the driver composition rules. -->

# OPT-1 — Research-backed CS context-design guide

**What this is.** The rules for composing the *performance block* of the CS project Agent Context that the loop (Arm L)
adds on top of the safety preamble. It is evidence-first: every section cites the principle (P#) and source (S-###) it
rests on, and only **Adopt** / **Use-with-care** principles from the synthesis are allowed in. It is the discipline
LB-065 required before any optimized context ships.

## 0. The two hard constraints (non-negotiable, checked on every draft)
1. **Fairness hard-line.** The performance block contains ONLY general, question-agnostic scientist-sharpening. It must
   never name or hint at the question's domain, the expected answer, or the field. If a line would read differently
   depending on which of our 3 test questions is being answered, it is too specific — cut it. (Re-checked line-by-line
   at draft time and again at pre-screen.)
2. **Guardrails intact.** The safety preamble (`CS_PROJECT_PREAMBLE.md`) is the **verbatim opening** of the Agent
   Context. The performance block is appended **after** it, never edited into it, never replacing it. Arm B gets the
   safety preamble alone.

## 1. Overall shape of the Agent Context
```
┌─────────────────────────────────────────────────────────────┐
│ [BLOCK 1]  SAFETY PREAMBLE  — verbatim from CS_PROJECT_PREAMBLE.md │  ← both arms; unchanged
│            (scope & safety boundary, run-identity slot filled)     │
├─────────────────────────────────────────────────────────────┤
│ [BLOCK 2]  PERFORMANCE BLOCK  — the OPT-1 optimized scaffolding    │  ← Arm L only; general only
│            §A capability activation                               │
│            §B evidence & citation discipline                      │
│            §C reasoning transparency                              │
│            §D anchored self-critique         (full context only)  │
│            §E completeness & actionability                        │
│            §F honest uncertainty                                  │
│            §G novelty, paired with plausibility (full only)       │
└─────────────────────────────────────────────────────────────┘
```
Ordering rationale (S-045 lost-in-the-middle): the safety boundary and the highest-value performance sections lead;
nothing critical is buried mid-context. Total length is capped (see §3 dose).

## 2. Section-by-section content (each traceable to evidence)
Written as *instruction intent*, not final wording (wording drafted in step 5, tested by subagents in step 6).

- **§A Capability activation** — *P1 (S-054 harness design, S-005).* Tell CS it has real featured connectors
  (biomedical/genomic/structural/literature data), compute, and skills, and that strong answers reach for real data and
  computation rather than working from memory. General — names capabilities, never a dataset for the question.
- **§B Evidence & citation discipline** — *P2 (S-050 attribute-first, S-051 CoVe).* Prefer primary sources; every
  citation must be real and verifiable; quote or point to the supporting span; distinguish primary from review. This is
  the grounding-cap the harness already enforces, stated as guidance.
- **§C Reasoning transparency** — *P3 (S-056 self-consistency, S-058).* Show the reasoning that leads to each claim;
  make the logical chain explicit and followable. Kept lean (S-058: the nudge need not be elaborate). Also feeds the
  creativity reasoning-trace gate.
- **§D Anchored self-critique** *(full context only)* — *P5 (S-059 self-refine, S-060 Reflexion) + self-correction
  caveat.* Before finalizing, run one critical pass anchored to **concrete checks**: are all citations real and
  supporting? any internal contradictions? any unsupported leap? Explicitly NOT a vague "review yourself" (unaided
  self-correction can backfire). Debate is deliberately absent (P6 cut, S-069 contested).
- **§E Completeness & actionability** — *P7.* Address every part of the ask; where relevant, decompose; end with
  concrete, usable next steps a scientist could act on.
- **§F Honest uncertainty** — *P8 (S-066, S-052).* State assumptions, flag what's unknown or weakly supported,
  calibrate confidence. Framed as honest-uncertainty (calibration ≠ "never hallucinate", S-066), which is
  grounding-positive.
- **§G Novelty paired with plausibility** *(full context only)* — *P9 (S-062, S-064) + P10 cut (S-063).* Seek genuinely
  novel, non-obvious, recombinative ideas — **and in the same breath** require that each is mechanistically plausible
  and carries an explicit reasoning line. Never novelty for its own sake (execution-gap caveat). This is the exact
  shape of our creativity gate (novelty × plausibility × reasoning-trace), so §G *is* the gate, restated as guidance.

## 3. Dose (why 3 variants, and what goes in each)
Motivated by P12 (context rot: S-045/S-046) and S-055 (prompts have an optimum):
- **C0 — safety-only (control).** Block 1 only. Identical to what Arm B receives. Proves the floor.
- **C1 — lean.** Block 1 + §A,§B,§C,§E,§F (the **Adopt** backbone). The bet: the strongly-supported levers give most
  of the gain at low context cost.
- **C2 — full.** C1 + §D,§G (the **Use-with-care** levers, in their anchored/paired form). Tests whether the
  conditional levers add value or whether the extra context dilutes (context rot).
Decision rule: if C2 ≤ C1 on the harness composite, ship **C1** (context-rot signal). This is measured, not assumed.

## 4. Anti-overfitting rules (standing threat-to-validity control)
- The context is **frozen before** any run and is **question-general** — it must help an arbitrary science question, not
  our 3.
- The **submission's final question is distinct** from the 3 test questions, so a context tuned to the test set gains
  nothing there.
- The step-6 pre-screen watches for a variant that helps the 3 test questions *disproportionately* vs its general
  phrasing — a red flag for overfitting, not a win.

## 5. Driver composition rules (how Arm L builds it per run — Option 2, LB-065)
The driver does NOT invent context per run. It **composes from this frozen guide**:
1. Take BLOCK 1 verbatim; fill only the run-identity slot (project name + granted folder), exactly as v7 already does.
2. Append the chosen dose's performance block (C0/C1/C2) — **fixed text from the frozen candidate**, not regenerated.
3. Never add anything question-specific. The driver has the question + digested inputs, but the CS context it writes
   stays general — the question itself travels only through the byte-identical question prompt, never the context.
4. Log which dose was used in the run's `run_log/` so the analysis can attribute the score to the context variant.

This keeps the loop's "compose per run" flexibility while guaranteeing fairness and reproducibility: the *only* thing
that varies between runs of the same arm is the dose we're deliberately testing.

## 6. What the harness will read back (closes the loop to measurement)
Because each section targets named rubric dimensions (see axis map), the per-dimension deltas in `scorecard_long.csv`
are the direct test of whether each lever worked: §A/§B/§F → grounding; §C/§D → reasoning; §E → completeness+usefulness;
§A/§E → usefulness; §G → creativity. A lever that moves its target dimension is kept; one that doesn't is dropped in the
next iteration. Evidence, not folklore, decides what stays.