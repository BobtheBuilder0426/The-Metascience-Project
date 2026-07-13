<!-- WHAT THIS FILE IS: the operator's prior-experience findings (A-G) on running a Claude-Code-driven Claude-Science
     loop, captured verbatim-in-substance + CS's design response to each. This is FOUNDATIONAL input for the v0 Agentic
     Loop and every iteration after. HOW TO USE: read before authoring/adjusting any loop version. These are strong
     priors from real prior runs — treat A/B/C/G as near-constraints and D/E/F as validated-but-improvable insights to
     TEST, not gospel (operator: "MUCH more to discover and improve — that is your task"). Source: S-014. -->

# Operator prior-experience input — findings A–G  [operator → CS] — 2026-07-09  (captured LB-019)

The operator ran CC-drives-CS loops before and handed over seven findings. Each below: **the finding**, then
**CS design response** (how the v0 loop + harness encode or test it). These reshape the Agentic Loop from a single
"CC drives CS" session into a **Mission-Control orchestrator** architecture.

## A. Context window is the binding constraint → Mission-Control architecture  [CENTRAL FLAG]
**Finding.** Even with 1M context, a single CC driver running the whole loop (constantly polling CS + spawning
reviewer/panel subagents) runs out of context. What worked: the **start CC session splits the task into substeps and
becomes "Mission Control"**; it instructs a **fresh CC session** to run the CS loop on substep 1 until the result is
good, that session **reports back**, Mission Control launches the **next substep session**, and at the end Mission
Control hands everything to CS to **integrate the substeps into one result**. Human can relay start-prompts/reports
between sessions, but **an automated relay would be much better**. Keep total `claude -p` budget in mind.
**CS response.** The v0 loop is **hierarchical (orchestrator–worker)**, not flat:
`Mission-Control CC (persistent, lightweight: holds plan + budget + integration)` → `substep worker CC sessions (fresh
context each, one substep, drive a CS session)` → report → next → `final integration by a CS session`. This is exactly
the **Co-Scientist Supervisor+worker pattern (S-004)** and the harness survey's **Meta-Harness/context-isolation**
(S-005). Automated relay: a thin file/queue hand-off between sessions (Mission Control writes `substep-N.task`, worker
writes `substep-N.result`), so the human is optional. **Context budget per session is now a first-class design metric.**

## B. Polling cadence: check CS far less often  [CENTRAL FLAG]
**Finding.** Subagents polled CS ~every minute; runs take longer, so **~5 min was much better** (saved context). Best:
**grant all needed permissions ONCE at the start (whole project) and then check ~every 10 min.**
**CS response.** Encoded into the loop's watchdog: **poll interval ≥5 min (default 10)**, not a busy-wait; and a
**pre-flight permission grant for the whole project** (CS scopes: code=Always, connectors=per-project, compute=all-jobs)
so residual permission cards are rare. This also directly cuts the context bleed from A. Poll cadence is a tunable
parameter in the loop config (an improvement axis).

## C. Multi-session-in-one-project data exchange  [CENTRAL FLAG — open question]
**Finding.** With the Mission-Control/substep approach, the substep CS sessions should live in the **same NEW CS
project** (a fresh project per Agentic-Loop build we try), and we **need to work out how different CS sessions in one
project share data/knowledge**.
**CS response.** CS sessions in one project **already share the artifact store + project memory + `host.query`
metadata** (this is how the current session reads prior sessions' artifacts). So the substep sessions coordinate by:
(i) **artifacts** (each substep saves its result as an artifact; the next reads it via `host.artifacts`/`{{artifact:}}`),
(ii) **project memory/notes** for lightweight state, (iii) a **shared handoff manifest** artifact Mission Control owns.
→ TODO: verify cross-session artifact visibility + memory in a fresh project during the harness dry-run. One new CS
project per loop-build keeps experiments clean (matches D1 §3 "no drift").

## D. Cheap improvement: a review loop AFTER THE PLAN (inject creativity/ambition early)  [INSIGHT — test]
**Finding.** A loop **after the plan** and **after the results** helps; **especially after the plan** you can inject
creativity + ambition — **much cheaper than re-running the whole results several times.**
**CS response.** The loop has **two review gates**: **(1) plan-stage** (before expensive work — inject
creativity/ambition here; cheapest leverage) and **(2) results-stage** (correctness + polish). Plan-stage review is the
default-on, high-ROI gate; results-stage repeats are budget-gated. This is an explicit, testable loop parameter (how
many passes at each gate).

## E. The review/feedback panel: correctness-checker FIRST, then a 2-lens × 2-brain panel  [INSIGHT — test]
**Finding.** First a **detailed, obsessive correctness checker**: verify every quote, every dataset mentioned, that the
code exists and is correct — pure anti-hallucination safety checking, everything corrected. **Then** a multi-lens panel
spawned with **identical instructions on two "brains" — Opus 4.8 AND (via Codex) GPT-5.5**. Two lenses that worked:
- **Young ambitious postdoc** — dreams big, adds the one thing that makes it a big Nature paper, pushes boundaries.
- **Experienced mentoring PI** — keeps methodology reliable/established/lean, knows what convinces a reviewer, focuses
  on controls/evidence/reasoning, makes the story bulletproof, trims over-engineering toward elegant + reliable.
The **productive tension** between lenses is the point. Karpathy's LLM-council inspired it; a **comparator + chairman
synthesis** step follows — **but must be done well.**
**CS response.** This is the loop's internal **improvement engine** and a prime improvement category. Ordering is
**gate-first**: correctness/anti-hallucination checker (reuses the harness's citation-verification + code/dataset
existence checks) runs BEFORE the creative panel, so we never polish a hallucination. Then the **2×2 panel**
(postdoc/PI × Claude/Codex) → **comparator** (surface the productive disagreements) → **chairman** (synthesise, decide).
Two brains blunt self-enhancement bias (S-008), matching the quantification judge-panel design. "Must be done well" →
the panel prompts + comparator/chairman are themselves things we iterate + measure.

## F. KEEP WHAT IS GOOD (anti-drift, anti-over-engineering)  [CENTRAL PRINCIPLE]
**Finding.** The loop must **first protect what already looks solid and works** — don't destroy a good result, don't
drift into hallucination or over-engineering. **Always: what is good and why, FIRST. Then what can be improved, with
evidence + reasoning.**
**CS response.** Every review gate opens with a mandatory **"KEEP" pass**: name what is good and why, and mark it
protected, **before** any "IMPROVE" suggestion — and every IMPROVE must carry **evidence + reasoning** (no vibe edits).
This becomes a hard rule in the panel/chairman prompts and a scored behaviour (did the loop preserve prior strengths?).
It also guards the metric itself against the over-engineering failure mode.

## G. Give every CC session + subagent WEB + LITERATURE access (and enforce citations)  [CENTRAL FLAG]
**Finding.** All CC sessions/subagents did **much better with web + literature access** than relying on training
knowledge; **enforcing citations / chain-of-thought lowered hallucination.**
**CS response.** Mandatory in the loop: the driven CS session exploits the **full featured-connector suite** (PubMed,
OpenAlex, Ensembl, Open Targets, …) and **every claim must carry a verifiable citation** (enforced by the harness's
citation-verification, which caps Grounding). This ties finding G to the quantification metric and to the
creativity-metric's reasoning-trace gate — citations + explicit chain-of-thought are exactly what those score.

---
## Net effect on the design (what changes vs the pre-input D1)
1. **Agentic Loop = Mission-Control orchestrator** (persistent MC + fresh substep workers + CS integration), not one flat CC. (A, C)
2. **Two review gates** — plan-stage (creativity injection, cheap) + results-stage (correctness, budget-gated). (D)
3. **Internal improvement engine = correctness-checker → 2-lens×2-brain panel → comparator → chairman**, KEEP-first. (E, F)
4. **Cadence + permissions** — poll ≥5 min (default 10), one project-wide permission grant up front. (B)
5. **Literature-grounded + citation-enforced** everywhere. (G)
6. **`claude -p` budget** is a first-class constraint tracked per session. (A)

The improvement-category search space in `experiment-loop-design.md §7` is updated to match (these become the axes we
actually test). **These are strong priors to validate + improve, not settled truth** (operator's explicit framing).
