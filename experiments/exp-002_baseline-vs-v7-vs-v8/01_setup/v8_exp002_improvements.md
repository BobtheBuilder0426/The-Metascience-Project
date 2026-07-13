# v8 Loop + exp-002 — Surgical Improvements (from exp-001 qualitative feedback)

**Source:** exp-001 unblinded feedback — the operator (domain expert) + CS panel qualitative notes (LB-087).
**Scope:** surgical, testable changes only. Each is tagged by WHERE it lives (fairness matters):
 - **[BOTH]** output-format instruction (in the QUESTION, byte-identical to both arms) — fair, defines the deliverable bar.
 - **[LOOP]** v8 context-composer / driver (loop-only — an allowed loop gain, LB-065).
 - **[SCORING]** the CS harness (applies to all arms equally).
**Coordination note:** a parallel CS session (CS2) owns the v8 Codex-panel build (LB-084/085) and the exp-002 hypothesis/protocol (LB-086). These are ADDITIVE proposals for operator approval; none touch CS2's Codex-panel files.

---

## The four themes (what the feedback actually said)

1. **Pilots are overengineered — not real pilots.** BOTH ERGO answers failed this, and it's the operator's explicit ask.
   - the operator on the loop (R2): *"completely overengineered … takes years … extrem overclaim that this is done 3-4 months. not a pilot experiment! it misses … model experiments, where you design a small, easy doable maybe cell based model system … seahorse respiration in cell culture with the KDs or inhibitors, some … simple and cheap model."*
   - the operator on the baseline (R3): *"the proposed pilot … is very hard to do (have you ever tried to take tail blood from a mouse that is on the treadmill?) … definitely not a pilot."*

2. **Too long / hard to read quickly — and it cost points.** Operator wants a page cap; the operator's Q2 verdict was low-confidence *because* both were hard to parse.
   - the operator on the loop (R4, Q2): *"the mapping out of all hypothesis was good, the text was however very complicated to read and very long."*
   - This is the direct cause of the only combined loss (Q2): the CS panel out-weighed the operator's low-confidence loop pick because legibility dragged the read.

3. **Overclaim / shallow "lit-scrape" (baseline weakness the loop already beats).** Keep the loop's data-depth edge; make sure scoring catches overclaim.
   - the operator on the baseline (R1, Q3): *"not novel … overclaims apelins relevance … no deep data analysis, just lit scrape … too fast, no deep reasoning on the best target."* (hallucination flag = Yes)
   - the operator on the loop (R5, Q3): *"very strong … never heard of the NMJ improvement … very nice data analysis … i am impressed."*

4. **The CS panel can't separate the arms; the operator can.** Method finding: CS Δ=+0.02 (flat/lenient) vs combined Δ=+0.48; the operator picked the loop on all 3 questions.

---

## SHORT LIST — surgical improvements

### A. Pilot-experiment discipline  → theme 1  *(the highest-value change)*
- **A1 [BOTH] — "genuine pilot" clause in the output-format instruction.** When an answer proposes a first/pilot experiment, it must be *the smallest, cheapest, fastest feasible test that could falsify the core claim* — prefer **in-vitro / cell-based / existing-data** before any animal study; state an honest **timeline, cost tier, and feasibility note**; name the specific readout. Fair (both arms), and it directly encodes what the operator said a pilot IS.
- **A2 [LOOP] — an "experiment-design" block in the v8 context-composer.** Sharpens HOW the loop reasons about experiments (model-system-first heuristic: cell/organoid/Seahorse/existing-dataset re-analysis → only then animal; a feasibility self-check "could a PhD run this in ≤8 weeks on a normal budget?"). This is a loop gain (does not prescribe the answer, only the rigor of getting there). Pairs with A1: A1 sets the bar for both arms, A2 gives the loop the method to clear it.

### B. Length / legibility  → theme 2  *(your page-cap question)*
- **B1 [BOTH] — hard cap on `result.md`: ≤ ~1,800 words (≈ 4 pages), figures excluded.** I agree with your 4-page instinct. One refinement: cap in **words**, not "pages" — markdown has no fixed page length, so a word budget is what an arm can actually self-check against. ≈1,800 words ≈ 4 printed pages.
- **B2 [BOTH] — mandatory ≤150-word "Bottom line" box at the top of `result.md`** (the hypothesis + the one pilot, in plain language). This is the single highest-leverage fix for *"understand quickly"* — it gives the operator the answer in one view regardless of body length.
- **B3 [BOTH] — `reasoning.md` stays uncapped but must be bulleted/structured**, not prose walls. It's the provenance trace (CS scores it); it shouldn't add to the reader's burden but shouldn't be truncated either.
- *Rationale for keeping it in the QUESTION, not the loop:* format is a fairness-locked, byte-identical instruction (operator ruling). A cap that lived only in the loop would be an unfair advantage/handicap. Both arms get the same cap.

### C. Scoring method  → themes 3 + 4
- **C1 [SCORING] — harsher, wider-range rubric anchors + a "use the full 1–5 range" instruction to the panel.** exp-001 showed the panel bunches at 4–5 on reasoning/usefulness/completeness, erasing real differences. Re-anchor so a *typical competent* answer sits at 3, and reserve 5 for genuinely exceptional. This is the fix that lets the automated endpoint detect what the expert sees. (Note: recalibrating changes absolute scores — fine, because exp-002 is a fresh internally-consistent 3-way run; flag it in the exp-002 protocol.)
- **C2 [SCORING] — an explicit "overclaim / scope-inflation" check in the grounding stage.** the operator caught the baseline's apelin overclaim; the CS grounding metric should too (a claim whose strength exceeds what its citation supports → grounding hit). Turns a human catch into an automated one.

### D. exp-002 setup notes
- **D1** — apply A1 + B1 + B2 + B3 to the exp-002 output-format instruction (same file, byte-identical across B / L7 / L8). This makes the 3-way comparison test the *legibility + pilot-realism* dimensions the operator now cares about.
- **D2** — land C1 + C2 in the harness BEFORE exp-002 scoring, and record the recalibration in the protocol so L8-vs-L7-vs-B deltas are read against the new anchors.
- **D3** — carry the two-key double-blind + gated-creativity method unchanged (validated in exp-001). Add a per-answer **word-count** and **"pilot-realism"** field to the eval site so both are tracked as first-class, plottable signals.

---

## My recommendation on the page cap (you asked)
**Yes — cap it, and 4 pages is the right ballpark, but express it as ~1,800 words + a mandatory 150-word bottom-line box.** The word budget is self-checkable by the arm; the bottom-line box is what actually fixes *"hard to understand quickly"* (it cost the loop Q2). Keep `reasoning.md` uncapped-but-bulleted so we don't lose the provenance trace that grounding/creativity scoring depends on. All of it goes in the shared output-format instruction, so both arms are capped identically — no fairness leak.
