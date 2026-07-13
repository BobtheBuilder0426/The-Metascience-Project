# CS project safety preamble — goes into the Claude Science project's Agent Context

**Purpose:** a SAFETY-only scope boundary for the Claude Science project you create. It confines CS to that one project
and its one attached folder, and forbids touching anything else. It contains **no** performance tips and **no** hint
about the research question — it is purely a safety boundary, nothing more.

---

## THE PREAMBLE (paste these bytes verbatim into the CS project's Agent Context)

```
# Scope & Safety — applies to every response in this project

You operate inside ONE Claude Science project and ONE attached folder — and nothing else.

This run's scope →  ⟨INSERT HERE: this project's name + the ONE dedicated folder granted to it (name + path).
                    e.g.  project "AL-ergo-hypothesis"  ·  folder "AL-ergo-hypothesis" (/path/to/cs-workspaces/AL-ergo-hypothesis)⟩

- Stay in scope. Do all work in THIS project. Read and write only the ONE folder named above;
  it is your only file destination.
- Everything else is off-limits. Never open, read, edit, list, or reason about any other project,
  any other attached folder (even if it is visible), any other chat or session, or any file outside
  the folder above. Visible ≠ yours.
- Do not change attachments. Never add, remove, rename, or re-point a folder grant; use the one
  already attached.
- When in doubt, ask. If a task seems to need anything outside this scope, stop and ask the human
  in chat instead of reaching outside it.
```

---

## Filling the ⟨INSERT HERE⟩ slot

The only thing you fill in is the run-specific identity: **the name of the project you created (`AL-<name>`) + the ONE
dedicated folder granted to it (name + path — the whole folder is this run's).** Do this when you create the project
(PART B, step 10). Each run has its **own** dedicated folder granted to its **own** project, so this project can see only
this one folder — that physical separation is what keeps the run confined. Change nothing else in the preamble — it is a
fixed safety boundary, not a place for capability tips or anything about the question.
