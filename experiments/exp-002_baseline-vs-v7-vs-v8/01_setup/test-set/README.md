# exp-002 test-set  [CS-authored]

**Status: DRAFT — question texts are PLACEHOLDERS awaiting operator input.** Categories, shape, arms, and the
output-format instruction are locked/carried; only the three question TEXTS are pending (operator's next decision).

## Design
3 questions (one per category) × 3 arms (**B** baseline / **L7** v7 loop / **L8** v8 loop) × 1 run = **9 answer-runs**.
Same two-key double-blind, dual scoring (CS 3-persona panel + citation agent + the operator), gated creativity, and
presentation-folder output as exp-001. Endpoint = the three pairwise deltas (Δ(L8−L7) primary, Δ(L8−B), Δ(L7−B)) —
see `../harness-3arm-extension.md`.

## The three categories (carried from exp-001, LB-074)
1. **day-in-the-lab** — ingest given publication(s) → analyse → follow-up hypothesis + design a first (pilot) experiment.
2. **maximum-creativity big-think** — a big unanswered biological question → generate + argue a genuinely new hypothesis.
3. **translational data breakthrough** — pull literature + public datasets → analyse → predict + argue a new treatment.

## What carries forward vs what changes
- **Same categories** as exp-001 (so results are comparable in KIND), **different question TEXTS** (new topics — a fresh test,
  not a re-run of the same three questions).
- **Output format updated (exp-002):** `result.md` now capped at ~1,800 words + a mandatory ≤150-word "Bottom line" box;
  `reasoning.md` bulleted. Appended byte-identical to all three arms (fair). From exp-001 feedback (answers too long / a
  pilot must be a real pilot). Full block: `loop-design/current/output-format-instruction.md`.
- **Harness recalibrated (exp-002):** harsher panel anchors (use the full 1–5 range) + an overclaim/scope-inflation
  grounding penalty. So exp-002 ABSOLUTE scores are NOT comparable to exp-001's — only within-exp-002 deltas are.

## To make this run-ready (operator + CS)
1. **Operator** provides the three question texts (see placeholders in `questions.json`) — one per category, new topics,
   each the SAME SHAPE as its exp-001 counterpart.
2. For category 1, operator names + attaches the publication PDF(s) to `materials/`.
3. CS fills `why_this_question` + fairness notes, verifies the output-format block is byte-identical across arms.
4. Operator LOCKs the questions (labbook), sets `run_flag` READY.
5. Bootstrap the v8 loop per question (the v8 bootstrap gives one start-prompt per driver run); run B / L7 / L8.

## Fairness (unchanged)
The question is word-identical across arms; only the loop machinery differs. The output-format instruction is appended
identically. L8's composed context + Codex panel sharpen HOW, never WHAT (firewall asserted clean). See `../protocol.md`.
