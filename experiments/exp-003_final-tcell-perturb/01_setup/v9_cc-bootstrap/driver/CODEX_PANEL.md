<!-- CODEX MULTI-LENS PANEL — shared operating manual for the DRIVER (every run). driver/CLAUDE.md routes here at two
     gates: Gate 1 (plan-stage, multi-lens panel + chairman) and Gate 2 (result-stage, single journal reviewer). This
     file holds the exact reviewer prompts, the codex-run invocation, output capture, and the hard blind-safety +
     fairness rules. Substitute YOUR run id wherever this file writes ⟨RUN⟩. -->

# CODEX_PANEL.md — external cross-vendor critique for the loop (Gate 1 + Gate 2)

## What this is (one paragraph)
The producer of the science is Claude Science (CS, a Claude model). The **critics are GPT-5.6-sol agents run via Codex
on this host** — a *different vendor* from the producer, which is the point: external, cross-vendor critique blunts the
self-enhancement bias a session reviewing its own work cannot escape. There are **two gates**. **Gate 1 (plan stage):**
after CS drafts its PLAN, you spawn a **4-lens panel** that critiques the plan (KEEP-first, then each lens's
improvements-with-reasoning), then a **chairman** that synthesises the four into one prioritised report; you hand that
report to CS, which reflects and revises its plan; only then GO. **Gate 2 (result stage):** after CS's own
KEEP+correctness pass, you spawn **one** GPT-5.6-sol **journal reviewer** that compares plan-vs-implementation and gives
bounded final-polish feedback; CS then triages it (the Re-Act phase in `driver/CLAUDE.md`) and integrates. Critics are
**advisory** — CS always decides.

## Model + reasoning effort (fixed loop setting — v9)  ⚠ READ BEFORE ANY GATE
Every Codex critic runs on **`gpt-5.6-sol`**. The **reasoning effort is fixed per gate** and is a v9 loop setting:
- **Gate 1 — all 4 lenses AND the chairman → reasoning effort `high`.**
- **Gate 2 — the single journal reviewer → reasoning effort `xhigh`** (the result-stage review is the highest-stakes
  critique, so it gets the deepest reasoning budget).

Pass the effort on **every** wrapper call (see "Invocation" for the exact flag). If the wrapper does not accept an
effort flag, pass it through to Codex natively with `-c model_reasoning_effort="<high|xhigh>"`. This is **loop
machinery**, not science content: it changes only *how hard the external critic thinks*, never *what* CS concludes, and
it is applied identically to every question and every arm that runs this loop — so it carries no fairness cost (the same
HOW-not-WHAT firewall below still governs everything a critic says). If a gate has to degrade to self-review (precondition
below), the effort setting is moot for that gate — log the degrade as usual.

## Precondition + degrade path (check FIRST, every gate)
- The panel needs the sanctioned Codex wrapper **`codex-run.ps1 -Search`** (GPT-5.6-sol with web+literature access,
  sandbox on). Its **absolute path and verified status are recorded in `driver/⟨RUN⟩/CONNECTION.md`** by the bootstrap
  pre-flight (`panel_available: yes|no`, `codex_run_path: …`, `panel_verify: …`).
- **If `panel_available: yes`** → run the gate as written below.
- **If the `panel_available` field is missing or unreadable** (older/malformed `CONNECTION.md`) → treat as `no` and
  degrade (log why).
- **If `panel_available: no`, OR any `codex-run.ps1` call fails at runtime (nonzero exit / empty final message / MCP
  cancel / timeout)** → **DEGRADE, do not stall:**
  - **Gate 1 degraded** → run the legacy self-review instead (CS critiques its own plan on AMBITION / GROUNDING /
    HALLUCINATION-RISK, then revises — the v7 Phase-3 text, preserved in `driver/CLAUDE.md`).
  - **Gate 2 degraded** → CS does one extra self-pass: "compare your final draft against your revised plan; name gaps;
    apply only evidence-backed fixes."
  - **Record the degrade honestly** in `run_log/run_log.md` and `RUN_REPORT.md`: `PANEL DEGRADED @ Gate N — <reason>`.
  A degraded run is still valid; a silently-faked panel is not. Never invent a panel/chairman/reviewer output.

## Scoped work area + BLIND-SAFETY (hard rules)
- All panel machinery lives under **`driver/⟨RUN⟩/OUTPUT/run-01/run_log/panel/`** — this is **loop machinery, NEVER
  evaluated**. Nothing panel-related may enter `presentation/`.
- `process_trace.json` stays **ACTION-labelled** (per `driver/CLAUDE.md`): it must **not** contain the words panel /
  lens / chairman / reviewer / Gate / Codex / GPT / **review / feedback / critique / "external review"**, any phase
  name, or **revision-history phrasing** ("after review I…", "revised", "v2", "initially…then"). The blinded scorer
  must not be able to tell a loop answer from a cold one by its presentation folder. **This same banned list applies to
  the CS-authored `presentation/` files** (the INTEGRATE standalone-answer guard in `driver/CLAUDE.md`).
- **CS is never told the panel exists.** You (the driver) capture CS's plan/draft text from its browser messages and
  write the panel inputs yourself; you paste the chairman/reviewer feedback to CS as *"external review feedback"* with
  **no** loop/phase vocabulary. Do not ask CS to write into `run_log/`.

## FAIRNESS FIREWALL (the panel sharpens HOW, never hands over WHAT)
The panel is a real advantage the baseline arm never gets — legitimate **only** if it never smuggles the domain answer.
- Every reviewer prompt is given the **question** and the **reframed brief** (HOW to pursue it) — never a target answer.
- Reviewers critique **method, ambition, rigor, grounding, logic**. They must **not** propose the specific
  conclusion/mechanism/number CS should output.
- The **chairman drops any recommendation that would hand CS a specific domain answer** (keeps HOW, cuts WHAT).
- You never add domain facts of your own into the panel or into CS. If a reviewer asserts a domain claim, it passes to
  CS as *"a reviewer raised X — verify it yourself before using it,"* never as truth.

## The reviewer context pack (every agent gets exactly this — write it once per gate)
Write `run_log/panel/context_pack.md` containing, in this order (front-load — models under-use mid-context):
1. **QUALITY NORTH-STAR (verbatim):** "This review serves one goal: get the most out of the AI scientist — a genuinely
   novel, ambitious answer, where every claim is grounded in excellent scientific practice, shows an explicit chain of
   reasoning, and carries verifiable citations (PMID/DOI). Push for a landmark answer that is also bulletproof."
2. **THE QUESTION (verbatim from `QUESTION.txt`).**
3. **HOW IT IS BEING PURSUED (the reframed brief, from `run_log/reframed_brief.md`).**
4. **YOUR TOOLS:** "You have web_search (live). Use it to verify factual claims and to check whether an ambitious
   direction is plausible and not already done. Do not raise a factual concern you have not checked."
5. **FAIRNESS RULE (verbatim):** "Critique the METHOD — ambition, rigor, grounding, reasoning, completeness. Do NOT
   state the specific answer/mechanism/number the scientist should conclude. Sharpen HOW, never hand over WHAT."
Then the artifact under review is a separate file: `plan_v1.md` (Gate 1) or, for Gate 2, `plan_final.md` + `draft.md`
**plus CS's actual deliverables in `artifacts/`** (`result.md`, `reasoning.md`, `sources.md`, and the rendered
`figures/`, attached as images) so the reviewer judges the real work, figures included.

---

## GATE 1 — plan-stage multi-lens panel + chairman

**Model + effort:** every lens AND the chairman run on **`gpt-5.6-sol`, reasoning effort `high`** (v9 fixed setting).

**Runs:** after CS returns its Phase-2 PLAN, instead of the legacy self-review. **Order:** 4 lenses (parallel or ≤2 at
a time on this host) → chairman → hand report to CS.

**Procedure**
1. Capture CS's plan text from its Phase-2 message; write it to `run_log/panel/plan_v1.md`. Write `context_pack.md`
   (above).
2. Run the **4 lenses**. For each, call the wrapper (see "Invocation") with the lens prompt; capture the agent's final
   message to `run_log/panel/lens_<Ln>.md`.
3. Run the **chairman** with all four lens files; capture to `run_log/panel/chairman_report.md`.
4. Hand the chairman report to CS as Phase 3 (see `driver/CLAUDE.md`), framed as external review feedback.

**The 4 lenses (independent; each = context pack + its block below + "Read context_pack.md and plan_v1.md first.").**
Each lens must answer in this fixed shape: **(A) KEEP** — what is strong and must be protected, and why; **(B)
OPTIMISE (this lens)** — the improvements this lens would make, each with its reasoning; **(C) TOP-2** — this lens's two
highest-leverage points.

- **L1 — Ambitious young postdoc.** "You want this to be a landmark, genuinely novel answer, not a safe textbook one.
  What is the one addition or reframing that would make it matter — a bolder hypothesis, a non-obvious connection, a
  higher-impact framing? For every bold move, name the evidence path that would support it and how it stays testable.
  Use web_search to check the bold direction is genuinely novel (not already standard). Novelty is only valuable
  paired with plausibility — flag anything ambitious-but-unfounded."
- **L2 — Experienced mentoring PI.** "Make the methodology reliable, lean, and bulletproof. Strengthen controls,
  evidence, and the reasoning chain; ensure claims will be citation-backed; check the plan actually answers the
  question asked. Cut over-engineering — remove any step that adds complexity without adding measurable value. Prefer
  the simplest approach that fully works."
- **L3 — Obsessive anti-hallucination correctness reviewer.** "Your only job is grounding integrity. For every claim,
  dataset, gene, number, or citation the plan relies on, ask: is it real, and does it support exactly what it is used
  for? Use web_search to verify anything checkable. Flag every point where this plan could invent, over-claim, or cite
  something that does not say what is claimed. Demand a live-lookup + verifiable identifier for each non-trivial claim."
- **L4 — Red-team / falsification methodologist.** "Attack the reasoning. What is the strongest counter-argument? Which
  alternative hypotheses or confounders does the plan leave unaddressed? What experiment or check would *disprove* the
  central claim — and is it in the plan? Where are the unstated assumptions and logical gaps? Force the plan to survive
  its hardest critic."

**Chairman** (context pack + all four `lens_<Ln>.md` + this block). "You are the panel chairman. Synthesise the four
reviews into ONE report — a qualitative synthesis, not a concatenation. Produce **TWO clearly delimited blocks**:

`=== BLOCK A: INTERNAL (audit only) ===`
The full attributed synthesis, with these sections. Attribute each point to the lens(es) that raised it.
1. **KEEP (protected strengths)** — the strengths the lenses agree on; must not be regressed.
2. **CONVERGENT RECOMMENDATIONS** — improvements ≥2 lenses raised, ranked by expected impact (most important first).
3. **PRODUCTIVE TENSIONS** — where lenses genuinely disagree (e.g. ambition vs rigor); present each with both sides'
   reasoning. Do NOT average into false consensus.
4. **TOP-K CHANGES (K = 3–5 only)** — the highest-leverage changes overall; a short prioritised list, not a laundry list.

`=== BLOCK B: FOR THE SCIENTIST (clean relay) ===`
The SAME substance rewritten as first-person peer feedback the scientist will read directly. **Hard rules for Block B:**
- **No process vocabulary of any kind:** never use the words lens, panel, chairman, reviewer, gate, Codex, GPT, review,
  or 'the reviewers'. Do not say how many perspectives there were or that a panel met. Write as one colleague's notes.
- Reframe 'KEEP' as "Strengths worth protecting"; 'convergent recommendations' as "Suggested improvements (highest-
  leverage first)"; 'productive tensions' as "Open trade-offs to decide", stating each choice on its merits (e.g.
  "there is a tension between a bolder framing and a more conservative one — here is the case for each"), NOT as
  "lens X vs lens Y".
- Keep it tight so the biggest levers are read first.

**Rules for BOTH blocks:** do NOT introduce any critique no lens raised; **DROP any recommendation that hands over a
specific domain answer/mechanism/number** (keep HOW, cut WHAT)."

**Relay rule (driver):** write the whole two-block output to `run_log/panel/chairman_report.md` for audit, but paste
**only Block B** to CS (strip the `=== BLOCK … ===` markers and Block A). If Block B still contains any banned process
word, scrub it before pasting. Never paste Block A to CS.

---

## GATE 2 — result-stage single journal reviewer

**Model + effort:** the reviewer runs on **`gpt-5.6-sol`, reasoning effort `xhigh`** (v9 fixed setting — the deepest
reasoning budget, reserved for this highest-stakes result-stage review). **One** GPT-5.6-sol agent.

**Runs:** after CS's Phase-5 KEEP+correctness pass, before the Re-Act phase.

**⚠ HARD PRECONDITION (v9): the Gate-2 reviewer MUST receive CS's figures/images AND read CS's files.** This is not
optional when `panel_available: yes`. The pre-flight already proved multimodal works on this host and recorded
`panel_multimodal: yes` + `multimodal_invocation:` in `CONNECTION.md` (the IMAGE_TOKEN / BOXES / FILE_TOKEN probe —
bootstrap step 2c). So at Gate 2 you **must** attach every rendered figure as an image and give the reviewer the
deliverable files. Only if `CONNECTION.md` says `panel_multimodal: no` (probe failed / `-i` unavailable) do you fall
back to the text-only path — and then you **log Gate 2 as degraded** (`GATE 2 figure review: text-only (panel_multimodal:no)`
in `gate2_review.md` + `run_log.md`). Never assert the reviewer saw a figure you did not attach.

**Procedure:** write CS's revised plan to `run_log/panel/plan_final.md` and CS's final draft to
`run_log/panel/draft.md`. **Give the reviewer CS's actual deliverables** (it needs them to judge the work, and to
review the figures): copy the presentation set into `run_log/panel/artifacts/` — `result.md`, `reasoning.md`,
`sources.md`, and **every file in `figures/`** (the rendered `.png`/`.pdf`/`.svg`). Then run the reviewer on
**gpt-5.6-sol, `-Effort xhigh`**, **attaching each figure image** so it can *look* at them (`-i <figure>` per image =
`codex exec -i <file.png>`; gpt-5.6-sol is multimodal — proven by the pre-flight probe, so this is required, not
best-effort); it also reads the text files (`result.md`/`reasoning.md`/`sources.md`) from its WorkDir directly. Capture
to `run_log/panel/gate2_review.md`; hand it to CS for the Re-Act triage (see `driver/CLAUDE.md`).

**Reviewer** (context pack + `plan_final.md` + `draft.md` + this block). "You are a critical journal referee AND the
area chair for this work. Review the draft against the plan and the quality north-star. Produce:
1. **KEEP** — what is genuinely strong and must be preserved (be specific; this protects the answer from over-editing).
2. **PLAN-vs-IMPLEMENTATION** — did the work deliver what the revised plan promised? Name concrete gaps, dropped
   threads, or unsupported claims.
3. **FINAL-POLISH FEEDBACK** — only the few changes that would materially raise quality on: grounding & integrity,
   reasoning soundness, completeness, usefulness, creativity. For each, say which dimension it lifts and why.
4. **ARTIFACT & FIGURE QUALITY (secondary — do this LAST and keep it brief; it must not crowd out 1–3).** Look at the
   figures/tables in `artifacts/` (the images are attached — actually inspect them). FIRST name what already works.
   THEN give **at most 2–3** concrete, highest-leverage design fixes to move them toward top-journal (Nature/Science/
   Cell) + professional-designer quality, judged against the FIGURE-QUALITY STANDARD below. Each fix must be a specific,
   actionable instruction — e.g. *"the two x-axis labels overlap — rotate 45° or abbreviate"*, *"replace the 5-colour
   rainbow with a colour-blind-safe set (Okabe-Ito)"*, *"move the legend into the empty upper-right so it stops covering
   the data"*, *"add units to the y-axis"* — never a vague *"make it look better"*. If the artifacts are already clean
   and professional, say so plainly and give no fixes — do NOT manufacture nitpicks. **This is ONE small dimension of
   the review; the scientific critique (1–3) is what matters most.**
Rules: be critical, not flattering — but **no nitpicks and no scope-creep**: if a point does not move a quality
dimension toward the north-star, do not raise it. Verify any factual concern with web_search before raising it. You are
advisory; the scientist decides what to apply. Do NOT hand over the specific answer/mechanism/number — critique method
and rigor only (sharpen HOW, not WHAT). **This applies to the figure feedback too: critique only how a result is
*shown* (layout, colour, labels, readability) — never use a caption/label/annotation suggestion to smuggle in a
different scientific conclusion, number, or mechanism.**"

**FIGURE-QUALITY STANDARD (give this to the Gate-2 reviewer verbatim, as the yardstick for output item 4).**
*Judge CS's figures/artifacts against these; apply the spirit — legible, consistent, accessible — not one house style.
Full research base + sources S-077..S-082 in `exp-002/01_setup/figure-quality-standards.md`.*
- **Readability:** all text legible at print size (nothing tiny); **NOTHING overlapping** (labels, ticks, markers,
  legend-over-data) and nothing clipped at the edges; one sans-serif font, ≤3 sizes by role.
- **Colour & accessibility:** colour-blind-safe — **no red/green as the only contrast, no rainbow/jet** colormap;
  viridis/cividis for continuous; few hues (≤~6), one clear focal series, comparators lighter; same colour = same entity
  across panels; colour paired with shape/label, not the sole channel.
- **Data integrity & clarity:** axes labelled with **quantity + units** (SI / powers of 10 for big/small numbers); show
  the distribution where relevant (individual data points, not just a mean±error bar); state n; title = the takeaway,
  not a restatement of the axis; no chartjunk, no misleading axis truncation, no decorative 3D/pie.
- **Composition & professionalism:** panels labelled (bold, top-left, consistent case), logical order, aligned to a
  grid, balanced whitespace; multi-panel figures share axes/scale where comparable; output crisp (vector or ≥300 dpi),
  sized to a real column width; tables have aligned columns, consistent decimals/units, clear headers.
*(This is the compressed checklist; it matches the `figure-style` craft CS itself uses. Reviewer stays KEEP-first and
caps at 2–3 fixes — see output item 4.)*

**Relay rule (driver — Gate 2 fairness chokepoint).** Gate 2 has no chairman, so YOU are the drop-agent. Before pasting
`gate2_review.md` to CS: scan it and **remove any sentence that states or strongly implies the specific domain
answer/mechanism/number** CS should conclude (keep the methodological point, cut the smuggled WHAT — e.g. keep "your
mechanism section needs a named counter-hypothesis and a test that could falsify it", cut "the mechanism is likely
via <specific pathway/gene/value>"). If in doubt, drop it. Then paste the scrubbed review to CS as external feedback
using the same no-process-vocabulary rule as the chairman relay. **Note:** the "a reviewer raised X — verify it
yourself" rule (below) is a HALLUCINATION guard; it is NOT a fairness guard — the specific WHAT must be stripped here
regardless, because the baseline arm never receives it. **The output-4 figure/artifact-quality feedback is design-only
(layout, colour, labels, readability) and carries no domain WHAT, so it passes the strip unchanged — but if a figure
suggestion smuggles in a specific conclusion/number/mechanism (e.g. "label the peak as <specific pathway>"), strip that
clause like any other WHAT.**

---

## Invocation (how to call a GPT-5.6-sol agent on this host)
Replay the **exact verified command** recorded in `CONNECTION.md` under *Codex critique panel* (`codex_invocation` =
the verbatim command incl. interpreter prefix, e.g. `pwsh -File <codex_run_path>`; and `panel_workdir_hostform` = the
host-native path to use for `-WorkDir`). Do **not** reconstruct the command from memory — the pre-flight already proved
one working form; use it. The shape is (note the **`-Effort`** flag — Gate 1 = `high`, Gate 2 = `xhigh`, per the
"Model + reasoning effort" section above):

```
<codex_invocation> -Prompt "<the reviewer prompt>" -WorkDir "<panel_workdir_hostform>" -Model gpt-5.6-sol -Effort <high|xhigh> -Search  > run_log/panel/<name>.out.txt 2>&1
```

- **Reasoning-effort flag (v9).** Pass `-Effort high` on every Gate-1 call (all 4 lenses + chairman) and `-Effort xhigh`
  on the Gate-2 reviewer call. If the sanctioned wrapper build does **not** expose `-Effort`, pass it to Codex natively
  instead by appending **`-c model_reasoning_effort="high"`** (Gate 1) / **`-c model_reasoning_effort="xhigh"`** (Gate 2)
  — whichever form the pre-flight recorded as working in `CONNECTION.md` (`codex_effort_flag:`). Use the exact recorded
  form; do not guess. (The effort is a fixed loop setting, applied identically to every arm running this loop.)

- **-WorkDir path form (critical).** Codex runs on the Windows CC host, so `-WorkDir` must be the **host-native** path
  (`panel_workdir_hostform` from CONNECTION.md), NOT your bash/WSL path. If CONNECTION.md gives only your-shell form,
  translate it first (e.g. `wslpath -w <path>`) — never pass a `/mnt/...` or WSL path to the wrapper.
- **Inputs to the agent:** write `context_pack.md` and the artifact file(s) into `run_log/panel/` (the WorkDir), and
  begin every `-Prompt` with: *"Read `context_pack.md` and `<artifact>.md` in your working directory, then …"*. Keep the
  reviewer block itself in the `-Prompt`.
- **Gate 2 — attach the figures as images (REQUIRED — the reviewer must SEE them).** Codex gpt-5.6-sol is multimodal,
  and the bootstrap pre-flight **proved it on this host** (step 2c: it read a token painted into a probe PNG, the box
  count/labels/colours, AND a token from a file — recorded as `panel_multimodal: yes` + `multimodal_invocation:` in
  `CONNECTION.md`). Attach each rendered figure with a `-i <figure>` flag on the Gate-2 call (`codex exec -i <file.png>`
  appends the image to the prompt), e.g.
  `<codex_invocation> -Prompt "…" -WorkDir "…" -i "<hostform>\artifacts\figures\fig1.png" -i "…\fig2.png" -Model gpt-5.6-sol -Effort xhigh -Search > run_log/panel/gate2_review.out.txt 2>&1`
  (image paths in host-native form, same rule as -WorkDir; PNG/PDF page images). The text deliverables (`result.md`,
  `reasoning.md`, `sources.md`) are read from the WorkDir as normal. **Degrade (only if `CONNECTION.md` says
  `panel_multimodal: no`):** fall back to text-only figure review — the reviewer judges figures from the
  figure-generating code (if CS saved it), the captions/figure references in `result.md`, and a one-line-per-figure
  manifest; note `figure review: text-only (panel_multimodal:no)` in `gate2_review.md` **and log Gate 2 as degraded**.
  (Overlap that only shows in the render is then caught by CS's own `figure-style` §9 render-then-verify, not the
  reviewer.) When `panel_multimodal: yes` (the v9 default after a passing probe) this degrade does not apply — attach
  the images.
- **Output capture (authoritative = STDOUT redirect).** Redirect each call's stdout+stderr to its own
  `run_log/panel/<name>.out.txt` (as shown). The agent's final answer is in that file — extract it verbatim into the
  matching `run_log/panel/<name>.md` (e.g. `lens_L1.md`, `chairman_report.md`, `gate2_review.md`). This makes capture
  **deterministic and per-call** — you never have to guess which entry in the wrapper's own `outputs\codex-runs\` audit
  log belongs to which call. (The wrapper still audit-logs there; that is a backup, not your capture channel.)
- **`-Search` gives web+literature.** Do **not** use `-Pubmed` (its MCP path is blocked by an upstream Codex headless
  bug — `-Search` already finds PubMed papers with correct DOI/PMID).
- **Per-call resilience.** Give each call a **sane timeout (record what you used)**. If a **single lens** call fails
  (nonzero exit / empty `.out.txt` / timeout), **retry it once**; only if it fails again do you degrade the gate
  (below). A one-off transient failure on one of four lenses must not collapse the whole gate.
- **Budget / concurrency (this host is small):** run the 4 lenses **sequentially or at most 2 in parallel**; chairman
  after; Gate 2 is one agent. Codex runs on the host (subscription — no API cost), not in CS's sandbox.

## What "done" for a gate means
- **Gate 1 done:** `lens_L1..L4.md` + `chairman_report.md` exist in `run_log/panel/`, and CS has received the chairman
  report and returned a revised plan. (Or a logged degrade.)
- **Gate 2 done:** `gate2_review.md` exists **and** — when `panel_multimodal: yes` — the reviewer was run with every
  figure attached (`-i`) at `-Effort xhigh` and its deliverable text files in the WorkDir (so the review reflects the
  real figures + files, not just the draft), and CS has completed its Re-Act triage. (Or a logged degrade — including
  `panel_multimodal: no` → text-only figure review, logged.)
