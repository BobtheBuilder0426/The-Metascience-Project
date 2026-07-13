<!-- Authored by [CS], the assistant-facing. The contract for the assistant's 03_final-report.md — what CS needs to analyse exp-001
     and decide the next iteration. the assistant is Mission-Control: he analyses the run + scores, does NOT evaluate the
     science himself (that's the operator) and does NOT design the next loop (that's CS). -->
<!-- ⚠ STALE — PENDING REWRITE (LB-072/LB-073). This spec predates several locked changes and must NOT be used as-is:
       • the assistant is NO LONGER Mission-Control — CS writes 03_final-report.md itself (operator override LB-032; the assistant = crash-fallback only).
       • Design is 3 questions × 1 run = 6 (not "≥2 runs each"); success = mean-Δ across questions + win-count k/3 (NOT "Δ > pooled run-to-run SD").
       • Scoring = mean(CS,the operator) per dimension (NOT "the operator vs harness, do not reconcile"); report per-dimension arm plots ×{CS,the operator,combined}.
       • The rewritten spec MUST include a **Methods** section that references and summarizes loop-design/current/blinding-protocol.md
         (the two-key double-blind) — the blinding scheme is a demonstrated submission method.
     Canonical until the rewrite lands: loop-design/current/dataflow-and-handoffs.md + loop-design/current/blinding-protocol.md. -->

# exp-001 — Final-report spec (the assistant → CS)  [CS-authored]  ⚠ STALE, see header (LB-072/LB-073)

**Your role here, the assistant:** you take the blank CC's raw run (`workspace/RUN_REPORT.md` + the two answer files), run the
**the Metascience Project scoring harness** on both answers, collect **the operator's evaluation**, and assemble one report CS can analyse. You
report facts + measurements; you do **not** judge the science (the operator) or design the next loop (CS). Write it as
`03_final-report.md` with EXACTLY the sections below. Every number must trace to a file.

## Required sections

**1. Run summary (from the CC's RUN_REPORT).**
- Test-set version + the verbatim question; date; CC model; both answer-file paths.
- Arm B: message count (expect 1), wall-clock. Arm L: per-phase timings, total wall-clock, #approval cards, whether
  `NEEDS_HUMAN.md` was ever written.
- **Fairness attestation** copied from the CC report (question byte-identical across arms; Arm B got no loop help).
- Any anomalies the CC logged (connector down, rate limit, session reset).

**2. Harness scores (the primary data).** Run the harness (`workspace/harness/`, real mode) on both answers, judges
blinded to arm, ≥2 runs each. Report as a table:
- per-arm, per-run: the 5 dimension scores + weighted composite + creativity_index + citation_verification_rate + #citations.
- **Δcomposite = mean(L) − mean(B)**, and the **pooled run-to-run SD**. State plainly whether Δ > SD (the pre-registered
  success test, 00_hypothesis.md).
- the **Elo** head-to-head result (L vs B).
- **attach the raw** `scorecard.json` + `scorecard.csv` (do not just summarize — CS needs the raw rows).

**3. Anti-hallucination audit (do NOT skip).** For every citation the harness flagged `nonexistent_reference` or
`claim_not_supported_by_cited_source` — plus any unresolved/unused dataset ID or unverified `process_trace` action —
list it (which arm, the claim, the citation/ID/step). This is the grounding-&-integrity backbone — CS needs to see
exactly what was caught.

**4. the operator's evaluation (verbatim).** Attach the operator's filled `04_evaluation.md` unedited. Then a small table:
the operator's per-dimension scores next to the harness's, with the **agreement** (differences per dimension) and any
**creativity honesty flags** the operator raised (Part B/D). Where the operator and the harness disagree, say so — do not reconcile them
yourself; that's CS's analysis.

**5. Machine-readable summary block.** A fenced JSON with:
`{exp, question_id, arms:{B:{mean_composite,sd,runs}, L:{...}}, delta_composite, pooled_sd, delta_gt_sd:bool,
elo_winner, human_overall_pick, human_harness_dim_agreement, hallucinations_caught:int, anomalies:[...]}`.
CS parses this directly.

**6. Your neutral observations (facts only).** Anything you noticed running it that CS should weigh — e.g. "Arm L spent
80% of wall-clock in ACT", "both arms cited the same 3 papers", "the loop's plan-review visibly changed the answer".
**No recommendations on the next loop** — just observations. CS decides the next hypothesis.

## Format rules
- Markdown; every quantitative claim links to the file/row it came from. Timestamps CEST.
- Attach (don't inline-summarize) the raw scorecard files + the operator's sheet + the CC's RUN_REPORT.
- If something is missing or the run degraded (NEEDS_HUMAN), report it as-is — a partial, honest report beats a
  polished, guessed one. CS would rather re-run than analyse fabricated numbers.

