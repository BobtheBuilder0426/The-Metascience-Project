# START HERE — run the Agentic Loop on a blank Claude Code

You are about to let a **blank Claude Code (CC)** answer research questions by driving a
**Claude Science (CS)** browser tab through a research loop. It works in **two kinds of session**: a
**bootstrap** session sets things up **once** and then prepares a ready-to-go **driver run for each
question you bring**; each **driver** session (a fresh session you start with a prompt the bootstrap
gives you) runs the loop for **one** question. You need: a blank Claude Code open **in this folder**
(the workspace root), and Claude Science running in Chrome on the same machine.

**One bootstrap → many questions.** You bootstrap once. After that, for every question you just give
the bootstrap the question + a short name, and it hands you a start prompt for that question's driver.
You never bootstrap again — even days later, the same bootstrap session (or a fresh one) just prepares
the next question. Different questions' drivers can run **at the same time**, each isolated.

---

## STEP 1 — start the BOOTSTRAP session (copy-paste this one line)

> **Read CLAUDE.md and bootstrap your workspace.**

The bootstrap CC then works on its own: it **pre-flights its environment** (what system it's on,
whether it can control Chrome, whether other AI models like Codex are available) and records **once**
where your CS workspace folders live. Then it asks you — per question — your research question, any
files, and a name for the run; creates that run's **own dedicated folder** + a fresh isolated Claude
Science project it grants that folder to; and **hands you back a short "start prompt"** for that
question's driver. **The bootstrap session never runs the loop itself** — that's each driver's job
(Step 5).

---

## STEP 2 — answer the two one-time setup questions

The first time, the CC asks you (in the Claude Code chat) for two things. Give it both in one reply:

1. **Your Claude Science URL.** Claude Science is an app that opens in a Chrome tab — it has no
   public web address the CC can guess or search for, so it needs *your* instance's address. Open
   Claude Science the way you normally do, **copy the URL from its Chrome tab's address bar** (looks
   like `http://localhost:8000/` or `http://127.0.0.1:<number>`), and paste it in.
2. **Where your Claude Science workspace folders live** — the **parent location** (a folder path) on
   the machine where Claude Science runs, under which the CC may create one folder per run. *The browser
   can't upload files directly, so each run's own folder is that run's data channel with CS.* You do just
   **one** thing:
   - **Tell the CC that one parent location** (e.g. where you keep your CS working folders) — its path.
     That's all; you do **not** make per-run folders yourself.
   - The CC does the rest: per question it creates a **dedicated folder** `AL-<name>/` under that parent,
     connects it, and grants **that** folder to that run's own Science project. **You do NOT need to add
     anything in Claude Science.**

*(Optional shortcut: you can pre-fill both answers in `SETUP.txt` in this folder to skip these
questions — see that file. The CC saves your answers there for next time.)*

**Privacy + isolation (automatic):** the CC always opens its **OWN new Science tab** and creates a
**new project per question**, each granted **only its own dedicated folder** — it will **not** touch any
Science tab you already have open (that's your live session), will **not** open your chats/projects/other
work, and one run's project can't see another run's folder.

---

## STEP 3 — give it your research question (+ any files)

The CC then asks — in the chat — for your **research question** and any **files** to start from.
**Paste the question exactly as a curious scientist would type it**, no editing (the driver does the
sharpening). If you have papers/data, tell the CC and it will pull them in and turn each into an
agent-ready digest. PDFs with figures are fine. One question at a time.

---

## STEP 4 — name the run

The CC asks **what to name this run**. Give it a short tag (letters/digits/hyphens), e.g.
`ergo-hypothesis` or `sarcopenia-q`. The CC uses that **same name for both** the Claude Science project
it creates (`AL-<name>`) and the run's folder here (`driver/AL-<name>/`), so everything for that
question stays together and can't collide with your other runs.

---

## STEP 5 — start the DRIVER session for that run (the loop)

For each prepared question the bootstrap prints a **START PROMPT** (naming that run). To run that loop:
**open a NEW Claude Code session in this same folder** and paste that run's prompt. (A new session is
required so the driver starts clean — the bootstrap won't run the loop itself.) The driver reads the
prepared handoff for its run, reframes your question, and drives Claude Science through the full loop.
It checks the CS tab every ~10 minutes (normal — not stuck). **When a permission card pops up in the CS
tab, click approve.** You can start several runs' drivers in parallel (each in its own new session).

**Another question?** After preparing one run the bootstrap asks if you have another. Say yes and just
give the next question + name — it prepares another driver run without redoing setup. Come back later
with more questions the same way (a fresh bootstrap session picks up where you left off).

---

## What you get at the end
For each run, in **that run's dedicated folder** under `AL-<name>/OUTPUT/run-01/` — reachable in one click
via the Verknüpfung the CC placed inside `driver/AL-<name>/`: a **`presentation/`** folder (the result to
collect — `result.md`, `reasoning.md`, `figures/`, `sources.md`, `process_trace.json`) and a sibling
**`run_log/`** folder (the loop's own record — `reframed_brief.md`, `run_log.md`, `meta.json`,
`RUN_REPORT.md`), which is not part of what gets evaluated.

If the CC gets stuck (either session) it writes **`NEEDS_HUMAN.md`** telling you exactly what to do.
A partial result is still useful — hand back whatever it produced.
