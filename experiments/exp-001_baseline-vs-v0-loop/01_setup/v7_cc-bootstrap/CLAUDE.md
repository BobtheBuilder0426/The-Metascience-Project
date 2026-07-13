<!-- WORKSPACE ROUTER. This is the ONLY file a session started at the workspace root auto-reads.
     It does not do any work itself — it sends you to the right folder for your role, and it guards against a
     fresh loop session accidentally re-running setup. Keep this file short. -->

# CLAUDE.md — workspace router (read this, then go to your folder)

This workspace runs an **Agentic Research Loop** in **two separate sessions**:

- **BOOTSTRAP session** — sets up the environment once (records where CS workspace folders live), then per question
  creates that run's dedicated folder + Claude Science project + bridge + permissions, reads the inputs, and **prepares a
  handoff** for that run's driver. It does **not** run the loop.
- **DRIVER session** — a **fresh, separate** session that reads the prepared handoff and **runs the loop**, driving
  Claude Science to answer the research question.

## Which one are YOU? (decide from your start prompt — do not guess)
Your start prompt tells you your role. Match it:

1. **If your start prompt is exactly `Read CLAUDE.md and bootstrap your workspace.` (or otherwise says "bootstrap")**
   → you are the **BOOTSTRAP** session. **But first check the identity guard below.**
2. **If your start prompt says you are the DRIVER / to "run the loop"** (a copy-paste START PROMPT the bootstrap
   produced) → you are a **DRIVER** session. It names your run id `⟨RUN⟩` (= `AL-<name>`); everything for your run lives
   in **`driver/⟨RUN⟩/`**. Go read **`driver/CLAUDE.md`** now and follow it, substituting your `⟨RUN⟩` throughout.
   **Ignore the rest of this file** — do not do any bootstrap/setup steps, and do not touch any other run's subfolder.

> **One bootstrap prepares MANY runs.** The bootstrap sets up the environment once, then prepares a separate, isolated
> run (its own `AL-<name>` CS project + its own `driver/AL-<name>/` subfolder + its own START PROMPT) for **each**
> question. Multiple drivers can run **concurrently**, one per run, without disturbing each other.

## 🚦 IDENTITY GUARD — read before doing anything (prevents wrecking a prepared workspace)
Check whether a file named **`HANDOFF_READY`** exists at this workspace root, then match your start prompt:

- **`HANDOFF_READY` EXISTS** → the environment is **already set up** (one-time PART A is done) and at least one run has
  been prepared (the marker gains a line per run as each is prepared).
  - **If your start prompt is a driver / run-the-loop prompt** → you are a **DRIVER**. Go read **`driver/CLAUDE.md`** and
    run the loop for your `⟨RUN⟩` only. **Do NOT re-run bootstrap, do NOT re-ask the setup questions, do NOT modify any
    `driver/AL-*/` subfolder other than your own, `CONNECTION.md`, or any Claude Science project.** Re-running a finished
    setup, or touching another run, is the genuinely harmful mistake here.
  - **If your start prompt is the bootstrap trigger** (`Read CLAUDE.md and bootstrap your workspace.`) → this is the
    **"add another question" path**. Go read **`bootstrap/CLAUDE.md`**: it will detect `HANDOFF_READY`, **skip the
    one-time setup (PART A)**, and do only **PART B** — prepare a brand-new named run for your next question **without
    disturbing any existing run**. This is expected and safe.
- **`HANDOFF_READY` does NOT exist** →
  - If your start prompt is the **bootstrap** trigger → you are the **BOOTSTRAP** session: go read **`bootstrap/CLAUDE.md`**
    and follow it (PART A one-time setup, then PART B for the first question).
  - If your start prompt is a **driver / run-the-loop** prompt → the handoff is **not ready yet**. **Stop** and tell the
    human: *"This workspace hasn't been bootstrapped yet — run the bootstrap session first (start a session with
    'Read CLAUDE.md and bootstrap your workspace.'), then start me again."* Do not try to drive an unprepared project.

**Default rule:** never re-run PART A once `HANDOFF_READY` exists. A driver drives its one run; a fresh bootstrap trigger
adds a new run via PART B. When your role is ambiguous, ask the human — the safe error is *not* re-running completed setup.

## Where things are
- `bootstrap/` — the bootstrap session's manual + human guide + setup inputs.
- `driver/` — the **shared** driver manual (`driver/CLAUDE.md`), plus **one subfolder per run** `driver/AL-<name>/`, each
  holding that run's bridge record (`CONNECTION.md`), frozen question (`QUESTION.txt`), input digests (`context/`),
  copy-paste `START_PROMPT.md`, and run output (`OUTPUT/`). Built by the bootstrap session; the per-run subfolders appear
  as each question is prepared, and `HANDOFF_READY` lists every run.
