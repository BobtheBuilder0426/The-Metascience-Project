# the Metascience Project scoring harness — the runnable core of the quantification

Implements `rubric.json` + `creativity-metric.md` as real code. Scores answers on the 5-dimension rubric
(grounding & integrity / reasoning & soundness / completeness / usefulness / creativity — rubric v2, LB-075, equal 0.20), with citation-verification, entity-specificity,
the multiplicative creativity gate, an LLM-judge panel, and an Elo tournament. Built 2026-07-09 (LB-020); migrated to rubric v2 + long scorecard + grounding-integrity 2026-07-10 (LB-077).

## Design in one line
A **pure scoring core** (`scoring/`) + a **dependency-injected adapters layer** (`adapters.py`) so the exact same
code runs **offline (dry-run, deterministic)** and **against live `host.llm` + `host.mcp`** in a Claude Science session.

## Layout
```
scoring/            pure, no network, no host.*
  extract.py         citations (PMID/DOI/author-year) + checkable entities (genes/assays/quant/pathways/drugs)
  novelty.py         retrieval-frequency (primary) + semantic-distance (flagged) novelty
  citations.py       2-stage citation verification (existence + support) -> Grounding cap
  citation_quality.py  citation QUALITY: venue quality, primary-vs-review ratio, retraction count, usage (CS's job, LB-029.5)
  judge.py           3-PERSONA reviewer jury (R1 Rigor / R2 Significance / R3 Novelty) filling the rubric, G-Eval style,
                     + creativity panel (plausibility + reasoning-trace). Claude-only personas (reviewer-panel-design.md).
  trace_verify.py    verifies a run bundle's process_trace.json step-by-step -> the CS verified/unverified badges (LB-029.4)
  composite.py       weighted composite + multiplicative creativity index
  elo.py             drift-robust pairwise tournament
adapters.py         DryRunAdapters (offline stubs) + RealAdapters(host, reasoning_model)
run_scoring.py      orchestrator + CLI
test_dryrun.py      12 offline asserts (anti-hallucination + ranking behaviours)
answers.example.json  fixture (baseline vs loop, incl. a fabricated-citation trap)
rubric.json         copy of the canonical loop-design/current/rubric.json
```

## Dry-run (offline, no network) — this is the verification
```
python test_dryrun.py                 # 12/12 asserts, exit 0
python run_scoring.py --dry-run --answers answers.example.json --rubric rubric.json --out out/
```
The dry-run proves the machinery (`test_dryrun.py`, 13/13 asserts): the fabricated-citation trap answer gets grounding
driven to 1 and lands with the **lowest composite of all answers** and **last in the Elo ranking**, below the weak
baselines. Fixture composites: baseline B = 2.06; the two good, cited, reasoned loop answers = 3.37 / 3.32; the trap =
1.81. So the **two good answers beat baseline by Δ +1.28**, while the **whole Arm-L mean (including the trap) is +0.77**
above baseline — the gap between those two numbers is exactly the harness doing its job (the trap drags the arm mean
down). The harness reports the arm-level delta (+0.77); the good-vs-baseline gap (+1.28) is the per-answer view.

## Real mode (inside a CS session, where `host` is available)
Real mode is NOT run from the CLI (it needs `host`). Import and inject:
```python
# In a CS analysis kernel (host.llm) — connector calls go through the repl bridge (host.mcp).
from adapters import RealAdapters  # RealAdapters(host, reasoning_model=host.reasoning_model())
from run_scoring import run_experiment
adapters = RealAdapters(host, reasoning_model=host.reasoning_model())
out = run_experiment(manifest, adapters, "rubric.json", "out/")
```
- **Reviewer panel** = 3 Claude personas via `host.llm` (R1 Rigor / R2 Significance / R3 Novelty; system prompts in
  `judge.py` → `REVIEWER_PERSONAS`), each blinded + rubric-conditioned + G-Eval form-filling. CS's side is **Claude-only**
  by design (host.list_models); there is NO non-Claude judge here — the multi-model + Codex lenses belong to the CC/CS
  loop-UNDER-TEST, a separate improvement category (see `loop-design/current/reviewer-panel-design.md`).
- **Self-enhancement bias** (Claude judging Claude) is **measured** vs the the operator human anchor, not removed by a cross-vendor
  judge — reported honestly.
- **Connectors** = `host.mcp("pubmed", ...)` / OpenAlex for novelty, citation resolution, and citation-quality metadata.
- **Connectors** = `host.mcp("pubmed", ...)` / OpenAlex for novelty + citation resolution.

## Real-mode caveat learned in the smoke test (LB-020) — READ THIS
A citation **existence** check is not sufficient: in the live smoke test, PubMed's `get_article_metadata(["00000001"])`
returned a **non-empty** article record (count = 1) rather than nothing — i.e. a fabricated or mistyped low-value PMID
can still resolve to *an* article. The guard that actually protects
Grounding is the **entailment stage** — does the *cited abstract* support the *specific claim*? `RealAdapters.resolver_fn`
returns title+abstract precisely so `entailment_fn` (an `host.llm` check) and a human auditor can catch
misattributed-but-real citations. Never treat "reference exists" as "claim supported".

## What each dimension leans on
- **Grounding** = min(judge score, citation-verification cap). No citations → cap 2; fabricated → cap 1.
- **Completeness** = mean(judge, entity-specificity signal).
- **Creativity** = the multiplicative gate `novelty × plausibility × reasoning-trace` (overrides the judges'
  free-text creativity), so a novel-but-unreasoned answer cannot score creative (the anti-hallucination requirement).
- **Reasoning / Usefulness** = judge panel means (G-Eval form-filling), cross-checked by Elo + the operator.
