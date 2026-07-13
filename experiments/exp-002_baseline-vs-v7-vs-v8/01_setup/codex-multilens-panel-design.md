<!-- WHAT THIS FILE IS: the design + decision record for the Codex multi-lens review panel — the v8 loop upgrade that
     adds EXTERNAL, cross-vendor (GPT-5.6-sol) critique to the CC-drives-CS inner loop at two gates (plan-stage panel +
     result-stage journal reviewer), followed by a CS Re-Act triage. Authored by Claude Science session 2 (CS2).
     HOW TO USE: Part 1 = decisions the OPERATOR has already locked (build to these). Part 2 = CS2's research-backed
     PROPOSAL for the three open research questions A/B/C — these await operator sign-off before build. Nothing in
     v8_cc-bootstrap/ is touched until the operator confirms. Sources cited by S-NNN from /SOURCES.md. -->

# v8 upgrade — Codex multi-lens review panel for the CC-drives-CS inner loop  [CS2]
**Status:** Part 1 LOCKED (operator decisions, 2026-07-12). Part 2 = PROPOSAL awaiting operator input on A / B / C.
**Owning labbook entries:** LB-081 (workstream lock), LB-082 (this design + research). **Loop line:** `v8_cc-bootstrap`.
**Scope guard:** this concerns ONLY the inner-loop critique layer (improvement category C3, finding E/F). It does not
touch the scoring harness, the eval site, the blinding protocol, the locked questions, or arms B / L7.

---

## 0. Why this upgrade (the one-paragraph case, grounded)
The current loop lets the driven CS session review its **own** plan and its **own** draft (self-review). The strongest
recent evidence says that is the weak form: LLMs **struggle to self-correct reasoning without external feedback, and
sometimes degrade after trying** (S-072). The fix the leading labs converge on is **external, tool-grounded critique**:
Google's Co-Scientist runs a **Reflection agent as a "virtual peer reviewer"** and a **Meta-review agent** that
synthesises all reviews — and its own ablation found that **giving the reviewer external search tools prevented the
hallucination of seemingly-novel-but-implausible hypotheses**, while a **scientific-debate prompt improved ranking**
(S-004). OpenAI's **CriticGPT** shows trained LLM critics **catch more bugs than paid human reviewers** and are
preferred >80% of the time — but they also hallucinate, so critics must be grounded and their output triaged (S-071).
Sakana's **AI-Scientist automated reviewer** reaches near-human accuracy by ensembling reviews under **real conference
guidelines** with an **Area-Chair meta-review** (S-075). This upgrade brings that external-critique engine into our
loop, using **GPT-5.6-sol via Codex** as the critic — which also makes the critic a **different vendor from the
producer** (CS = Claude), the genuine "two brains" that blunts self-enhancement bias (S-008) more cleanly than any
within-vendor panel could.

---

# PART 1 — LOCKED (operator decisions)

## 1.1 Placement in the loop (locked)
Two external-critique gates are inserted into the existing driver loop, plus a new CS-owned Re-Act phase:

```
 REFRAME → FRAME → PLAN
                    │
        ┌───────────┴───────────────────────────────────────────────┐
        │ GATE 1 — PLAN-STAGE CODEX MULTI-LENS PANEL                  │  ← cheapest, highest-leverage point (S-014 D)
        │  driver spawns N GPT-5.6-sol lenses on CS's proposed PLAN   │
        │  each: (1) KEEP-first  → (2) optimise + WHY, per its lens   │  ← S-014 E/F
        │  each has web + literature tools + full goal context        │  ← S-004, S-014 G
        │  → CHAIRMAN (GPT-5.6-sol) = qualitative synthesis, not glue │  ← S-004 meta-review, S-042
        │  → driver delivers chairman report to CS                    │
        │  → CS REFLECTS (report + own reflection) + REVISES plan     │  ← external feedback drives, CS integrates
        │  → driver GO                                                │
        └───────────┬───────────────────────────────────────────────┘
                    ▼
                   ACT  (CS executes the revised plan: connectors, data, reasoning, draft)
                    │
                   CS-self RESULT-REVIEW  (KEEP-first → obsessive anti-hallucination correctness, live-tool verified)
                    │
        ┌───────────┴───────────────────────────────────────────────┐
        │ GATE 2 — RESULT-STAGE SINGLE CODEX JOURNAL REVIEWER         │  ← stop gate before integration
        │  one GPT-5.6-sol "critical journal reviewer" (persona: 2.3) │
        │  compares (revised) PLAN vs the actual IMPLEMENTATION       │
        │  KEEP-first, then bounded final-polish feedback toward our  │
        │  goals; web/lit tools to verify before raising a concern    │  ← S-075, S-004, S-071
        └───────────┬───────────────────────────────────────────────┘
                    ▼
        ┌───────────────────────────────────────────────────────────┐
        │ RE-ACT — CS OWNS THE FINAL CALL (new, locked)               │
        │  CS triages each reviewer point: ACCEPT / REJECT(+reason) / │
        │  DEFER; decides what to RE-RUN vs not; applies only changes │
        │  that raise quality toward our goals without regressing     │
        │  KEEP or over-engineering; logs the triage reasoning        │  ← S-072, S-074, S-014 F, S-063
        └───────────┬───────────────────────────────────────────────┘
                    ▼
                 INTEGRATE → presentation folder (unchanged contract)
```

## 1.2 Locked decisions (operator, 2026-07-12)
1. **The panel is EXTERNAL and runs on the plan** — the driver no longer lets CS/driver review the plan alone; it
   spawns a Codex GPT-5.6-sol multi-lens panel to critique CS's proposed plan.
2. **All panel + chairman + gate-2 agents are GPT-5.6-sol via Codex** (not Claude). Producer = CS (Claude); critics =
   GPT. This cross-vendor split is the anti-self-enhancement mechanism (S-008).
3. **Every critic agent must have web search + literature-research access** and **optimal context** on the goal / what
   the user wants (S-004, S-014 G, S-023).
4. **Each lens does KEEP-first, then optimise-with-reasoning** (never verdicts without the "why") (S-014 E/F).
5. **Chairman = a GPT-5.6-sol agent spawned after the lens reviews are in**, produces a **qualitative synthesis** (not
   concatenation); the driver delivers it to CS.
6. **CS reflects on the chairman report AND self-reflects, then revises its plan** — only then does the driver GO.
7. **Gate 2 = a single GPT-5.6-sol journal-reviewer** after the run, before integration; compares plan vs
   implementation; says what is good; gives feedback to bring the result to best final quality.
8. **Re-Act phase (new):** after Gate 2, CS decides which reviewer input is worth acting on, what to re-run and what
   not, applies the sensible improvements, then integrates.
9. **Everything aligned to the project north-star:** get the most out of CS; real creativity + novelty **with clear
   reasoning / chain-of-thought**; grounded in excellent scientific practice.
10. **v8 may carry several upgraded variables** (composed context + this panel). Time-box precludes strict
    one-variable-at-a-time; the honest consequence (L8 is the cumulative loop, not a clean OPT-1 isolate) is recorded
    in LB-081 and must be stated in any write-up.

## 1.3 The Codex / GPT-5.6-sol capability (verified, operator-provided)
- Sanctioned wrapper **`codex-run.ps1`** verified on codex **v0.144.1**; model **gpt-5.6-sol** proven two ways —
  direct `codex exec -m gpt-5.6-sol` (→ SOL_OK, exit 0) and wrapper `codex-run.ps1 -Model gpt-5.6-sol` (scoped,
  sandboxed, audit-logged to `outputs\codex-runs\`; → WRAPPER_SOL_OK, exit 0).
- Runs on the **ChatGPT subscription — no API key, no extra cost** beyond the sub. This is what makes a multi-agent
  Codex panel affordable.
- The Codex agents run on the **Windows CC host**, not in the CS Linux sandbox — so they do **not** consume the CS
  ~2 GiB RAM. Concurrency/context are still bounded on the host side (§3.4).

---

# PART 2 — PROPOSAL (research-backed; awaiting operator input on A / B / C)

## A. The lens set — proposal
**Locked by operator:** keep the **ambitious postdoc** and the **experienced mentoring PI**, add an **obsessive
anti-hallucination correctness** lens, and add **one more** researched lens. Proposal = a **4-lens panel**, run as
**independent parallel reviews** (not inter-agent debate — see rationale), each GPT-5.6-sol, each KEEP-first, each
tool-grounded, each given the goal context:

| # | Lens | What it optimises (maps to our rubric) | Grounding |
|---|------|----------------------------------------|-----------|
| L1 | **Ambitious young postdoc** — "what would make this a landmark, genuinely novel answer, not a safe one? add the one thing that makes it matter — but every bold move must name its evidence path and be testable." | creativity + usefulness | S-006/S-062 (AI ideas can be *more* novel) paired with S-063 (novel≠better on execution) + S-004 (search prevents implausible-novelty) → **novelty gated by plausibility** |
| L2 | **Experienced mentoring PI** — "keep the methodology reliable, lean, established; strengthen controls, evidence, reasoning; make the story bulletproof; cut over-engineering toward elegant + reliable." | reasoning-soundness + completeness | S-014 E (the lens that worked) + S-076 (simplest solution that works; add complexity only for measurable value) |
| L3 | **Obsessive anti-hallucination correctness reviewer** — "check every claim/dataset/citation the plan relies on is real and supports what it's cited for; flag every point where this could hallucinate or over-claim." | grounding & integrity | S-071 (LLM critics beat humans at catching errors) + S-004 (tool-grounded reflection kills implausible novelty) + S-051/S-052 (CoVe / SelfCheck) — **must query web/lit to verify, not opine** |
| L4 | **Red-team methodologist / falsification lens (CS2 RECOMMENDATION)** — "what is the strongest counter-argument? which alternative hypotheses/confounds are unaddressed? what experiment would *disprove* this? where does the reasoning chain have gaps or unstated assumptions?" | reasoning-soundness + creativity (breaks recombination-bias) | S-004 (scientific-debate prompt was Co-Scientist's biggest ranking lever) + S-043/S-044 (adversarial/divergent critique raises factuality) + classic reviewer-2 |

**Why L4 = red-team/falsification (my recommendation).** The other three cover *expand* (L1), *constrain & de-risk*
(L2), and *verify facts* (L3). The gap is **stress-testing the logic itself** — alternatives, confounds,
falsifiability. It (a) is universally valuable across all three question categories, (b) most directly attacks the AI
"recombine-old-stuff" bias by forcing non-obvious reasoning, and (c) institutionalises the "scientific debate" that
gave Co-Scientist its largest quality gain (S-004) without paying for a full multi-agent debate.
**Runner-up (operator's call):** a **Significance / translational "so-what" lens** (maps to usefulness) — stronger if
the question set leans translational (cat-3). I recommend red-team as the default because it is the most goal-aligned
("real novelty *with clear reasoning*, excellent scientific practice").

**Why independent parallel, not debate.** Multi-agent debate gains are **fragile under fair baselines** (S-069) and
add cost/latency; Anthropic's guidance is to prefer the simplest structure that adds measurable value (S-076).
Independent lenses + a synthesising chairman capture the diversity benefit (S-017 PoLL, S-042 MoA) while the *chairman*
surfaces the productive disagreement (the debate value) — exactly Co-Scientist's meta-review pattern (S-004). It is
also cheaper on the host (§3.4).

## B. The chairman — proposal
**Locked:** a GPT-5.6-sol agent spawned after the lenses; qualitative synthesis; report delivered to CS by the driver.

**Proposed synthesis contract (the report schema CS receives), engineered for maximum quality-gain and minimum
dilution:**
1. **KEEP (protected strengths):** the consensus of what the lenses judged good — CS must not regress these (S-014 F).
2. **Convergent recommendations:** where ≥2 lenses agree on an improvement, **ranked by expected impact** (front-loaded
   — S-045 says models under-use mid-context, so the few biggest levers go first).
3. **Productive tensions (surfaced, not averaged):** where L1↔L2 (ambition↔rigor) or others disagree, presented as an
   **explicit decision for CS**, with each side's reasoning — never blended into false consensus (S-044).
4. **Top-K highest-leverage changes only** (K≈3–5): a prioritised shortlist, not a laundry list — the anti-over-
   engineering / anti-dilution guard (S-076).
5. **Attribution + grounding:** every synthesised point is **attributed to the lens(es) that raised it** and the
   chairman may **not invent new critiques** — this bounds the CriticGPT hallucination risk (S-071).
6. **Fairness note:** any recommendation that would smuggle a specific domain answer/conclusion is dropped (it must
   sharpen HOW, not hand CS the WHAT — same firewall spirit as the context-composer).

**Grounding:** Co-Scientist Meta-review "summarises common patterns across reviews… prevents oversight of critical
details" (S-004); MoA aggregator fuses proposer outputs into one stronger output (S-042); MARG's leader synthesises
specialised agents' findings into one review (S-073).
**Authority:** chairman **synthesises only — it does not edit or decide.** CS reflects and revises (locked #6). This
keeps CS's scientific agency and avoids a critic silently rewriting the science.

## C. The Gate-2 journal reviewer — proposal
**Locked:** one GPT-5.6-sol critical journal reviewer after the run, before integration; compares plan vs
implementation; KEEP-first; feedback to reach best final quality.

**Proposed best-practice spec (maximise benefit; avoid over-engineering / chaos / quality-dilution):**
1. **Persona = journal referee + Area-Chair**, the configuration Sakana validated to near-human review accuracy —
   reflection + **real review guidelines** + a chair-style verdict (S-075). Not a generic "give feedback" prompt.
2. **Rubric- and goal-anchored:** scores/《comments》conditioned on our 5 dimensions + the project north-star + the
   actual question (S-020 anchored rubrics) — so feedback pushes *our* goals, not generic reviewer-2 preferences.
3. **Plan-vs-implementation diff (operator's ask):** did the run deliver what the revised plan promised? name concrete
   gaps and unfulfilled claims.
4. **KEEP-first, then bounded feedback:** protect strengths (S-014 F); then only the **few** changes that would
   *materially* improve quality. Explicit instruction: **no nitpicks, no scope-creep, no over-engineering** — "if it
   doesn't move a rubric dimension toward our goals, don't raise it" (S-071 nitpick/hallucination tradeoff; S-076).
5. **Tool-grounded:** must verify any factual concern via web/lit before raising it (S-004; avoid hallucinated
   critiques, S-071).
6. **Advisory only → CS's Re-Act triage decides.** The reviewer cannot force churn. This is the core anti-chaos /
   anti-dilution guard and the anti-sycophancy guard **in both directions**: the reviewer is told to be critical (not
   flatter), and CS is told to weigh, not comply (S-074).

**Why a single reviewer at Gate 2 (not a panel).** The heavy multi-lens lift sits at the plan stage, which is the
cheapest, highest-leverage point to change direction (S-014 D). At the result stage the answer is nearly done;
over-reviewing a finished result invites over-editing and dilution. One strong, bounded strategic review + CS triage
is the defensible, budget-aware choice.

## The Re-Act phase — proposal (fills out locked #8)
After Gate 2, CS runs an explicit, logged triage before integrating:
1. **Per reviewer point → ACCEPT / REJECT(+reason) / DEFER.** Reasoned, not reflexive — external feedback is what makes
   correction actually work (S-072), but caving to a critic without judgement is sycophancy (S-074).
2. **Decide re-runs:** what to re-query / re-analyse / pull more literature for, vs. what needs none — bounded by the
   host/subscription budget.
3. **Apply only quality-raising changes** that do not regress the KEEP list or over-engineer (S-014 F, S-076).
4. **Log the triage** (accept/reject + reasoning) into `run_log/` — this is genuine-reasoning evidence for the
   write-up, and it is what makes "the loop improved the result" auditable rather than asserted (S-063 honesty).
Then INTEGRATE (unchanged presentation-folder contract).

---

## 3. Cross-cutting design (applies to A, B, C)

### 3.1 Reviewer context pack (every agent gets it)
The driver assembles, per agent: the **project north-star** (get the most out of CS; novelty + reasoning; grounded
science), **what the user wants** (the goal / reframed brief — HOW-level, never answer-priming), the **question**, and
the artefact under review (the PLAN at Gate 1; the PLAN + DRAFT at Gate 2). Grounded in context-engineering (S-023) and
MARG's context distribution (S-073). Tools: web search + literature lookup enabled (S-004, S-014 G).

### 3.2 Fairness (this is a loop advantage — legitimate, must be documented)
External GPT critique is a real advantage the **baseline (Arm B) never receives** — exactly like the composed context.
That is fair **iff**: (a) the question stays byte-identical across arms; (b) the critique sharpens **HOW** (rigor,
ambition, grounding, logic), never smuggles the **WHAT** (a domain answer/mechanism) — enforced in the chairman/gate-2
prompts and the "drop answer-priming recommendations" rule; (c) it is **documented as part of the loop method** in the
run bundle (that a Codex panel/reviewer ran, with which lenses and what it changed), so any "loop beat baseline" claim
honestly accounts for it. This mirrors the fairness bookkeeping designed for the multimodel module (S-042 design).

### 3.3 Cross-vendor anti-self-enhancement (a property worth stating)
Producer = CS (Claude); all critics = GPT-5.6-sol. The critic is a **different vendor from the producer** — the
genuine "two brains" of finding E and the cleanest available control against self-enhancement bias (S-008), which CS's
own within-vendor scoring panel cannot achieve. This is a real methodological strength of routing critique through
Codex.

### 3.4 Budget & concurrency (2 GiB host discipline)
- Codex agents run on the **Windows CC host** (subscription-bounded, no API cost), not the CS sandbox — no CS-RAM hit.
- Bound host concurrency: run the 4 lenses **sequentially or ≤2 in parallel**, chairman after; Gate 2 is a single
  agent. Keep the driver's context lean (finding A — context is the binding constraint) and poll cadence disciplined
  (finding B). Each Codex call is audit-logged via `codex-run.ps1` to `outputs\codex-runs\`.

### 3.5 Honesty guards & named threats to validity
- **Critics hallucinate** (S-071) → tools + attribution + "verify before raising" + CS triage.
- **Self-correction / debate gains can be fragile** (S-069, S-072) → critique is external + cross-vendor + tool-
  grounded, and CS triages rather than blindly applies.
- **Sycophancy both ways** (S-074) → reviewer told to be critical & evidence-based; CS told to weigh, not comply.
- **Over-engineering / dilution** (S-076) → PI lens + top-K bounded feedback + KEEP-first + CS Re-Act triage.

---

## 4. Open decisions for the operator (please rule on these)
1. **A — 4th lens:** red-team / falsification (my recommendation) **vs** significance / translational so-what **vs**
   experimental-design methodologist. Which one?
2. **A — interaction:** independent parallel lenses (my recommendation) **vs** lenses debate each other before the
   chairman?
3. **Result-stage stacking:** keep the CS-self KEEP+correctness pass *before* Gate 2 (my recommendation — it is the
   live-tool verification CS alone can do) **vs** fold all correctness into L3 + Gate 2 only?
4. **Gate 1 plan-review:** the panel is the sole plan-review and CS's self-critique becomes the "reflect on the
   chairman report" step (my recommendation) **vs** keep a separate CS self-plan-review too?
5. **Chairman:** confirm GPT-5.6-sol + synthesis-only/no-edits (my recommendation).
6. **Panel size:** 4 lenses as above — or trim to 3 / expand — given the host budget?
7. **Build-time must-verify:** does `codex exec` / `codex-run.ps1` have **web + literature access** in this setup? The
   correctness (L3) and postdoc-plausibility (L1) guards depend on it (S-004). If not, we need a fallback (e.g. the
   driver hands retrieved sources into the reviewer context).

---

## 5. Sources used (registered in /SOURCES.md)
New this workstream: **S-071** CriticGPT / LLM Critics Help Catch LLM Bugs (McAleese et al. 2024) · **S-072** LLMs
Cannot Self-Correct Reasoning Yet (Huang et al., ICLR 2024) · **S-073** MARG multi-agent review generation (D'Arcy et
al. 2024) · **S-074** Towards Understanding Sycophancy (Sharma et al., Anthropic 2023) · **S-075** The AI Scientist /
automated reviewer (Lu et al. 2024, Nature 2026) · **S-076** Building Effective Agents (Anthropic 2024).
Existing, load-bearing here: **S-004** Co-Scientist (Reflection + Meta-review + tool-grounded reflection + scientific
debate) · **S-003** Robin · **S-002** ERA · **S-008** MT-Bench (self-enhancement / 2-brain) · **S-042** Mixture-of-
Agents · **S-043/S-044** multi-agent debate factuality / divergent thinking · **S-069** debate-gains-fragile caution ·
**S-045** Lost-in-the-Middle (front-load) · **S-051/S-052** CoVe / SelfCheckGPT · **S-014** operator findings E/F/G ·
**S-017** PoLL · **S-018** ChatEval · **S-020** Prometheus · **S-023** context engineering · **S-006/S-062/S-063**
idea-novelty & ideation-execution gap.
