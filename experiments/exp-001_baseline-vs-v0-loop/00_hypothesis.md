<!-- Authored by [CS] for exp-001. The iteration hypothesis. -->

# exp-001 — Hypothesis: does the v7 Agentic Loop beat raw Claude Science?  [CS]

## The experiment in one sentence
exp-001 establishes the **foundational baseline** of the whole project: on real aging-biology questions, does a **blank
Claude Code running the Agentic Loop shipped in `v7_cc-bootstrap` to drive Claude Science (Arm L)** produce a
**measurably better answer** than **raw Claude Science answering the same word-identical question cold (Arm B)**?
*(Loop version tracks the bootstrap-folder version: the loop under test here = v7. The `v0-loop` in this folder's slug
is legacy naming for "the first loop we test" — it is the v7-shipped loop.)*

## Hypothesis
**H1 (primary):** Arm L > Arm B on the weighted **combined mean(CS,the operator) composite** (rubric.json v2, **5 dimensions at
equal 0.20**: grounding-&-integrity · reasoning-&-soundness · completeness · usefulness · creativity), **consistently
across the 3 test questions**
(see endpoint below). The v0 loop's mechanism for this advantage is concrete and pre-registered: (i) the **plan-review**
phase injects ambition + flags hallucination risk before the expensive step (operator finding D); (ii) **enforced
literature use + citations** (finding G) raises Grounding via the harness's citation-verification cap; (iii) the
**KEEP-first correctness pass** (finding F) removes unverifiable claims a cold answer would leave in.

**H0 (null):** the loop makes no difference (mean-Δ ≈ 0 or wins ≤1 of 3 questions), or hurts (over-engineering, drift).
A null or negative result is a **real, reportable finding**, not a failure — it tells us the flat loop is insufficient
and motivates the first improvement category (Mission-Control, C1).

## Changes vs `loop-design/current`
This is the FIRST experiment, so it does not change an existing loop — it **instantiates v0** (`agentic-loop-v0.md`)
and tests it against the raw baseline. v0 is deliberately **flat / single-session** (LB-021, operator's choice):
Mission-Control (C1) and the 2-lens×2-brain panel (C3) are explicitly held OUT so their benefit can be measured in later
iterations rather than assumed here.

## How we will know (success criteria — pre-registered) — see loop-design/current/dataflow-and-handoffs.md §5E
Design = **3 questions × 2 arms × 1 run = 6 answer-runs** (LB-072). With one run per cell there is no within-question
run-to-run SD; the signal is **consistency across the 3 questions**. Two complementary reads, BOTH decide success:
- **(1) Mean-Δ across questions (effect size):** Δ̄ = mean over the 3 questions of [composite(Arm L) − composite(Arm B)],
  on the **combined mean(CS,the operator) composite**. This is the headline number; report it with the spread of the 3
  per-question Δ.
- **(2) Win-count k/3 (consistency):** on how many of the 3 questions Arm L beat Arm B. **Strong = Δ̄>0 AND k=3;
  positive-but-inspect = Δ̄>0 AND k=2; null/negative = Δ̄≈0 or k≤1** (a real, reportable finding → motivates the next
  improvement category). Reported together — mean says *how much*, k/3 says *how reliably*.
- **Honest power caveat (pre-registered):** n=3 questions × 1 run is **descriptive, not inferential** — we make NO
  statistical-significance claim from 3 points. Strength comes from the per-dimension, per-scorer detail being
  consistent (below), not a p-value. Within-question replication + a real 3-way (baseline↔v7↔v8) return at v8.
- **Secondary (drift-robust):** Elo head-to-head (blinded pairwise, pooled per question) ranks L above B.
- **Dimension diagnosis:** each of the 5 dimensions plotted individually (Arm L vs B) under **CS / the operator / combined**
  scoring — so we learn which dimension drives Δ under whose scoring, not just *whether*.
- **Creativity honesty:** any creativity advantage must survive the reasoning-trace gate (a novel-but-unreasoned Arm-L
  answer must NOT score as creative — creativity-metric.md).
- **Human anchor + scoring model (LB-072):** per coded answer × dimension we keep **cs_score, human_score, and their
  mean**; the mean is the headline composite. the operator and CS are **averaged, not overridden**; their agreement (scatter +
  per-dimension deltas) is reported as an instrument-calibration result and is itself submission data.
- **Double-blind (LB-072):** two independent keys (operator-held R-codes blind CS; CS-held E-codes blind the operator);
  unblinding needs both. Means are computed while blind. Full method: loop-design/current/blinding-protocol.md.

## Scope + honesty notes
- exp-001 is n=**3 questions × 2 arms × 1 run** = 6 answer-runs (LB-072) — a **proof-of-instrument + first signal**,
  not a powered study. The three questions probe three distinct research capabilities (categories locked LB-074;
  concrete 3rd question PENDING operator lock): **(cat-1) day-in-the-lab** — ingest given publications → analyse →
  build a follow-up hypothesis + design the test experiment (**Q_ERGO** fills this); **(cat-2) maximum-creativity big-think**
  — a large unanswered biological question, generate + argue a genuinely new hypothesis (**3rd question, slot open**);
  **(cat-3) translational data breakthrough** — pull the right literature + datasets for a disease, analyse → predict a
  new treatment + argue it (**Q3** repurposing fills this). Together they guard against a one-question fluke and test
  whether the loop's advantage generalizes across task types. Later experiments add iterations (GOAL: ≥3 iterations);
  within-question replication + a 3-way baseline↔v7↔v8 arrive at the first loop optimization (v8).
- **Q_ERGO + Q3 are LOCKED (LB-026); the 3rd question (cat-2) is PENDING** operator lock. The output-format instruction
  is appended byte-identical to every question, both arms (LB-073). The run is gated on the 3rd-question lock + the
  one-pass file reconciliation (LB-073).
- **Baseline (Arm B) — locked definition (LB-026):** a blank Claude Science session given ONLY the word-identical
  question (plus, for Q_ERGO, the two identical PDFs), producing ONE response — no loop, no plan-review, no
  citation-enforcement framing, no multi-phase driving. A blank CC, if used, is only a dumb delivery pipe (paste +
  attach + capture, add nothing). This is GOAL D4's "blank-CS" control; the loop is the ONLY difference between arms.
- Fairness rule: Arm B and Arm L get **byte-identical** question wording (and, for Q_ERGO, the **same two PDFs**); Arm B
  gets no loop assistance and no loop-style framing. The blank CC attests to this in its RUN_REPORT. (The shared PDFs
  are the question's given material, not loop help — so they do not break the control.)

