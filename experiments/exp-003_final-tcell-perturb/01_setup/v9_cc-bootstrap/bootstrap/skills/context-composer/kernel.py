"""
context-composer kernel helper — assembles a per-question CS project Agent Context from a FROZEN,
fairness-checked block library. The blank CC sets general task-shape FLAGS (never domain content); this
code selects + orders the blocks and runs a fairness firewall. The domain/answer never enters the context.

Loaded automatically when the context-composer skill is loaded. Entry point: compose_context(...).
"""
import json, re, os

_HERE = os.path.dirname(os.path.abspath(__file__))

def _load_blocks(path=None):
    with open(path or os.path.join(_HERE, "blocks.json"), encoding="utf-8") as f:
        return json.load(f)

# ---- Fairness firewall -------------------------------------------------------
# PRIMARY guarantee = the block library is frozen + pre-checked general text. This firewall is the
# TRIPWIRE for the two ways WAS could still leak into the context: (a) a future hand-edit adds task
# content to a block, (b) the composer is misused to inject question text. The precise test is
# QUESTION-CONTENT-OVERLAP: no distinctive content-word from THIS question may appear in the performance
# block. A regex can't tell "seek a hypothesis" (general, fine) from "the hypothesis is X" (leak), so we
# key off the actual question instead. Only the PERFORMANCE block is scanned; the frozen safety preamble
# (incl. its benign example project names) is exempt by design.

# Function words + GENERAL science-methodology vocabulary that legitimately appears in both questions and
# the general blocks. A token in this set never counts as a leak (it isn't distinctive to any one question).
_STOP = set("""
a an the of to in on for from with without into onto by at as is are was were be been being this that these those
and or not but if then so than about over under between across your you it its their there here new newly
starting come up how what why which who when where whom whose do does did done make made get gets got
provided publications publication paper papers study studies dataset datasets data publicly available
hypothesis hypotheses rationale idea ideas novel plausible propose proposal proposed generate generating
question questions task tasks experiment experiments protocol protocols test tests testing predict prediction
analyse analyze analysis method methods approach approaches result results evidence source sources citation
citations reasoning mechanism mechanistic reasonable reasonably first pilot design designs step steps
increase increases increasing decrease acts act against age related treat treatment treating patients patient
""".split())

def _content_tokens(question):
    """Distinctive lowercase content-words from the question (len>=4, minus the general stoplist)."""
    toks = re.findall(r"[A-Za-z][A-Za-z\-]{3,}", (question or "").lower())
    return sorted({t for t in toks if t not in _STOP})

def firewall_scan(performance_block, question):
    """Return list of leaked content-words: distinctive question tokens that appear in the performance
    block. Clean composition => []. Any hit is a real signal to review the offending block/identity text."""
    if not performance_block:
        return []
    hay = performance_block.lower()
    hits = []
    for tok in _content_tokens(question):
        # word-boundary match so 'cell' doesn't hit 'excellent'
        if re.search(r"\b" + re.escape(tok) + r"\b", hay):
            hits.append(tok)
    return hits

# ---- Task-shape flags (GENERAL signals only — the blank CC sets these) -------
FLAG_KEYS = ["supplies_inputs", "involves_data", "asks_experiment",
             "asks_hypothesis", "asks_novelty", "asks_prediction"]

def compose_context(preamble_body, identity_line, flags, question="", dose="auto", blocks=None):
    """
    preamble_body : str  — the v7 safety preamble body, VERBATIM (guardrails intact).
    identity_line : str  — the run-identity text for the INSERT HERE slot (project + granted folder).
    flags         : dict — general task-shape booleans (subset of FLAG_KEYS); domain content NEVER here.
    question      : str  — the actual question text, used ONLY by the fairness firewall to check that no
                           distinctive question content-word leaked into the performance block. It is NEVER
                           written into the context.
    dose          : 'safety_only' | 'lean' | 'full' | 'auto'  (auto = full backbone + triggered conditionals)
    Returns dict: {context, sections_used, dose, performance_block, firewall_hits}.
    """
    B = blocks or _load_blocks()
    flags = {k: bool(flags.get(k, False)) for k in FLAG_KEYS}

    # 1) safety preamble, verbatim, with identity slot filled.
    # The slot spans from the opening bracket to the closing one, ACROSS the multi-line "e.g." example —
    # match the whole span at once so no example fragment or stray bracket survives.
    pre = re.sub(r"\u27e8INSERT HERE.*?\u27e9", identity_line.strip(), preamble_body, flags=re.S)
    if "INSERT HERE" in pre:  # ascii-bracket fallback (if the preamble ever uses < >)
        pre = re.sub(r"<INSERT HERE.*?>", identity_line.strip(), pre, flags=re.S)

    if dose == "safety_only":
        return {"context": pre, "sections_used": [], "dose": dose,
                "performance_block": "", "firewall_hits": []}

    # 2) always-on backbone + triggered conditionals (order = library order = evidence-priority order)
    order = ["capability_activation","citation_discipline","reasoning_transparency",
             "completeness","honest_uncertainty","anchored_self_critique","novelty_paired",
             "pilot_design"]
    used, perf = [], []
    for key in order:
        blk = B[key]
        if blk["mode"] == "always":
            if dose in ("lean","full","auto"):
                perf.append(blk["text"]); used.append(key)
        else:  # conditional
            triggered = any(flags.get(t) for t in blk.get("triggers", []))
            if dose == "full" or (dose == "auto" and triggered):
                perf.append(blk["text"]); used.append(key)
            # lean never includes conditionals

    perf_block = "\n\n".join(perf)
    ctx = pre + "\n\n---\n\n# Performance scaffolding (how to do strong scientific work in this project)\n\n" + perf_block + "\n"
    return {"context": ctx, "sections_used": used, "dose": dose,
            "performance_block": perf_block, "firewall_hits": firewall_scan(perf_block, question)}

def classify_flags_help():
    """Human-facing: how the blank CC decides each flag from the QUESTION SHAPE (not its content)."""
    return {
        "supplies_inputs": "Did the human attach papers/files with the question? (yes/no) — general, not what they are about.",
        "involves_data":   "Does the task involve datasets / quantitative analysis / computation? (structural, not which data)",
        "asks_experiment": "Does the task ask for an experiment / protocol / test to be designed?",
        "asks_hypothesis": "Does the task ask for a hypothesis / explanation / rationale?",
        "asks_novelty":    "Does the task ask for something new / not-yet-proposed / a novel idea?",
        "asks_prediction": "Does the task ask to predict / propose a candidate (compound, target, outcome)?",
    }
