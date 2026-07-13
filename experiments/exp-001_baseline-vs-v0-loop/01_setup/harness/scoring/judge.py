"""judge.py — the CS scoring panel (quantification.md §3, reviewer-panel-design.md).

CS's RULER for measuring answer quality. A JURY of reviewer PERSONAS (Verga 2024 PoLL:
a panel beats a single judge; Chan 2023 ChatEval: distinct reviewer ROLES track humans
better). All personas run on Claude (host.list_models = Claude-only on CS's side — there
is NO non-Claude judge here; that lives inside the CC/CS loop-under-test, a separate
improvement category, NOT this ruler). Diversity = persona system-prompt + sampling.
Each persona is G-Eval form-filling (S-007), rubric-CONDITIONED (Prometheus/Kim 2023),
blinded. Self-enhancement bias (Claude judging Claude) is MEASURED vs the the operator human
anchor, not removed by cross-vendor (stated honestly).

`judge_fn` is ONE injected callable: judge_fn(prompt, system) -> str (or {"text":..}).
The panel loops the 3 personas, passing each persona's system prompt. Dry-run injects a
deterministic stub; real mode wraps host.llm.
"""
import json
import statistics as stats

RUBRIC_DIMS = ["grounding", "reasoning", "completeness", "usefulness", "creativity"]

# ── The 3 reviewer personas (accepted LB-034; dims -> rubric v2, LB-075). Same anchored rubric, different scrutiny. ──
_FORM = (
    "Fill the form: for EACH dimension give an integer 1-5 and a one-sentence justification "
    "quoting evidence from the answer. CALIBRATE HARD and USE THE FULL 1-5 RANGE: 3 = a competent, "
    "typical answer (this is your DEFAULT starting point); award 4 only for genuinely strong work and "
    "5 ONLY for the rare, exceptional case; 2 = weak, 1 = poor. Do NOT cluster at 4-5 — if two answers "
    "differ in quality, their scores MUST differ. Anchor every score to the substance, not to politeness. "
    "Dimensions: grounding (are claims, sources, datasets & claimed actions real "
    "and verified — nothing fabricated); reasoning (is the chain of thought sound, clear and "
    "elegant, alternatives weighed — and WHERE a test/method is proposed, is it valid; if the "
    "question asks only for a hypothesis/argument, score reasoning quality and do NOT penalise the "
    "absence of a proposed experiment); completeness; usefulness; creativity. Output STRICT JSON "
    "only with keys: grounding, grounding_reason, reasoning, reasoning_reason, completeness, "
    "completeness_reason, usefulness, usefulness_reason, creativity, creativity_reason. Use "
    "non-angle delimiters."
)
REVIEWER_PERSONAS = [
    {"id": "R1_rigor", "label": "Rigor / Methods reviewer",
     "system": ("You are a demanding JOURNAL METHODS REFEREE reviewing ONE answer to a research "
                "question, blinded. You scrutinize whether the science is SOUND and not overstated, "
                "whether the chain of thought is valid, elegant and free of errors, whether — WHERE a "
                "test/method is proposed — it is valid and FALSIFIABLE (but if the question asks only "
                "for a hypothesis or argument, judge the reasoning, not a missing experiment), and "
                "whether claims are properly grounded. You are hard to impress on reasoning + grounding; "
                "most answers are a 3 — award 4-5 only when the work earns it. " + _FORM)},
    {"id": "R2_significance", "label": "Significance / Impact reviewer",
     "system": ("You are a TOP-VENUE 'SO WHAT?' REFEREE reviewing ONE answer, blinded. You scrutinize "
                "whether this MATTERS to the field, whether it is COMPLETE (mechanism + prediction + "
                "the requested experiment/protocol), and whether it is USEFUL + actionable for a "
                "wet-lab scientist. You reward substance, penalize padding; most answers are a 3 — "
                "award 4-5 only when the work earns it. " + _FORM)},
    {"id": "R3_novelty", "label": "Novelty / Creativity reviewer",
     "system": ("You are a HACKATHON JUDGE + research-idea rater reviewing ONE answer, blinded. You "
                "scrutinize whether the core idea is GENUINELY NOVEL and non-obvious versus what the "
                "field already knows, and whether novelty is backed by a legible reasoning chain (not "
                "hollow). You reward creative, well-reasoned leaps; you flag confident hand-waving; "
                "most answers are a 3 — award 4-5 only when the work earns it. " + _FORM)},
]

_CREATIVITY_SYSTEM = (
    "You are a rigorous aging-biology reviewer. Assess ONE hypothesis on TWO axes, each "
    "1-5. plausibility = consistent with established biology, no wrong-direction/dose/"
    "contraindication errors. reasoning_trace = is there a CLEAR legible chain of thought "
    "from established facts to the novel claim that an expert can follow and CHECK "
    "(5=explicit premises->mechanism->falsifiable prediction with a distinguishing control; "
    "1=bare assertion with no derivable reasoning = hallucination signature). You MUST quote "
    "the reasoning chain you found, or state you could not find one. Output STRICT JSON only: "
    "plausibility, plausibility_reason, reasoning_trace, reasoning_trace_reason, "
    "reasoning_chain_quote, redflags (list). Use non-angle delimiters."
)


def _parse_json(text: str) -> dict:
    import re
    m = re.search(r"\{.*\}", text, re.S)
    if not m:
        return {"_parse_error": text[:200]}
    try:
        return json.loads(m.group(0))
    except Exception as e:
        return {"_parse_error": f"{e}", "_raw": text[:200]}


def _as_text(raw):
    return raw if isinstance(raw, str) else raw.get("text", "")


def run_rubric_panel(answer_text: str, question: str, judge_fn, personas=None) -> dict:
    """A jury of reviewer personas fills the 5-dim rubric. `judge_fn(prompt, system)->str`.
    Loops the personas, one system prompt each. Returns per-persona + aggregate + disagreement."""
    personas = personas or REVIEWER_PERSONAS
    prompt = f"RESEARCH QUESTION:\n{question}\n\nANSWER TO SCORE:\n{answer_text}"
    per_reviewer = []
    for p in personas:
        parsed = _parse_json(_as_text(judge_fn(prompt, p["system"])))
        parsed["_persona"] = p["id"]
        per_reviewer.append(parsed)
    agg, disagree = {}, {}
    for d in RUBRIC_DIMS:
        vals = [r[d] for r in per_reviewer if isinstance(r.get(d), (int, float))]
        agg[d] = round(stats.mean(vals), 3) if vals else None
        if len(vals) >= 2:
            pairs = [abs(a - b) for i, a in enumerate(vals) for b in vals[i+1:]]
            disagree[d] = round(sum(pairs) / len(pairs), 3)
    return {"per_judge": per_reviewer, "aggregate": agg, "inter_judge_absdiff": disagree,
            "n_judges": len(personas), "personas": [p["id"] for p in personas]}


def run_creativity_panel(hypothesis_text: str, judge_fn, n_raters=2) -> dict:
    """Score plausibility + reasoning-trace (the two creativity gates). `judge_fn(prompt, system)->str`.
    Runs n_raters times (sampling diversity) and aggregates."""
    prompt = f"HYPOTHESIS:\n{hypothesis_text}"
    per_judge = []
    for _ in range(max(1, n_raters)):
        parsed = _parse_json(_as_text(judge_fn(prompt, _CREATIVITY_SYSTEM)))
        per_judge.append(parsed)
    def _agg(key):
        vals = [p[key] for p in per_judge if isinstance(p.get(key), (int, float))]
        return round(stats.mean(vals), 3) if vals else None
    redflags, chains = [], []
    for p in per_judge:
        if isinstance(p.get("redflags"), list):
            redflags.extend(p["redflags"])
        if p.get("reasoning_chain_quote"):
            chains.append(p["reasoning_chain_quote"])
    return {"per_judge": per_judge, "plausibility": _agg("plausibility"),
            "reasoning_trace": _agg("reasoning_trace"), "redflags": redflags,
            "reasoning_chain_quotes": chains, "n_judges": len(per_judge)}
