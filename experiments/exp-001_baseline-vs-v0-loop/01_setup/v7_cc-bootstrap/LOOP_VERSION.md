# LOOP VERSION — v7_cc-bootstrap

- **Version name:** `v7_cc-bootstrap`
- **Content hash (sha256, first 16 hex, all 23 files concatenated in sorted path order):** `6bbd94a13d13e462`
- **Maintained source:** `experiments/exp-000_pilot_ergo-disease/01_setup/v7_cc-bootstrap/`
- **This copy:** frozen for exp-001 (`exp-001_baseline-vs-v0-loop`); byte-identical to the maintained source
  (verified with `diff -r`) as of 2026-07-11.
- **Architecture (this revision):** bootstrap-once → drive-many with **dedicated per-run CS-workspace folders**.
  PART A records the parent location where CS workspace folders live (no shared folder). PART B, per question:
  creates a dedicated folder `<cs-workspaces>/AL-<name>/`, a handoff subfolder `driver/AL-<name>/` with a
  Verknüpfung, a CS project `AL-<name>` (safety preamble in its context), grants that dedicated folder to that
  project, digests inputs, and prints a START PROMPT. Each run is physically isolated (own folder + own project).
  Concurrent bootstraps serialized by `bootstrap.lock`; many drivers run in parallel.

To recompute the hash:
`find v7_cc-bootstrap -type f -not -path '*/.git/*' | sort | xargs cat | sha256sum | cut -c1-16`
