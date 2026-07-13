This folder shows the SHAPE that every per-run driver subfolder takes. It is a template, not a live run.

When the bootstrap session prepares a question, it creates a real run subfolder:

  driver/AL-<name>/
  ├── QUESTION.txt        the frozen research question (verbatim)
  ├── CONNECTION.md       this run's bridge record (CS URL, project AL-<name>, shared-folder paths, run area)
  ├── START_PROMPT.md     the copy-paste prompt that starts THIS run's driver session
  ├── context/            agent-ready digests of this run's input files (one <file>.digest.md each)
  └── OUTPUT/run-01/       this run's results — presentation/ (evaluated) + run_log/ (loop machinery)

The driver manual driver/CLAUDE.md is SHARED by all runs; each driver is told its own ⟨RUN⟩ = AL-<name>
in its START PROMPT and substitutes it wherever the manual writes ⟨RUN⟩.
