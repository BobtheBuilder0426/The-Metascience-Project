# CS-project naming convention — loop-driven sessions vs. our real research project

**Problem.** The Agentic Loop works by a blank Claude Code (CC) **creating a brand-new Claude Science
(CS) project** and driving it. That CC-created project runs *in parallel* with THIS project — the Metascience Project, our
real research + control workspace. They must never be confused: a run must not write into the Metascience Project, and we
must not mistake a disposable loop session for real research.

**Solution — a reserved prefix + a strict pattern.** Every CS project a loop creates is named with the
`AL-` prefix (**A**gentic **L**oop). Our real project keeps its own name (the Metascience Project / "Claude Science
Hackathon"). The prefix alone makes them sortable and unmistakable in the CS project switcher.

## The pattern
```
AL-<expNNN>-<QID>-<arm><run>
```
| field    | meaning                                  | example      |
|----------|------------------------------------------|--------------|
| `AL-`    | reserved prefix: loop-driven, disposable | `AL-`        |
| `expNNN` | which experiment                         | `exp000`     |
| `QID`    | question id (short, uppercase)           | `QDIS`       |
| `arm`    | `B` baseline / `L` loop                  | `L`          |
| `run`    | run number for that arm                  | `1`          |

**Examples**
- `AL-exp000-QDIS-L1`  → pilot, question "best disease target for EGT", Arm L, run 1
- `AL-exp001-QERGO-L2` → exp-001, ergothioneine brief, Arm L, run 2
- `AL-exp001-Q3-B1`    → exp-001, Q3, baseline, run 1

## Rules
1. **Prefix is reserved.** Only loop-driven CS projects use `AL-`. Never rename the Metascience Project to start with `AL-`.
2. **One project per run.** Each Arm-L run gets its own fresh CS project (clean context = fair, reproducible,
   and a crash in one run can't corrupt another). Do not reuse a project across runs.
3. **The CC records the exact name it created** in `meta.json` (`cs_project_name`) and in `run_log.md`, so
   every result folder is traceable back to the CS project that produced it.
4. **Description field** (when CS offers one) = a one-line warning so a human never mistakes it for real work:
   `"Agentic-Loop driven session — <expNNN> <QID> <arm><run> — auto-created + driven by a blank Claude Code.
   NOT a research project; safe to delete after results are captured."`
5. **Isolation still holds.** The `AL-` project is the CC's own scratch space. The CC never touches the Metascience Project,
   this shared folder, or the labbook (that would break the "blank" premise).

## Why a new project each time (not one shared loop project)
- **Fairness / reproducibility:** every run starts from an identical blank slate — no leftover context.
- **Crash-safety:** runs are independent; one failing never contaminates another.
- **Clean teardown:** after results are copied out, the whole `AL-…` project can be deleted with zero risk
  to the Metascience Project.
