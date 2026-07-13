<!-- Authored by [CS2] for exp-002 / v8. PROPOSAL — awaiting operator confirm before any v8 edit. -->

# Proposed v8 add-on — Gate-2 reviewer also critiques figure/artifact quality  [CS2]

**Status:** PROPOSAL. No `v8_cc-bootstrap/` file touched yet. Awaiting operator confirm (CS2 confirm-first rule).
**Goal (operator):** Gate-2 reviewer sees all CS artifacts + gives *non-dominant* feedback to lift figures/artifacts to
Nature/Science/Cell + human-designer quality. Research base: `figure-quality-standards.md` (checklist) + S-077..S-082.

---

## The gap I found (why this is also a real fix, not just an add-on)
Today the Gate-2 reviewer is handed **only** `plan_final.md` + `draft.md` (CODEX_PANEL.md line 67 + line 145). It does
**not** receive CS's `figures/` or the actual presentation deliverables. So it currently reviews the *draft text* blind
to the figures. Your instruction — "the reviewer should see all artifacts prepared by CS" — closes this gap: the driver
must place CS's real artifacts in the reviewer's WorkDir. That is prerequisite to the figure-quality add-on anyway.

---

## Proposed edits (all surgical; mostly ONE file: `driver/CODEX_PANEL.md`; +1 line in `driver/CLAUDE.md`)

**E1 — Gate-2 procedure (CODEX_PANEL.md ~line 141): driver provides the artifacts.**
Add: before running the reviewer, copy CS's presentation deliverables into the reviewer WorkDir —
`run_log/panel/artifacts/` ← `result.md`, `reasoning.md`, `figures/*`, `sources.md`. The reviewer sees the real output.

**E2 — context pack (line 67): note the Gate-2 artifact set now includes the deliverables + figures**, not just draft.md.

**E3 — a compact FIGURE-QUALITY STANDARD block** in CODEX_PANEL.md (the compressed Part-3 checklist), so the reviewer
carries the yardstick self-contained (it runs on the CC host and can't read the exp-002 file). Cites S-077..S-082.

**E4 — Gate-2 reviewer prompt (lines 145–155): add a 4th output item = ARTIFACT-QUALITY (small, explicitly non-dominant).**
> 4. **ARTIFACT & FIGURE QUALITY (secondary — after the science above; keep it brief).** Look at the figures/tables in
>    `artifacts/`. First name what already works. Then give **at most 2–3** concrete, highest-leverage design fixes to
>    move them toward top-journal + professional-designer quality, using the FIGURE-QUALITY STANDARD (readability / no
>    overlap / CVD-safe colour / labelled-units / clean composition). Each fix a specific instruction ("rotate the two
>    overlapping x-labels"; "swap the 5-colour rainbow for the Okabe-Ito set"; "move the legend into the empty upper
>    right"), never "make it prettier". If the artifacts are already clean, say so — do not manufacture nitpicks. This
>    is ONE small dimension; it must not dominate or dilute the scientific critique above.

**E5 — fairness reinforcement (one line):** figure critique is HOW (presentation/craft) only — never smuggle a
different conclusion, number, or mechanism via a caption/label change. Design feedback changes how a result is shown,
never what it is. (Rides the existing Gate-2 WHAT-strip; the strip already scrubs any smuggled WHAT.)

**E6 — blind-safety check (no new leak):** improved figures must still read as first-authored — CS re-renders silently,
never captions "figure revised after review". Already covered by the INTEGRATE standalone guard + banned words
(incl. "revised"); I'll confirm the banned-word list catches figure-revision phrasing.

**E7 — driver/CLAUDE.md Re-Act (one line):** the figure-quality feedback flows through the same relay + Re-Act triage;
CS decides which figure fixes to apply and re-renders. Adds "…including any figure/artifact re-work" to Re-Act scope.

---

## The one genuine unknown — can the Codex reviewer SEE image files?
`codex-run.ps1 -Search` runs gpt-5.6-sol via `codex exec`. Whether that path accepts **image inputs (vision)** is the
open question. The design degrades cleanly either way:

- **If VISION available (best):** driver puts the rendered figure files in the WorkDir; reviewer opens and *looks* at
  them — catches actual overlap, real "look", low contrast in the rendered output.
- **If TEXT-ONLY:** reviewer judges from (a) the figure-generating code if CS saved it, (b) the figure captions/
  references in `result.md`, and (c) a one-line-per-figure manifest CS writes (normal caption content, blind-safe).
  This still catches most of the checklist — rainbow colormap, unset figure size, missing units, too many hues,
  legend-in-code — but not pixel-level overlap. CS's own `figure-style` skill §9 (render-then-verify) is the backstop
  for overlap regardless.
- **Recommended:** a tiny pre-flight probe records `codex_vision: yes|no` in CONNECTION.md; the reviewer prompt branches
  on it. If you already know the answer, we skip the probe.

---

## Decisions needed (confirm before I touch v8)
1. **Confirm the edit set E1–E7?** (surgical; ~1 file + 1 driver line)
2. **Image capability:** does `codex-run.ps1` / gpt-5.6-sol accept image files? — `yes` / `no` / `probe-to-find-out`.
3. **Reviewer yardstick location:** inline compressed checklist in the prompt (self-contained — my recommendation), or
   copy the full `figure-quality-standards.md` into the WorkDir?
