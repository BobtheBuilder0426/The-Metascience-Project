# skills/ — self-contained capabilities shipped with this bootstrap

Everything the blank Claude Code needs to perform its non-trivial mechanical tasks is in THIS folder — code,
step-by-step skill instructions, the exact subagent brief, the output schema, a worked example, and fallbacks. Nothing
is assumed to pre-exist on the host except a Python 3 interpreter and a shell (both part of a normal Claude Code
environment). The one third-party Python package used (`pypdfium2`, by pdf-digest) is **auto-installed on first use** by
the script itself — it is a pure wheel with its PDF engine bundled, so there is no system dependency (no poppler, no
compiler). `context-composer` is pure standard-library Python — no install at all.

## `pdf-digest/` — FULLY read a PDF (every page + every figure) → one agent-friendly digest file
The capability the DRIVER relies on: turn each input paper into a dense, information-complete digest so the driver
holds full context **before it ever prompts Claude Science**. The reading is done by the **CC itself via a spawned
subagent**, NOT by Claude Science.
- **`render_pdf.py`** — code. PDF → one PNG per page + page-delimited text + manifest. Self-installs `pypdfium2`.
  Run: `python skills/pdf-digest/render_pdf.py "<file.pdf>" "<out_dir>"`.
- **`SKILL.md`** — the full method: why the earlier CC couldn't read PDFs and how this fixes it; the render step; the
  **exact brief to paste to the reading subagent**; the 9-section digest schema; the verify checklist; fallbacks.
- **`worked_example.digest.md`** — a REAL digest of a neutral demo paper (`example_paper.pdf`, shipped alongside),
  produced by this exact pipeline (the quality bar: every page read, every figure interpreted).
- (The same schema is also summarized in `../DIGEST.md`, which points here.)

## `bridge-shortcut/` — a human-visible, clickable shortcut ("Verknüpfung") to the shared bridge folder
- **`make_shortcut.sh`** — code. **Environment-aware**: detects WSL / native-Windows / macOS / Linux (or takes a hint
  from the pre-flight result) and makes the right native shortcut — a Windows `.lnk` (WSL/Windows), a Finder alias
  (macOS), or a `.desktop` launcher + symlink (Linux) — **always placed inside the CC's workspace folder, never the
  Desktop** (v7 safety fix). Run (bridge folder first, then your workspace root):
  `bash skills/bridge-shortcut/make_shortcut.sh "<bridge-folder>" "<workspace-root>" ["<name>"] ["<env-hint>"]`.
- **`SKILL.md`** — when/why, the per-environment mechanism, usage, verify, and fallbacks (the bridge still works via
  `CONNECTION.md` paths if the shortcut can't be created).

## `context-composer/` — build the per-question CS project Agent Context (guardrails + task-sharpened performance block)
The v8 capability: instead of pasting the bare safety preamble as the CS project context, the bootstrap composes a
context tuned to **this** question — `[safety preamble, verbatim] + [a performance block that sharpens how CS works as a
scientist]`. It sharpens the **WIE** (use real tools, cite primary sources, show reasoning, be complete, honest about
uncertainty, seek novel-but-plausible ideas), never the **WAS** (it reveals no domain, answer, mechanism, dataset, or
method). Pure standard-library Python.
- **`kernel.py`** — code. `compose_context(preamble_body, identity_line, flags, question, dose)` assembles the context
  from the frozen block library; `firewall_scan(perf_block, question)` is the fairness check (question-content-overlap);
  `classify_flags_help()` documents the six flags. No install.
- **`blocks.json`** — the FROZEN, fairness-checked block library (general scientist-craft, each block traced to a
  research principle P1–P12 / source S-054..S-070). **Do not add task/domain text to it** — that is a research change,
  not a per-run edit.
- **`SKILL.md`** — when/how the bootstrap uses it: set six general task-shape flags (no prose about the question),
  compose, **assert the firewall is clean**, paste the result as the Agent Context, log sections+dose.

## How the bootstrap uses these
`../CLAUDE.md` invokes them at the right moments: `bridge-shortcut` in PART B step 9 (once per run, right after that
run's dedicated folder is created — the shortcut lands inside `driver/AL-<name>/`); `context-composer` in PART B step 10
(when the CS project is created — it builds and sets the project's Agent Context); and `pdf-digest` in PART B step 14
(once per input file). You don't need to load anything — just run the commands/skills above from the bootstrap folder as
the manual directs.
