exp-003 dataset delivery = DOI-ONLY (operator ruling 2026-07-13, LB-104). NO files are staged here by design.

Both arms received the dataset as a pointer inside the byte-identical prompt:
  DOI https://doi.org/10.64898/2025.12.23.696273  (genome-scale CD4+ T-cell Perturb-seq, Marson lab)
  + a compute-caution: "the full dataset is very large and you are running on a small laptop with limited compute —
    do not download or load the entire raw dataset; work from a tractable subset or the paper's processed / summary data."

Registered in SOURCES.md: S-084 (dataset: CZI Virtual Cells Platform; GEO GSE314342; SRA SRP643211;
public S3 s3://genome-scale-tcell-perturb-seq/) and S-085 (preprint: bioRxiv 2025.12.23.696273).

Why DOI-only, not staged files: the raw atlas is ~1.8 TB (cell-level h5ad 119-173 GB each); even the processed DE
tensor GWCD4i.DE_stats.h5ad is 16.8 GB. Author CSV supp tables (~15 MB) exist on the public bucket and were inspected
this session, but the operator chose a DOI-only pointer + compute-caution so both arms decide their own tractable slice
(both streamed the processed DE tensor rather than downloading raw — LB-104). Byte-identical delivery = fairness intact.
