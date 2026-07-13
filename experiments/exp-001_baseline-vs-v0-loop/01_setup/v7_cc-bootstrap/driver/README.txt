driver/ — the DRIVER side of the loop (one bootstrap prepares MANY runs)

- CLAUDE.md         the SHARED driver manual. Every run's driver reads this and substitutes its own ⟨RUN⟩.
- AL-<name>/        ONE subfolder per prepared run (created by the bootstrap session). Fully isolated:
                    its own QUESTION.txt, CONNECTION.md, START_PROMPT.md, context/, and OUTPUT/. A driver
                    session works ONLY inside its own AL-<name>/ subfolder and drives ONLY the CS project
                    of the same name. Runs never touch each other, so drivers can run concurrently.
- _run-template/    a shape-only illustration of what each AL-<name>/ subfolder contains (not a live run).

No AL-<name>/ subfolders exist until the bootstrap session prepares questions; HANDOFF_READY (at the
workspace root) lists every run that has been prepared.
