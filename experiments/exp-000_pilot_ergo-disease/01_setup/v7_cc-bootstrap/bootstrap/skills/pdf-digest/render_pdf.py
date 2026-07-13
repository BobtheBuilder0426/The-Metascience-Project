#!/usr/bin/env python3
"""render_pdf.py — turn a PDF into per-page PNG images + extracted text, for a reading subagent.

Why this exists: a blank Claude Code must FULLY read an input paper — every page, every figure — without
depending on Claude Science or a system PDF viewer. This script uses pypdfium2, a pip wheel that BUNDLES the
PDFium engine (no system poppler needed — poppler was the v5 blocker). It emits one PNG per page (so a
vision-capable subagent can SEE every figure/schematic) plus the page text (so nothing textual is lost).

Usage:
    python render_pdf.py <input.pdf> <out_dir> [--dpi 150]

Output in <out_dir>/:
    pNNN.png         one image per page (zero-padded), rendered at --dpi
    text.txt         full extracted text, page-delimited with '===== PAGE N ====='
    manifest.json    {file, pages, dpi, page_pngs:[...], sha256}
Exit 0 on success; prints a one-line SUMMARY the CC can parse.
"""
import sys, os, json, hashlib, argparse

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf"); ap.add_argument("out"); ap.add_argument("--dpi", type=int, default=150)
    a = ap.parse_args()

    # pypdfium2 is a pure wheel with a bundled binary — install if missing (no compiler needed).
    try:
        import pypdfium2 as pdfium
    except ImportError:
        import subprocess
        print("pypdfium2 not found — installing (pip wheel, bundled binary)...", file=sys.stderr)
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--quiet", "pypdfium2"])
        import pypdfium2 as pdfium

    os.makedirs(a.out, exist_ok=True)
    doc = pdfium.PdfDocument(a.pdf)
    n = len(doc)
    scale = a.dpi / 72.0
    pngs, texts = [], []
    for i in range(n):
        page = doc[i]
        # render image (for figures/schematics)
        img = page.render(scale=scale).to_pil()
        name = f"p{i+1:03d}.png"
        img.save(os.path.join(a.out, name))
        pngs.append(name)
        # extract text (for exact wording / numbers)
        t = page.get_textpage().get_text_range()
        texts.append(f"===== PAGE {i+1} =====\n{t}")
    with open(os.path.join(a.out, "text.txt"), "w", encoding="utf-8") as f:
        f.write("\n\n".join(texts))
    sha = hashlib.sha256(open(a.pdf, "rb").read()).hexdigest()
    manifest = {"file": os.path.basename(a.pdf), "pages": n, "dpi": a.dpi,
                "page_pngs": pngs, "sha256": sha}
    with open(os.path.join(a.out, "manifest.json"), "w") as f:
        json.dump(manifest, f, indent=2)
    print(f"SUMMARY rendered={n} pages dpi={a.dpi} out={a.out} text_chars={sum(len(t) for t in texts)}")

if __name__ == "__main__":
    main()
