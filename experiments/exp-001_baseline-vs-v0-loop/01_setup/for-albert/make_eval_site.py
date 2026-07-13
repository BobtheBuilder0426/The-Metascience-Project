#!/usr/bin/env python3
"""the Metascience Project — blinded evaluation-site generator (v2).  [CS-authored]

Turns a run's answers into ONE self-contained, offline HTML file that the operator opens to
evaluate blinded, plus a SEPARATE blinding_key.json that the operator never opens.

WHAT OPERATOR SCORES (science only — citations are CS's job, not the operator's):
  per answer: reasoning, completeness, usefulness, creativity (1-5, anchored)
              (process_trace is NOT shown here — CS scores it; excluding it keeps the site blind-safe)
            + creativity-honesty check (is the 'novel' claim real & reasoned?)
            + red flags (per answer)
            + qualitative "what's weak / what would make it good"
  per question: head-to-head best pick + why + confidence

WHAT THE SITE SHOWS per answer (so the operator can judge):
  - the answer, markdown-rendered, with any figures embedded inline
  - a PROVENANCE TIMELINE (the one-view "what happened" schematic), each step
    carrying a CS-verified ✓ badge (or ⚠ if CS could not verify) — so the operator trusts
    the trace without re-checking it.

CAPTURE (fixes the "where did the download go" problem):
  PRIMARY = "Copy my evaluation" → clipboard → paste into the CS chat.
  Secondary = Download; Fallback = a always-visible textarea to hand-select.

INGESTION:  answers.json  --(this script)-->  eval_site.html + blinding_key.json
Usage:  python make_eval_site.py answers.json eval_site.html blinding_key.json [--seed N]

answers.json schema:
{
  "experiment": "exp-001",
  "questions": [
    {"id":"Q_ERGO","question_text":"...",
     "answers":[
       {"arm":"B","run":1,"answer_md":"...","figures":[{"caption":"..","path":"..png"}|{"caption":"..","b64":"..","mime":"image/png"}],
        "process_trace":[{"action":"connector_query","detail":"PubMed: ...","evidence":"12 hits"}],  # action-labelled; CS-scored, NOT rendered in this site (blind-safety)
        "citations":[{"id":"PMID:123","note":"CS scores these"}]}
     ]}
  ]
}
"""
import argparse, base64, html, json, mimetypes, os, random, sys

try:
    import markdown as _md
    def render_md(text):
        return _md.markdown(text or "", extensions=["tables", "fenced_code", "sane_lists"])
except Exception:
    # Degraded fallback: escape + keep paragraph/line breaks. Never fabricate structure.
    def render_md(text):
        esc = html.escape(text or "")
        return "<p>" + esc.replace("\n\n", "</p><p>").replace("\n", "<br>") + "</p>"

# ---- the operator's science categories (NO grounding/citations — that's CS's harness job) ----
CATS = [
    {"key": "reasoning",    "label": "Reasoning & soundness", "help": "Is the chain of thought sound, clear and elegant — valid inferences, no scientific errors, alternatives weighed? WHERE a test/method is proposed, is it valid — but if the question asks only for a hypothesis or argument, judge the reasoning and don't penalise a missing experiment."},
    {"key": "completeness", "label": "Completeness", "help": "Does it actually answer the whole question with concrete specifics — named entities, a testable prediction (and the requested experiment, where one is asked for)?"},
    {"key": "usefulness",   "label": "Usefulness",   "help": "Could a domain scientist act on this? Is it worth a researcher's time?"},
    {"key": "creativity",   "label": "Creativity",   "help": "Is the idea genuinely novel and non-obvious vs what the field already knows — and sensible?"},
]
SCALE = {1:"1 — poor", 2:"2 — weak", 3:"3 — ok", 4:"4 — strong", 5:"5 — excellent"}

HONESTY = [
    {"key":"novel_to_you", "q":"Is the core idea actually novel to you (a domain expert)?", "opts":["Yes, novel","Somewhat","No, known","Can't tell"]},
    {"key":"reasoning_followable", "q":"Can you follow a clear reasoning chain from known facts to the novel claim?", "opts":["Yes, clear","Partly","No chain"]},
    {"key":"hallucination_flag", "q":"Does any 'novel' claim smell like confident hallucination (no real basis)?", "opts":["No","Maybe","Yes — flag"]},
]
REDFLAGS = [
    ("vague", "Vague / hand-waving (no specifics)"),
    ("overclaim", "Overclaims certainty beyond evidence"),
    ("slop", "Generic AI-slop filler / padding"),
    ("unfalsifiable", "Prediction not actually falsifiable"),
    ("misused_ref", "A cited paper seems misused (if you happened to notice)"),
    ("offtopic", "Drifts off the question"),
]

CSS = r"""
/* Warm, light, low-fatigue palette for long focused reading:
   cream page + soft-white cards + deep-charcoal text (high contrast, not harsh),
   muted teal accent, warm ochre question headers, generous whitespace, soft shadows. */
:root{
  --bg:#f6f1e7;        /* warm cream page */
  --panel:#fffdf8;     /* soft white card */
  --panel2:#fbf7ee;    /* faint warm tint for nested blocks */
  --ink:#2f2a24;       /* deep warm charcoal text */
  --dim:#6b6459;       /* muted warm grey for secondary text */
  --acc:#2e8b83;       /* calm muted teal (primary) */
  --acc-soft:#e3efec;  /* teal wash */
  --acc2:#b9772e;      /* warm ochre (question headers) */
  --acc2-soft:#f6ecdb; /* ochre wash */
  --good:#2f7d5b;      /* muted green */
  --good-soft:#e6f1ea;
  --warn:#b23b3b;      /* muted brick red */
  --warn-soft:#f6e6e4;
  --line:#e6ddcd;      /* soft warm hairline */
  --line2:#d8cdb8;
}
*{box-sizing:border-box}
html,body{margin:0;background:var(--bg);color:var(--ink);
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Inter,Roboto,Helvetica,Arial,sans-serif;
  font-size:15px;line-height:1.65;-webkit-font-smoothing:antialiased}
.wrap{max-width:860px;margin:0 auto;padding:34px 24px 110px}
h1{font-size:23px;font-weight:700;letter-spacing:.2px;color:var(--ink);margin:0 0 4px}
.sub{color:var(--dim);font-size:13.5px;margin-bottom:22px;line-height:1.5}
.scan{display:none}   /* removed: no scanline overlay */
.card{background:var(--panel);border:1px solid var(--line);
  border-radius:14px;padding:22px 24px;margin:20px 0;box-shadow:0 1px 2px rgba(60,50,35,.04),0 6px 22px rgba(60,50,35,.06)}
.qbar{border-left:4px solid var(--acc2);padding:12px 16px;background:var(--acc2-soft);border-radius:8px;margin:2px 0 6px;
  font-size:15.5px;line-height:1.55}
.qbar b{color:var(--acc2);font-weight:700;margin-right:6px}
.ansgrid{display:grid;grid-template-columns:1fr;gap:18px}
.anshead{display:flex;align-items:center;gap:12px;border-bottom:1px solid var(--line);padding-bottom:12px;margin-bottom:16px}
.tag{display:inline-block;background:var(--acc);color:#fff;font-weight:700;border-radius:8px;padding:5px 14px;
  letter-spacing:.5px;font-size:13.5px}
/* the answer body — serif for comfortable long-form reading, roomy line height */
.body{background:var(--panel2);border:1px solid var(--line);border-radius:10px;padding:18px 22px;max-height:560px;overflow:auto;
  font-family:Georgia,Cambria,"Times New Roman",serif;font-size:15.5px;line-height:1.7;color:#332e27}
.body h1,.body h2,.body h3{font-family:-apple-system,"Segoe UI",sans-serif;color:var(--acc);font-size:16px;font-weight:700;
  border-bottom:1px solid var(--line);padding-bottom:4px;margin:14px 0 8px}
.body table{border-collapse:collapse;width:100%;margin:12px 0}
.body th,.body td{border:1px solid var(--line2);padding:7px 10px;font-size:14px;text-align:left}
.body th{background:var(--acc2-soft)}
.body code,.body pre{background:#f1eadb;color:#7a4a12;border-radius:5px;padding:1px 6px;
  font-family:ui-monospace,Menlo,Consolas,monospace;font-size:13.5px}
.body pre{padding:12px;overflow:auto;border:1px solid var(--line)}
.body img{max-width:100%;border:1px solid var(--line);border-radius:8px;margin:10px 0;background:#fff}
.figcap{color:var(--dim);font-size:12.5px;margin:-2px 0 12px;font-style:italic}
.tl{margin:12px 0 2px;border-left:2px solid var(--line2);padding-left:0}
.tl .step{position:relative;padding:9px 12px 9px 22px;border-bottom:1px solid var(--line)}
.tl .step:last-child{border-bottom:none}
.tl .step:before{content:"";position:absolute;left:-6px;top:15px;width:9px;height:9px;border-radius:50%;
  background:var(--acc)}
.ph{color:var(--acc2);font-weight:700;font-size:12.5px;letter-spacing:.4px}
.ev{color:var(--dim);font-size:13px}
.badge{float:right;font-size:11.5px;padding:2px 10px;border-radius:12px;font-weight:600}
.badge.ok{color:var(--good);background:var(--good-soft);border:1px solid #bfe0cd}
.badge.no{color:var(--warn);background:var(--warn-soft);border:1px solid #e6c4c0}
.formsec{margin-top:16px}
.lbl{color:var(--dim);font-weight:700;font-size:12px;letter-spacing:.8px;text-transform:uppercase;margin:16px 0 6px}
.catrow{display:flex;align-items:center;gap:12px;margin:8px 0;flex-wrap:wrap}
.catname{min-width:120px;font-weight:600}
.cathelp{color:var(--dim);font-size:13px;flex:1 1 100%;line-height:1.5}
select,textarea,input[type=text]{background:#fff;color:var(--ink);border:1px solid var(--line2);
  border-radius:8px;padding:8px 10px;font-family:inherit;font-size:14px}
select:focus,textarea:focus,input:focus{outline:none;border-color:var(--acc);box-shadow:0 0 0 3px var(--acc-soft)}
textarea{width:100%;min-height:76px;resize:vertical;line-height:1.6}
.qual{border:1px solid #e7d3b0;border-radius:10px;padding:14px;background:var(--acc2-soft);margin-top:4px}
.qual .lbl{color:var(--acc2)}
.flags label{display:block;margin:5px 0;color:var(--ink);font-size:14px}
.hon{margin:8px 0}
.hon .q{font-size:14px;margin-bottom:3px}
.bar{position:fixed;bottom:0;left:0;right:0;background:rgba(255,253,248,.96);backdrop-filter:blur(6px);
  border-top:1px solid var(--line2);padding:14px 22px;display:flex;gap:12px;align-items:center;z-index:10;
  box-shadow:0 -3px 18px rgba(60,50,35,.08)}
button{font-family:inherit;font-weight:700;letter-spacing:.3px;border-radius:9px;padding:11px 20px;cursor:pointer;
  border:1px solid transparent;font-size:14px}
.primary{background:var(--acc);color:#fff;box-shadow:0 2px 8px rgba(46,139,131,.28)}
.primary:hover{background:#26746d}
.ghost{background:#fff;color:var(--acc);border:1px solid var(--acc)}
.ghost:hover{background:var(--acc-soft)}
.status{color:var(--good);font-size:13.5px;margin-left:auto;font-weight:600}
.help{color:var(--dim);font-size:12.5px}
#dump{width:100%;min-height:90px;margin-top:10px;display:none;font-family:ui-monospace,Menlo,Consolas,monospace}
.note{color:var(--ink);font-size:13.5px;border:1px solid var(--line2);background:var(--acc-soft);border-radius:10px;
  padding:12px 16px;margin:10px 0;line-height:1.6}
.h2h{border:1px solid #cfe3df;border-radius:10px;padding:14px;margin-top:8px;background:var(--acc-soft)}
"""

JS = r"""
const KEY_ORDER = __ORDER__;
function collect(){
  const out={experiment:EXP, evaluator:"the operator", generated:GEN, questions:{}};
  let missing=0;
  for(const q of DATA){
    const qo={question_id:q.id, answers:{}, head_to_head:{}};
    for(const a of q.disp){
      const ao={scores:{}, honesty:{}, redflags:[], qualitative:""};
      for(const c of CATS){
        const el=document.querySelector(`[name="${q.id}__${a.label}__${c.key}"]`);
        ao.scores[c.key]= el && el.value ? Number(el.value): null;
        if(!el || !el.value) missing++;
      }
      for(const h of HON){
        const el=document.querySelector(`[name="${q.id}__${a.label}__hon__${h.key}"]`);
        ao.honesty[h.key]= el ? el.value : null;
      }
      const fix=document.querySelector(`[name="${q.id}__${a.label}__hon__fix"]`);
      ao.honesty.one_line_fix = fix? fix.value : "";
      document.querySelectorAll(`[name="${q.id}__${a.label}__flag"]:checked`).forEach(x=>ao.redflags.push(x.value));
      const rfo=document.querySelector(`[name="${q.id}__${a.label}__flag_other"]`);
      if(rfo && rfo.value) ao.redflags.push("other:"+rfo.value);
      const ql=document.querySelector(`[name="${q.id}__${a.label}__qual"]`);
      ao.qualitative = ql? ql.value : "";
      qo.answers[a.label]=ao;
    }
    const best=document.querySelector(`[name="${q.id}__best"]`);
    const conf=document.querySelector(`[name="${q.id}__conf"]`);
    const why =document.querySelector(`[name="${q.id}__why"]`);
    qo.head_to_head={best: best?best.value:"", confidence: conf?conf.value:"", why: why?why.value:""};
    out.questions[q.id]=qo;
  }
  out._missing_scores=missing;
  return out;
}
function payload(){ return JSON.stringify(collect(), null, 2); }
function setStatus(m){ document.getElementById("status").textContent=m; }
async function copyEval(){
  const txt=payload();
  try{ await navigator.clipboard.writeText(txt);
       setStatus("✓ Copied — paste it into the CS chat."); }
  catch(e){ const d=document.getElementById("dump"); d.style.display="block"; d.value=txt; d.select();
       setStatus("Clipboard blocked — select-all in the box below and copy manually."); }
}
function downloadEval(){
  const blob=new Blob([payload()],{type:"application/json"});
  const a=document.createElement("a"); a.href=URL.createObjectURL(blob);
  a.download=EXP+"_human-eval_FILLED.json"; document.body.appendChild(a); a.click(); a.remove();
  setStatus("Downloaded "+EXP+"_human-eval_FILLED.json (check your Downloads). Copy-paste is more reliable.");
}
function showJSON(){ const d=document.getElementById("dump"); d.style.display="block"; d.value=payload(); d.select();
  setStatus("Preview below — this is exactly what Copy sends."); }
"""

def _fig_html(fig):
    cap = html.escape(fig.get("caption", "") or "")
    b64 = fig.get("b64"); mime = fig.get("mime")
    if not b64 and fig.get("path") and os.path.exists(fig["path"]):
        mime = mime or (mimetypes.guess_type(fig["path"])[0] or "image/png")
        with open(fig["path"], "rb") as fh:
            b64 = base64.b64encode(fh.read()).decode("ascii")
    if not b64:
        return f'<div class="figcap">[figure missing: {cap or "untitled"}]</div>'
    out = f'<img alt="{cap}" src="data:{mime or "image/png"};base64,{b64}">'
    if cap:
        out += f'<div class="figcap">{cap}</div>'
    return out

def _trace_html(trace):
    # ⚠ INTENTIONALLY UNUSED (LB-072/077): process_trace.json is scored by CS only and MUST NOT appear
    # in the human eval site — rendering a phase/action trace could out Arm L to the operator and break the blind.
    # Kept as a hard stub so nobody re-wires it into _answer_block. Do not call.
    raise RuntimeError("process_trace is excluded from the eval site by design (blind-safety, LB-072). "
                       "It is scored by the CS harness (trace_verify.py), never shown to the human evaluator.")
    rows = []
    for s in trace:
        ph = html.escape(str(s.get("phase", "")))
        act = html.escape(str(s.get("action", "")))
        det = html.escape(str(s.get("detail", "")))
        ev = html.escape(str(s.get("evidence", "")))
        verified = s.get("verified", None)
        if verified is True:
            badge = '<span class="badge ok">CS ✓ verified</span>'
        elif verified is False:
            badge = '<span class="badge no">⚠ unverified</span>'
        else:
            badge = ''
        rows.append(f'<div class="step">{badge}<span class="ph">{ph}</span> · {act}<br>{det}'
                    + (f'<br><span class="ev">→ {ev}</span>' if ev else '') + '</div>')
    return '<div class="tl">' + "".join(rows) + '</div>'

def _answer_block(qid, a):
    lab = a["label"]
    body = render_md(a.get("answer_md", ""))
    figs = "".join(_fig_html(f) for f in (a.get("figures") or []))
    ncit = len(a.get("citations") or [])
    # process_trace is DELIBERATELY NOT rendered here (LB-072 blind-safety): it is scored by CS only
    # and excluded from the human eval site, so the operator can never infer the arm from a phase/action trace.
    # science score rows
    catrows = []
    for c in CATS:
        opts = '<option value="">—</option>' + "".join(f'<option value="{v}">{html.escape(t)}</option>' for v, t in SCALE.items())
        catrows.append(
            f'<div class="catrow"><span class="catname">{html.escape(c["label"])}</span>'
            f'<select name="{qid}__{lab}__{c["key"]}">{opts}</select>'
            f'<span class="cathelp">{html.escape(c["help"])}</span></div>')
    # honesty (per answer)
    honrows = []
    for h in HONESTY:
        opts = '<option value="">—</option>' + "".join(f'<option value="{html.escape(o)}">{html.escape(o)}</option>' for o in h["opts"])
        honrows.append(f'<div class="hon"><div class="q">{html.escape(h["q"])}</div>'
                       f'<select name="{qid}__{lab}__hon__{h["key"]}">{opts}</select></div>')
    honrows.append(f'<div class="hon"><div class="q">If you flagged hallucination, one-line why / the fix:</div>'
                   f'<input type="text" style="width:100%" name="{qid}__{lab}__hon__fix"></div>')
    # red flags (per answer)
    flagrows = "".join(
        f'<label><input type="checkbox" name="{qid}__{lab}__flag" value="{k}"> {html.escape(v)}</label>'
        for k, v in REDFLAGS)
    flagrows += (f'<label>Other: <input type="text" name="{qid}__{lab}__flag_other" '
                 f'style="width:60%"></label>')
    return f"""
    <div class="card">
      <div class="anshead"><span class="tag">ANSWER {lab}</span>
        <span class="help">provenance verified by CS · citations checked by CS ({ncit} found) — you judge the science</span></div>
      <div class="lbl">The answer</div>
      <div class="body">{body}{figs}</div>
      <div class="formsec">
        <div class="lbl">Your science scores (1–5)</div>
        {''.join(catrows)}
        <div class="lbl">Creativity honesty check (this answer)</div>
        {''.join(honrows)}
        <div class="lbl">Red flags (this answer)</div>
        <div class="flags">{flagrows}</div>
        <div class="qual"><div class="lbl">What's weak — what would this need to become good?</div>
          <textarea name="{qid}__{lab}__qual" placeholder="Your qualitative feedback (this is the field the operator asked for)."></textarea></div>
      </div>
    </div>"""

def build_site(answers_path, out_html, out_key, seed=None):
    with open(answers_path) as fh:
        data = json.load(fh)
    exp = data.get("experiment", "exp")
    rng = random.Random(seed)
    key = {}
    disp_data = []       # for JS: list of {id, disp:[{label}]}
    blocks = []
    for q in data["questions"]:
        qid = q["id"]
        ans = list(q["answers"])
        rng.shuffle(ans)                                   # blind: randomize order per question
        labels = [chr(ord('A') + i) for i in range(len(ans))]
        disp = []
        keymap = {}
        for lab, a in zip(labels, ans):
            a["label"] = lab
            disp.append({"label": lab})
            keymap[lab] = {"arm": a.get("arm"), "run": a.get("run")}
        key[qid] = keymap
        disp_data.append({"id": qid, "disp": disp})
        # head-to-head selector
        bestopts = '<option value="">—</option>' + "".join(f'<option value="{l}">Answer {l}</option>' for l in labels)
        confopts = '<option value="">—</option>' + "".join(f'<option value="{c}">{c}</option>' for c in ["low","medium","high"])
        h2h = (f'<div class="h2h"><div class="lbl">Head-to-head (this question)</div>'
               f'Best answer overall: <select name="{qid}__best">{bestopts}</select> &nbsp; '
               f'Confidence: <select name="{qid}__conf">{confopts}</select>'
               f'<div class="lbl">Why is it best?</div>'
               f'<textarea name="{qid}__why" placeholder="What makes the winner better than the others?"></textarea></div>')
        qhtml = (f'<div class="qbar"><b>{html.escape(qid)}</b> &nbsp; {html.escape(q.get("question_text",""))}</div>'
                 + '<div class="ansgrid">' + "".join(_answer_block(qid, a) for a in ans) + '</div>' + h2h)
        blocks.append(f'<div class="card">{qhtml}</div>')

    js = (f'const EXP={json.dumps(exp)};\nconst GEN={json.dumps(data.get("generated",""))};\n'
          f'const CATS={json.dumps(CATS)};\nconst HON={json.dumps(HONESTY)};\n'
          f'const DATA={json.dumps(disp_data)};\n'
          + JS.replace("__ORDER__", json.dumps(list(key.keys()))))

    doc = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>the Metascience Project · {html.escape(exp)} · blinded evaluation</title><style>{CSS}</style></head>
<body><div class="scan"></div><div class="wrap">
<h1>the Metascience Project // Evaluation Console</h1>
<div class="sub">EXPERIMENT {html.escape(exp)} · BLINDED · answers shown in randomized order · you judge the science, CS checks citations + provenance</div>
<div class="note">Score each blinded answer on the four science dimensions, run the per-answer honesty check + red flags,
and write what's weak. Then pick the best answer per question. When done, click <b>Copy my evaluation</b> and paste it
into the CS chat. (Citations and "did it really happen" are already checked by CS — the ✓ badges — so you don't spend
time on them.)</div>
{''.join(blocks)}
</div>
<div class="bar">
  <button class="primary" onclick="copyEval()">⧉ Copy my evaluation</button>
  <button class="ghost" onclick="downloadEval()">⬇ Download (backup)</button>
  <button class="ghost" onclick="showJSON()">show JSON</button>
  <span id="status" class="status"></span>
</div>
<div class="wrap"><textarea id="dump" readonly></textarea></div>
<script>{js}</script>
</body></html>"""
    with open(out_html, "w") as fh:
        fh.write(doc)
    with open(out_key, "w") as fh:
        json.dump({"experiment": exp, "note": "TRUE arm/run per display label — the operator never opens this; unblind only after eval is in.",
                   "key": key}, fh, indent=1)
    return out_html, out_key, key

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("answers"); ap.add_argument("out_html", nargs="?", default="eval_site.html")
    ap.add_argument("out_key", nargs="?", default="blinding_key.json")
    ap.add_argument("--seed", type=int, default=None)
    a = ap.parse_args()
    h, k, key = build_site(a.answers, a.out_html, a.out_key, seed=a.seed)
    print("wrote", h, "and", k)
    print("blinding:", json.dumps(key, indent=1))
