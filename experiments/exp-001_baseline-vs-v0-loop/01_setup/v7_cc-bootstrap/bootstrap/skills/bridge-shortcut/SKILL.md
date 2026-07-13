# Skill: bridge-shortcut — a human-visible clickable shortcut ("Verknüpfung") to the shared bridge folder

## When to use
During bootstrap SETUP, right after you have resolved + verified the shared workspace/bridge folder from your shell.
The human wants a **shortcut they can see and click** that opens the bridge folder directly — a convenience, and a
visible, reliable marker of the bridge that a future session in this workspace can find immediately. `CONNECTION.md`
remains the durable text record; this skill adds the clickable artifact on top of it.

## ⚠️ SAFETY RULE (v7 — non-negotiable): the shortcut goes INSIDE your workspace, never the Desktop
The shortcut is placed **only inside the CC's own workspace folder** (the folder you were given as your workspace).
It is **never** written to the Desktop or anywhere else on the human's machine. You have no business touching the
human's Desktop or any path outside your workspace — doing so was a real breach in the previous version and is now
blocked. The shortcut's whole purpose is that the human (and any future session) browsing **inside the workspace** can
find the shared CS/bridge folder reliably. The script now **requires** a `<workspace-root>` argument and refuses to
run without it — it will not guess a location.

## It adapts to YOUR environment (do not assume WSL)
The blank CC that runs this bootstrap may live in different environments, and Claude Science runs on the same machine.
`make_shortcut.sh` **detects** the environment (or takes an explicit hint from your PRE-FLIGHT result) and makes the
right native shortcut — always placed **inside your workspace folder**:
- **WSL** (Linux under Windows — our reference setup) → a real Windows **`.lnk`** inside the workspace, target
  `<wsl>\...`. `wslpath -w` produces the correct UNC form for THIS Windows build + distro (we do NOT hardcode
  it). The result is a standard Windows folder shortcut the user can double-click in Explorer to open the bridge folder.
- **native Windows** (CC in Git-Bash/MSYS) → a Windows **`.lnk`** inside the workspace (via `cygpath -w` + PowerShell
  WScript.Shell COM).
- **macOS** → a **Finder alias** inside the workspace (via `osascript`); falls back to a symlink if osascript is missing.
- **plain Linux** → a **`.desktop`** launcher inside the workspace **plus** a symlink (works in file managers + terminals).
- **CS on a remote/headless host** → the script still drops a symlink inside the workspace; record the path in `CONNECTION.md`.

In every case the **last-resort fallback is a symlink inside the workspace**, and the bridge itself always still works via
the paths in `CONNECTION.md` — the shortcut is a convenience/visibility layer, never the bridge.

## Mechanism (no extra installs — shell + OS built-ins only)
- WSL/Windows: `wslpath -w`/`cygpath -w` → Windows path for BOTH the target folder and the workspace destination;
  PowerShell **WScript.Shell** `CreateShortcut → TargetPath → Save()` writes the `.lnk` **into the workspace**; `Test-Path`
  verifies it. (We do **not** call `GetFolderPath("Desktop")` any more — the destination is always the workspace.)
- macOS: `osascript` tells Finder to `make alias file` in the workspace.
- Linux: write a `[Desktop Entry] Type=Link URL=file://…` file + `ln -sfn`, both in the workspace.

## Usage
```
bash skills/bridge-shortcut/make_shortcut.sh "<bridge-folder>" "<workspace-root>" ["<shortcut-name>"] ["<env-hint>"]
```
- `<bridge-folder>`   **(required)** path to point at (the run's dedicated CS folder), as THIS shell sees it.
- `<workspace-root>`  **(required)** the destination directory the shortcut is placed IN — must be your OWN workspace or a
                      folder inside it (never the Desktop, never outside). In v7's per-run flow this is the run's handoff
                      subfolder **`driver/AL-<name>/`**, so each run's Verknüpfung sits next to that run's handoff files.
- `<shortcut-name>`   base name of the shortcut (default: the bridge folder's own name — keeps it neutral).
- `<env-hint>`        `wsl` | `windows` | `macos` | `linux` to FORCE the environment (default: auto-detect). Pass the
                      value from your PRE-FLIGHT step-1 result if auto-detect guesses wrong.

Both `<bridge-folder>` and `<workspace-root>` are mandatory; omit either and the script prints `SHORTCUT-FAIL` and
exits without writing anything. There is no Desktop option and no free destination override — that is the v7 safety fix.

Read the output: on success it prints `SHORTCUT-OK`, the resolved `shortcut_placed` path (inside your workspace), and the
exact `recreate:` command — copy that into `CONNECTION.md` so any future session can rebuild the link.

## Verify (do this, don't assume)
- The script printed `SHORTCUT-OK` (not `SHORTCUT-FAIL`).
- `shortcut_placed` is **inside your workspace folder** — confirm the path begins with your workspace root and that
  nothing was written to the Desktop or any outside location.
- Tell the human it's in the workspace + that they can see/click it (they report back; the loop needn't block on it).

## If it fails (the bridge still works)
- The bridge is fully functional via the paths + attach recorded in `CONNECTION.md`. Do not block the run.
- The script prints a manual recipe (e.g. inside your workspace folder, right-click → New → Shortcut → paste the path).
- Record in `CONNECTION.md` that the shortcut couldn't be auto-created, plus the recreate command, so it can be retried.

## Notes
- Re-running is safe: it overwrites an existing shortcut of the same name; it never deletes anything else.
- It touches only the one shortcut (and, on Linux, one symlink) it creates.
