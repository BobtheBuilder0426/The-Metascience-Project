# CC Bootstrap — version archive (all previous tries, numbered)

Every previous version of the blank-CC bootstrap package, kept for provenance. **Nothing here is for use** — the
current, ready-to-give package is its sibling in this same experiment's setup folder:
**`experiments/exp-000_pilot_ergo-disease/01_setup/v7_cc-bootstrap/`** (see its `HOW-TO-USE.txt`).

**Naming + location rule (locked — see DOCUMENTATION.md §3b):** the current bootstrap is always a folder named
`<version>_cc-bootstrap` living in the active experiment's `01_setup/`, next to this archive. After each run, when we
promote to the next version, the current folder is copied **into this archive under its exact version name** and the
next version is built from it. Every version is named in its owning LABBOOK entry.

The bootstrap evolved in two architectural lines. Folders here are numbered by that evolution; finer per-file
snapshots (where a folder was edited in place rather than re-foldered) are recovered from the artifact store into each
folder's `version-snapshots/`.

## Numbered history (folder ↔ labbook entry ↔ what changed)

| # | Version | Folder / snapshot | LABBOOK | What it was / why it was replaced |
|---|---------|-------------------|---------|-----------------------------------|
| 1 | **v1** pilot | `01_single-folder-bootstrap_v1-v5/version-snapshots/CLAUDE.md.v1–v3` | LB-039, LB-041, LB-042 | First single-folder pilot bootstrap; PRE-FLIGHT self-diagnostic + permissions policy + parent-folder guard added. |
| 2 | **v2** privacy-hardened | `…/CLAUDE.md.v4–v5` | LB-043, LB-044, LB-046 | **Pilot run 1 = privacy breach** (blank CC was logged into the operator's personal Claude, read private chats). Hard privacy block + own-tab/own-project rule + adversarial self-audit added. |
| 3 | **v3** access-fix | `…/CLAUDE.md.v6` | LB-047 | **Run 2:** privacy held ✅ but CC couldn't reach Claude Science. Root cause: CS is a LOCAL app — fixed the reach/identify-before-screenshot flow. |
| 4 | **v4** neutral channel | `…/CLAUDE.md.v7` | LB-049 | **Run 3:** nearly worked (privacy/URL/project/perms all ✅), only the browser PDF **upload** failed. Switched to a neutral shared-folder data channel; 0 project-identity leaks. |
| 5 | **v5** self-attach | `…/CLAUDE.md.v8–v9` + folder `01_…/` (final state) | LB-050, LB-051 | **Run 4 = BREAKTHROUGH:** CC builds the bridge + attaches the folder ITSELF (human only names it); real-file transport verified end-to-end. Only gap: CC couldn't read PDFs locally (no renderer). |
| 6 | **v6.0** two-session | `02_two-session_v6.0_pre-correction/` (from tarball v1) | LB-054 … LB-059 | Rebuilt as **bootstrap→driver** two-session model + router + identity guard + persistent CONNECTION.md + structured intake. **Superseded** because PDF-digest was done inside Claude Science (wrong side) and the clickable shortcut was deferred. |
| 7 | **v6.1** | `v6.1_cc-bootstrap/` (this archive) | LB-061 | Operator rework: PDF-digest is now a **CC-side subagent** (renders every page + reads every figure locally, so the driver holds full context before prompting CS), and the bridge is a **real cross-platform Verknüpfung** (WSL/Windows/macOS/Linux, chosen from the pre-flight result). **First real run** got the bootstrap half all the way to the driver START PROMPT (LB-064). Superseded after 4 issues surfaced (2 safety). |
| 8 | **v7** CURRENT | *(not in archive — the CURRENT folder `../v7_cc-bootstrap/`)* | LB-064, LB-066 | Fixes the 4 issues from the v6.1 run: **① shortcut now placed INSIDE the CC workspace, never the Desktop** (was a safety breach); **②a** exact folder-grant click-path (composer "+" → Your files → Grant folder…); **②b** isolation reworked for CS's **global-scope** grants (visible ≠ yours; add-only, never modify existing grants); **③** intake now asks for input files together with the question (setup-questions ask only URL+folder); **④** a "STAY IN BOUNDS" isolation guardrail baked into the driver START PROMPT + `driver/CLAUDE.md`. **CS-Agent-Context work (safety preamble + optimized loop context) is deliberately deferred to a later version** pending the context-design research. This is the one to use — folder `01_setup/v7_cc-bootstrap/`. |

## Provenance / recovery
- Single-folder line (v1–v5) was edited in place, so only the **final** on-disk state survives as a folder
  (`01_…/`), plus **9 CLAUDE.md + 9 START_HERE** version snapshots recovered from artifact `7595849e…` (CLAUDE.md)
  and `28490522…` (START_HERE) into `01_…/version-snapshots/`.
- Two-session line: **v6.0** = tarball artifact `1985f5e2…` **v1**; **v6.1** = same artifact **v2** (now archived here as
  `v6.1_cc-bootstrap/`); **v7 (current)** = built from v6.1, lives at `../v7_cc-bootstrap/`.
- Full narrative for every version is in `LABBOOK.md` at the entries cited above (ground truth).
