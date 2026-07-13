# Multi-model literature-synthesis context module (SPEC) — DEFERRED / shelved
**Status:** prepared, NOT in the v6 tested bootstrap (operator decision LB-052). Add as a measured improvement after the
first clean loop run. **Author:** Claude Science · **Date:** 2026-07-10 · **Grounding:** cutting-edge lit pass
S-038..S-053 (all DOIs verified, 0 retracted), plus S-034..S-037.

## Purpose
Before the driver runs the loop, give it a **concise, grounded, high-quality background brief** on the question's topic,
built by two different models and fused. The goal is a real head-start in domain understanding — but the brief only
helps if it is **current, high-quality, citation-grounded, and short**. A brief full of stale, low-quality, same-idea
papers would make the driver anchor on tired hypotheses (the operator's stated failure mode) — and the recent evidence
says a bad brief is not neutral but actively harmful (distractor context measurably degrades a downstream model, S-046).
So this SPEC is dominated by three design forces the literature identifies: **source quality/novelty selection**,
**faithful multi-model synthesis**, and **concision + ordering for the consuming agent**.

## State of the art this design builds on (why these choices)
- **Retrieval-augmented literature synthesis is now the established shape**, up to Nature-2026-level results
  (S-038) and agents that reach citation accuracy above human baselines (PaperQA2, S-039). We follow that shape:
  retrieve real sources first, synthesize second, cite + verify throughout — never synthesize from model memory.
- **Automated survey generation** has a proven pipeline (AutoSurvey, S-040): retrieve → outline → draft sections in
  parallel → iterative refinement. We adopt the staged structure rather than a single monolithic prompt.
- **Multi-model aggregation genuinely helps** when structured as proposers → aggregator (Mixture-of-Agents, S-042), and
  **multi-agent debate raises factuality** (S-043) — but only if disagreement is surfaced, not collapsed
  (divergent-thinking / anti-"degeneration-of-thought", S-044). This justifies the two-model-pass + synthesis design AND
  the hard rule to flag disagreement instead of averaging it away.
- **Long, middle-heavy context is under-used by models** (Lost-in-the-Middle, S-045) and **distractor passages degrade
  generation** (Power of Noise, S-046). Both push the same way: the brief must be **short and front-loaded**, and source
  filtering (precision) matters more than recall. This is the quantitative backbone of the operator's "no stale consensus
  dump" requirement.
- **Novelty is measurable**, so source selection need not rely on gut feel: the CD/disruption index (S-047, with its
  citation-inflation caveat S-048) and atypical/surprising-combination impact (S-049) give real signals to prefer
  disruptive/novel work over consolidating consensus.
- **Grounding is enforceable**: local span-level attribution while generating (Attribute First, S-050), Chain-of-
  Verification self-checking (S-051), SelfCheckGPT consistency detection (S-052), and interleaved retrieve-while-reason
  (IRCoT, S-053) are concrete, cited mechanisms — the module uses them rather than a vague "cite your sources."

## Where it sits in the flow (when activated)
Bootstrap INTAKE (after question + PDF digests) → **build context brief** → save to `driver/context/topic_brief.md` →
driver reads it alongside the digests. Modular + optional: if it fails or is disabled, the handoff still completes and
the driver still runs (additive context, never a dependency).

## Pipeline (5 stages)
### 1. Iterative, quality-first retrieval (the decisive stage)
Seed from the question + input digests; retrieve from real connectors (PubMed/OpenAlex/web). Do it **IRCoT-style** (S-053):
retrieve, read, identify what's still missing, retrieve again — not one-shot. Then **rank/filter for precision**, because
distractors hurt (S-046):
- **Recency-weighted** — bias to the last ~3–5 years; forward-citation-walk from the seed papers so the newest
  extending/contesting work is included (current front, not founding consensus).
- **Novelty-aware** — use the disruption/CD index (S-047, corrected for citation-inflation bias S-048) and
  atypical-combination signal (S-049) to PREFER disruptive/novel work and DEMOTE pure consolidation. This is the
  quantitative answer to "not shitty old papers all claiming the same idea."
- **Primary + high-signal venues** over review-of-reviews and low-signal journals; citation velocity + venue are signals,
  never the sole filter (a naive most-cited sort surfaces stale generic papers — demonstrated in the worked example).
- **Diversity / contrarian inclusion** — keep well-supported minority findings; the set must represent real disagreement.
- **Retraction screen** — drop retracted/heavily-corrected papers (verify_dois-style).
- Output: a ranked source set (~15–30) with {DOI, title, year, venue, novelty-signal, why-included}, shared by both
  model passes so they reason over identical evidence.

### 2. Two independent model passes (Mixture-of-Agents "proposers", S-042)
Claude and Codex (or whatever models the user has) EACH draft a grounded background from the SAME ranked set, using
**local attribution while generating** (S-050) — every claim tied to a specific source as it is written, not cited
post-hoc. Neither sees the other's draft (independence preserves the diversity that makes aggregation work, S-042/S-043).
If only one model is available, degrade to a single grounded pass (still valid).

### 3. Synthesis / aggregation → ONE concise report (AutoSurvey-staged, S-040; MoA aggregator, S-042)
Fuse the two drafts into a single **≤3–4 page** `topic_brief.md`:
- keep only claims backed by a real source in the set;
- where the two passes **disagree, surface it explicitly** as an open question (S-044) — never average into false
  consensus (that is exactly the failure MAD warns against);
- **front-load** the most decision-relevant content and keep it short (Lost-in-the-Middle, S-045): structure =
  *what's established · what's actively contested/emerging · what's NOT known (gaps) · highest-quality primary sources to
  build on*, then the source list.

### 4. Verify (Chain-of-Verification + SelfCheckGPT, S-051/S-052)
Before shipping: generate verification questions for the brief's key claims and answer them against the sources (CoVe,
S-051); run a sample-consistency hallucination check (SelfCheckGPT, S-052); confirm every DOI resolves and none are
retracted. Any claim that fails is cut or downgraded to "reported by X, unverified."

### 5. Fairness bookkeeping (mandatory)
The brief is a loop-only advantage the baseline never receives. Legitimate, but **documented as part of the loop
method**: record in the run bundle that a multi-model brief was provided and from which sources, so any later "loop beat
baseline" claim honestly accounts for the self-briefing. Store brief + source list in the bundle.

## Quality bar (operator's requirement, made testable)
A shippable brief is: **recent** (low median source age), **novel/primary-leaning** (high primary:review ratio; positive
mean disruption signal; includes atypical-combination work), **diverse** (contains flagged disagreement), **grounded**
(100% of claims locally attributed + every DOI resolves + 0 retracted + passes CoVe/SelfCheck), and **concise** (≤4
pages, front-loaded). A brief that is old-consensus-heavy, review-heavy, contains any unresolvable/retracted citation, or
exceeds the length cap FAILS and is not shipped to the driver.

## Why deferred
Prove one clean end-to-end loop first (operator LB-052); then add this as an improvement category and measure
driver-with-brief vs driver-without against the fixed baseline (the disruption/novelty metrics above double as the
outcome instrumentation). Building it now (spec + worked example) means it is ready to switch on the moment the first run
succeeds.

## Activation checklist (when switching it on later)
- [ ] Enable the module; add the "build context brief" call to bootstrap INTAKE.
- [ ] Confirm ≥1 non-Claude model available at pre-flight (Codex found), else run single-model grounded mode.
- [ ] Enforce the quality-bar gate (recency + novelty signal + primary ratio + attribution + CoVe/SelfCheck + length)
      before the brief is written to driver/context/.
- [ ] Add the fairness note + source list to the run bundle.
