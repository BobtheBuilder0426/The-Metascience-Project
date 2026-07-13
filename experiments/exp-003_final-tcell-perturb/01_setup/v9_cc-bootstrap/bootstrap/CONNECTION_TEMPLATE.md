<!-- TEMPLATE. During PART B (BUILD HANDOFF) for a run, copy this to driver/AL-<name>/CONNECTION.md and fill every ⟨…⟩
     from what you actually verified. This is that run's PERSISTENT BRIDGE RECORD: the run's driver (and any future
     session) reads it to learn the CC↔CS connection WITHOUT redoing setup. Fill only with verified values — no guesses.
     ⟨RUN⟩ = this run's id AL-<name>. -->

# CONNECTION.md — the CC ↔ Claude Science bridge for run ⟨RUN⟩ (persistent record)
**Written by:** the bootstrap session · **On:** ⟨YYYY-MM-DD HH:MM⟩ · **Run:** ⟨RUN⟩ · **Status:** ⟨VERIFIED / PARTIAL⟩

## Claude Science
- **URL:** ⟨e.g. http://localhost:8000/ — the exact tab URL where CS runs on THIS machine (same for every run)⟩
- **Project name:** ⟨RUN⟩   (= AL-<name>; this run's OWN isolated CS project)
- **Project id:** ⟨the proj_… id shown in the CS URL/settings, if visible; else "not shown"⟩
- **Agent Context:** `[safety preamble, verbatim (from CS_PROJECT_PREAMBLE.md, slot filled with this project + this
  run's ONE dedicated folder ⟨RUN⟩)] + [a task-shape-tuned performance block composed by the context-composer skill]`.
  The performance block sharpens HOW CS works (generic craft), never WHAT to conclude; a fairness firewall is asserted
  clean before use. Record `dose: ⟨auto/lean/full/safety_only⟩` and `sections_used: ⟨…⟩` from the skill result.

## This run's dedicated folder (the data channel — this run's OWN folder, granted to ONLY this project)
- **Your-shell path (where the CC reads/writes):** ⟨e.g. ~\cs-workspaces\⟨RUN⟩  OR  /home/you/cs-workspaces/⟨RUN⟩⟩
- **CS-side path (what CS sees when the folder is granted):** ⟨e.g. /home/you/cs-workspaces/⟨RUN⟩⟩
- **Verknüpfung:** a clickable shortcut inside `driver/⟨RUN⟩/` points at this dedicated folder ⟨record the shortcut path +
  its `recreate:` command here, so a future session can rebuild the link⟩
- **How CS sees it:** granted via CS composer "+" → Your files → "Grant folder…" → **Read & write** (this run's own folder
  only; folder grants are account-wide, so other runs' folders may also be visible — leave those untouched)
- **Layout for this run:** `inputs/` (read-only starting files) · `OUTPUT/run-01/` (this run's bundle) — both at the root
  of this dedicated folder (no sub-area; the whole folder is this run's)

## The Verknüpfung (human-visible clickable shortcut to this folder)
- **Environment (from pre-flight):** ⟨wsl / windows / macos / linux — where the bootstrap CC ran⟩
- **Status:** ⟨CREATED / FAILED — from the make_shortcut.sh result at bootstrap⟩
- **Shortcut kind + location:** ⟨the `shortcut_placed` value — always **inside the CC workspace folder**, never the
  Desktop; e.g. Windows `.lnk` at `<wsl>\…\<workspace>\run01.lnk` · or a macOS Finder alias / Linux
  `.desktop` (+ symlink) inside the workspace⟩
- **Points at (target):** this run's dedicated folder above (native form for that environment — e.g. `<wsl>\...`
  via `wslpath -w` for WSL)
- **Recreate command (if the shortcut is missing/broken — run from the bootstrap folder in the CC's shell):**
  `bash skills/bridge-shortcut/make_shortcut.sh "⟨bridge-folder shell path⟩" "⟨your workspace-root⟩" "⟨shortcut name⟩" ⟨env⟩`
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
- **Codex critique panel (drives Gate 1 + Gate 2, see `driver/CODEX_PANEL.md`):**
  - `panel_available:` ⟨yes / no⟩ — yes only if the sanctioned wrapper verified with a real GPT-5.6-sol `-Search` call
  - `codex_run_path:` ⟨absolute path to codex-run.ps1, e.g. …\.claude\scripts\codex-run.ps1 / n/a⟩
  - `codex_invocation:` ⟨the EXACT working command the driver replays, incl. interpreter prefix — e.g. `pwsh -File C:\…\codex-run.ps1` / n/a⟩
  - `panel_workdir_hostform:` ⟨how to express a run's `run_log/panel` path as a Windows host-native path for `-WorkDir` — the literal path or the rule, e.g. `wslpath -w <path>` / n/a⟩
  - `codex_effort_flag:` ⟨the EXACT working reasoning-effort flag form (v9) — e.g. `-Effort <lvl>` OR `-c model_reasoning_effort="<lvl>"`; the driver uses **high** at Gate 1 and **xhigh** at Gate 2 / n/a⟩
  - `panel_multimodal:` ⟨yes / no — **v9 Gate-2 hard precondition.** `yes` only if the probe proved the reviewer both SAW an image and READ a file (see below). Record the exact tokens it returned⟩
    - `image_token_seen:` ⟨the token painted into the probe PNG that gpt-5.6-sol read back, e.g. `VISION-OK-7F3A9` / n/a⟩
    - `boxes_read:` ⟨the count + labels/colours it reported from the probe image, e.g. `3 — ARGX-119:light blue, MuSK:light green, DOK7:pale yellow` / n/a⟩
    - `file_token_read:` ⟨the token it read from the probe text file via a file read, e.g. `DATA-8K2M-2026` / n/a⟩
    - `multimodal_invocation:` ⟨the EXACT working image-attach form, e.g. `-i <hostform>\probe.png` (Codex `codex exec -i <file.png>` attaches the image to the prompt) / n/a⟩
  - `panel_verify:` ⟨e.g. "codex-run.ps1 -Model gpt-5.6-sol -Effort high -Search → PANEL_OK, web_search live, exit 0" / reason it failed⟩
  - If `panel_available: no` (or missing/unreadable), the driver runs the loop with the built-in degrade (self-review at both gates) — not fatal. **But `panel_multimodal: no` while `panel_available: yes` means the Gate-2 figure review runs text-only and MUST be logged as a degraded Gate 2 (v9 wants full multimodal — see `driver/CODEX_PANEL.md` Gate 2).**
- **Chrome control:** ⟨PASS — own MCP tab, tabId ⟨…⟩⟩

## Inputs staged for this run
⟨list each file copied into inputs/ with size, e.g. "- paperA.pdf (5.9 MB) — digested → context/paperA.pdf.digest.md"⟩

## How to resume (for THIS run's driver / any later session)
0. **Find the folder fast:** the Verknüpfung above (a clickable shortcut located **inside `driver/⟨RUN⟩/`** — never on the
   Desktop) opens this run's dedicated folder directly. If it's gone, run the recreate command above to restore it — then
   continue.
1. Open your OWN new Chrome tab to the **URL** above (never the account home, never someone else's open tab).
2. Open project **⟨RUN⟩** (do NOT create a new project; do NOT re-attach the folder — both already exist). Do not open any
   other `AL-*` project — those belong to other runs.
3. Send `reply OK`, confirm `OK` back → channel live. Then run the loop (see driver/CLAUDE.md, substituting your ⟨RUN⟩).

**If CS shows "login no longer valid" / "reconnecting", or the tab is dead:** the login link is single-use and expires
in ~3 min (and a daemon restart kills the open session) — mint a **fresh** one; never reuse a link/bookmark. From
PowerShell: `wsl -- bash -lc "claude-science url"` → paste the printed `http://localhost:8000/?nonce=…` into your own
Chrome tab → **Sign in** → reopen project **⟨RUN⟩** (do not recreate it or re-attach the folder). Daemon down? Force it
with `wsl -- bash -lc "claude-science serve --port 8000 --no-browser --detached"` (harmless if already up), then get a
fresh link. **Full procedure: `bootstrap/RECONNECT_CLAUDE_SCIENCE.md`.** Only escalate to the human if
`claude-science url` itself errors.
