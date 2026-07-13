# exp-002 — Operator instructions for the operator's BLIND evaluation

**You are the operator. This step is a PAUSE: CS waits for the operator's blind scores before continuing.**

## What this is
`eval_site.html` is a single, self-contained offline web page (no internet needed — all 9 answers and
33 figures are embedded). It shows **9 answers labelled E1–E9**, grouped under the 3 research questions,
in randomized order. There is **no arm, no method, no folder name, no R-code** anywhere on the page —
that is the point. the operator judges the science; CS has already checked citations and provenance.

## The double blind (why this matters)
- **the operator/you are blind to the arm.** The page is E-codes only. Even you (the operator) cannot tell which
  answer came from which arm by looking at it.
- **CS is blind to the arm too.** CS scored the same answers as R-codes and does **not** hold the
  R-code→arm map — **you do** (that is Key-1). Neither key alone reveals the arm.
- Do not tell the operator anything about the arms, the loop, or which answer is which. Just: "score the science."

## What the operator does (5 minutes to start, ~30–45 min to finish)
1. **Open `eval_site.html`** in any browser (double-click it).
2. For **each** answer E1–E9: set the four science scores (Reasoning, Completeness, Usefulness,
   Creativity, each 1–5), answer the three honesty questions, tick any red flags, and write one line on
   "what's weak / what would make it good".
3. For **each question**: pick the best answer of the three and say why (+ confidence).
4. When done, click the big **"⧉ Copy my evaluation"** button at the bottom. This copies a JSON blob to
   the clipboard.
5. **Paste that JSON straight into the CS chat.** That's it.
   - Backup if the copy button is blocked: click **"⬇ Download (backup)"** — it saves
     `exp-002_human-eval_FILLED.json` to Downloads; send CS that file instead.
   - Second backup: **"show JSON"** prints the same text in a box to select-all and copy by hand.

## What you must NOT do
- Do **not** open `key2_eval_to_R.json` and do **not** send it to the operator — that is CS's Key-2 (E→R map).
  Opening it doesn't reveal the arm (only CS→R), but keep the workflow clean.
- Do **not** hand CS the R-code→arm map (Key-1) yet. CS asks for it **after** the operator's eval is pasted in —
  that is the two-key unblind, done in one deliberate step so no arm knowledge can leak into any score.

## After the operator's eval is in
CS validates it covers all 9 E-codes × 4 dimensions + honesty/red-flags/head-to-head, saves it as
`human_eval.json`, then asks you for **Key-1** (`Rn → arm`). CS composes Key-1 ∘ Key-2 → the full
`E→R→arm` map, merges the operator's E-scores with CS's R-scores on the common (question, arm) key, and only then
computes the Δ(L8−L7) primary endpoint. Unblinding attaches labels; it never changes a score.
