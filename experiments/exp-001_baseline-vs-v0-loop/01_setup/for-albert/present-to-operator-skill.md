<!-- Authored by [CS], the assistant-facing. Spec for the CC skill the assistant runs to present exp-001 to the operator, take his questions,
     and capture his blinded evaluation. This is a CLAUDE CODE skill the assistant runs — NOT a CS skill. -->

# exp-001 — Present-to-the operator skill spec (the assistant-run CC skill)  [CS-authored]

**Purpose.** Give the operator (busy human expert) the shortest path to a high-quality evaluation: show him the two answers
**blinded**, let him ask questions, and capture his scores into `04_evaluation.md` without biasing him. the assistant runs this
as a CC skill; it does not touch the CS side.

## Inputs the skill needs
- The pinned question (`test-set/questions.json`).
- The two answers: `workspace/arm_B_baseline_answer.md`, `workspace/arm_L_loop_answer.md`.
- The blank eval sheet (`for-the operator/eval-sheet-template.md`).

## The flow (what the skill does)
1. **Blind + randomize.** Assign the two answers to "Answer 1" / "Answer 2" in a random order. **Store the true mapping
   in a separate file the assistant keeps** (`workspace/_blinding_key.md`) — NEVER show it to the operator. the operator must not be able to
   infer which is the loop (no "the AI loop said…", no metadata, strip any self-scorecard that reveals the arm).
2. **Present understandably.** Show the operator: the question, then Answer 1 and Answer 2 side by side, in plain readable form.
   Offer a one-paragraph plain-language framing of what he's doing ("two answers to the same question; score each; I
   won't tell you which is which until after"). Keep it neutral — no hints about which you expect to be better.
3. **Take his questions.** Let the operator ask for clarification or for a citation to be pulled up. the operator may use his own
   literature access; if he asks the assistant to fetch a paper, the assistant may — but the assistant must **not** offer opinions on which
   answer is better or coach his scoring.
4. **Capture the eval.** Walk him through the sheet (Parts A–E). Record his scores + words **verbatim** into a copy
   saved as `04_evaluation.md`. Do not round, "clean up", or reinterpret. If he skips a field, leave it blank.
5. **Unblind last.** Only AFTER the sheet is saved, reveal the mapping (from `_blinding_key.md`) if the operator wants to know.
   The reveal must not let him edit prior scores.

## Hard rules (bias control — these protect the human-eval result)
- **Blinding is sacred.** If blinding is broken at any point, the assistant records that in the report and the eval is flagged
  as non-blind (still useful, but marked).
- **No coaching, no leading.** the assistant never signals a preferred answer, never explains "why answer X is cleverer".
- **Verbatim capture.** the operator's scores + comments go in unedited. the assistant's job is faithful stenography + logistics.
- **the operator is the anchor.** His judgment overrides the harness on disagreement (recorded in the final report for CS).

## Output
- `04_evaluation.md` — the operator's filled sheet, verbatim.
- `workspace/_blinding_key.md` — the true arm↔label mapping (the assistant-only; goes into the assistant's report to CS, not to the operator).
- A one-line confirmation to the assistant that the eval is captured + whether blinding held, for the final report §4.

## Note on building it
This spec is enough to run the flow manually if the skill isn't built. If the assistant wants it as a reusable CC skill, the
above is the behaviour to encode; keep it a thin logistics+blinding wrapper, not an analysis tool (analysis is CS's).

