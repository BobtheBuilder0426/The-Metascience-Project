# Skill: context-composer — build the per-question CS project Agent Context (guardrails + task-sharpened performance block)

## When to use
Once per run, in PART B, **right when you create the Claude Science project** for a question (the step where you paste
the project's Agent Context). Use it **after** you have the question and any input files in hand, and after you have
chosen the run name (so you know the project name + granted folder for the safety slot).

## What it does — and the ONE rule it never breaks
It writes the CS project's Agent Context = **[safety preamble, verbatim] + [a performance block tuned to THIS
question's SHAPE]**. The performance block sharpens *how CS works as a scientist* (use real tools, cite primary
sources, show reasoning, be complete, be honest about uncertainty, seek novel-but-plausible ideas, self-check) so the
session is optimized for exactly this task.

**It never tells CS how to solve the task, and never reveals what the task is about.** It sharpens the **HOW** (general
scientist craft), never the **WHAT** (the domain, the answer, a mechanism, a dataset, a method). This is not a matter
of care — it is enforced mechanically (see Fairness firewall). The baseline arm must be able to receive the *same*
question and the composer must add nothing that hints at the answer.

## Why it is safe by construction
- The performance text comes from a **frozen, pre-checked block library** (`blocks.json`), each block written as
  general scientist-craft and traceable to the OPT-1 research (principles P1–P12, sources S-054..S-070). You do **not**
  write prose about the question — you only set general **task-shape flags**.
- A **fairness firewall** then scans the assembled performance block and fails if any distinctive content-word from the
  actual question appears in it. Clean composition returns no hits; any hit is a hard stop to review.

## How to use it (the blank CC's job = set flags, not write prose)
The kernel helper is auto-loaded when this skill loads. Steps:

1. Read the question. Decide these **general** yes/no flags from the question's SHAPE (not its subject). Run
   `classify_flags_help()` to see the exact wording of each:
   - `supplies_inputs` — did the human attach papers/files with the question?
   - `involves_data` — does the task involve datasets / quantitative analysis / computation?
   - `asks_experiment` — does it ask to design an experiment / protocol / test?
   - `asks_hypothesis` — does it ask for a hypothesis / explanation / rationale?
   - `asks_novelty` — does it ask for something new / not-yet-proposed?
   - `asks_prediction` — does it ask to predict / propose a candidate (compound, target, outcome)?
   None of these reveal the subject — they are structural.

2. Build the safety `identity_line` for this run: the project name + the ONE dedicated folder granted to it
   (name + path) — exactly what you already fill into the safety preamble's `⟨INSERT HERE⟩` slot.

3. Compose:
   ```python
   res = compose_context(
       preamble_body = open("bootstrap/CS_PROJECT_PREAMBLE.md").read().split("```")[1].strip("\n"),
       identity_line = 'project "AL-<name>" · folder "AL-<name>" (/path/to/cs-workspaces/AL-<name>)',
       flags         = {"supplies_inputs": True, "asks_hypothesis": True, "asks_experiment": True},  # example
       question      = "<the exact question text>",   # used ONLY by the firewall; never written into the context
       dose          = "auto",   # recommended: full backbone + only the conditionals this task triggers
   )
   ```

4. **Check the firewall before using the output:**
   ```python
   assert res["firewall_hits"] == [], f"FAIRNESS STOP — question content leaked: {res['firewall_hits']}"
   ```
   If it is not empty, do **not** paste the context — a block or the identity line contains task content; fix and
   recompose. (With the frozen library + a clean identity line this is always empty.)

5. Paste `res["context"]` as the CS project's Agent Context. Log `res["sections_used"]` and `res["dose"]` in the run's
   `run_log/` so the analysis can attribute the result to the context that was used.

## Dose
- `auto` (recommended): always-on backbone (capability activation, citations, reasoning, completeness, honest
  uncertainty) **+** the conditional levers this task triggers (anchored self-critique when inputs/data/experiment;
  novelty-paired-with-plausibility when hypothesis/novelty/prediction).
- `lean`: backbone only (no conditionals). `full`: everything. `safety_only`: preamble alone (= what the baseline
  arm gets; use if you ever need to reproduce the control).
The OPT-1 measurement plan compares doses; `auto` is the default the loop ships.

## Files in this skill
- `SKILL.md` — this file.
- `blocks.json` — the frozen, fairness-checked block library (general scientist-craft; do NOT add task/domain text).
- `kernel.py` — auto-loaded helper: `compose_context(...)`, `firewall_scan(...)`, `classify_flags_help()`, `FLAG_KEYS`.

## What NOT to do
- Do **not** write your own sentences about the question into the context. If you think a block is missing, that is an
  OPT-1 research change (edit the frozen library deliberately + re-run the fairness check), not a per-run edit.
- Do **not** skip the firewall assert.
- Do **not** edit the safety preamble text — only fill its identity slot.
