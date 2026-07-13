# CS-project naming convention — the loop's disposable sessions

**Why this exists.** The Agentic Loop works by a blank Claude Code (CC) **creating a brand-new Claude Science
(CS) project** and driving it. That CC-created project may run *alongside* the user's own real CS projects, so
it must be **instantly recognizable and safe to delete** — never confused with the user's actual research, and
never written into by mistake.

**Solution — a reserved prefix + a human-chosen name.** Every CS project the loop creates is named with the
`AL-` prefix (**A**gentic **L**oop) followed by a short name the human gives for that run. Any real project keeps its own
name. The prefix alone makes loop sessions sortable and unmistakable in the CS project switcher; the human-chosen suffix
makes each run easy to find.

## The pattern
```
AL-<name>            e.g. AL-ergo-hypothesis, AL-sarcopenia-q, AL-origin-of-life
```
`<name>` is what the human answers when the bootstrap asks *"what should I name this run?"*, normalized to a safe slug
(lowercase, spaces→hyphens, only `[a-z0-9-]`, ~40 chars max). **The same `AL-<name>` is used for BOTH the CS project and
the run's driver subfolder `driver/AL-<name>/`** — so the project and its folder always share one identity. If a name
collides with an existing run, append `-2`, `-3`, … until unique.

## Rules
1. **Prefix is reserved.** Only loop-driven CS projects use `AL-`. Never rename a real project to start with `AL-`.
2. **One project per run, name = folder.** Each run gets its own fresh CS project `AL-<name>` AND a matching driver
   subfolder `driver/AL-<name>/` (clean context = reproducible; a crash in one run can't corrupt another). Do not reuse a
   project across runs, and never point two runs at the same name.
3. **The CC records the exact name it created** in that run's `meta.json` (`cs_project_name` = `run_name` = `AL-<name>`)
   and in `run_log.md`, so every result folder is traceable back to the CS project that produced it.
4. **Description field** (when CS offers one) = a one-line warning so a human never mistakes it for real work:
   `"Agentic-Loop driven session — auto-created + driven by a blank Claude Code. NOT a research project; safe to
   delete after results are captured."`
5. **Isolation still holds.** The `AL-` project is the CC's own scratch space. The CC never touches any other CS
   project or any folder except its bootstrap folder and the workspace folder it was given.

## Why a new project each time (not one shared loop project)
- **Reproducibility:** every run starts from an identical blank slate — no leftover context.
- **Crash-safety:** runs are independent; one failing never contaminates another.
- **Clean teardown:** after results are copied out, the whole `AL-…` project can be deleted with zero risk.
