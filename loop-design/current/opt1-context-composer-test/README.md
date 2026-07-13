# OPT-1 context-composer — offline subagent A/B test

**Purpose.** Verify (before shipping in v8) that the per-question context the `context-composer` skill produces
actually *sharpens* CS output, and that it leaks no task content (fairness firewall). Operator-requested subagent test.

## Method
- 2 self-contained locked questions (Q2 origin-of-life hypothesis; Q3 exercise-mimetic compound). Q_ERGO is
  excluded here because it depends on its attached PDFs, which are not reachable in an offline `host.llm` sandbox —
  Q_ERGO is validated in the real loop instead.
- **Isolated variable = the performance block.** Baseline arm system prompt = "You are a scientist. Answer the
  question." Composed arm = "You are a scientist." + the composer's performance block (dose=auto). The safety
  preamble is constant across the two real arms, so it is held out of this comparison (it is not the variable).
- An identical offline note is appended to BOTH arms (tools unreachable → answer from knowledge, name what you'd
  verify) so the tool-seeking behavior the context correctly induces resolves to text rather than a stalled
  tool-call. Not a confound (identical to both).
- Answers generated with the kernel utility model for cross-arm consistency; blind judge (reasoning model) scores
  each answer 0–1 on the 5 rubric dimensions, answers shuffled + arm-hidden.

## Result (n=2, directional — not powered)
Composed context scored **higher on all 5 dimensions**; overall +0.060.

| dimension | baseline | composed | Δ |
|---|---|---|---|
| grounding | 0.350 | 0.435 | **+0.085** |
| reasoning | 0.535 | 0.585 | +0.050 |
| completeness | 0.540 | 0.565 | +0.025 |
| usefulness | 0.350 | 0.425 | +0.075 |
| creativity | 0.485 | 0.550 | +0.065 |
| **overall** | **0.452** | **0.512** | **+0.060** |

Largest gains — grounding and usefulness — are exactly the dimensions the citation-discipline + capability-activation
+ completeness blocks target, i.e. the effect lands where the research predicted.

## Fairness
The firewall (question-content-overlap) was run at **composition time on all three locked questions' composed
contexts — Q_ERGO, Q2, Q3 — and returned [] (clean) for each** (Q_ERGO is firewall-checked even though it is excluded
from the A/B answer-generation/judging below, which used only the two self-contained questions). A negative-control
injected leak ("ergothioneine…") was caught. No distinctive question content-word appears in any performance block.

## Honest limitations
- n=2 offline; a directional signal, not proof. The real test is the in-loop 3-way comparison (baseline / v7 / v8)
  on all 3 questions with CS's real tools.
- A single judge model here; the full harness uses the 3-persona panel + citation agent.
- Offline note suppresses the strongest observed effect (the composed context drives CS to pull primary literature
  and refuse to confabulate) — so this understates grounding gains relative to the real, tool-enabled loop.

## Files
- `README.md` — this file. `results.png` — the two-panel figure.
- `answers.json` — the 4 raw answers. `scores_blind.json` — blind judge scores + code→arm map. `summary.json` — deltas.
