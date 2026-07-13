<!-- the Metascience Project exp-002 FINAL RESULT. Two-key double-blind unblinded 2026-07-13.
     CS scored R1–R9 on claude-opus-4-8 without arm knowledge (Key-1 operator-held);
     the operator scored E1–E9 without R-code knowledge (Key-2 CS-held). Both frozen before unblind. -->

# exp-002 — Does the agentic loop beat baseline? (Baseline vs v7-loop vs v8-loop)

**the Metascience Project · Researcher track · 3-arm blinded evaluation · FINAL RESULT**

## Bottom line

**The v8 agentic loop (L8) is the best arm on every aggregate metric and every scorer, and the
pre-registered primary endpoint Δ(L8−L7) is positive in all three questions for all three scorers.**
The v7 loop (L7) does **not** reliably beat baseline — the improvement is specific to v8. The evidence is
directionally strong and internally consistent, but the sample is small (n = 3 questions, one answer per
arm per question); we report it as a **consistent directional result, not a powered significance test**.

| Arm | CS composite (0–5) | CS mean-4 | the operator mean-4 (1–5) | Combined |
|---|---|---|---|---|
| Baseline (blank CS) | 3.548 | 3.852 | 2.750 | 3.301 |
| v7-loop | 3.397 | 3.996 | 2.667 | 3.331 |
| **v8-loop** | **3.672** | **4.174** | **3.250** | **3.712** |

*Combined = mean of CS and the operator on the four shared science dimensions. L8 wins all five columns
(CS composite, CS mean-4, the operator mean-4, combined-raw, and the z-standardized combined not shown here).*

## Design

Three research questions, each answered independently by three arms — **Baseline** (a blank Claude Science
with no loop), the **v7 agentic loop**, and the **v8 agentic loop** — giving 9 answers in a **randomized
complete block design** (question = block; each block contains exactly one B, one L7, one L8). This is the
correct structure for the primary analysis: **within-question paired deltas** control for question
difficulty, which varies far more than the arm effect.

- **Q1** — propose a metabolite cocktail (+ the experiment) to rejuvenate aged skeletal muscle.
- **Q2** — why does biological aging occur? (open-ended "big-think" hypothesis)
- **Q3** — propose a new compound (+ development plan) for a complex-I mitochondrial disease.

**Two-key double-blind.** CS scored the nine answers as R-codes on `claude-opus-4-8` (every LLM judge —
rubric panel, creativity panel, citation-support entailment, pairwise Elo) with **no knowledge of arm**.
the operator (human domain expert) scored the same nine as E-codes on four science dimensions with **no knowledge
of R-code or arm**. The operator held Key-1 (R→arm); CS held Key-2 (E→R). Both scorers were **frozen
before either key was applied** — unblinding only attached labels, it never changed a score. Design
integrity at unblind: each question's triad resolved to exactly one B / L7 / L8, and Key-1's own question
labels independently matched the CS blind grouping.

## 1. L8 is highest across all three scorers

![Arm means by scorer — each grey line is one question (n=3), bold line is the arm mean]({{artifact:art_0acf323c-a5e8-46de-80e5-508314032a9a}})

The bold arm-mean trajectory **dips at v7 then rises to v8** for both the CS panel and the operator, and rises
monotonically B→L7→L8 in the combined view. The pattern is the same whether the judge is the LLM harness
or the human expert: **v8 on top, v7 no better than (or below) baseline.**

## 2. Primary endpoint: Δ(L8−L7) > 0 on 3/3 questions, every scorer

![Within-question deltas — primary endpoint Δ(L8−L7) in green, each dot one question]({{artifact:art_221981b9-4caa-40c8-9d8f-98f5bf889225}})

| Metric | Δ(L8−L7) | Δ(L8−B) | Δ(L7−B) |
|---|---|---|---|
| CS composite | **+0.275** (3/3 ↑) | +0.124 (2/3) | −0.151 (1/3) |
| CS mean-4 | **+0.177** (3/3 ↑) | +0.321 (3/3) | +0.144 (2/3) |
| the operator mean-4 | **+0.583** (3/3 ↑) | +0.500 (2/3) | −0.083 (1/3) |
| Combined | **+0.380** (3/3 ↑) | +0.411 (2/3) | +0.030 (2/3) |

The primary contrast **Δ(L8−L7) is positive in every question for every scorer** — the single most robust
signal in the experiment. The secondary contrasts are where the honesty lives: **Δ(L7−B) is the weakest
column** (negative for CS-composite and the operator), i.e. the v7 loop did not deliver a clean win over doing
nothing. The v8→v7 gap is real and consistent; the v7→baseline gap is not.

An omnibus Friedman test (block = question) gives χ² = 4.67, p = 0.097 (CS mean-4); p = 0.26 (the operator);
p = 0.37 (combined). With only three blocks these are **underpowered by construction** and reported for
completeness, not as the headline. The sign-consistency of the paired primary endpoint (9/9 positive
across the three questions × three scorers) is the stronger statement the data can support.

## 3. Where v8's gains come from — and one honest wrinkle

![Per-dimension means by arm — CS 5 dimensions (incl. grounding), the operator 4 science dimensions]({{artifact:art_a1b7a7a1-6bf7-4e3b-8927-7398dacafad0}})

The gains concentrate in specific dimensions rather than being uniform:

- **Creativity** — v8 highest for **both** scorers; CS creativity Δ(L8−L7) = +0.43 (3/3 positive), the operator
  creativity Δ(L8−L7) = +0.67 (2/3). After the LB-098 creativity-gate fix this is a genuine, discriminating
  axis, and it is where the loop helps most.
- **Reasoning** — the operator's reasoning score rises Δ(L8−L7) = +1.00 (3/3): the human expert found the v8
  answers' arguments clearly the most followable and sound.
- **Grounding (CS-only)** — the wrinkle. CS grounding is *highest for baseline* (2.33) and drops for both
  loop arms (v7 1.00, v8 1.67). Part of this is a **resolver-coverage artifact**, not fabrication: the
  Step-1 integrity scan cached PubMed/Crossref/GEO resolvers but not UniProt/Ensembl, so real, on-topic
  protein/gene accessions cited more heavily by the loop arms count as "unresolved" and trip the integrity
  cap (see §5 and BLIND_ANALYSIS §7). The 0-fabricated certification (121/121 PMIDs, 112/112 DOIs, 36/36
  GEO) stands for all nine. Grounding is CS's job and was deliberately excluded from the operator's evaluation.

## 4. Head-to-head is task-dependent: v8 and baseline split the wins

![Head-to-head winner per question × scorer]({{artifact:art_bc6ac163-e429-492b-8c74-9da0eddad8fb}})

The win matrix is the most important counterweight to the headline. Across the 9 (question × scorer)
cells, **v8 wins 4, baseline wins 4, v7 wins 1**:

- **Q1 (metabolite cocktail): v8 wins** (CS-composite + the operator; Elo picks v7).
- **Q2 (why aging): baseline wins — unanimously** (CS-composite, CS-Elo, and the operator all pick the baseline
  answer). On the open-ended "big-think" question, the loop's structured, tool-driven machinery did not
  help; the direct baseline answer was judged best by everyone.
- **Q3 (complex-I compound): v8 wins** (CS-composite + the operator; Elo picks baseline).

So the mean-score story ("v8 best overall") and the head-to-head story ("v8 and baseline tie on wins")
are both true and non-contradictory: **v8 lifts the average — especially on the two concrete
design/proposal questions — but the loop is not universally better, and on open-ended conceptual
questions the baseline can still win outright.**

## 5. Limitations (stated plainly)

1. **n = 3 questions, one answer per arm per question.** No within-cell replication; significance tests
   are underpowered. The result is a *consistent direction across all cells*, not a powered p-value.
2. **CS grounding caps mix signal and coverage.** Some low grounding scores reflect uncached
   UniProt/Ensembl resolvers, not fabrication (§3, BLIND_ANALYSIS §7). This depresses the loop arms'
   CS-composite specifically, so the true CS Δ in favour of v8 is if anything *understated*.
3. **Absolute scores are not comparable to exp-001** (harness C1/C2 recalibration). Only within-exp-002
   comparisons and the arm deltas are valid.
4. **One human evaluator.** the operator's scores are a single expert's judgement; the CS↔the operator agreement below is
   the available cross-check, not inter-rater reliability across a panel.

## 6. CS ↔ the operator agreement (cross-check)

Within-question **top-pick agreement between CS-composite and the operator is 3/3** (Q1 both pick the L8 answer,
Q2 both pick the baseline answer, Q3 both pick the L8 answer). Q2's full ranking is **identical** across
CS-composite, CS-Elo, and the operator. The human expert scores reasoning/completeness/usefulness ~1.3–1.8 points
*below* the LLM panel (the panel is more generous on absolute level) but rates creativity slightly higher
— i.e. **CS's creativity gate is the stricter of the two.** The one sharp divergence is answer R8/E3
(a baseline Q1 answer): CS rated it 4.10 on the four shared dimensions while the operator rated it 1.50 and
hallucination-flagged it ("just cramped a few co-factors together"). That is exactly the kind of
shallow-but-well-formatted answer an LLM rubric can over-reward and a domain expert catches.

## 7. Interpretation for the Metascience Project mission

The experiment's purpose is to prove, measurably, that the agentic loop beats a raw baseline. exp-002
gives a **qualified yes, with a version story**: the **v8 loop** improves on both the raw baseline and the
earlier **v7 loop**, consistently and across an independent human expert and an LLM panel, with the
clearest gains in **creativity and reasoning** on concrete scientific-design tasks. The **v7 loop did not
clear that bar** — evidence that the loop's *design* matters, not merely its presence, and that the
iteration from v7→v8 was the productive one. The honest boundary: on open-ended conceptual questions
(Q2), the loop did not help and the baseline won. A powered follow-up would add questions and within-cell
replication to convert this consistent direction into a significance claim.

## 8. Provenance

Full unblinding key `04_evaluation/blinding_key_FULL.json` (Key-1 ∘ Key-2 → E→R→arm). CS blind scores
`02_results/scoring/blind_scores_opus/R{1..9}.json` (all `_model=claude-opus-4-8`, creativity-refixed).
the operator's eval `04_evaluation/human_eval.json`. Master merged dataset `05_analysis/master_3arm.csv`; result
tables `05_analysis/table_{total,per_question,per_dimension,deltas}_by_arm.csv`; summary
`05_analysis/final_3arm_summary.json`. Blind analysis (arm-free, computed before any key)
`02_results/scoring/BLIND_ANALYSIS.md`. Every scoring/analysis step logged in LABBOOK.md (LB-095…LB-103).
Arm map (this experiment): Baseline = R8/R1/R4, v7-loop = R9/R5/R2, v8-loop = R3/R7/R6.
