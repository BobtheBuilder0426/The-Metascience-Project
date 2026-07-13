<!-- WHAT THIS FILE IS: the QUANTIFICATION spec — how the Metascience Project turns a research-question answer into numbers, identically
     and blinded, for both arms. It defines the 5-dimension quality rubric (machine-readable in rubric.json), the
     automatic citation-verification + specificity checks, and the LLM-judge panel protocol. HOW TO USE: read with
     rubric.json (the machine form the harness loads) and creativity-metric.md (dimension 5 in depth). The scoring
     harness (exp-001/01_setup/workspace/) implements exactly this. Cited basis: method-foundations.md. -->

# Quantification — making "better" measurable  [CS] — 2026-07-09  (v1)

**Goal.** Given an answer to a test-set question from either arm, output a **comparable, blinded, multi-dimensional
score** so we can say — defensibly — that one arm is better, and by how much. The metric is **identical across arms
and iterations** (it is the fixed yardstick of §5 in the design doc).

## 1. The quality rubric (5 dimensions, anchored 1-5)

Machine-readable form: **`rubric.json`** (the harness loads this; do not hand-edit scores away from it). Summary:

| Dim | Weight | Measures | Automatic signal |
|---|---|---|---|
| **Grounding & integrity** | 0.20 | every claim, **source, dataset, AND claimed action** is real & verified — nothing fabricated, and the reported analysis actually happened | citation-verification rate + dataset/accession resolution + **trace_verify action-check** |
| **Reasoning & soundness** | 0.20 | chain of thought is sound, clear, elegant; alternatives weighed; **IF** a test is proposed it is valid & controlled (test clause is **conditional** — not penalised when the question doesn't ask for one) | judge-only |
| **Completeness** (specificity) | 0.20 | whole question addressed with named entities + concrete predictions | entity-specificity count |
| **Usefulness** (actionability) | 0.20 | a domain scientist could act on it; worth doing | judge + the operator |
| **Creativity** (novelty × plausibility) | 0.20 | genuinely novel AND sensible core idea | composite novelty score (see creativity-metric.md) |

Each dimension has **anchored descriptors for every point 1-5** (in `rubric.json`) so scoring is reproducible, not
vibes. A judge fills, per dimension, `{score, one-sentence justification, evidence_span}` — the **G-Eval form-filling
paradigm** (S-007), which correlates better with human judgment than free-form rating.

**Weights rationale (v2 — LB-075).** **EQUAL 0.20 across all five**, by operator decision — simple, and it lifts the
creative + reasoning axes the operator cares about (creativity 0.15→0.20; **Reasoning** is now a first-class 0.20
dimension) relative to the earlier rigor-dominant v1 prior (grounding+correctness were 0.50). Grounding stays a hard
**integrity gate** via its auto-caps — a fabricated citation *or* a fabricated action caps it at 1 — so equalising the
weight does **not** reward hallucination; it just stops rigor from crowding out the differentiator. Two v2 changes of
substance: (i) **Grounding → "Grounding & integrity"** now folds in the *did-it-really-happen* check — datasets/DB IDs
must resolve *and be used*, and every claimed calculation/query/code-run must be evidenced in a real CS message
(`trace_verify.py`); (ii) **Correctness → "Reasoning & soundness"**, with the proposed-test clause made **conditional**
so cat-2 big-think answers (hypothesis + argument, no experiment) are scored on reasoning quality, not dinged for a
missing protocol. Weights remain a **pre-registered prior**, sensitivity-checked in analysis (we report the composite
under alternate weightings so no conclusion hangs on one weighting).

**Aggregate = weighted sum.** Primary endpoint (see `00_hypothesis.md` / dataflow §5E) = on the combined mean(CS,the operator)
composite, **mean-Δ (Arm L − Arm B) across the 3 questions AND win-count k/3**; n=3×1 is descriptive, not inferential.
We also always report per-dimension means + spread, the creativity sub-score (novelty and
plausibility separately), the citation-verification rate, and inter-judge agreement — never a single number alone.

## 2. Automatic checks (cheap, run every iteration)

These are computable without a human, so they run on every arm/every run and make the rubric scores auditable.

### 2a. Citation verification (feeds Grounding) — the credibility backbone
The single most important automatic check, because fabricated/mis-attributed citations are the classic failure of
LLM science. Pipeline (implemented in the harness against live connectors):
1. **Extract** every citation the answer makes (PMID / DOI / title / claim it's attached to).
2. **Resolve existence** via PubMed / OpenAlex — *does the reference exist?* → flag `nonexistent_reference`.
3. **Check support** — fetch the abstract and run an **LLM entailment check**: *does the cited source actually support
   the specific claim it's attached to?* → flag `reference_exists_but_irrelevant` / `claim_not_supported_by_cited_source`.
4. **Rate** = supported_citations / total_citations. A low rate caps the Grounding score.

This directly encodes the credibility/hallucination guard the GOAL asks for, and it's the kind of check the Gladstone
judges will respect (it's real verification, not self-report).

### 2b. Entity specificity (feeds Completeness)
Count named, checkable entities — gene/protein symbols, drug/compound names, pathways, assays, quantitative
predictions. A generic answer ("modulating metabolism may help aging") scores low; a specific one ("PGC-1α induction via
low-dose X, measured by Seahorse OCR, predicting ≥20% ↑ spare capacity") scores high. Genes/species italicized per
convention when rendered.

### 2c. Plausibility red-flags (feeds Creativity's plausibility gate)
A checklist seeded by **the operator's calibration answer** (request-to-operator.md, question B: "what makes you instantly distrust
an AI hypothesis in aging biology"). Examples: implausible dose, wrong-direction effect, ignores a known
contraindication, mechanism contradicts established biology. Any red-flag pulls the plausibility multiplier down (see
creativity-metric.md).

## 3. The LLM-judge panel (scalable scoring for iteration)

Human expert scoring (the operator) is the ground truth but doesn't scale to every run. So iteration uses a **judge panel**.

> **⚠ LENS SCOPE — locked distinction (operator, LB-032). Two DIFFERENT lens/model sets; do not conflate:**
> - **(A) Inside the CC/CS agent loop under test** (the product we optimize): the **multi-model (Codex/GPT) + the
>   "ambitious young postdoc" vs "mentoring PI" lenses** live HERE — they shape how the loop PRODUCES answers, and are
>   tested as improvement categories (C3, 2nd-model). They are NOT CS's ruler.
> - **(B) CS's own SCORING panel** (this section — the ruler that measures loop-vs-baseline output): must mimic
>   **hackathon judges / journal reviewers** — personas capable of judging the creativity / outcome / usefulness of what
>   CS produces. **This panel's exact personas, count, and format are PROVISIONAL — they require literature research on
>   review-panel / reviewer-persona design AND operator final-accept before locking.**
> - **Model reality (checked):** CS's scoring side has **Claude-family models only** (`host.list_models()`); there is
>   **no non-Claude model on CS's side**. So the CS panel is Claude-based reviewer PERSONAS with diversity from distinct
>   system-prompts / temperature / seed — honestly labeled as within-vendor. (A real non-Claude judge exists only on the
>   CC side and belongs to set (A).)

- **Panel, not a single judge** (S-008): ≥2 reviewer-persona judges via `host.llm`, aggregated, to reduce single-judge
  variance. Personas TBD by research (§ below) — e.g. reviewer archetypes a journal/hackathon would use. Self-enhancement
  bias (a Claude judge over-rating Claude output) is real and, since we can't cross to another vendor on CS's side, is
  mitigated by **blinding + the human anchor (the operator)**, not by a non-Claude judge — stated honestly.
- **Bias controls** (S-008): randomize arm order (position bias); strip identifying style (blinding); form-filling with
  justification (reduces verbosity bias); report **inter-judge agreement** so we know when the panel is unreliable.
- **Calibration to the human anchor:** where the operator has scored items, we report **judge-vs-the operator agreement** (weighted κ /
  correlation). the operator is the ground-truth the panel is checked against — if the panel tracks the operator, we trust it for
  un-scored runs; if not, we down-weight it and lean on the operator.
- **Elo cross-check:** in addition to absolute rubric scores, we run a **pairwise Elo tournament** across arms/iterations
  (see creativity-metric.md §Elo) — a drift-robust *relative* ranking that doesn't depend on absolute-scale stability.

**STATUS: the panel design (personas/count/format) is NOT accepted yet — pending research + operator sign-off (LB-032).**

## 4. What the harness emits (the scorecard)
One row per (question × arm × run): the 5 dimension scores, per-judge + aggregate, citation-verification rate,
entity-specificity count, plausibility red-flags, creativity sub-scores, and the weighted composite. Aggregated to a
**scorecard** (CSV + figure) per experiment: Arm L vs Arm B, with spread, and the iteration-over-iteration improvement
curve that is the D2 headline.

## 5. Honesty guards (so the numbers mean something)
- Never report the composite without per-dimension detail + spread (small n).
- Never let novelty raise the score without passing the plausibility gate (S-006/S-009).
- Anchor to the operator (the human ground-truth) whenever self-enhancement bias is possible — CS's side is Claude-only, so
  blinding + the human anchor are the guard, NOT a non-Claude judge (that lives only on the CC side). (S-008)
- Report the metric under alternate weightings; if a conclusion flips, say so.
- The automatic checks are auditable (every flagged citation is listed), so a reader can spot-check.
