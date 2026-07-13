<!-- Authored by [CS], the operator-facing. Standardized so every experiment is scored the same way and the operator's expert judgment
     both anchors and can recalibrate the automated harness. the operator fills a COPY of this as 04_evaluation.md. -->

# exp-001 — Evaluation sheet (the operator)  [CS-authored template]

**You are the human expert anchor (aging biology).** You are shown **two answers to the same question, blinded** —
labelled **Answer 1** and **Answer 2** (you are NOT told which is the baseline and which is the loop; the assistant randomizes
the order). Please score each **independently** on the same 1–5 scales the automated system uses, so we can check the
machine against your expertise. Takes ~10–15 min. Be candid — a low score with a reason is the most useful thing here.

**The question both answers addressed:** _(the assistant pastes the exact pinned question here)_

---
## Part A — score EACH answer 1–5 (fill for Answer 1 and Answer 2 separately)

| # | Dimension | What 1 vs 5 means | Answer 1 | Answer 2 |
|---|---|---|---|---|
| 1 | **Grounding** | 1 = claims uncited/unsupported; 5 = every key claim backed by a real, correctly-used citation | ☐ | ☐ |
| 2 | **Reasoning & soundness** | 1 = contains a clear scientific error or non-sequitur; 5 = sound, clear, elegant chain of thought, alternatives weighed (where a test is proposed it's valid; if the question asks only for a hypothesis, judge the reasoning, not a missing experiment) | ☐ | ☐ |
| 3 | **Completeness** | 1 = vague/generic; 5 = specific (named genes/pathways/assays/doses), covers what matters | ☐ | ☐ |
| 4 | **Usefulness** | 1 = you couldn't act on it; 5 = you could take this to the bench / write a grant aim from it | ☐ | ☐ |
| 5 | **Creativity** | 1 = textbook recombination; 5 = genuinely novel AND plausible AND clearly reasoned | ☐ | ☐ |

## Part B — the creativity honesty check (the project's open question)
For the answer you scored **higher on creativity**:
- **B1. Is the novel idea actually novel to you, or does it just *sound* new?** ☐ genuinely novel ☐ sounds-new-but-known ☐ not novel
- **B2. Can you follow a clear line of reasoning from known biology to the novel claim?** ☐ yes, clear ☐ partial/gappy ☐ no — it's asserted
- **B3. If B2 is "no", flag it as a possible confident-but-unfounded claim (hallucination):** ☐ flag ☐ ok
- **B4. One sentence: what would make this genuinely creative *and* trustworthy?** _______

## Part C — head-to-head
- **C1. Which answer is better overall, as a working scientist?** ☐ Answer 1 ☐ Answer 2 ☐ genuinely tied
- **C2. Why? (1–3 sentences)** _______
- **C3. Your confidence in that call:** ☐ low ☐ medium ☐ high

## Part D — red flags (the "AI-slop" detector — seeds the harness plausibility gate)
Tick anything you saw in EITHER answer (note which): wrong-direction effect ☐ · implausible dose/route ☐ · ignores a
known contraindication ☐ · mechanism contradicts established biology ☐ · correlation stated as causation ☐ ·
citation that doesn't say what it's claimed to ☐ · confident claim with no mechanism ☐ · other: _______

## Part E — free comment (optional but gold)
Anything the scales missed — what a great answer here would have done, or what annoyed you about either. _______

---
### For the assistant (how to use this sheet)
- Present the two answers **blinded + order-randomized**; record the true mapping separately (in the final report, not
  on the operator's sheet).
- Save the operator's filled sheet verbatim as `04_evaluation.md`. Do **not** edit his scores or wording.
- His Part A scores are compared to the harness's per-dimension scores (agreement / κ); his Part B/D directly feed the
  creativity reasoning-trace gate and the plausibility red-flag list. Where the operator and the harness disagree, **the operator is the
  anchor** and the harness is recalibrated (noted in 05_analysis).

