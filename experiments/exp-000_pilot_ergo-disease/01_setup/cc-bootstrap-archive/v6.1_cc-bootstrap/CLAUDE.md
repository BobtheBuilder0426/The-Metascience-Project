<!-- WORKSPACE ROUTER. This is the ONLY file a session started at the workspace root auto-reads.
     It does not do any work itself — it sends you to the right folder for your role, and it guards against a
     fresh loop session accidentally re-running setup. Keep this file short. -->

# CLAUDE.md — workspace router (read this, then go to your folder)

This workspace runs an **Agentic Research Loop** in **two separate sessions**:

- **BOOTSTRAP session** — sets up the environment (Claude Science project, the shared-folder bridge, permissions),
  reads the inputs, and **prepares a handoff** for the driver. It does **not** run the loop.
- **DRIVER session** — a **fresh, separate** session that reads the prepared handoff and **runs the loop**, driving
  Claude Science to answer the research question.

## Which one are YOU? (decide from your start prompt — do not guess)
Your start prompt tells you your role. Match it:

1. **If your start prompt is exactly `Read CLAUDE.md and bootstrap your workspace.` (or otherwise says "bootstrap")**
   → you are the **BOOTSTRAP** session. **But first check the identity guard below.**
2. **If your start prompt says you are the DRIVER / to "run the loop"** (the copy-paste START PROMPT the bootstrap
   produced) → you are the **DRIVER** session. Go read **`driver/CLAUDE.md`** now and follow it. **Ignore the rest of
   this file** — do not do any bootstrap/setup steps.

## 🚦 IDENTITY GUARD — read before doing anything (prevents wrecking a prepared workspace)
Check whether a file named **`HANDOFF_READY`** exists at this workspace root:

- **`HANDOFF_READY` EXISTS** → this workspace is **already bootstrapped**. Setup is done and locked.
  - You are almost certainly the **DRIVER**. Go read **`driver/CLAUDE.md`** and run the loop.
  - **Do NOT re-run bootstrap, do NOT re-ask the setup questions, do NOT modify `driver/`, `CONNECTION.md`, or the
    Claude Science project.** Re-running a finished bootstrap is the one genuinely harmful mistake here.
  - Only if you were *explicitly* told to re-bootstrap from scratch (rare) should you proceed to `bootstrap/` — and even
    then, ask the human to confirm first.
- **`HANDOFF_READY` does NOT exist** →
  - If your start prompt is the **bootstrap** trigger → you are the **BOOTSTRAP** session: go read **`bootstrap/CLAUDE.md`**
    and follow it.
  - If your start prompt is a **driver / run-the-loop** prompt → the handoff is **not ready yet**. **Stop** and tell the
    human: *"This workspace hasn't been bootstrapped yet — run the bootstrap session first (start a session with
    'Read CLAUDE.md and bootstrap your workspace.'), then start me again."* Do not try to drive an unprepared project.

**Default rule:** never assume "bootstrap" by default once `HANDOFF_READY` exists. When your role is ambiguous, prefer
DRIVER (or ask the human) — the safe error is *not* re-running a completed setup.

## Where things are
- `bootstrap/` — the bootstrap session's manual + human guide + setup inputs.
- `driver/` — the driver's manual (`CLAUDE.md`), the bridge record (`CONNECTION.md`), input digests (`context/`), the
  copy-paste `START_PROMPT.md`, and the run output (`OUTPUT/`). Built by the bootstrap session; empty until `HANDOFF_READY`.
