<!-- Authored by [CS]. THE canonical, submission-grade statement of the Metascience Project double-blind evaluation method.
     Locked by LB-072. Referenced from dataflow-and-handoffs.md (§5G), the experiment protocol, and the final report.
     If anything disagrees, THIS + the labbook win. -->

# the Metascience Project — Two-Key Double-Blind Evaluation Protocol  [CS]
*A methodological contribution of this project — demonstrated in the submission.*

## Why a two-key scheme (the problem a single relabel does NOT solve)
In the Metascience Project the **operator** occupies two roles that would normally be separated: they **run the arms** (so they know which
answer folder came from which arm — baseline blank-CS vs the CC-driven loop) **and** they carry the answers to the
**human expert evaluation** (the operator). A single relabeling of the folders cannot blind a person from knowledge they already
hold. If the same party who knows `folder→arm` also sees the codes used in the eval, the human evaluation is not truly
blind. We therefore split knowledge across **two keys held by two parties**, so that **neither party alone can map any
answer back to its arm**.

## The scheme
Let the 6 answer-runs of exp-001 be produced (3 questions × {baseline, loop} × 1 run).

**Key-1 — held by the OPERATOR — blinds CS.**
After the runs, the operator renames the 6 presentation folders to a **private random shuffle** `R1 … R6` and keeps the
map `Key-1 = {Rn → (question, arm)}`. Only the arm-stripped `R1…R6` folders enter the repo (`02_results/`). **CS never
sees Key-1 until unblinding**, so CS scores without knowing which arm any answer came from.

**Key-2 — held by CS — blinds the OPERATOR/the operator.**
CS scores `R1…R6` blind, then builds the human eval site under a **second, independent random shuffle** `E1 … E6`,
keeping `Key-2 = {Em → Rn}` in `04_evaluation/key2_eval_to_R.json`. **Key-2 is withheld from the operator until
unblinding.** the operator evaluates answers labelled `E1…E6` — codes the operator has never seen and cannot relate to the `Rn`
folders they created. The human evaluation is therefore blind too.

**Unblinding — requires BOTH keys, applied jointly.**
`Em  →(Key-2, CS)  Rn  →(Key-1, operator)  arm`. Neither key alone maps an answer to an arm; the composition
`blinding_key_FULL.json = {Em → Rn → arm}` is formed only when both parties bring their key, at the end.

```
   arms          Key-1 (operator)        Key-2 (CS)              eval
 baseline ─┐                                                   ┌─ the operator sees E1..E6
   loop  ──┴─► folders ──rename──► R1..R6 ──re-shuffle──► E1..E6 ┘  (never saw R codes)
                        {Rn→arm}            {Em→Rn}
                        held by OPERATOR     held by CS
                              └────────── unblind = BOTH ──────────┘
```

## Why scoring stays valid under the blind
- **CS harness scoring** runs on `R1…R6` — arm-agnostic by construction.
- **the operator scoring** runs on `E1…E6` — arm-agnostic by construction.
- **The mean(CS, the operator) per answer × dimension is computed while still blind** (both scores key to the codes, not the
  arm). Unblinding only **attaches arm labels** to already-final scores — it can never retro-influence a score.
- **`process_trace.json`** (the provenance/"did-it-really-happen" record, scored by CS) is **action-labelled**, never
  loop-phase-labelled, and is **excluded from the human eval site** — so neither the CS scorer nor the operator can infer the arm
  from it. The loop's phase-structured log lives only in the separate, out-of-band `run_log.md` (read post-unblind).

## Crash-recovery (every state is a file)
- `key2_eval_to_R.json` is written by CS the instant the eval site is generated (persistent, CS-side).
- Key-1 lives with the operator (outside the repo) until unblind, then enters as `blinding_key_arm.json`.
- At unblind, CS composes `blinding_key_FULL.json`. All scores exist on disk **before** any key is applied, so a crash at
  any point loses nothing and the final per-arm attribution is reproducible from the two keys + the scorecard.

## What ships in the submission
The submission presents this scheme as part of the **method**: the two-key diagram above, the guarantee that neither
party alone can deanonymize an arm, and the resulting scorecards/plots (per-dimension arm comparisons under CS / the operator /
combined scoring; CS-vs-the operator agreement). The point demonstrated: **the loop-vs-baseline comparison was measured under a
genuine double-blind**, not a self-graded or single-party-blinded one.
