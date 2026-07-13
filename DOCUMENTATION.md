# the Metascience Project -- Repository Documentation (the operating manual)

<!-- WHAT THIS FILE IS: the self-contained operating manual for this repo. It tells Claude Science (CS) and
     Claude Code (the assistant / a blank CC) HOW this repo is organized and HOW to work in it. It is fully authoritative:
     everything you need is inside this repo -- there are NO references to anyone's private workspace.
     HOW TO USE: read it fully before doing any work here. Everything you create/place/annotate must match it. -->

**Scope:** this hackathon project only -- STANDALONE, no overspill with any other project. English throughout.

---

## 1. What this repo is + working principles

Claude Science researches **how to build the best automated loop for Claude Science** (an agentic research +
hypothesis-generation loop), tested as a scientific-method loop: **hypothesis -> test -> analyse -> repeat**. Each
iteration is an "experiment". This repo is BOTH the joint working folder (CS + Claude Code write the same files) AND
the open-source submission repo. See `Hackathon.md` for the event, rules, deadline, judging, and prizes.

Working principles:
- **English everywhere.**
- **The labbook is the top documentation duty** -- every unit of work gets an entry (Section 7 + 8).
- **Every source is registered in `SOURCES.md`** and cited by number.
- **Do not run heavy code directly from this folder if you reach it over a network/file-share mount** -- copy what you
  need into a local runtime area outside this repo, run it there, and copy results back. (CS runs natively and is not
  affected; this matters for a Windows-side runner.)
- **Every file starts with a crash-recovery header:** what it is + how to use it.

## 2. Roles & tags (locked)

| Tag | Who | Does |
|---|---|---|
| `[CS]` | Claude Science (Linux) | designs experiments (hypothesis + setup), captures + scores outputs, prepares the operator's eval, writes the final scoring report, prepares the next experiment, keeps the labbook — **owns the critical path (operator override, LB-032)** |
| `[the assistant]` | the assistant -- the operator's Claude Code | **CRASH FALLBACK ONLY (operator override, LB-032):** blackbox forensic report if the blank CC/CS loop fails. Not in the normal flow. |
| `[Operator]` | the operator (the human) | the **A→B bridge**: copies setups/workspaces/output-bundles/eval-JSON between the isolated CC runtime and this repo under CS instruction |
| `[CC]` | a blank Claude Code session | executes ONE experiment setup in a local runtime area |
| `[the operator]` | the human | evaluates each experiment, blinded (human-in-the-loop) |

## 2b. Two loops (do not confuse)

- **Experiment Loop** = the OUTER loop we RUN to discover the best setup: the scientific-method cycle
  hypothesis -> test -> analyse -> repeat. Each turn is an "experiment" (`experiments/exp-NNN/`).
- **Agentic Loop** = the INNER product we are building: the automated, self-improving research loop in which Claude
  Code drives Claude Science, which a blank Claude Code bootstraps + runs. Evolving design in `loop-design/`; the final
  version is applied in `final-run/` and must be self-bootstrapping (a downloader gets the working loop automatically).

## 3. File map

```
(repo root)
├── CLAUDE.md                 START HERE -- entry point + read-order + working rules (auto-loads for Claude Code)
├── README.md                 public README / judge entry point  [PLACEHOLDER until submission]
├── LICENSE                   OSS license  [PLACEHOLDER until submission]
├── Hackathon.md              the event: rules, deadline, judging, prizes (in-repo copy)
├── DOCUMENTATION.md          THIS manual
├── LABBOOK.md                append-only joint labbook (TOP documentation duty)
├── SOURCES.md                central numbered source registry [S-NNN]
├── GOAL.md                   the locked research GOAL (Northstar + Sections 1-6)
├── ROADMAP.md                the phase plan (goals + Done-when gates, setup -> submission)
├── STATUS.md                 living: which phase we are in + the next action (update after every step)
├── loop-design/              the evolving PRODUCT = current best CS loop
│   ├── current/              latest promoted loop design
│   └── CHANGELOG.md          version per iteration + why
├── experiments/              the PROCESS = one folder per iteration
│   ├── RESULTS-LOG.md        cross-experiment overview table
│   └── _TEMPLATE/            the exp-NNN shape to copy (placeholder files inside)
├── test-sets/                versioned investigable test sets (control variable)
├── final-run/                the real research question on the optimized loop (headline)
├── cs-artifacts/             verbatim Claude Science exports (provenance)
├── resources/                what CS may use: RESOURCES.md (specs/access/infra), claude-science-handbook.md, the operator's profile + starter papers
└── submission/               submission-checklist.md (+ final summary/video at the end)

experiments/exp-000_pilot_ergo-disease/01_setup/     (the CC-bootstrap versioning lives INSIDE the experiment — see §3b)
├── <version>_cc-bootstrap/   ★ the ready-to-give blank-CC start package = the highest versioned folder here (copy this whole folder; see its HOW-TO-USE.txt). DOCUMENTATION doesn't name which version is current — the owning LABBOOK entry does.
├── cc-bootstrap-archive/     all PREVIOUS bootstrap versions, numbered (README.md = version↔labbook map). Provenance only — do NOT use.
├── bootstrap-design-notes.md literature grounding for the bootstrap
└── project-naming-convention.md   CS-project naming for loop-driven sessions
```

## 3b. CC bootstrap package — versioning & archive policy

The blank-CC start package (what a fresh Claude Code is given as its workspace to run the loop) is the most-iterated
artifact in this project. It is versioned by FOLDER NAME, and the current version + the archive of all past versions
BOTH live inside the active experiment folder. This is the locked way of working:

- **Current bootstrap = one folder named `<version>_cc-bootstrap`, inside the active experiment's `01_setup/`.**
  It carries a plain **`HOW-TO-USE.txt`** for the human and is the ONLY folder ever handed to a blank CC.
  DOCUMENTATION.md deliberately does **not** hard-code which version is current (that pointer only drifts) — the owning
  LABBOOK entry names the exact version it used (see the naming rule below), and `STATUS.md` says which run is live.
- **All previous versions live in `01_setup/cc-bootstrap-archive/`, numbered.** Sibling to the current folder, in the
  SAME experiment. Folders are numbered by architectural line (`01_single-folder-bootstrap_v1-v5`,
  `02_two-session_v6.0_pre-correction`, …); where a version line was edited in place, per-file snapshots are recovered
  into that folder's `version-snapshots/` (e.g. `CLAUDE.md.v1 … v9`). The archive is **provenance only — never launch a
  run from it**. `cc-bootstrap-archive/README.md` holds the authoritative version ↔ LABBOOK ↔ what-changed table.
  **Nothing is ever deleted** (archived, not removed).
- **THE PROMOTION RITUAL — after every run, when we decide to optimize to the next version:**
  1. **Copy** the current `<version>_cc-bootstrap/` folder into `cc-bootstrap-archive/` **under its exact version name**
     (e.g. `v6.1_cc-bootstrap/` → `cc-bootstrap-archive/v6.1_cc-bootstrap/`).
  2. **Build the next version FROM that folder**, renamed to the new version (e.g. `v6.2_cc-bootstrap/` or the next
     major), living again in `01_setup/`.
  3. **Add a row** to `cc-bootstrap-archive/README.md` (version ↔ LABBOOK ↔ what-changed).
  4. **Write/append the LABBOOK entry** that OWNS the new version — its header and body MUST name the exact folder
     (e.g. "v6.2_cc-bootstrap"). This is how we always know which LB entry describes which folder.
- **Naming rule for the labbook (MANDATORY):** every LABBOOK entry about a bootstrap, a loop, or an experiment version
  must name the exact version string (`v6.1_cc-bootstrap`, later `v1_loop`, `exp-001`, …). Never write "the current
  bootstrap" — write its versioned name, so any entry is unambiguous about what was used.
- **FUTURE — once a loop actually runs (later phases):** the versioned artifact becomes the loop itself, named
  `v1_loop`, `v2_loop`, …. **Each run is its own experiment folder** (`exp-001_…`, `exp-002_…`) holding the loop
  version used for that run PLUS that run's outputs, scoring, and evals. A new loop version → a new experiment folder →
  the next run. Same rule: the folder name carries the version, the LABBOOK entry names it, crash-recovery safe.
- **Version ↔ labbook map:** the authoritative version↔LABBOOK table lives in `cc-bootstrap-archive/README.md` (a row
  is added on every promotion per the ritual above). DOCUMENTATION.md does not duplicate it or mark any version
  "current" — the **naming rule below** is what guarantees every labbook entry states the exact version it used.

## 4. One experiment (the loop)

```
experiments/exp-NNN_<slug>/          (NNN matches the local run number)
├── 00_hypothesis.md      [CS]     hypothesis for this iteration + what it changes vs loop-design/current
├── 01_setup/             [CS]     the package a BLANK Claude Code receives:
│   ├── bootstrap.md               blank-CC entry point (how to self-assemble the workspace)
│   ├── workspace/                 ready-to-use CC workspace template (self-installing research loop)
│   ├── protocol.md                blank-CC: WHEN/WHERE/WHAT to document + HOW to document + report its own run
│   ├── test-set/                  the investigable test set (or a pin -> ../../test-sets/<version>)
│   └── for-the operator/                CS-authored, the assistant-facing:
│       ├── final-report-spec.md       how the assistant writes the final report to CS
│       ├── present-to-operator-skill.md   the CC skill: how the assistant presents the experiment to the operator
│       └── eval-sheet-template.md     the standardized eval sheet the operator fills
├── 02_results/           [the assistant] outputs copied back from the local run
├── 03_final-report.md    [the assistant] final report to CS (per 01_setup/for-the operator/final-report-spec.md)
├── 04_evaluation.md      [the operator]   filled eval sheet (via the assistant's CC skill; flows back to CS)
└── 05_analysis.md        [CS]     analysis + next hypothesis + prep of exp-(N+1)
```

**Flow:** `[CS]` designs `00_hypothesis` + `01_setup` -> `[the assistant]` pulls `01_setup` out to a local runtime area
(outside this repo) -> `[CC]` (blank) self-assembles the workspace + runs the test-set per `protocol.md` +
documents/reports its own run -> `[the assistant]` copies results to `02_results/`, writes `03_final-report.md`, presents to
the operator via the CC skill -> `[the operator]` fills `04_evaluation.md` (flows back to CS) -> `[CS]` writes `05_analysis.md` +
the next hypothesis; if the loop improved, CS promotes it to `loop-design/current/` (log in
`loop-design/CHANGELOG.md`). Repeat. Finally, `final-run/` runs the real question on the optimized loop and feeds
`submission/`.

## 4b. Hand-offs (the STATUS baton)

`STATUS.md`'s **Next action** is the baton: whoever finishes their part updates it to say WHO is next + WHAT, and
writes a labbook entry. Look at STATUS to know whose turn it is. The relay per experiment (human-relayed -- the operator is the
trigger between the separate systems; keep hand-offs **few + explicit**):
1. **CS** finalises `exp-NNN/01_setup` -> STATUS "Next: run exp-NNN" + labbook.
2. **the operator** starts the blank Claude Code run (on the pulled setup) -- the human trigger CS -> CC.
3. **blank CC** runs -> outputs + RUN-NOTES.
4. **the assistant** pulls results back, analyses, writes `03_final-report` -> STATUS "Next: the operator eval exp-NNN" + labbook.
5. **the operator** evaluates (via the CS-made present-to-operator skill) -> `04_evaluation` -> STATUS "Next: CS analyse exp-NNN".
6. **CS** analyses -> `05_analysis` + next hypothesis -> STATUS "Next: run exp-(N+1)". Repeat.

## 5. File categories (define the kind of every loose file)

| category | what it is / when to use |
|---|---|
| `hypothesis` | a proposed idea to test (an iteration hypothesis) |
| `setup` | a bootstrap / workspace / configuration a run consumes |
| `protocol` | instructions for how a run is executed + documented + reported |
| `testset` | an investigable test set a setup runs on |
| `result` | measurements / outputs produced by a run |
| `report` | a written report of an experiment's outcome |
| `eval` | a filled evaluation sheet (human-in-the-loop) |
| `analysis` | CS's analysis of results + next-step reasoning |
| `artifact` | a verbatim CS export kept as provenance |
| `source` | a saved copy of an external source (paper/dataset snapshot) |
| `note` | a working note that does not fit the above |

## 6. Naming convention (loose files)

```
YYYY-MM-DD_HHMM_<category>_<short-description>.<ext>
```
- **Timestamp first** (date + 24h time, CEST) so files sort chronologically -- newest always at the bottom.
- **category** from the table above; **short-description** = 2-4 kebab-case words.
- No version suffix normally; a real re-issue gets `_v2`.
- Example: `2026-07-09_1432_result_loop-accuracy.csv`
- Fixed stage files inside `exp-NNN/` keep their structural names (`00_hypothesis.md`, `03_final-report.md`, ...).

## 7. Documentation duties -- WHEN / WHO / WHAT / WHERE / HOW

**The LABBOOK is the top documentation duty: every unit of work gets a labbook entry.** If in doubt, log it.

| When (trigger) | Who | What | Where | How |
|---|---|---|---|---|
| Any work unit (task / step / run / decision) | CS or the assistant | a labbook entry | `LABBOOK.md` | append-only, English, all fields |
| After every step + at each phase transition | whoever advanced it | update the snapshot + current phase | `STATUS.md` | keep current; the LABBOOK stays the full history |
| A source is used (paper/dataset/tool/doc) | whoever uses it | register once, numbered | `SOURCES.md` | `S-NNN` row; then cite `S-NNN` everywhere |
| New iteration hypothesis | CS | hypothesis + what changes | `exp-NNN/00_hypothesis.md` | + labbook |
| Setup produced | CS | bootstrap+workspace+protocol+test-set+for-the operator | `exp-NNN/01_setup/` | + labbook + sources |
| Run executed | blank CC | run outputs + its own run report | the local runtime area | per `01_setup/protocol.md` |
| Result captured | the assistant | copy results back + final report | `exp-NNN/02_results/` + `03_final-report.md` | + labbook |
| Human eval | the operator (via the assistant's CC skill) | filled eval sheet | `exp-NNN/04_evaluation.md` | flows back to CS |
| Analysis + next hypothesis | CS | analysis | `exp-NNN/05_analysis.md` | + labbook; promote loop-design if improved |
| Loop improves | CS/the assistant | version bump | `loop-design/current/` + `CHANGELOG.md` | + labbook |

## 8. The labbook -- rules + schema

- **Append-only.** Never edit/delete a past entry; a correction is a NEW entry referencing the old `LB-NNN`.
- **English only.** Timestamps in **CEST**. Tags: `[CS]` / `[the assistant]` / `[CC]` / `[the operator]` (Section 2).
- **One entry per work unit.** Newest at the bottom.
- **Atomic append.** Append so concurrent writes never clobber each other: CS appends natively (it is on the same
  machine as the file); a Windows-side agent appends from the Linux side (via WSL) rather than over the file-share.
- **Cite sources** by `S-NNN` from `SOURCES.md`, each with a short what/why.

```
### LB-NNN | YYYY-MM-DD HH:MM CEST | [CS|the assistant|CC] | <short clear header>
- **Goal:** <idea / aim of the task or experiment>
- **What & how:** <what was done, how carried out - method, tools, CS session ref or run number>
- **Outcome:** <the exact result - numbers, finding, pass/fail, decision>
- **Data / artifacts:** <where it lives + exact filenames>
- **Sources:** <S-NNN (short what/why it was used), ...>
```

## 9. Golden rules

1. **Labbook everything** (Section 7). No un-logged work.
2. **Every source is registered in `SOURCES.md` (S-NNN)** and cited by number with a short what/why.
3. **Never run heavy code directly from a networked mount of this folder** -- copy to a local runtime area, run, copy results back.
4. **English everywhere in this repo.**
5. **Every file starts with a crash-recovery header:** what it is + how to use it.
6. **Append-only where it says append-only** (labbook, sources, changelogs) -- never rewrite history.
