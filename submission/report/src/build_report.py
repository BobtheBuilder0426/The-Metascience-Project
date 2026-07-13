#!/usr/bin/env python3
"""Build the report PDF from report.html + report.css and enforce the page budget.

Budget rule: the COUNTED sections (Abstract + Introduction + Results + Discussion) must fit
in <=10 A4 pages. Methods / Sources / Supplementary come after a <div class="counted-end">
boundary marker and do NOT count.

Usage: python build_report.py [report.html] [out.pdf]
Exit code 0 if within budget, 2 if over (still writes the PDF so you can inspect).
"""
import sys, re
from pathlib import Path
from weasyprint import HTML

HERE = Path(__file__).parent
html_path = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "report.html"
out_path  = Path(sys.argv[2]) if len(sys.argv) > 2 else HERE.parent / "report.pdf"

doc = HTML(filename=str(html_path)).render()
total_pages = len(doc.pages)

# The first back-matter heading carries id="backmatter-start" and forces a page break,
# so it lands on the first UNCOUNTED page. Counted sections = everything before it.
backmatter_page = None
for i, page in enumerate(doc.pages, start=1):
    if "backmatter-start" in page.anchors:
        backmatter_page = i
        break
counted_pages = (backmatter_page - 1) if backmatter_page else total_pages

doc.write_pdf(str(out_path))
budget = 10
status = "OK" if counted_pages <= budget else "OVER"
print(f"total_pages={total_pages}  counted_sections_pages={counted_pages}  budget={budget}  -> {status}")
print(f"wrote {out_path} ({out_path.stat().st_size} bytes)")
sys.exit(0 if counted_pages <= budget else 2)
