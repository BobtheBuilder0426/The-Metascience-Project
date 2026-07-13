"""extract.py — pull citations + checkable entities out of an answer.

Pure functions, no network. Used by citations.py (verification) and by the
Completeness dimension (entity specificity). See quantification.md §2.
"""
import re

# --- dataset / DB accessions (LB-075: grounding & integrity) ---------------
# GEO series/sample, SRA, ArrayExpress, PDB, UniProt, Ensembl, dbGaP, BioProject.
_DATASET_PATTERNS = {
    "GEO": re.compile(r"\bG(?:SE|SM|DS)\d{3,7}\b"),
    "SRA": re.compile(r"\b[SED]R[APRSX]\d{6,9}\b"),
    "ArrayExpress": re.compile(r"\bE-[A-Z]{4}-\d+\b"),
    "PDB": re.compile(r"\bPDB[:\s]?[0-9][A-Za-z0-9]{3}\b"),
    "UniProt": re.compile(r"\b[OPQ][0-9][A-Z0-9]{3}[0-9]\b|\b[A-NR-Z][0-9](?:[A-Z][A-Z0-9]{2}[0-9]){1,2}\b"),
    "Ensembl": re.compile(r"\bENS[A-Z]*[GTP]\d{11}\b"),
    "dbGaP": re.compile(r"\bphs\d{6}\b"),
    "BioProject": re.compile(r"\bPRJ[EDN][A-Z]\d+\b"),
}


def extract_dataset_ids(text: str) -> list:
    """Return [{'id','db'}] for every dataset/DB accession named in the answer.
    Deduplicated, order-preserving. Feeds the grounding-integrity dataset-resolution check."""
    out, seen = [], set()
    for db, pat in _DATASET_PATTERNS.items():
        for m in pat.finditer(text or ""):
            acc = m.group(0)
            key = (db, acc.upper())
            if key not in seen:
                seen.add(key)
                out.append({"id": acc, "db": db})
    return out


# --- citations -------------------------------------------------------------
_PMID = re.compile(r"\bPMID:?\s*(\d{6,9})\b", re.I)
_DOI = re.compile(r"\b(10\.\d{4,9}/[-._;()/:A-Z0-9]+)\b", re.I)
# (Author, 2023) or (Author et al., 2023)
_AUTHORYEAR = re.compile(r"\(([A-Z][A-Za-z\-]+(?:\s+et\s+al\.?)?),?\s+((?:19|20)\d{2})[a-z]?\)")


def extract_citations(text: str) -> list:
    """Return a list of {kind, value, raw} citation records found in `text`."""
    out = []
    for m in _PMID.finditer(text):
        out.append({"kind": "pmid", "value": m.group(1), "raw": m.group(0)})
    for m in _DOI.finditer(text):
        val = m.group(1).rstrip(").,;")
        out.append({"kind": "doi", "value": val, "raw": m.group(0)})
    for m in _AUTHORYEAR.finditer(text):
        out.append({"kind": "authoryear", "value": f"{m.group(1)} {m.group(2)}", "raw": m.group(0)})
    # de-dup on (kind,value)
    seen, uniq = set(), []
    for c in out:
        k = (c["kind"], c["value"].lower())
        if k not in seen:
            seen.add(k); uniq.append(c)
    return uniq


# --- checkable entities (Completeness / specificity) -----------------------
# Conservative, dependency-free heuristics. Not meant to be exhaustive NER —
# meant to give a monotone "how specific is this answer" signal.
_GENE = re.compile(r"\b([A-Z][A-Z0-9]{2,9}|[A-Z][a-z]{1,3}[0-9]{1,3}|PGC-?1[αa]?|mTOR|AMPK|SIRT[1-7]|NAD\+?)\b")
_ASSAY = re.compile(r"\b(Seahorse|respirometr|Western blot|qPCR|RNA-?seq|scRNA-?seq|immunohisto|"
                    r"OCR|ELISA|flow cytometry|mass spec|metabolomic|proteomic|CRISPR|knockout|knockdown|"
                    r"luciferase|immunoblot|histolog|microscopy|actigraphy|grip strength|treadmill)\w*", re.I)
_QUANT = re.compile(r"(?<![\w])([+\-]?\d+(?:\.\d+)?\s?(?:%|percent|fold|-fold|mg/kg|µM|uM|nM|mM|days?|weeks?|months?))")
_PATHWAY = re.compile(r"\b(mitophagy|autophagy|apoptosis|senescence|OXPHOS|glycolysis|"
                      r"oxidative phosphorylation|electron transport chain|mitochondrial biogenesis|"
                      r"unfolded protein response|inflamma(?:tion|some)|circadian|NAD\+? (?:salvage|metabolism))\b", re.I)
_DRUGHINT = re.compile(r"\b(rapamycin|metformin|urolithin[ -]?A|nicotinamide riboside|NMN|resveratrol|"
                       r"spermidine|senolytic|dasatinib|quercetin|fisetin|KIRA6|leflunomide|"
                       r"\w+(?:mycin|inib|statin|parib|mab|sartan))\b", re.I)

_STOP_UPPER = {"DNA", "RNA", "ATP", "ROS", "AML", "PICI", "USA", "PI", "CS", "CC", "AI", "LLM", "GOAL"}


def extract_entities(text: str) -> dict:
    """Count named, checkable entities. Returns counts + the matched tokens."""
    genes = {m.group(1) for m in _GENE.finditer(text) if m.group(1) not in _STOP_UPPER}
    assays = {m.group(0).lower() for m in _ASSAY.finditer(text)}
    quants = {m.group(1).strip() for m in _QUANT.finditer(text)}
    pathways = {m.group(1).lower() for m in _PATHWAY.finditer(text)}
    drugs = {m.group(1).lower() for m in _DRUGHINT.finditer(text)}
    counts = {"genes": len(genes), "assays": len(assays), "quant_predictions": len(quants),
              "pathways": len(pathways), "drugs": len(drugs)}
    counts["total"] = sum(counts.values())
    return {"counts": counts,
            "tokens": {"genes": sorted(genes), "assays": sorted(assays),
                       "quant_predictions": sorted(quants), "pathways": sorted(pathways),
                       "drugs": sorted(drugs)}}


def specificity_score(entities: dict) -> int:
    """Map entity counts -> a 1..5 Completeness sub-signal (monotone, saturating)."""
    t = entities["counts"]["total"]
    # 0 -> 1, 1-2 -> 2, 3-5 -> 3, 6-9 -> 4, 10+ -> 5
    for thr, sc in [(10, 5), (6, 4), (3, 3), (1, 2)]:
        if t >= thr:
            return sc
    return 1
