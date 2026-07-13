<!-- exp-002 RUN PACKS — operator-facing. Everything you copy-paste to run the 9 answer-runs, plus the folder-creation
     checklist. Authored by [CS], LB-093. The delivered prompt (question + output-format) is byte-identical across all
     three arms; only the delivery channel differs. -->

# exp-002 — RUN PACKS (copy-paste ready for all 3 arms)

**Experiment:** `exp-002_baseline-vs-v7-vs-v8` — one loop-optimization test, **3 questions × 3 arms × 1 run = 9 answer-runs**.
**Arms:** **B** = baseline blank CS · **L7** = v7 loop · **L8** = v8 loop (v7 + composed CS context + Codex review panel).
**The one invariant:** each question is delivered **byte-identical** to all three arms — the *question text + the
output-format block*, verbatim. Only *how* it is delivered differs (paste into a blank CS project vs. hand to a bootstrap
CC). That identity is the fairness backbone of the experiment; the files here are built so you never have to retype it.

---

## The three questions (locked verbatim, `test-set/questions.json`, status READY)
| QID | Category | Question (verbatim) | Materials |
|---|---|---|---|
| **Q1** | 1 — day-in-the-lab (paper → hypothesis + pilot) | *"inspired by the publication attached, generate a novel method to identify a different metabolite cocktail that rejuvenates the skeletal muscle in vivo, what would be your first pilot experiment to test this prediction? (paper attached)"* | **1C paper (S-083)** — attach to ALL arms |
| **Q2** | 2 — maximum-creativity big-think | *"Generate a novel, plausible, unifying hypothesis for: Why does biological aging occur?"* | none |
| **Q3** | 3 — translational data breakthrough | *"Starting from publicly available datasets, propose a not-thought-of-yet or new compound to treat complex-I mitochondrial diseases."* | none |

The paper for Q1 is `1C Metabolite Cocktail Muscle Reprogramming.pdf` (Hernandez-Benitez et al. 2024, *Cell Reports
Medicine* 5, 101449 — S-083), staged in `resources/papers/` and this experiment's `test-set/materials/`.

---

## The exact loop folders (what you copy for each loop arm)

- **L8 (v8 loop) — the FINAL v8 cc-bootstrap folder is:**
  ```
  <repo>/experiments/exp-002_baseline-vs-v7-vs-v8/01_setup/v8_cc-bootstrap
  ```
  Windows/WSL view: `<repo>\experiments\exp-002_baseline-vs-v7-vs-v8\01_setup\v8_cc-bootstrap`
  Content hash `331d802b219b4e69` (27 files, excl. `LOOP_VERSION.md`). This is the loop under test.

- **L7 (v7 loop) — copy this folder:**
  ```
  <repo>/experiments/exp-001_baseline-vs-v0-loop/01_setup/v7_cc-bootstrap
  ```
  Content hash `6bbd94a13d13e462` (23 files). Byte-identical to the maintained source at
  `experiments/exp-000_pilot_ergo-disease/01_setup/v7_cc-bootstrap` — either copy is the same loop.

- **B (baseline)** uses **no loop** — just a blank CS project with the guardrail context in this pack.

---

## What's in this pack
```
run-packs/
├── README.md                              ← this file
├── arm-B-baseline/
│   ├── Q1_baseline_PROJECT-CONTEXT.md      paste into the CS project's Agent Context (fill 1 folder path)
│   ├── Q1_baseline_PASTE-question.txt      paste into the CS chat (attach the 1C paper)
│   ├── Q2_baseline_PROJECT-CONTEXT.md   ·  Q2_baseline_PASTE-question.txt
│   └── Q3_baseline_PROJECT-CONTEXT.md   ·  Q3_baseline_PASTE-question.txt
├── arm-L7-v7-bootstrap/
│   └── Q1/Q2/Q3_L7_bootstrap-intake-question.txt   paste when the v7 bootstrap asks for the question
└── arm-L8-v8-bootstrap/
    └── Q1/Q2/Q3_L8_bootstrap-intake-question.txt   paste when the v8 bootstrap asks for the question
```

---

## Folders YOU create (you said you'd own this)
You make the folders; the packs fill them. For each of the 9 runs the pattern is one dedicated folder = one CS project.

1. **Baseline (3 folders).** Create one working folder per baseline question — suggested names
   `exp002-baseline-Q1`, `-Q2`, `-Q3` (anywhere under your CS-workspaces parent). Create a **blank CS project** per
   question, **grant that one folder** to it, and paste its path into the `<<FILL IN …>>` slot of the matching
   `*_PROJECT-CONTEXT.md`. That folder is where CS writes `presentation/`.
2. **Loops (L7 + L8).** You do **not** pre-make per-run folders for the loops — the **bootstrap CC makes them itself**
   (`<cs-workspaces>/AL-<name>/`) when you give it a run name. You only tell the bootstrap, once, the **parent location**
   where CS workspace folders live. Give each run a name when asked (e.g. `AL-exp002-Q1-L8`).

---

## How to run each arm

**Arm B (baseline) — per question (Q1, Q2, Q3):**
1. Create the folder + blank CS project, grant the folder (step 1 above).
2. Open `arm-B-baseline/<Q>_baseline_PROJECT-CONTEXT.md`, fill the one folder-path slot, paste the fenced block into the
   project's **Agent Context**.
3. Paste `arm-B-baseline/<Q>_baseline_PASTE-question.txt` into the chat. **For Q1, attach the 1C paper** to that message.
4. Take CS's single response; it writes `presentation/` into the granted folder. No loop, no follow-ups.

**Arm L7 (v7 loop) and Arm L8 (v8 loop) — per question:**
1. Copy the loop folder (L7 or L8 path above) to the machine as a blank Claude Code workspace (one copy total per loop —
   you reuse it for all 3 questions).
2. Start a blank Claude Code in it and send exactly: **`Read CLAUDE.md and bootstrap your workspace.`**
   First time it asks two setup questions (your CS URL + the parent location for CS workspace folders).
3. When it asks for the research question, paste `arm-L<7|8>-…/​<Q>_L<7|8>_bootstrap-intake-question.txt`. Give the run a
   name. **For Q1, provide the 1C paper** when it asks for files (it copies + digests it).
4. It prints a **START PROMPT**. Open a **new** blank Claude Code and paste that prompt → that session drives the loop and
   writes `driver/AL-<name>/OUTPUT/run-01/presentation/`. Repeat step 3 for the next question (no re-bootstrapping).

> The output-format block is already appended to every intake question, so the loop and baseline receive the exact same
> instruction. Do **not** add or edit it — that byte-identity is the fairness lock.

---

## Collect results → hand back to CS
Copy each run's `presentation/` folder into `02_results/` under an arm-labelled name:
```
experiments/exp-002_baseline-vs-v7-vs-v8/02_results/<QID>_arm_<B|L7|L8>_run01/presentation/
```
(9 folders total.) Then CS scores all nine through the shared harness and runs `make_analysis_3arm.py` +
`make_3arm_figs.py` for the Δ(L8−L7)/Δ(L8−B)/Δ(L7−B) endpoints and figures.

## Two-key double-blind (unchanged from exp-001)
You hold **Key-1** (map each of the 9 runs to a neutral R-code before CS sees them); CS holds **Key-2** (E-codes for
the operator's eval site). Unblinding needs both keys. Keep Key-1 to yourself until scores are in — see
`loop-design/current/blinding-protocol.md`.
