# Skill: pdf-digest — spawn a subagent that FULLY reads a PDF (every page + every figure) → agent-friendly file

## When to use
At INTAKE, whenever the human supplies a PDF (or any figure-bearing document) as input to the run. A scientific
paper's **figures and schematics often ARE the result** (pathways, dose-responses, knockouts), so skimming the
abstract is a no-go. This skill makes the blank Claude Code itself able to read the whole document — it does NOT
rely on Claude Science or on a system PDF viewer.

## Why the earlier blank CC couldn't read PDFs (the exact failure this fixes)
A prior run failed to read input PDFs through a **three-layer** failure — understand it so you don't repeat it:
1. **The built-in Read tool needs an external renderer.** Claude Code's file-Read turns a PDF into text/images by
   calling a system PDF renderer — **poppler** (`pdftoppm`/`pdftotext`). On the Windows/WSL side poppler was **not
   installed**, so Read could not open the PDFs at all (verbatim from that run: *"my side has no PDF renderer (poppler
   missing), so I can't use the Read tool for ground truth"*).
2. **Raw byte-parsing can't substitute.** Reading the `.pdf` as raw bytes fails because PDF content streams are
   zlib-compressed binary — you get an embedded font/EPS name and an ambiguous `/Count`, never the real text/figures.
3. **So it offloaded reading to Claude Science** — the exact dependency we must remove: the CC itself never saw the
   papers or their figures.

## The mechanism (why THIS always works)
`render_pdf.py` turns the PDF into **one PNG per page** (so figures are visible to your vision) **+ full page text**
(so wording and numbers are exact). It uses **pypdfium2** — a pip wheel that **BUNDLES its own PDF engine**
(`libpdfium.so`, Google's PDFium, ~7.7 MB, the same engine inside Chrome). It does **NOT** call poppler or any system
tool, so it works regardless of what is installed on the host. (Verified: on a machine with poppler absent, it renders
every page.) It pip-installs itself on first use if absent — a pure wheel, no compiler needed.
2. You (the CC) then **spawn a dedicated subagent** whose ONLY task is to read every rendered page image + the text
   and produce the digest. Isolating it in a subagent is what forces a complete read — the main session's other
   work can't interrupt or truncate it, and its context is spent entirely on this one document.

## Step 1 — render (run once per file)
```
python skills/pdf-digest/render_pdf.py "<inputs>/<file>.pdf" "<work>/<file>.pages" --dpi 150
```
Check the `SUMMARY` line: `rendered=<N> pages`. That `<work>/<file>.pages/` folder now holds `p001.png … pNNN.png`,
`text.txt` (page-delimited), and `manifest.json`. If `rendered=0` or the command errors, STOP and see Fallbacks.

## Step 2 — spawn the reading subagent
Spawn a subagent (Task tool) with this brief. **Give it every page image and the text file** — it must open and look
at all of them, not just the first few:

> *"You are a PDF-reading subagent. Inputs: the page images `p001.png … pNNN.png` and `text.txt` in
> `<work>/<file>.pages/` (N pages). Read EVERY page image in order and the matching text — do not skim, do not stop
> early, do not work from the abstract. For EVERY figure, scheme, and table, look at the image and interpret it (what
> it shows, the data/mechanism, the key quantitative result with direction+magnitude, why it matters) — never just
> echo a caption. Then write a digest to `<driver>/context/<file>.digest.md` in exactly the schema below. Anchor
> every non-trivial statement with (p.N) or (Fig.N). Be dense and complete — this file REPLACES the paper for every
> downstream agent, so it must lose no load-bearing information. If any page or figure was unreadable, say so
> explicitly; never invent a figure you did not see. End with `PHASE_COMPLETE` on its own line."*

### Digest schema (what the subagent writes)
```
# Digest: <file>
**Identity:** <title> · <authors> · <venue> <year> · DOI <…> · <N> pages · pages covered: 1–<N>
## Synopsis            (one paragraph — what the paper establishes)
## Objective           (the question it addresses)
## Methods             (key systems/assays, 3–8 bullets)
## Key findings        (bullets, each with a (p.N) anchor; direction+magnitude where stated)
## Figures & schematics(one entry PER figure/scheme/table: "Fig N: what — data/mechanism — result — why it matters")
## Mechanism / model   (the causal chain A → B → C, explicit)
## Limitations & open questions
## Claims resting on cited references   ({claim → cited ref}, so the driver knows own-result vs borrowed)
```

## Step 3 — verify before accepting
- Digest states the page count and "pages covered: 1–N" matching the render.
- There is one Figures&schematics entry for EVERY figure/scheme (count them against the paper).
- Figure entries INTERPRET (data/mechanism), they don't restate captions.
- Every key finding carries a (p.N)/(Fig.N) anchor.
- Honesty: any unreadable page/figure is flagged, not fabricated.
Record the digest path + page count in `run_log.md`.

## Fallbacks (if render fails)
- **pip blocked / offline:** try `py -m pip install pypdfium2` (Windows launcher) or a user/venv install; pypdfium2 is
  a pure wheel (no compiler). If still blocked, ask the human once to `pip install pypdfium2`.
- **Truly no Python PDF path:** as a LAST resort, ask the human to export the PDF pages to images, or note in
  `run_log.md` that the file could not be digested and proceed with a text-only read of `text.txt` — but flag the run
  as degraded (figures unseen).

## Notes
- A large paper is fine: render all pages; if the subagent's context is tight, split into two subagents by page range
  and concatenate their digests. Coverage beats brevity.
- The digest lives in `driver/context/` so the DRIVER session has full paper context BEFORE it ever prompts Claude
  Science — the driver reads digests first, then reframes, then drives CS.
