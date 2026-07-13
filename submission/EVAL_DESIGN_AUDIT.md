# Evaluation-design audit

**Why this document.** Before any figure or Results prose, this reconstructs the
evaluation design exactly as it ran — prompts, arm assignment, models, rubric, scorer
instructions, blinding, reruns, exclusions, overrides, and the dependence structure of
the scorers — and fixes the *estimand*, the *experimental unit*, and the *aggregation
rules* up front. Everything downstream inherits these definitions. Anchors are LABBOOK
`LB-NNN` and the frozen files under each experiment's `04_evaluation/` and `05_analysis/`.

This is an audit of *design integrity*, not a defence of the result. Where the design is
weak (small n, no within-cell replication, one human evaluator, a cumulative-upgrade
confound), it is stated plainly here so the report cannot overclaim.

---

## 1. The estimand and the experimental unit (fixed before analysis)

- **Scores** are on a **1–5 ordinal rubric** (higher = better), assigned per dimension.
- **Experimental unit = one answer to one question by one arm** — i.e. the (question, arm)
  cell. There is **one answer per cell** (no within-cell replication in exp-001/002; the
  earlier "≥2 runs + mean" idea in GOAL §4 was not executed — see §6).
- **Design = randomized complete block**, with **block = question**. exp-001: 3 questions ×
  2 arms. exp-002: 3 questions × 3 arms. **n = 3 blocks.**
- **Primary endpoint (exp-002)** = the **within-question paired difference Δ(L8−L7)**,
  summarized as a mean and a **sign-count (n positive of 3)**. exp-001's endpoint = the
  within-question **Δ(L−B)** on the combined composite (mean-Δ and k-wins of 3).
- **Inference scope.** With n = 3 blocks the study is **underpowered by construction**. The
  warranted inference is **sign-consistency / direction** of the paired differences, not a
  powered significance test. Friedman omnibus p-values are computed and reported **for
  completeness only** and are never the headline.

---

## 2. Scorers, and their dependence structure

Three score streams appear in the tables. Their independence is **not** symmetric, and the
report keeps them visibly distinct in every format:

| Stream | What it is | Dimensions | Independent? |
|---|---|---|---|
| **CS-harness panel** | An automated 3-persona LLM reviewer jury (Rigor / Significance / Novelty) run inside Claude Science, plus deterministic citation-existence + entailment + reasoning-trace checks. Scoring model **claude-opus-4-8**. | 5: grounding, reasoning, completeness, usefulness, creativity | Machine scorer |
| **Human expert** | A single domain expert (aging biology), scoring blind via an offline HTML eval site. | 4: reasoning, completeness, usefulness, creativity (**grounding omitted** — citation integrity is the harness's job; also keeps exp-001↔exp-002 human evals comparable) | One human; **not independent replicates of each other** |
| **Combined** | **DERIVED SUMMARY.** Per shared dimension, `(CS + human)/2`, then averaged over the 4 shared science dimensions. | 4 shared dims | **NOT a third scorer and NOT an independent replicate** — a deterministic function of the two above |

**Load-bearing consequence:** the "combined" column must never be presented as a third,
independent opinion or as extra sample size. It is a convenience average. The report labels
it *derived* wherever it appears, and the true independent-observation count remains **two
scorers over three questions**.

CS scores the 5-dim rubric; the human scores 4 dims. The **4 shared science dimensions**
(reasoning, completeness, usefulness, creativity) are the only common ground, so cross-scorer
comparisons and the combined mean use **mean-of-4**, while CS-composite (mean-of-5, includes
grounding) is reported as the harness's own internal number.

---

## 3. Arm assignment, blinding, and concealment (two-key double-blind)

exp-002 ran a **two-key double-blind** so neither the scorer nor the evaluator could infer
the arm (verified in `04_evaluation/blinding_key_FULL.json`, LB-101→LB-103):

- **Key-1 (R-code → arm), operator-held.** Each answer was filed under a neutral run code
  R1–R9. CS scored the R-coded answers **blind to arm**. Arm map (revealed only at unblind):
  **Baseline = R8/R1/R4, v7 = R9/R5/R2, v8 = R3/R7/R6.**
- **Key-2 (E-code → R-code), CS-held.** For the human eval, a global reshuffle (seed 2002)
  mapped R-codes to display codes **E1–E9**, with per-question display order re-shuffled
  (seed 777). The operator/human saw only E-codes. **Neither key alone reveals the arm.**
- Unblind = compose Key-1 ∘ Key-2 → `blinding_key_FULL.json` (E→R→arm). Design-integrity
  check passed: each question's triad contained exactly one B / one L7 / one L8.
- **Blind-safety of the eval site:** the process/action trace was **excluded by construction**
  (the generator hard-stubs the trace renderer so it cannot leak an arm); the generated HTML
  was scanned — 0 bare R-codes, 0 arm labels — before release. Inline `{{artifact:…}}` markers
  and broken image tags from the source sessions were stripped so the CS-supplied figures were
  the single figure channel.

exp-001 used the same two-key structure (`04_evaluation/` + `05_analysis/blinding_key_FULL.json`).
exp-003 was **not blinded and not scored** — it is a showcase (see §7).

---

## 4. The rubric and scorer instructions

- **Rubric** (`loop-design/current/rubric.json`, LB-016): 5 dimensions with weights —
  grounding .25, correctness/reasoning .25, completeness .20, usefulness .15, creativity .15.
  The CS-composite in the tables is reported as an **unweighted mean of the 5 dims** (the
  weighted rubric drove the harness's internal scoring; the analysis tables carry the
  unweighted per-dimension means, which is what `build_spine.py` reproduces).
- **Grounding** is gated by a deterministic citation pipeline: existence check (does the
  PMID/DOI/accession resolve?) + entailment (does the cited source support the sentence?) +
  a reasoning-trace check. Grounding is **capped** when identifiers do not resolve.
- **Creativity** is scored as `Novelty × Plausibility-gate × ReasoningTrace-gate`
  (multiplicative; `creativity-metric.md`, LB-018) — a deliberately strict gate that
  zeroes "novel but implausible or unsupported" ideas.
- **Human instructions:** per answer, 4 science scores (1–5) + 3 honesty checks
  (novel-to-you / reasoning-followable / hallucination-flag) + 6 red-flag checkboxes + a
  free-text "what's weak"; per question, a head-to-head best pick + confidence + why.

---

## 5. A documented scorer disagreement (kept, not smoothed)

exp-002 answer **R8/E3** (baseline, Q1): the CS harness gave a 4-dimension mean of **4.10**;
the human expert gave **1.50** and raised the **hallucination flag** ("very weak, just cramped
a few co-factors together"). This is a genuine machine-vs-expert divergence — a
shallow-but-well-formatted answer the automated rubric over-rewarded and the expert caught.
It is **retained** in the analysis and reported as a limitation of automated scoring, not
excluded. (This is also why the human's mean levels sit ~1.3–1.8 points below the LLM panel on
reasoning/completeness/usefulness, while the human is *stricter* on creativity than CS's gate.)

Cross-scorer structure: within-question **top-pick agreement CS↔human = 3/3**; on Q2 the full
ranking is identical. Pooled across all 9 answers the Spearman correlation is ≈ −0.12 (n.s.) —
a **cross-question pooling artifact** (within-question orderings agree, absolute levels shift
across questions in opposite directions for the two scorers). The meaningful signal is the
within-question agreement; the pooled correlation is reported honestly as the pooling artifact
it is.

---

## 6. Reruns, exclusions, overrides, and known confounds

- **Cumulative-upgrade confound (exp-002).** By operator ruling (LB-081), v8 was **not** built
  one-variable-at-a-time; it bundles **two** upgrades over v7 (OPT-1 context-composer + the
  Codex critique panel, plus a Gate-2 figure add-on). Therefore **Δ(L8−L7) is the effect of
  the whole v8 bundle, not of any single change.** Stated wherever the delta appears.
- **Grounding resolver-coverage artifact.** CS grounding is highest for the *baseline* arm
  (B 2.33 > L8 1.67 > L7 1.00). Root cause (BLIND_ANALYSIS §7, LB-099): the integrity scan
  cached GEO/PMID/DOI resolvers but **not** UniProt/Ensembl, so real, on-topic protein
  accessions returned `None` and were counted as "unresolved," capping grounding. This is a
  **resolver-coverage gap, not fabrication** — a separate existence certification found
  **0 fabricated** identifiers (121/121 PMID, 112/112 DOI, 36/36 GEO). Scores were **not
  silently rescored**; the caveat is carried forward and, if anything, means the true CS
  grounding delta *understates* v8.
- **Rerun.** exp-002 blind scoring was re-run on claude-opus-4-8 (the two-key concealment was
  preserved across the rerun); scores were frozen before any arm was revealed.
- **No exclusions.** All 9 exp-002 answers and all 6 exp-001 answers are in the analysis,
  including the R8/E3 divergence.
- **Single human evaluator.** All human scores come from **one** domain expert — a strength for
  consistency, a limit for generalization; stated as a limitation.
- **exp-001 naming drift.** The exp-001 folder slug reads `v0-loop`, but the loop under test
  was **v7_cc-bootstrap** (hash `6bbd94a13d13e462`, LB-077). Pinned here and in the timeline so
  the record is not misread.

---

## 7. exp-003 is a showcase, not a measured comparison

Operator ruling (LB-104): exp-003 is a **showcase** — both PDF reports go to the judges
to compare; there is **no CS rubric scoring, no two-key blind, no human rubric pass**. It is
**n = 1 per arm, one question, two arms (baseline vs v9 loop)**. The prompt (question + DOI-only
dataset pointer + compute-caution) was **byte-identical** to both arms. The arms' scientific
claims were **not re-verified by CS** (documentation only). The dataset accessions were recorded
as verified during the original run (NCBI E-utilities, 2026-07-13; SOURCES.md S-084, LB-106) and
**independently re-confirmed live on 2026-07-13 in this submission's verification track** — all four
pointers (GEO GSE314342, SRA SRP643211, BioProject PRJNA1359008, preprint DOI 10.64898/2025.12.23.696273)
resolve publicly and are recorded in `submission/report/verification_ledger.csv`. The report treats exp-003 as an **open, symmetric** comparison
with predefined inspection dimensions — never a bare "judge for yourself" and never a measured
win.

---

## 8. Aggregation rules (frozen, used by `evidence/build_spine.py`)

1. Per-answer: `cs_composite` = mean of 5 CS dims; `cs_mean4` / `human_mean4` = mean of the 4
   shared dims; `combined_mean4` = mean over shared dims of `(cs+human)/2`.
2. Arm mean = mean of the 3 per-question answers for that arm (equal question weight).
3. Within-question delta = arm-minus-arm within each block; endpoint = mean of the 3 deltas +
   sign-count.
4. Friedman across the 3 arms with question as block; reported for completeness only.
5. Every number in the report is the value `build_spine.py` recomputes from the raw
   per-answer scores in `master_3arm.csv` / `scorecard_long_unblind.csv` **and** matches the
   frozen `05_analysis/` tables. Any value that fails to reproduce does not ship.
