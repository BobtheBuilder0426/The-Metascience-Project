# Submission acceptance matrix

**Purpose.** One contract for the whole submission: every deliverable, its canonical
path, the inputs it draws from, the test that says it is done, and who owns it. Fixed
*before* authoring so no later step creates a duplicate or a contradictory copy. If a
file is not on this matrix (or on the support list below), it does not ship.

**Public project name (confirmed, used consistently across all deliverables):**
*The Metascience Project* — a neutral, descriptive public name for the overall endeavour
(the loop it builds is referred to as *the Agentic Loop*, the method/product). It threads
through the report title, figures, README and LICENSE.

**Canonical layout**

```
submission/
  ACCEPTANCE_MATRIX.md      <- this file (contract)
  INVENTORY.md              <- D-A.1 annotated file/dir map
  TIMELINE.md               <- D-A.2 labbook-anchored timeline
  EVAL_DESIGN_AUDIT.md      <- evaluation-design audit (grounds Results/Methods)
  summary.md                <- D-C 100-200 word summary
  evidence/                 <- frozen evidence spine (single source of truth)
    checksums.sha256        <- SHA-256 of every authoritative input
    build_spine.py          <- scripted derivations (units/formulas/estimands)
    evidence_spine.csv       <- every atomic claim -> value, type, source anchor+ID
    derived_numbers.json    <- machine-readable recomputed values
  report/
    report.pdf              <- D-B the report (Abstract+Intro+Results+Discussion <=10pp)
    src/                    <- report source (Typst/markdown) + build
    figures/                <- paper figures (SVG masters + PNG/PDF exports)
    verification_ledger.csv <- D-B every shipping claim -> source ID, verified live
  talk-figures/             <- D-D five talk figures (SVG masters + PNG/PDF)
LICENSE                     <- D-E clean OSI MIT at repo root (authorized holder + 2026)
README.md                   <- D-F judge entry point at repo root
```

## The seven deliverables

| # | Deliverable | Canonical path | Inputs | Completion test | Owner |
|---|---|---|---|---|---|
| D-A.1 | Inventory | `submission/INVENTORY.md` | full repo tree; checksums; LABBOOK | Every top-level dir + every shipping file classified (what / why / ships Y-N); trash + duplicates flagged with paths | CS |
| D-A.2 | Timeline | `submission/TIMELINE.md` | LABBOOK LB-001..LB-106; LOOP_VERSION files | exp-000->001->002->003 and v0->v6->v7->v8->v9 each with an LB-anchor; pivots named | CS |
| D-B | Report (PDF) | `submission/report/report.pdf` | evidence spine; eval audit; figures; verification ledger | Abstract+Intro+Results+Discussion <=10 pp (Methods/Sources/Supp after, uncounted); five threads present; every non-trivial claim has a ledger row; figures legible at final size | CS |
| D-B (ledger) | Verification ledger | `submission/report/verification_ledger.csv` | shipping claims; connectors | Every non-trivial scientific claim -> PMID/DOI/accession (live-checked, exact-statement) or labbook anchor; unconfirmable claims dropped from the report | CS |
| D-C | Summary | `submission/summary.md` | report | 100-200 words; human register; hook + finding + why-it-matters; no AI cadence | CS |
| D-D | Talk figures | `submission/talk-figures/` | evidence spine; paper figure masters | 5 figures; fig 4 shows all 3 arms + human score + CS-harness score + combined mean; SVG + PNG/PDF; legible at projection size | CS |
| D-E | LICENSE | `LICENSE` (repo root) | — | Exact OSI MIT text; authorized neutral copyright holder + 2026 (never blank); placeholder replaced | CS |
| D-F | README | `README.md` (repo root) | all deliverables | Judge entry point: what this is / what happened / where each deliverable lives; every link resolves in a fresh checkout | CS |

## Foundation artifacts (support the above; ship as provenance)

| Artifact | Canonical path | Completion test |
|---|---|---|
| Acceptance matrix | `submission/ACCEPTANCE_MATRIX.md` | This file; all paths agreed before authoring |
| Evidence spine | `submission/evidence/` | Inputs checksummed; derivations scripted + reproduced; every atomic claim tagged measured/derived/observed-once/hypothesised with a source anchor |
| Eval-design audit | `submission/EVAL_DESIGN_AUDIT.md` | Design reconstructed (prompts, arms, models, rubric, blinding, unit, aggregation); combined mean labelled DERIVED; inference confined to n=3 |

## Reconciliation of the existing `submission/`

- **`submission/submission-checklist.md`** (pre-existing, 1.1 KB) — an internal build-time
  checklist (deadline, required-items boxes, demo-video pointer). It is a *working* file,
  not a judge deliverable. **Disposition:** keep in the repo as provenance; it is NOT one
  of the seven deliverables and the README does not route the judge to it. No content
  conflicts with the deliverables above.
- No other files existed under `submission/` before this build, so there are no duplicate
  or contradictory artifacts to resolve. All new work writes to the canonical paths above.

## Conflict-precedence rule (applies to every number and claim downstream)

When sources disagree, precedence is:

1. **LABBOOK.md** (append-only ground truth of what happened) —
2. each experiment's **`05_analysis/` tables + `FINAL_RESULT.md` + `04_evaluation/` JSON**
   (the frozen computed record) —
3. **SOURCES.md** and **`LOOP_VERSION.md`** (registered sources; loop identity/hashes) —
4. **STATUS.md / ROADMAP.md / drafts** (working notes).

Contradictions are **recorded, not silently resolved** (noted in the evidence spine and,
where they affect a shipping claim, in the report). Numbers in the report are the ones the
`evidence/build_spine.py` script recomputes from the tier-2 data files and that match the
frozen tables; any value that cannot be reproduced from a checksummed input does not ship.
