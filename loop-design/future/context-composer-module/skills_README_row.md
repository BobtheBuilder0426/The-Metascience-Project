### context-composer
Build the per-question CS project Agent Context: safety preamble (verbatim) + a performance block tuned to the
question's SHAPE (not its content). Use once per run, at the "create CS project" step, after you have the question and
have chosen the run name. The blank CC only sets general task-shape flags; a fairness firewall guarantees no task
content leaks into the context. See `context-composer/SKILL.md`.
