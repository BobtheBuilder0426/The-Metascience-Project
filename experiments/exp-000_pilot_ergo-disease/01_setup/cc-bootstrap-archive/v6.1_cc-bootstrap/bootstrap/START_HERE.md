# START HERE — run the Agentic Loop on a blank Claude Code

You are about to let a **blank Claude Code (CC)** answer a research question by driving a
**Claude Science (CS)** browser tab through a research loop. This runs in **two sessions**:
a **bootstrap** session sets everything up, then a **driver** session (a fresh session you start
with a prompt the bootstrap gives you) runs the loop. You need: a blank Claude Code open **in this
folder** (the workspace root), and Claude Science running in Chrome on the same machine.

Everything the CC needs is already here. You do one action to start, answer two quick setup
questions, give it your research question, then start the driver with one copy-paste prompt.

---

## STEP 1 — start the BOOTSTRAP session (copy-paste this one line)

> **Read CLAUDE.md and bootstrap your workspace.**

The bootstrap CC then works on its own: it **pre-flights its environment** (what system it's on,
whether it can control Chrome, whether other AI models like Codex are available), and prepares a
fresh, isolated Claude Science project to drive. It pauses to ask you the two setup questions below,
then your research question, then it **prepares a handoff and hands you back a short "start prompt"**
for the driver. **The bootstrap session does not run the loop itself** — that's the driver's job (Step 4).

---

## STEP 2 — answer the two setup questions

Partway through setup the CC will ask you (in the Claude Code chat) for two things. Give it both in
one reply:

1. **Your Claude Science URL.** Claude Science is an app that opens in a Chrome tab — it has no
   public web address the CC can guess or search for, so it needs *your* instance's address. Open
   Claude Science the way you normally do, **copy the URL from its Chrome tab's address bar** (looks
   like `http://localhost:8000/` or `http://127.0.0.1:<number>`), and paste it in.
2. **A workspace folder** — a shared folder you and Claude Science exchange files through (your input
   files in, the results out). *The browser can't upload files directly, so this shared folder is how
   data moves between you and CS.* You do just **one** simple thing:
   - **Make an empty folder** on the machine where Claude Science runs — one folder per run (e.g. put
     these next to your other work, NOT inside this bootstrap folder) — and **tell the CC its name and
     where it is.** That's all.
   - The CC does the rest itself: it builds the connection to that folder, puts the files in it, and
     **attaches it to its own Claude Science project** for you. **You do NOT need to add the folder in
     Claude Science.**
   - *(Optional:* if you already have input file(s) for the run, you can drop them into an **`inputs/`**
     subfolder inside that workspace folder — the CC will otherwise create `inputs/` and `OUTPUT/`.)*

*(Optional shortcut: you can pre-fill both answers in `SETUP.txt` in this folder to skip the
questions — see that file. Either way works, and the CC saves your answers there for next time.)*

**Privacy + isolation (automatic):** the CC always opens its **OWN new Science tab** and creates its
**OWN new project** — it will **not** touch any Science tab you already have open (that's your live
session), will **not** open your chats/projects/other work, and uses **only** the one workspace
folder you named (it ignores any other folders it might see mounted in CS).

---

## STEP 3 — give it your research question (+ any files)

When the bootstrap CC finishes setup it asks — in the chat — for your **research question** and any
**files** to start from. **Paste the question exactly as a curious scientist would type it**, no
editing (the driver does the sharpening). If you have papers/data, drop them into the **`inputs/`**
subfolder of your workspace folder; the CC turns each into an agent-ready digest. PDFs with figures
are fine.

---

## STEP 4 — start the DRIVER session (the loop)

When the handoff is ready, the bootstrap prints a **START PROMPT** and stops. To run the loop:
**open a NEW Claude Code session in this same folder** and paste that prompt. (A new session is
required so the driver starts clean — the bootstrap won't run the loop itself.) The driver reads the
prepared handoff, reframes your question, and drives Claude Science through the full loop. It checks
the CS tab every ~10 minutes (normal — not stuck). **When a permission card pops up in the CS tab,
click approve.**

---

## What you get at the end
In your **workspace folder** under `driver/OUTPUT/run-01/`: the final answer (`answer.md`), any
figures, and the full step-by-step of what happened (`process_trace.json`), plus `run_log.md` and
`RUN_REPORT.md`.

If the CC gets stuck (either session) it writes **`NEEDS_HUMAN.md`** telling you exactly what to do.
A partial result is still useful — hand back whatever it produced.
