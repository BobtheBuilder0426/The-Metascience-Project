# experiments/_TEMPLATE -- copy this shape for each experiment

<!-- WHAT THIS FOLDER IS: the template describing ONE experiment folder. HOW TO USE: for experiment N, create
     experiments/exp-NNN_<slug>/ with the structure below (NNN matches runtime/run-NNN; <slug> = 2-4 kebab words).
     Do NOT put real work in _TEMPLATE. Every file created gets a crash-recovery header; log each step in the labbook. -->

```
experiments/exp-NNN_<slug>/
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
├── 02_results/           [the assistant] outputs copied back from runtime/run-NNN
├── 03_final-report.md    [the assistant] final report to CS (per 01_setup/for-the operator/final-report-spec.md)
├── 04_evaluation.md      [the operator]   filled eval sheet (via the assistant's CC skill; flows back to CS)
└── 05_analysis.md        [CS]     analysis + next hypothesis + prep of exp-(N+1)
```

See ../../DOCUMENTATION.md sections 4 + 7 for the loop flow and documentation duties.
