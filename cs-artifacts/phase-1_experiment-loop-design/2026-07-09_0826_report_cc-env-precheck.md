<!-- WHAT THIS FILE IS: the CC-side environment pre-check report, produced by a BLANK Claude Code on 2026-07-09 from
     the prompt in 2026-07-09_0130_protocol_cc-env-precheck.md. PROVENANCE: the blank CC was (correctly) kept ISOLATED
     from this shared repo — it did NOT read or write the shared folder and made NO labbook entry (a blank CC that
     edited our repo would no longer be "blank"). The report below was relayed by the operator (the operator) and saved here by
     CS as the repo record. HOW TO USE (CS): this + 2026-07-09_0130_report_cs-env-selfcheck.md = the full environment
     picture the loop design is grounded in. Verbatim report follows. -->

# CC-side environment pre-check report  [CC, operator-relayed] — 2026-07-09 08:26 CEST (UTC+0200)

Prepared by: a blank Claude Code (CC) for partner system "Claude Science" (CS).
Scope note (operator instruction, 2026-07-09): probing was confined to the CC workspace
`…/the Metascience Project-hackathon-life-sciences/runtime/Pre Check`. The Metascience Project root and the `shared/` submit-repo
(WSL mount) were **intentionally NOT touched** — no reads, no writes. No `LABBOOK.md` entry was made.
This report is the only artifact, written into the CC workspace (not the shared repo).
All probes were read-only; no secrets are printed (PRESENT/ABSENT only).

Verdict legend: **WORKS** / **PARTIAL** / **FAILS** / **UNKNOWN**.

---

## A. Claude Code itself

- **A1 version / model / plan — PARTIAL.** `claude --version` → `2.1.91 (Claude Code)`. Active model:
  **Opus 4.8** (`claude-opus-4-8`), per session runtime. Plan tier (Max / Max-20x): **UNKNOWN** — not
  verifiable from here without account/billing access. Consistent-with-paid-Max signals: OAuth auth (no
  API key in env, see E) and Opus 4.8 availability. `claude` binary: `~\AppData\Roaming\npm\claude`.
- **A2 parallel sub-agents (Task/Agent tool) — WORKS (capability), use sparingly.** Agent tool present;
  subagent types available: `claude`, `Explore`, `general-purpose`, `Plan`, `claude-code-guide`,
  `statusline-setup`. Not stress-tested (would be heavy / consume allowance). **Realistic parallelism is
  RAM-bound**, not tool-bound: ~2.3 GB free (dipped to ~0.7 GB under load; see C11) on a shared machine also
  running Chrome + CS. Recommend ≤2–3 light agents at once; avoid heavy parallel fan-out.
- **A3 skills + MCP servers — WORKS.** Skills available (subset of ~25): `deep-research`, `code-review`,
  `verify`, `run`, `init`, `security-review`, `simplify`, `claude-api`, `dataviz`, `docx`/`pdf`/`pptx`/`xlsx`,
  `skill-creator`, `schedule`, `loop`, `update-config`, `consolidate-memory`, plus project skill
  `a separate project-combo-discovery`. MCP: `claude mcp list` shows **codex** ✓ Connected at CLI level
  (`codex mcp-server -c sandbox_mode=workspace-write -c approval_policy=never -c windows.sandbox=unelevated`).
  Additional MCP tool namespaces provided by the host app this session: `claude-in-chrome`, `codex`,
  `ccd_session` / `ccd_directory` / `ccd_session_mgmt`, `visualize`, `Claude_Preview`, `mcp-registry`,
  `scheduled-tasks`.
- **A4 headless `claude -p` — WORKS.** `claude -p "reply with the token PRECHECK-OK"` → returned
  `PRECHECK-OK`, exit 0, within the 90 s time-box. It ran (not blocked); remaining free-allowance not
  measured but the call was not rate-limited.

---

## B. Drive channel (Chrome control of the CS tab)   <-- most important

**Summary verdict — NOT INDEPENDENTLY VERIFIED BY CC; OPERATOR-ATTESTED.** Per operator instruction on
2026-07-09, CC did **not** run a live browser test against the running CS session. The operator (the operator)
has personally verified that the CC→CS browser drive works and has stated **CS should accept that
attestation**. What CC *could* confirm read-only is below; the live round-trip + approval-card click were
deliberately not executed.

- **Q5 extension installed & connected — WORKS.** `list_connected_browsers` → 1 browser:
  `{name:"Browser 1", osPlatform:"Windows", isLocal:true, deviceId:74fce274-…}`. The Claude-in-Chrome MCP
  is present and reachable from this CC. **Important mechanism note:** the MCP drives its **own tab group**;
  `tabs_context_mcp` reported *"No tab group exists for this session."* The live CS tab is therefore **not
  currently under MCP control** — a driving CC must first bring the CS tab under control
  (`tabs_context_mcp{createIfEmpty}` / `navigate` to the CS URL) before it can read or type into it.
- **Q6 (i) see/read, (ii) locate composer, (iii) type, (iv) submit, (v) read reply — NOT EXECUTED
  (operator-attested WORKS).** Tools exist for each step and are loaded: (i) `read_page` (a11y tree) /
  `get_page_text`; (ii) `find "message composer"`; (iii) `computer{action:type}` or `form_input{ref}`;
  (iv) `computer{action:key, text:"Enter"}` or find+click the Send button; (v) `get_page_text` / `read_page`
  after completion. None were run against CS.
- **Q7 turn-completion signal — DESIGN NOTE (unverified).** No single reliable "done" event was tested.
  Recommended signal for the driving CC: **poll** the page and treat the turn as complete when BOTH (a) the
  generating/"Stop" affordance disappears and the Send control re-enables, AND (b) the response node's text
  is **stable across two consecutive reads**. A single read risks capturing a partial stream. Reliability:
  moderate, polling-based — build in a stable-text debounce, not a one-shot read.
- **Q8 approval cards (folder / host / run-code / plan) — NOT VERIFIED; feasible in principle.** Such cards
  render as DOM buttons and would be visible via `read_page` and clickable via `computer{left_click}` /
  find+click "Approve". **Not exercised here.** For an *unattended* loop this is a critical unknown — if a
  permission card appears and is not detected/clicked, the loop stalls. Recommend an explicit
  detect-and-approve watchdog before running unattended.
- **Q9 round-trip latency — UNKNOWN (not measured for CS).** No browser round-trip was performed. For
  reference, non-browser round-trips this session were fast: Codex MCP ≈ immediate; `claude -p` well under
  90 s. A CS browser cycle adds UI-render + model-streaming + poll-interval time on top.

---

## C. Local runtime area

- **C10 Windows-native vs WSL, + local path — WORKS (Windows-native).** `uname -a` →
  `MINGW64_NT-10.0-19045 … Msys` (Git Bash on Windows); `ver` → `Microsoft Windows NT 10.0.19045`. CC runs
  **Windows-native, NOT inside WSL.** A WSL Ubuntu exists separately (the `shared/` symlink targets
  `~/…`) but CC is not in it. Local runtime areas OUTSIDE the shared mount:
  the CC workspace `…\the Metascience Project-hackathon-life-sciences\runtime\Pre Check` and the session scratchpad
  `…\AppData\Local\Temp\claude\…\scratchpad`.
- **C11 versions / venv / disk / RAM — PARTIAL.**
  - node **v24.14.1**; git **2.53.0.windows.2**.
  - python: default `python` → **3.11.15** but it resolves to a *foreign* venv
    (`…\AppData\Local\hermes\hermes-agent\venv\…`); `py -3` → **3.12.10** (system launcher); `python3` is the
    Windows Store stub (absent).
  - **venv + pip — PARTIAL/PROBLEM:** `python -m venv` (and `py -3 -m venv`) scaffolds the venv directory,
    but **`ensurepip` fails (exit 1)** for *both* interpreters → a fresh venv comes up **without pip**.
    The global hermes-venv pip works (`pip 24.0`). Actual `pip install` was **not run** (hard rule: no installs);
    global pip is functional, but "create clean venv → pip install" is **not** working out-of-the-box.
  - Disk: **351.2 GB free** on C: (roomy).
  - RAM: **7.7 GB total; ~2.3 GB free (30%) on re-check** (2026-07-09 ~08:30 CEST). An earlier reading during
    parallel probing momentarily showed only ~0.7 GB free, so headroom is **variable and modest** under load.
    Commit limit 31.7 GB (pagefile-backed), ~11.1 GB committed — short spikes page out rather than OOM.
- **C12 internet from runtime — WORKS.** `pypi.org/simple/` → 200 (≈6.4 s, slow), `api.anthropic.com` →
  404 (reachable), `google.com` → 200. Web + pip index + Anthropic API host are all reachable (no download performed).
- **C13 read shared + write file CS sees — NOT TESTED against shared (operator instruction).** The `shared/`
  mount was intentionally not touched. **Local** write capability WAS verified in the CC workspace: created
  `phase1-cc-bridge-test.txt` (103 bytes), read it back, deleted it cleanly (DELETE OK). Whether a file
  written by CC is visible to CS via the shared mount was **not** verified here.
- **C14 atomic append to `LABBOOK.md` — NOT PERFORMED (operator instruction: no labbook entry).** Method that
  *would* be used per repo convention: a **WSL-native append on the Linux side**
  (`printf '…\n' >> LABBOOK.md` executed inside Ubuntu against the native path), rather than writing over the
  `<wsl>` file-share from Windows. Reported as method-only; not executed.

---

## D. Codex (2nd model)

- **D15 available / invocation / auth — WORKS.** Codex is available two ways: (a) MCP tool
  `mcp__codex__codex` (`claude mcp list` → **codex ✓ Connected**), and (b) CLI `codex` on PATH
  (`~\AppData\Roaming\npm\codex`). It is **authenticated** (it produced output without an auth
  prompt). Server launch config: `sandbox_mode=workspace-write`, `approval_policy=never`,
  `windows.sandbox=unelevated`.
- **D16 trivial round-trip — WORKS.** `mcp__codex__codex(prompt:"…reply with token CODEX-OK…",
  sandbox:read-only, approval:never)` → returned exactly **`CODEX-OK`**. Low latency, no auth blocker.

---

## E. API access (the $200 credits — availability only)

- **E17 Anthropic API key present — ABSENT.** Env check (names + length only, values never printed):
  `ANTHROPIC_API_KEY` ABSENT, `CLAUDE_API_KEY` ABSENT, `ANTHROPIC_AUTH_TOKEN` ABSENT, `OPENAI_API_KEY` ABSENT,
  `CODEX_API_KEY` ABSENT. Only `ANTHROPIC_BASE_URL` is PRESENT (25-char value = a standard endpoint URL, not a
  secret). Interpretation: Claude Code is authenticated via **OAuth (Max plan)**, not via a raw API key.
  **A trivial direct API call would NOT succeed as-is** — no key is wired into the environment. To use the
  $200 credits, CS must supply/configure a key (e.g. set `ANTHROPIC_API_KEY`). Verdict: key **ABSENT** →
  API-call-ready **NO** without adding a key.

---

## Blockers / risks for an unattended CS-driving loop

1. **Approval cards + turn-completion are unverified for automation — top unattended-loop risk.** The loop must
   reliably (a) detect the "turn done" state via a stable-text + button-state debounce (no clean event exists,
   see B/Q7) and (b) detect+click permission cards; if it misses either it can stall silently. Add a
   detect-and-approve watchdog before running unattended.
2. **Drive channel not CC-verified — rests on operator attestation.** The load-bearing capability (type into CS,
   submit, read reply, click approvals) was not tested by CC. Operator attests it works; CS is asked to accept
   that. No CC-measured latency/reliability data exists. Also: the CS tab is not auto-under-MCP-control — the
   driving CC must "take over" the tab first.
3. **No API key in env → the $200 credits are unusable as-is.** Requires configuring a key (e.g. `ANTHROPIC_API_KEY`).
4. **RAM modest and variable.** Re-checked ~2.3 GB free of 7.7 GB (30%); an earlier reading under parallel load
   dipped to ~0.7 GB. Commit limit 31.7 GB (pagefile) means spikes page out rather than OOM, but keep agent
   parallelism low (≤2–3) and avoid heavy local jobs while Chrome + CS run.
5. **Fresh-venv pip is broken (`ensurepip` fails).** Any "clean venv → pip install" step will fail; use
   `--system-site-packages` / the existing hermes venv / a manual pip bootstrap.
6. **`python` on PATH is a foreign tool's venv** (hermes-agent 3.11.15), not a clean interpreter; prefer `py -3`
   (3.12.10) as a base — but the ensurepip issue affects both.
7. **Slow pypi egress (~6.4 s).** Network out may be sluggish; factor into fetch timeouts.

## Anything surprising or better than expected

- **Codex is fully wired out of the box** — MCP + CLI + authenticated, instant `CODEX-OK`. The 2nd-model
  improvement path is ready with zero setup.
- **`claude -p` headless works cleanly** — good for nested / scripted calls.
- **Disk is generous (351 GB free)** despite the small-RAM machine.
- **Internet reaches pypi and the Anthropic API host** from the Windows-native runtime.
- **The Chrome extension is connected and the full read/type/submit/read toolset is present** — the mechanism
  is in place; only the live end-to-end verification was deferred to the operator.
- **RAM headroom recovered on re-check** to ~2.3 GB free (the initial ~0.7 GB was a transient spike during
  parallel probing) — the machine is tighter than roomy, but not on the edge.
