# skills/ — self-contained capabilities shipped with this bootstrap

Everything the blank Claude Code needs to perform its two non-trivial mechanical tasks is in THIS folder — code,
step-by-step skill instructions, the exact subagent brief, the output schema, a worked example, and fallbacks. Nothing
is assumed to pre-exist on the host except a Python 3 interpreter and a shell (both part of a normal Claude Code
environment). The one third-party Python package used (`pypdfium2`) is **auto-installed on first use** by the script
itself — it is a pure wheel with its PDF engine bundled, so there is no system dependency (no poppler, no compiler).

## `pdf-digest/` — FULLY read a PDF (every page + every figure) → one agent-friendly digest file
The capability the DRIVER relies on: turn each input paper into a dense, information-complete digest so the driver
holds full context **before it ever prompts Claude Science**. The reading is done by the **CC itself via a spawned
subagent**, NOT by Claude Science.
- **`render_pdf.py`** — code. PDF → one PNG per page + page-delimited text + manifest. Self-installs `pypdfium2`.
  Run: `python skills/pdf-digest/render_pdf.py "<file.pdf>" "<out_dir>"`.
- **`SKILL.md`** — the full method: why the earlier CC couldn't read PDFs and how this fixes it; the render step; the
  **exact brief to paste to the reading subagent**; the 9-section digest schema; the verify checklist; fallbacks.
- **`worked_example.digest.md`** — a REAL digest of a 30-page paper produced by this exact pipeline (the quality bar).
- (The same schema is also summarized in `../DIGEST.md`, which points here.)

## `bridge-shortcut/` — a human-visible, clickable shortcut ("Verknüpfung") to the shared bridge folder
- **`make_shortcut.sh`** — code. **Environment-aware**: detects WSL / native-Windows / macOS / Linux (or takes a hint
  from the pre-flight result) and makes the right native shortcut — a Windows `.lnk` (WSL/Windows), a Finder alias
  (macOS), or a `.desktop` launcher + symlink (Linux). Run:
  `bash skills/bridge-shortcut/make_shortcut.sh "<bridge-folder>" ["<name>"] ["<env-hint>"]`.
- **`SKILL.md`** — when/why, the per-environment mechanism, usage, verify, and fallbacks (the bridge still works via
  `CONNECTION.md` paths if the shortcut can't be created).

## How the bootstrap uses these
`../CLAUDE.md` invokes them at the right moments: `bridge-shortcut` in SETUP step 6 (right after the bridge folder is
resolved), and `pdf-digest` in INTAKE step 14 (once per input file). You don't need to load anything — just run the
commands above from the bootstrap folder as the manual directs.
