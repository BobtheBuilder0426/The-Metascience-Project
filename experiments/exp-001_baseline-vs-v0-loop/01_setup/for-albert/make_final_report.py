"""make_final_report.py — submission-grade FINAL REPORT (one self-contained HTML). [CS-authored]

The judge-facing centerpiece: presents ONE experiment end-to-end — question, methodology, the human (the operator)
+ machine (harness) results side by side, the finding, creativity/novelty, and an honest limitations box.
Driven by the merged scorecard so exp-001 just swaps real data in.

Usage:
  python make_final_report.py <merged_scorecard.json> <example_eval.json> <out.html> [--demo]

merged_scorecard.json schema (produced by the ingest→unblind→score→merge pipeline):
  {"experiment","evaluator_human","mode","questions":{QID:{"answers":[{arm,run,shown_as,human_mean,human_scores,
    human_redflags,human_qualitative,human_honesty,machine_composite,machine_grounding_cap,machine_cite_verify,
    machine_creativity_idx}], "human_best_arm","human_best_why"}}}
"""
import json, sys, html, statistics as st

def esc(s): return html.escape(str(s if s is not None else ""))

def bar(val, maxv, color):
    if val is None: return '<span style="color:#6b6459">—</span>'
    pct = max(0, min(100, 100*val/maxv))
    return (f'<span class="barwrap"><span class="barfill" style="width:{pct:.0f}%;background:{color}"></span></span> '
            f'<b>{val:.2f}</b>')

CSS = """
:root{--bg:#f6f1e7;--panel:#fffdf8;--ink:#2f2a24;--dim:#6b6459;--acc:#2e8b83;--acc2:#b9772e;
 --good:#2f7d5b;--warn:#b23b3b;--line:#e6ddcd;--line2:#d8cdb8}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);
 font-family:-apple-system,"Segoe UI",Inter,Roboto,sans-serif;font-size:15px;line-height:1.65}
.wrap{max-width:940px;margin:0 auto;padding:36px 26px 90px}
h1{font-size:26px;margin:0 0 4px}h2{font-size:19px;margin:26px 0 8px;color:var(--acc);
 border-bottom:2px solid var(--line);padding-bottom:5px}h3{font-size:15.5px;margin:16px 0 6px;color:var(--acc2)}
.sub{color:var(--dim);font-size:14px;margin-bottom:8px}
.badge-demo{display:inline-block;background:#f6ecdb;color:#8a5a1e;border:1px solid #e7d3b0;border-radius:20px;
 padding:4px 14px;font-size:12.5px;font-weight:700;letter-spacing:.4px;margin-bottom:14px}
.card{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:20px 24px;margin:16px 0;
 box-shadow:0 1px 2px rgba(60,50,35,.04),0 6px 22px rgba(60,50,35,.06)}
.kpi{display:flex;gap:16px;flex-wrap:wrap;margin:8px 0}
.kpi .box{flex:1 1 180px;background:#fbf7ee;border:1px solid var(--line);border-radius:12px;padding:14px 16px}
.kpi .box .n{font-size:26px;font-weight:800;color:var(--acc)}
.kpi .box .l{font-size:12.5px;color:var(--dim);margin-top:2px}
.qbar{border-left:4px solid var(--acc2);padding:10px 14px;background:#f6ecdb;border-radius:8px;margin:8px 0}
table{border-collapse:collapse;width:100%;margin:8px 0;font-size:13.5px}
th,td{border:1px solid var(--line2);padding:8px 11px;text-align:left;vertical-align:top}
th{background:#f1eadb;font-size:12.5px}
.barwrap{display:inline-block;width:110px;height:11px;background:#e6ddcd;border-radius:6px;vertical-align:middle}
.barfill{display:inline-block;height:11px;border-radius:6px}
.armL{color:var(--acc);font-weight:700}.armB{color:var(--acc2);font-weight:700}
.chip{display:inline-block;background:#efe7d6;color:#7a5a24;border-radius:10px;padding:1px 8px;margin:1px 2px;font-size:11.5px}
.delta{margin-top:10px;padding:10px 14px;background:#e3efec;border:1px solid #cfe3df;border-radius:8px;font-size:14px}
.note{background:#e3efec;border:1px solid #cfe3df;border-radius:10px;padding:13px 16px;margin:10px 0;font-size:13.5px}
.limit{background:#f6e6e4;border:1px solid #e6c4c0;border-radius:10px;padding:13px 16px;margin:10px 0;font-size:13.5px}
.method li{margin:5px 0}.foot{color:var(--dim);font-size:12.5px;margin-top:24px;border-top:1px solid var(--line);padding-top:12px}
.q{font-style:italic;color:#4a4238}
"""

def build(merged, example_eval, demo=False):
    Q = merged["questions"]
    # overall pooled deltas
    def pooled(key_):
        B=[a[key_] for q in Q.values() for a in q["answers"] if a["arm"]=="B" and a.get(key_) is not None]
        L=[a[key_] for q in Q.values() for a in q["answers"] if a["arm"]=="L" and a.get(key_) is not None]
        return (st.mean(B) if B else None, st.mean(L) if L else None)
    fB,fL = pooled("human_mean"); mB,mL = pooled("machine_composite")
    fD = (fL-fB) if (fB is not None and fL is not None) else None
    mD = (mL-mB) if (mB is not None and mL is not None) else None
    n_answers = sum(len(q["answers"]) for q in Q.values())
    n_L = sum(1 for q in Q.values() for a in q["answers"] if a["arm"]=="L")
    n_B = n_answers - n_L

    # per-question blocks
    qblocks=[]
    for qid,q in Q.items():
        rows=[]
        for a in sorted(q["answers"], key=lambda a:(a["arm"],a["run"])):
            cls = "armL" if a["arm"]=="L" else "armB"
            fl = "".join(f'<span class=chip>{esc(f)}</span>' for f in a.get("human_redflags",[]))
            rows.append(f"""<tr>
              <td><span class="{cls}">Arm {a['arm']}</span> · run {a['run']}</td>
              <td>{bar(a.get('human_mean'),5,'#2e8b83')}</td>
              <td>{bar(a.get('machine_composite'),5,'#b9772e')}</td>
              <td>{fl or '—'}</td>
              <td class="q">{esc(a.get('human_qualitative')) or '—'}</td></tr>""")
        def d(key_):
            B=[a[key_] for a in q["answers"] if a["arm"]=="B" and a.get(key_) is not None]
            L=[a[key_] for a in q["answers"] if a["arm"]=="L" and a.get(key_) is not None]
            return (st.mean(L)-st.mean(B)) if (B and L) else None
        df,dm=d("human_mean"),d("machine_composite")
        agree = (df is not None and dm is not None and (df>0)==(dm>0))
        av = ("✓ agree" if agree else "✗ disagree")
        ac = "#2f7d5b" if agree else "#b23b3b"
        dl = (f'Δ (mean L − mean B): the operator <b>{df:+.2f}</b> · Machine <b>{dm:+.2f}</b> → '
              f'<b style="color:{ac}">{av}</b> on direction' if (df is not None and dm is not None) else "Δ: n/a")
        qblocks.append(f"""<div class="card">
          <div class="qbar"><b>{esc(qid)}</b> — the operator's blinded pick: <b>Arm {esc(q.get('human_best_arm'))}</b>
          ("{esc(q.get('human_best_why'))}")</div>
          <table><thead><tr><th>Answer (unblinded)</th><th>the operator (human) 1–5</th><th>Machine composite</th>
          <th>Flags</th><th>the operator: what's weak</th></tr></thead><tbody>{''.join(rows)}</tbody></table>
          <div class="delta">{dl}</div></div>""")

    demo_badge = '<div class="badge-demo">◆ DEMONSTRATION — synthetic answers; structure is submission-ready, real exp-001 data swaps in</div>' if demo else ''
    finding = ""
    if fD is not None and mD is not None:
        if (fD>0)==(mD>0):
            finding = (f"Both scorers agree on direction: Arm L (loop) { 'beats' if mD>0 else 'trails' } "
                       f"Arm B (baseline) overall — the operator Δ={fD:+.2f}, Machine Δ={mD:+.2f}.")
        else:
            finding = (f"The scorers <b>disagree on overall direction</b> (the operator Δ={fD:+.2f}, Machine Δ={mD:+.2f}) — "
                       f"a signal worth inspecting per answer, not a null result. See per-question detail.")

    return f"""<!doctype html><html><head><meta charset="utf-8">
<title>{esc(merged['experiment'])} — Final Report</title><style>{CSS}</style></head><body><div class="wrap">
{demo_badge}
<h1>{esc(merged['experiment'])} — Final Report</h1>
<div class="sub">Does a blank Claude Code driving Claude Science through the <b>v0 Agentic Loop</b> (Arm L) beat
raw blank Claude Science (Arm B) on the <b>same word-identical question</b>? · Human evaluation: {esc(merged.get('evaluator_human','the operator'))}
· Machine scoring: the Metascience Project harness · {esc(merged.get('mode',''))}</div>

<h2>Headline</h2>
<div class="kpi">
  <div class="box"><div class="n">{fD:+.2f}</div><div class="l">the operator Δ (mean L − mean B), pooled</div></div>
  <div class="box"><div class="n">{mD:+.2f}</div><div class="l">Machine Δ (mean L − mean B), pooled</div></div>
  <div class="box"><div class="n">{n_answers}</div><div class="l">answers scored ({n_L} loop / {n_B} baseline)</div></div>
  <div class="box"><div class="n">{len(Q)}</div><div class="l">questions</div></div>
</div>
<div class="note"><b>Finding.</b> {finding}</div>

<h2>What was compared</h2>
<div class="card">
<h3>The two arms (identical input, different process)</h3>
<ul>
<li><span class="armB">Arm B — baseline:</span> a blank Claude Science session gets ONLY the word-identical
question (+ any provided PDFs), gives one response. No loop, no reframing, no citation framing.</li>
<li><span class="armL">Arm L — loop:</span> a blank Claude Code gets the SAME word-identical question, reframes
it into a rigorous brief (never changing WHAT is asked), and drives a Claude Science session through the v0 loop
(Frame → Plan → Plan-review → Act → Result-review → Integrate).</li>
</ul>
<p class="sub">Fairness rule: the human-typed question is byte-identical across arms. Any advantage must come from
the loop machinery, not a better prompt — the loop's enrichment is generated by the CC, never seen by the baseline.</p>
</div>

<h2>How it was scored (two independent scorers)</h2>
<div class="card method">
<h3>Machine — the Metascience Project harness (CS's ruler)</h3>
<ul>
<li><b>3-persona reviewer jury</b> (Rigor · Significance · Novelty), each blinded to arm, filling one anchored
1–5 rubric — five dimensions at equal 0.20 weight (grounding &amp; integrity, reasoning &amp; soundness,
completeness, usefulness, creativity) → mean + inter-reviewer spread.</li>
<li><b>Grounding &amp; integrity</b> — every PMID/DOI checked to exist AND to actually support its claim; every
dataset/DB accession resolved and checked it was really used; every claimed action in <code>process_trace.json</code>
re-verified. A fabricated citation OR a fabricated action hard-caps grounding at 1.</li>
<li><b>Citation quality</b> — venue strength, primary-vs-review ratio, retractions (quantified, plottable).</li>
<li><b>Creativity index</b> — novelty × plausibility-gate × reasoning-trace-gate (a novel claim with no legible
reasoning chain is not rewarded — guards against hallucination dressed up as creativity).</li>
<li><b>Elo</b> head-to-head + <b>process-trace verification</b> (each claimed step re-checked; ✓/⚠ badges).</li>
</ul>
<h3>Human — {esc(merged.get('evaluator_human','the operator'))} (independent expert layer)</h3>
<ul>
<li>Scores answers <b>blinded</b> (coded E1…E6, arm hidden — the second of the two independent blinding keys) on the
science dimensions (reasoning, completeness, usefulness, creativity), flags red-flags + a creativity-honesty check per
answer, and picks the best answer head-to-head.</li>
<li>The human and the machine never see each other's scores — no anchoring. <b>Disagreement is treated as a
signal</b> (inspected per answer), not an error.</li>
</ul>
</div>

<h2>Results (unblinded)</h2>
{''.join(qblocks)}

<h2>Creativity & novelty</h2>
<div class="note">Creativity is scored on both sides and compared: the machine computes a transparent
novelty × plausibility × reasoning-trace index; {esc(merged.get('evaluator_human','the operator'))} judges creativity-honesty
per answer (novel-to-you? reasoning followable? hallucination?). Where a high machine-novelty answer has a weak
reasoning trace, the gate pulls the index down — the design guard against "novelty that is really hallucination."</div>

<h2>Limitations & honesty</h2>
<div class="limit">
<ul>
<li><b>{"DEMONSTRATION run — synthetic answers." if demo else "Small n."}</b> {"These numbers exercise the pipeline; they are NOT a scientific finding. Real exp-001 swaps in the 8 real answer-runs." if demo else "Few runs per arm; deltas are reported against run-to-run spread, not over-interpreted."}</li>
<li><b>Self-enhancement bias.</b> The machine judges are Claude-family (CS is Claude-only). This bias is
<i>measured</i> against the human anchor, not assumed away.</li>
<li><b>Text-only machine.</b> The harness reads text; a figure/dataset a human values may be under-credited by
the machine — one reason human + machine are both kept.</li>
</ul></div>

<div class="foot">the Metascience Project · "Built with Claude: Life Sciences" · Experiment Loop → Agentic Loop v0 ·
Full methodology: loop-design/current/ (experiment-loop-design, quantification, creativity-metric,
reviewer-panel-design, dataflow-and-handoffs) · provenance: LABBOOK.md + SOURCES.md.</div>
</div></body></html>"""

if __name__ == "__main__":
    args=[a for a in sys.argv[1:] if not a.startswith("--")]
    demo = "--demo" in sys.argv
    merged=json.load(open(args[0])); example=json.load(open(args[1])) if len(args)>1 and args[1]!="-" else {}
    out=args[2] if len(args)>2 else "final_report.html"
    open(out,"w").write(build(merged, example, demo=demo))
    print("wrote", out)
