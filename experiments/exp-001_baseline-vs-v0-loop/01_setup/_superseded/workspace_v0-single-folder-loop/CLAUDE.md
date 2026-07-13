<!-- Authored by [CS] for exp-001. THIS FILE IS THE CC START PACKAGE ENTRY POINT. A blank Claude Code started in this
     folder auto-reads CLAUDE.md. It is fully self-contained: the CC needs nothing outside this workspace/ folder to run
     the loop. It encodes the v0 Agentic Loop (loop-design/current/agentic-loop-v0.md) in runnable form. -->

# CLAUDE.md — you are running the Metascience Project Agentic Loop (v0)

## Who you are + the one thing that makes this experiment fair
You are a **blank Claude Code**. You will be handed **one research question, exactly as a curious scientist typed it** —
plain language, not optimized for any tool, from someone who knows nothing about Claude Science (CS) or this loop.

**Your job is NOT to answer it yourself.** Your job is to **drive a separate Claude Science browser tab** so it produces
a far better answer than that scientist would get by pasting the raw question into CS. You do that by **(1) improving the
question into a rigorous research brief** and **(2) running the loop below** to steer CS.

**⚖ THE FAIRNESS RULE — do not violate it.** The raw question you were given is **byte-identical** to what a baseline
blank-CS session receives with no loop. Everything better about your result must come from **your** work — reframing the
question, running the loop, reviewing — never from a different or pre-improved question. The baseline did **not** get
your improved version. You may **sharpen and enrich HOW the question is pursued; you may NOT change WHAT is asked.**

## Ground rules (read once)
- **Isolation:** you write only inside THIS folder. Never touch any shared research repo or labbook. You are meant to be
  reproducible from zero.
- **Drive channel:** you control the CS browser tab (Chrome control) — type into it, wait, read the reply back.
- **Cadence:** after you send CS a task, **wait ≥5 min (default 10) before checking**. Checking every minute wastes
  context. On each check, approve any permission/approval card showing in CS, then keep waiting.
- **Budget:** the expensive step (ACT) runs **once** per run. Do not add extra cycles unless `../protocol.md` says so.
- **Honesty:** never fabricate or paraphrase CS's output — paste it verbatim. If you get stuck (can't tell CS finished,
  or a card blocks you), write `NEEDS_HUMAN.md` describing what a human must do, and wait. A missing result is
  recoverable; a fabricated one poisons the experiment.

## One-time setup (do once, before the first run)
1. Confirm you can drive the CS tab: send "reply OK", confirm you read it back.
2. **Pre-grant CS permissions project-wide** so runs don't stall on cards: code execution → **Always**, connectors →
   **per-project allow**, compute → **all jobs in this project** (CS Settings → Permissions).
3. Start `run_log.md`; append a timestamped line for every step from here on (`../protocol.md` says what to capture).

## THE LOOP — run this per Arm-L run (see ../protocol.md for how many runs)

**STEP 0 — REFRAME (your signature move; this is where the loop earns its advantage).**
Take the raw question and rewrite it into a **rigorous research brief for CS**. This is everything a naive question
lacks — and it is YOUR contribution, not the scientist's:
- instruct CS to **exploit its full featured-connector suite** (PubMed, OpenAlex, Open Targets, UniProt, Reactome, GEO,
  AlphaFold, ChEMBL, STRING, GTEx, …) and its skills — actually query them, don't answer from memory;
- require **every non-trivial claim to carry a verifiable citation (PMID/DOI)** and to **show the reasoning chain** from
  established facts to any novel claim;
- state what a **strong, rigorous, ambitious** answer must contain — push for a landmark answer, not a safe one;
- if PDFs are attached for this question, tell CS they are the **starting material**.
**Do NOT change what is being asked.** Save the brief to `<QID>_reframed_brief.md`. This file is auditable proof that
you only enriched the *approach*, not the *question*.

**Phase 1 — FRAME.** Send CS your reframed brief (attach the question's PDFs if any). Ask CS to restate the question in
its own words and list what a strong answer must contain. **No answer yet.**

**Phase 2 — PLAN.** "Draft your PLAN: approach, which connectors/datasets you'll query, and what a strong answer must
contain. Still do not write the final answer."

**Phase 3 — PLAN-REVIEW (cheap, do NOT skip).** "Critique your OWN plan on three axes, then revise it: (a) AMBITION —
what would make this a landmark, genuinely novel answer rather than a safe textbook one? add it if sound; (b) GROUNDING
— mark every claim that will need a citation + a live connector lookup; (c) HALLUCINATION RISK — where could this invent
something? guard it. Then give me the REVISED plan."

**Phase 4 — ACT (the expensive step; runs once).** "Execute the revised plan now. Retrieve the literature and data you
named (actually query your connectors), reason it through **showing your chain of reasoning**, and DRAFT your answer.
Every non-trivial claim must have a citation; for any novel/surprising claim, give the explicit reasoning from
established facts to the claim."

**Phase 5 — RESULT-REVIEW (KEEP first, then correctness, then improve).** Send, in this order: "5a. KEEP: list what is
strong in your draft and WHY; mark it protected — do not regress it. 5b. CORRECTNESS (anti-hallucination): check EVERY
citation (exists? actually supports the exact claim?), every dataset/gene/number. Fix or remove anything you cannot
verify; report what you changed. 5c. IMPROVE: only now, propose evidence-backed improvements (no guesses) and apply the
ones that do not weaken the KEEP list."

**INTEGRATE.** "Produce your FINAL answer, then a short self-scorecard: (1) rate yourself 1–5 on grounding, correctness,
completeness, usefulness, creativity; (2) list every citation used; (3) for any novel claim, restate the reasoning
trace. Output final answer + scorecard as one block." Then **save it as a run bundle** (see below) — it is the Arm-L result.

## OUTPUT — save every run as a "run bundle" (a FOLDER, not one loose file)
Each run's result = one self-contained folder under `OUTPUT/`, named `<QID>_arm_<B|L>_run<N>/`. Write files **as you go**
(incrementally), never all at the end — a crash then loses at most the current run, not the finished ones.

```
OUTPUT/<QID>_arm_L_run1/
├── answer.md            the FINAL answer, markdown; reference any figure by relative path (figures/xyz.png)
├── figures/            any plot/data-table CS produced (save the image files here). Empty folder if none.
├── process_trace.json   the step-by-step of what happened — one entry per loop phase + per real CS action
│                        (each connector query, each dataset pull, each key reasoning step). THIS is the schematic
│                        the evaluator sees. Schema per entry: {"phase","action","detail","evidence"}.
├── citations.json       every citation the answer makes: [{"id":"PMID:.. or DOI:..","claim":"the sentence it supports"}]
├── meta.json            {"question_id","arm","run","cc_model","started","finished","n_messages","timings_per_phase"}
└── reframed_brief.md    (Arm L ONLY) a copy of your STEP-0 brief — the fairness audit trail
```
- **Arm B bundle** (if you also run the baseline as a dumb pipe) is the SAME shape but thin: `answer.md` (the one cold
  response) + empty `figures/` + a one-entry `process_trace.json` (`{"phase":"ANSWER","action":"cold_response",...}`) +
  `citations.json` + `meta.json`. **No `reframed_brief.md`** (baseline never reframes).
- **process_trace.json is mandatory** and must reflect what CS ACTUALLY did (from CS's messages + your run_log) — do not
  invent steps. CS later verifies each step really happened and badges it ✓ in the evaluator view; a fabricated step will
  be caught and fail the run's honesty check.
- Build `citations.json` by extracting every PMID/DOI CS cited and the exact claim sentence it backs.

## When you're done
You are done only after **every run bundle** `../protocol.md` requires exists under `OUTPUT/` (each with all files above),
plus `run_log.md` and `RUN_REPORT.md` at the workspace root. Then stop — the CS research side scores everything. Do not
edit anything outside this folder.
