<!-- TEMPLATE. During BUILD HANDOFF, copy this to driver/CONNECTION.md and fill every ⟨…⟩ from what you actually
     verified during setup. This is the PERSISTENT BRIDGE RECORD: the driver (and any future session in this workspace)
     reads it to learn the CC↔CS connection WITHOUT redoing setup. Fill only with values you verified — no guesses. -->

# CONNECTION.md — the CC ↔ Claude Science bridge (persistent record)
**Written by:** the bootstrap session · **On:** ⟨YYYY-MM-DD HH:MM⟩ · **Status:** ⟨VERIFIED / PARTIAL⟩

## Claude Science
- **URL:** ⟨e.g. http://localhost:8000/ — the exact tab URL where CS runs on THIS machine⟩
- **Project name:** AL-run-01
- **Project id:** ⟨the proj_… id shown in the CS URL/settings, if visible; else "not shown"⟩
- **Agent Context:** empty (fairness — the project carries no project-specific instructions)

## The shared workspace folder (the data channel)
- **Your-shell path (where the CC reads/writes):** ⟨e.g. ~\run01  OR  /home/you/run01⟩
- **CS-side path (what CS sees when the folder is attached):** ⟨e.g. /home/you/run01⟩
- **How CS sees it:** attached via CS Files → "Add folder…" → **Read & write** (granted at bootstrap)
- **Layout on this folder:** `inputs/` (read-only starting files) · `driver/OUTPUT/run-01/` (the run bundle goes here)

## The Verknüpfung (human-visible clickable shortcut to this folder)
- **Environment (from pre-flight):** ⟨wsl / windows / macos / linux — where the bootstrap CC ran⟩
- **Status:** ⟨CREATED / FAILED — from the make_shortcut.sh result at bootstrap⟩
- **Shortcut kind + location:** ⟨the `shortcut_placed` value, e.g. Windows `.lnk` at C:\Users\you\Desktop\run01.lnk ·
  or macOS Finder alias at ~/Desktop/run01 · or Linux ~/Desktop/run01.desktop (+ symlink)⟩
- **Points at (target):** the workspace folder above (native form for that environment — e.g. `<wsl>\...`
  via `wslpath -w` for WSL)
- **Recreate command (if the shortcut is missing/broken — run from the bootstrap folder in the CC's shell):**
  `bash skills/bridge-shortcut/make_shortcut.sh "⟨your-shell path⟩" "⟨shortcut name⟩" ⟨env⟩`
  *(This is why CONNECTION.md is kept: it is the durable memory of how to rebuild the bridge AND the clickable link.
  The shortcut is a convenience/visibility layer — if it's gone, the bridge still works via the paths above; just
  re-run the command to restore the clickable folder shortcut.)*

## Verification (what was actually checked at bootstrap)
- **Shell R/W:** ⟨PASS/FAIL⟩ — wrote + read back a sentinel in `inputs/_bridge_check.txt`
- **Channel token round-trip:** ⟨PASS/FAIL⟩ — CS opened the attached folder and read back the same token
- **Real-file check:** ⟨PASS/FAIL⟩ — CS opened ⟨channel-check filename⟩ from the attached folder and reported
  ⟨the concrete detail it returned, e.g. "30 pages, title '…'"⟩, which matches the real file
- **Permissions pre-granted (project scope):** code/bash exec = ⟨Always/for-project⟩ · connectors =
  ⟨for-project⟩ · compute = ⟨for-project⟩

## Other capabilities found at pre-flight (for the driver to exploit)
- **System:** ⟨OS / machine label⟩
- **Other AI models:** ⟨e.g. Codex CLI 0.x present at ⟨path⟩ / none found⟩ — available for cross-model checks if the loop wants them
- **Chrome control:** ⟨PASS — own MCP tab, tabId ⟨…⟩⟩

## Inputs staged for this run
⟨list each file copied into inputs/ with size, e.g. "- paperA.pdf (5.9 MB) — digested → context/paperA.pdf.digest.md"⟩

## How to resume (for the driver / any later session)
0. **Find the folder fast:** the Verknüpfung above (a clickable shortcut in Explorer, usually on the Desktop) opens
   this workspace directly. If it's gone, run the recreate command above to restore it — then continue.
1. Open your OWN new Chrome tab to the **URL** above (never the account home, never someone else's open tab).
2. Open project **AL-run-01** (do NOT create a new project; do NOT re-attach the folder — both already exist).
3. Send `reply OK`, confirm `OK` back → channel live. Then run the loop (see driver/CLAUDE.md).
If the URL no longer resolves (CS moved/port changed), that is the ONE thing to ask the human — everything else is here.
