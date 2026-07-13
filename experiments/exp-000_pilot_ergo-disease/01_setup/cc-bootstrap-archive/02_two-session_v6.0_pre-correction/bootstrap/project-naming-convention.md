# CS-project naming convention — the loop's disposable sessions

**Why this exists.** The Agentic Loop works by a blank Claude Code (CC) **creating a brand-new Claude Science
(CS) project** and driving it. That CC-created project may run *alongside* the user's own real CS projects, so
it must be **instantly recognizable and safe to delete** — never confused with the user's actual research, and
never written into by mistake.

**Solution — a reserved prefix + a strict pattern.** Every CS project the loop creates is named with the
`AL-` prefix (**A**gentic **L**oop). Any real project keeps its own name. The prefix alone makes loop sessions
sortable and unmistakable in the CS project switcher.

## The pattern
```
AL-run-<NN>            e.g. AL-run-01
```
For a single run, `AL-run-01` is the name to use. If you run a series (multiple questions, arms, or repeats),
extend it so each run is unique and traceable, e.g.:
```
AL-<runid>            AL-run-01, AL-run-02, ...
AL-<qid>-<arm><n>     AL-q1-L1  (question 1, loop arm, run 1) / AL-q1-B1 (baseline)
```
Keep it short, uppercase-ish, and unique per run.

## Rules
1. **Prefix is reserved.** Only loop-driven CS projects use `AL-`. Never rename a real project to start with `AL-`.
2. **One project per run.** Each run gets its own fresh CS project (clean context = fair, reproducible, and a
   crash in one run can't corrupt another). Do not reuse a project across runs.
3. **The CC records the exact name it created** in `meta.json` (`cs_project_name`) and in `run_log.md`, so every
   result folder is traceable back to the CS project that produced it.
4. **Description field** (when CS offers one) = a one-line warning so a human never mistakes it for real work:
   `"Agentic-Loop driven session — auto-created + driven by a blank Claude Code. NOT a research project; safe to
   delete after results are captured."`
5. **Isolation still holds.** The `AL-` project is the CC's own scratch space. The CC never touches any other CS
   project or any folder except its bootstrap folder and the workspace folder it was given.

## Why a new project each time (not one shared loop project)
- **Fairness / reproducibility:** every run starts from an identical blank slate — no leftover context.
- **Crash-safety:** runs are independent; one failing never contaminates another.
- **Clean teardown:** after results are copied out, the whole `AL-…` project can be deleted with zero risk.
