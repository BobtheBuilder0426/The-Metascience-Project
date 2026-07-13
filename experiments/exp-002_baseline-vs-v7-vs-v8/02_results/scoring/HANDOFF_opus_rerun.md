# HANDOFF — exp-002 blind scoring must re-run on OPUS (fresh session)

**Written:** 2026-07-12 by [CS] session 1 (frame `2b15ce99-f95d-49e6-9e98-f4fbacba951f`).
**Why a new session:** this frame hit its **2.0M host.llm per-frame token ceiling** (burned on discarded
Sonnet runs). Every `host.llm` call here now fails instantly, Opus included. A fresh frame = fresh ceiling.
**Operator ruling (hard, non-negotiable):** the CS scoring panel runs on **`claude-opus-4-8` ONLY**. Never
Sonnet, never Haiku, anywhere in the scoring path.

---

## TL;DR for the next session — do exactly this
1. Read this file + `plan` (artifact `616b7ed3-730c-43a6-8331-f6bdf06d577d`) + LABBOOK LB-095 (+addenda) & LB-096.
2. Run the Opus scoring driver (it is self-contained; makes ZERO connector calls; all judges = Opus):
   ```python
   # fresh CS python kernel, environment="python"
   import os
   os.chdir("<repo>/experiments/exp-002_baseline-vs-v7-vs-v8/02_results/scoring")
   exec(open("run_opus_scoring.py").read())
   main(host)                      # scores all 9 -> blind_scores_opus/<R>.json  (~25-30 min; background it)
   ```
   Sanity-check first with `main(host, only=["R8"])` (one answer, ~2 min) to confirm Opus routing + the
   parse-gate before the full batch. Background the full run (`background=true`) and poll.
3. Then resume the approved 8-step plan at **Step 3** (blind analysis + figures) → Step 4 (HTML eval site,
   operator-blind) → PAUSE for the operator eval → Steps 6-8 (two-key unblind → 3-arm analysis → FINAL_RESULT).

---

## What is DONE and VALID (reuse as-is — do NOT redo)
- **Blind inventory + question grouping** (blinding hides ARM, not QUESTION):
  - **Q1_exp002** (metabolite-cocktail / muscle rejuvenation): **R3, R8, R9**
  - **Q2_exp002** (why does biological aging occur): **R2, R4, R6**
  - **Q3_exp002** (new compound for complex-I mito disease): **R1, R5, R7**
  - Blind INTACT: no `meta.json`; the only arm-word grep hits (R3 "baseline grip", R8 "4th arm acetate")
    are innocent scientific usage. `:Zone.Identifier` files are Windows ADS junk — ignore, don't touch.
- **Integrity / citation-existence scan** (deterministic API calls, model-independent → VALID):
  **121/121 PMIDs, 112/112 DOIs, 36/36 datasets resolve → ZERO fabricated citations across all 9.**
  (5 ChEMBL IDs are target-IDs not molecule-IDs — legitimate.) → `integrity_table.json`, `extraction_scan.json`.
- **`connector_cache.json`** (290 KB, sha256[:16]=`23a6f1bc5de06e9f`): namespaces pmid_meta (121, +116 abstracts),
  doi_crossref (112), dataset (36), novelty (Q1 hits=5 / Q2=72 / Q3=296). The Opus driver reads this → **no
  connector calls at all in the re-run**, so 100% of the Opus token budget goes to judging.
- **`scoring_input.json`** (234 KB): the 3 questions + 9 answers with FULL result.md text + normalized
  process_trace. Self-contained; the driver reads only this + the cache.
- **`run_opus_scoring.py`**: the Opus scoring driver (below).

## What is DISCARDED (void — in `_DISCARDED_sonnet_scores/`, kept for provenance only)
All first-pass blind scores. They ran the rubric/creativity/Elo panels on `claude-sonnet-5` and the
citation-entailment on the kernel default (no `model` key set → not Opus; exact family unconfirmed, immaterial). **VOID under the Opus-only ruling.** Do not read them
as data.

## Reliability lessons from the Sonnet pass — already baked into `run_opus_scoring.py` as HARD GATES
The Sonnet pass hit three failure modes; the driver defends against all three:
1. **`reasoning` dim returned as PROSE not an integer** → silently `None` for 8/9 answers (the model read
   the key "reasoning" as "give your reasoning"). FIX: a STRICT integer-format coda appended to every judge
   prompt (dims MUST be integers 1-5; justifications only in `*_reason` twins). Rubric/anchors unchanged.
2. **`max_tokens` empty responses** on long answers (Opus/Sonnet spend budget on reasoning before JSON).
   FIX: token escalation 8k→16k + one transient retry per call.
3. **No validation before writing** → wasted a 30-min batch before noticing. FIX: a per-answer PARSE-GATE —
   after scoring, if any of the 5 rubric dims is non-numeric the rubric panel is RE-CALLED (≤3×); the row is
   written only when all 5 dims + both creativity gates are numeric. `_attempts` + `_dim_parse_ok` recorded.

## The harness (shared, arm-generic) — unchanged, committed
`experiments/exp-001_baseline-vs-v0-loop/01_setup/harness/` — rubric v2 (5 dims equal 0.20), 3-persona panel
(rigor/significance/novelty) + creativity panel (plausibility × reasoning-trace gate) + citation-quality agent
+ existence-aware grounding cap + C2 overclaim cap + Elo. The **committed harness files were NOT edited** —
all Opus pinning + token/format hardening live in `run_opus_scoring.py`'s `OpusAdapters` subclass + the coda.
Blind mechanism: **`arm = code = R-code`** (Key-1 maps R→real arm only at unblind).

## Remaining plan steps (after Opus scoring lands in blind_scores_opus/)
- **Step 3** — `BLIND_ANALYSIS.md` + blind figures (R-coded): per-question composites, per-dimension bars,
  creativity-gate decomposition, citation-quality panel, blind Elo. Figures via `figure-style`.
- **Step 4** — HTML eval site under **Key-2** (reshuffle R→E1..E9, save `key2_eval_to_R.json` CS-side).
  Warm/light retro aesthetic (reuse exp-001 `make_eval_site.py`). 5-dim scales + per-answer comment +
  red-flag + creativity-honesty + figures inline + process schematic + head-to-head. **process_trace.json
  EXCLUDED.** OPERATOR-BLIND: E-codes only — never folder names, never R-codes, never arm. Idiot-proof
  copy/paste + download instructions. Deliver to `04_evaluation/`.
- **Step 5** — PAUSE. Operator runs the operator's blind eval, pastes JSON back → `04_evaluation/human_eval.json`.
- **Step 6** — Two-key unblind: operator hands over Key-1 (R→arm). Compose `blinding_key_FULL.json`
  {E→R→(question,arm)}; merge the operator + CS onto (question,arm). Mirror exp-001 `unblind_and_analyze.py`.
- **Step 7** — 3-arm analysis: `make_analysis_3arm.py` + `make_3arm_figs.py` (both in
  `exp-002/.../01_setup/harness/`). Primary **Δ(L8−L7)** + Δ(L8−B) + Δ(L7−B); per-question + per-dimension
  plotted individually × {CS, the operator, combined}; per-arm means; k/3 for L8>L7; mean-Δ across questions;
  CS-vs-the operator scatter. Honest n=3×1 descriptive caveat + L8-is-cumulative-bundle caveat.
- **Step 8** — `FINAL_RESULT.md` + `SUBMISSION_INDEX.md` + LB entry + STATUS baton.

## Key IDs
- Plan: `616b7ed3-730c-43a6-8331-f6bdf06d577d` (v `27af60d9-fe1e-4453-b2b5-7aa88471a121`)
- exp-002 questions (locked): `experiments/exp-002_baseline-vs-v7-vs-v8/01_setup/test-set/questions.json`
- exp-001 unblind reference: `blinding_key_FULL.json` id `ab4df0a5-...`, `make_analysis.py` id `05b515cc-...`
- Frame that hit the ceiling (this one): `2b15ce99-f95d-49e6-9e98-f4fbacba951f`
