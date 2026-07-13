# Skill: bridge-shortcut — a human-visible clickable shortcut ("Verknüpfung") to the shared bridge folder

## When to use
During bootstrap SETUP, right after you have resolved + verified the shared workspace/bridge folder from your shell.
The human wants a **shortcut they can see and click** that opens the bridge folder directly — a convenience, and a
visible, reliable marker of the bridge that a future session in this workspace can find immediately. `CONNECTION.md`
remains the durable text record; this skill adds the clickable artifact on top of it.

## It adapts to YOUR environment (do not assume WSL)
The blank CC that runs this bootstrap may live in different environments, and Claude Science runs on the same machine.
`make_shortcut.sh` **detects** the environment (or takes an explicit hint from your PRE-FLIGHT result) and makes the
right native shortcut:
- **WSL** (Linux under Windows — our reference setup) → a real Windows **`.lnk`** on the Windows Desktop, target
  `<wsl>\...`. `wslpath -w` produces the correct UNC form for THIS Windows build + distro (we do NOT hardcode
  it). The result is a standard Windows folder shortcut the user can double-click in Explorer to open the bridge folder.
- **native Windows** (CC in Git-Bash/MSYS) → a Windows **`.lnk`** (via `cygpath -w` + PowerShell WScript.Shell COM).
- **macOS** → a **Finder alias** on `~/Desktop` (via `osascript`); falls back to a symlink if osascript is unavailable.
- **plain Linux** → a **`.desktop`** launcher on `~/Desktop` **plus** a symlink (works in file managers + terminals).
- **CS on a remote/headless host** → the script still drops a symlink you can reach; record the path in `CONNECTION.md`.

In every case the **last-resort fallback is a symlink**, and the bridge itself always still works via the paths in
`CONNECTION.md` — the shortcut is a convenience/visibility layer, never the bridge.

## Mechanism (no extra installs — shell + OS built-ins only)
- WSL/Windows: `wslpath -w`/`cygpath -w` → Windows path; PowerShell `[Environment]::GetFolderPath("Desktop")` →
  Desktop (handles OneDrive redirection); PowerShell **WScript.Shell** `CreateShortcut → TargetPath → Save()` writes the
  `.lnk`; `Test-Path` verifies it.
- macOS: `osascript` tells Finder to `make alias file`.
- Linux: write a `[Desktop Entry] Type=Link URL=file://…` file + `ln -sfn`.

## Usage
```
bash skills/bridge-shortcut/make_shortcut.sh "<bridge-folder>" ["<shortcut-name>"] ["<env-hint>"] ["<dest-dir>"]
```
- `<bridge-folder>`  path to point at, as THIS shell sees it (default: current dir).
- `<shortcut-name>`  base name of the shortcut (default: the folder's own name — keeps it neutral).
- `<env-hint>`       `wsl` | `windows` | `macos` | `linux` to FORCE the environment (default: auto-detect). Pass the
                     value from your PRE-FLIGHT step-1 result if auto-detect guesses wrong.
- `<dest-dir>`       where to place the shortcut, in that env's native path form (default: the Desktop).

Read the output: on success it prints `SHORTCUT-OK`, the resolved `shortcut_placed` path, and the exact `recreate:`
command — copy that into `CONNECTION.md` so any future session can rebuild the link.

## Verify (do this, don't assume)
- The script printed `SHORTCUT-OK` (not `SHORTCUT-FAIL`).
- `shortcut_placed` points where you expect (Desktop unless you overrode it).
- Tell the human where it is + that they can see/click it (they report back; the loop needn't block on it).

## If it fails (the bridge still works)
- The bridge is fully functional via the paths + attach recorded in `CONNECTION.md`. Do not block the run.
- The script prints a manual recipe (e.g. right-click Desktop → New → Shortcut → paste the path).
- Record in `CONNECTION.md` that the shortcut couldn't be auto-created, plus the recreate command, so it can be retried.

## Notes
- Re-running is safe: it overwrites an existing shortcut of the same name; it never deletes anything else.
- It touches only the one shortcut (and, on Linux, one symlink) it creates.
