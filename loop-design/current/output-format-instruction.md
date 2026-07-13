<!-- Authored by [CS]. THE single source of truth for the output-format instruction appended to every exp-001 test
     question. Locked by LB-073. questions.json imports this VERBATIM; both arms receive it byte-identical. If any copy
     disagrees with this file, THIS + the labbook win. -->

# the Metascience Project — Output-format instruction (append to every question, both arms)  [CS]

## Why this exists
The presentation format must come from the **question**, not the loop — otherwise a nicely-structured output would be a
loop-engineered advantage rather than a genuine quality difference. So the exact block below is appended, **byte-identical**,
to every test question, and given to **both** arms (baseline blank-CS and the CC-driven loop). Both arms are asked for
the same deliverables; only *how well* each fulfils them may differ — that difference is the loop effect we measure.

**Length + bottom-line box (added for exp-002, from exp-001 feedback; see the exp-002 output-format labbook entry).** exp-001 answers were "too long / hard to
understand quickly" (the operator); the loop's only combined loss (Q2) was legibility-driven, not content-driven. So the block
now carries a ~1,800-word cap on `result.md`, a mandatory ≤150-word bottom-line box, and a bulleted `reasoning.md`.
This is a **fairness-neutral** change: it is appended **byte-identical to every arm** (B / L7 / L8), so it cannot
advantage the loop — it only raises the legibility bar for everyone equally. Word budget (not "pages") because markdown
has no fixed page length; a word count is what an arm can self-check against.

## The instruction — appended VERBATIM to every question (both arms)
> **How to present your results.** Please hand back your answer as a small **presentation folder** containing:
> **`result.md`** — open with a **"Bottom line" box of 150 words or fewer** (your single main answer, and — if you propose one — the first experiment, in plain language a busy reader grasps in 30 seconds), then give your full answer and the case for it. Keep `result.md` to **about 1,800 words or fewer (≈ 4 pages)**, excluding figures and the bottom-line box — be complete but concise; length earns no credit, clarity does.
> **`reasoning.md`** — the line of thought that got you there, written as **structured bullet points or short sections** (not long prose); no length limit, but keep it scannable.
> a **`figures/`** folder with any plots, tables, or other artefacts you produced, each clearly labelled;
> **`sources.md`** — every source you drew on, with identifiers; and **`process_trace.json`** — a step-by-step record
> of what you actually did to reach the answer.

## What each deliverable is scored on (loop side must NOT re-engineer this — it is identical for both arms)
| File | Scored for (rubric dimension / check) |
|---|---|
| `result.md` | correctness · usefulness · how well-argued (the final answer + its case) |
| `reasoning.md` | creativity · depth · the reasoning-trace gate (novel-not-obvious, honestly reasoned) |
| `figures/` | use of CS's analytical power (did they produce real supporting analysis?) |
| `sources.md` | citation existence · support · quality (venue, primary-vs-review, retraction) — CS only |
| `process_trace.json` | provenance / "did it really happen" / hallucination check / documentation — CS only |

## Two hard rules on `process_trace.json` (blind-safety — enforced in the loop driver, v7)
1. **ACTION-labelled, not phase-labelled.** Each entry is `{"action","detail","evidence","t"}`. It must NOT carry the
   loop's internal phase names (REFRAME / PLAN-REVIEW / INTEGRATE / …). Phase names would reveal to the blinded scorer
   that an answer came from the loop. The loop's phase-structured log lives OUTSIDE the presentation folder (in the
   driver's `run_log/`), read only after unblinding.
2. **`process_trace.json` is scored by CS but is EXCLUDED from the human eval site** — the operator/the operator see
   `result.md` + `reasoning.md` + `figures/` + `sources.md` only. This keeps the human evaluation blind to arm as well.

## Nothing loop-specific inside the presentation folder
No reframed brief, no phase log, no "the loop did X" notes. The `presentation/` folder must look structurally the same
whether the answer came from the loop or a cold session — only its quality may differ.
