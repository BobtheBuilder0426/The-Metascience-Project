# v6 architecture: bootstrap session → handoff → driver session
**Date:** 2026-07-10 · **Author:** Claude Science (CS) · **For:** v6 rebuild plan step 2 (LB-051)

## Why two sessions
Through v5 a single blank Claude Code (CC) both set up the environment AND ran the loop. The operator wants these
split: a **bootstrap session** that prepares everything and then **locks + documents** it, and a **separate driver
session** — started fresh in the same workspace — that reads the prepared handoff and runs the research loop. Reasons:
a clean driver starts with a purpose-built context (no setup clutter in its history), the handoff is an explicit,
inspectable artifact, and the division mirrors the "Document-and-Clear / fresh context per session" best practice
(S-022). The hard risk this introduces is **identity confusion**: a driver session starting in the same workspace must
never mistake itself for the bootstrap and re-run setup. The design below makes role assignment explicit and adds a
guard.

## Workspace layout (top level of the shared workspace folder)
```
<workspace>/
├── CLAUDE.md              ROUTER — the only file a cold session auto-reads. Dispatches by role, enforces identity guard.
├── bootstrap/             the BOOTSTRAP session's home (the neutral start package the operator hands over)
│   ├── CLAUDE.md          full bootstrap manual (pre-flight → setup → build bridge → intake → BUILD HANDOFF → lock)
│   ├── START_HERE.md      the human's short guide
│   ├── SETUP.txt          optional pre-fill: CS URL + workspace folder name/location
│   ├── project-naming-convention.md
│   └── materials/         optional shipped starter files + channel-check file
├── driver/                the DRIVER session's home (BUILT BY the bootstrap session, empty until then)
│   ├── CLAUDE.md          the loop manual: how to run the loop (written/locked by bootstrap)
│   ├── CONNECTION.md      the persistent bridge record (CS URL, project, paths, mount+perms, verification)
│   ├── context/           agent-optimized inputs: PDF digests (+ later, the lit-synthesis brief)
│   ├── START_PROMPT.md    the copy-paste prompt the operator pastes into the fresh driver session
│   └── OUTPUT/            the run bundle lands here (run-01/ …)
└── HANDOFF_READY          a marker file written by bootstrap ONLY when the driver folder is fully prepared + locked
```
Note: `inputs/` and `OUTPUT/` for the actual data live under the workspace as before; the driver reads inputs and
writes its bundle to `driver/OUTPUT/`. (Exact input path is recorded in CONNECTION.md so there is one source of truth.)

## Role assignment = the start prompt, not inference
A session never *guesses* its role. It is told, by the prompt it is started with:
- **Bootstrap session** is started with: **"Read CLAUDE.md and bootstrap your workspace."** The router sees the word
  **bootstrap** → routes to `bootstrap/CLAUDE.md`.
- **Driver session** is started with the **copy-paste START PROMPT** (produced by bootstrap, stored in
  `driver/START_PROMPT.md`). Its first line is an explicit role declaration, e.g.
  **"You are the DRIVER session. Read driver/CLAUDE.md and run the loop. Do NOT bootstrap."** The router sees **DRIVER**
  → routes to `driver/CLAUDE.md`.

## The router CLAUDE.md (workspace root) — logic
The router is short and does four things:
1. **State the two roles** and that the session must already know which it is from its start prompt.
2. **Dispatch:** if the start prompt says *driver* (or "run the loop") → go read `driver/CLAUDE.md` and STOP reading this
   file. If it says *bootstrap* → go read `bootstrap/CLAUDE.md`.
3. **IDENTITY GUARD (the critical part):**
   - *If `HANDOFF_READY` exists* → the workspace is already bootstrapped. A session that is not explicitly told it is the
     driver must **NOT** re-run bootstrap. It should assume it is the driver (or ask the human which session this is)
     — never silently redo setup, never re-ask the setup questions, never clobber `driver/` or `CONNECTION.md`.
   - *If `HANDOFF_READY` does NOT exist* and the prompt is a driver/run-the-loop prompt → the handoff isn't ready; STOP
     and tell the human to run the bootstrap first (do not attempt to drive an unprepared project).
4. **Never assume bootstrap by default.** Ambiguous start + `HANDOFF_READY` present → treat as driver / ask; ambiguous
   start + no marker → treat as bootstrap. This asymmetry is deliberate: re-running a finished bootstrap is the harmful
   case, so the default leans away from it once setup is locked.

## Bootstrap's new final phase: BUILD HANDOFF + LOCK
After the existing setup+verify steps, the bootstrap session's closing job is to **prepare the driver folder** and lock:
1. Write `driver/CONNECTION.md` (the persistent bridge record — plan step 3).
2. Run the structured intake (question + files), digest each input into `driver/context/` (plan steps 4–5).
3. Write `driver/CLAUDE.md` (the loop manual for the driver) and `driver/START_PROMPT.md` (the copy-paste prompt).
4. Write the `HANDOFF_READY` marker (with a timestamp + a one-line manifest of what's in `driver/`).
5. Print the START PROMPT to the human and stop. The bootstrap session does not run the loop.

## Driver's first action: confirm identity, load bridge, go
The driver session, sent to `driver/CLAUDE.md`, must FIRST: (a) confirm `HANDOFF_READY` exists (else stop — not
bootstrapped); (b) read `CONNECTION.md` to learn the CS URL, project, paths, mount + permission state, and verified
channel — it does **not** re-do setup, it **resumes** the already-attached project; (c) read `context/` digests; then
(d) run the loop. If the browser session dropped, it re-opens its own tab to the CS URL from CONNECTION.md and
re-enters the existing project — it never creates a new project or re-attaches folders.

## What this changes vs v5
- v5 CLAUDE.md (single manual) → split into a **router** + **bootstrap/CLAUDE.md** + **driver/CLAUDE.md**.
- The bootstrap gains a **BUILD HANDOFF + LOCK** phase and no longer runs the loop itself.
- New persistent **CONNECTION.md** replaces relying on in-session memory of the bridge.
- New **identity guard** prevents the same-workspace driver from re-bootstrapping.
