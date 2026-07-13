# Reasoning — how I got to a complex I positive allosteric modulator

## Framing the question
- "Not-yet-thought-of" compound for **complex-I** mitochondrial disease → the answer must be
  (a) mechanistically distinct from what's been tried, and (b) grounded in public data, not
  invented. So the real work is: *find the mechanistic gap, then design into it.*
- Two failure modes to avoid: proposing something already in trials (not novel), or proposing
  something with no causal basis (not grounded). I attacked both explicitly.

## Step 1 — Map the disease in public databases
- Resolved ontology IDs: complex I deficiency = **MONDO:0100133**, Leigh = MONDO:0009723,
  LHON = MONDO:0010788, MELAS = Orphanet:550.
- Open Targets: **2,420 associated targets, 0 associated drugs** for CI deficiency. Top genes =
  the enzyme's own subunits/assembly factors (NDUFS/NDUFV/NDUFA, FOXRED1, NUBPL). → It's a
  disease *of the enzyme*, and there is literally no approved pharmacology.

## Step 2 — Inventory what's been tried, and classify it
- Open Targets disease→drugs + ClinicalTrials.gov: idebenone, EPI-743/vatiquinone,
  sonlicromanol, CoQ10, elamipretide, NR, niacinamide, rapamycin, cysteamine, cyclosporine,
  mannitol, curcumin.
- **Classification insight:** collapse them into mechanism classes and only two remain —
  (i) quinone/chromanol **antioxidant redox carriers**, (ii) **NAD⁺-pool** precursors. Both are
  *downstream* of the broken catalytic step. None restores forward NADH→CoQ electron flow.
- This is the gap. But a gap isn't a proposal — I need a *causal* reason to think closing it
  helps.

## Step 3 — Find the causal clue (and avoid the obvious trap)
- I first hypothesized **HIF-PH inhibitor repurposing** (roxadustat/daprodustat — approved,
  hypoxia-pathway). Checked druggability: EGLN1 = CHEMBL5697, approved inhibitors exist. Looked
  promising.
- **Then I checked the primary literature and reversed course.** Jain 2016 (*Science*): hypoxia
  rescues the *Ndufs4*-KO Leigh mouse. Jain 2019 (*Cell Metab*): rescue works by normalizing
  **brain hyperoxia**, and **HIF activation is NOT sufficient** (can be deleterious). → HIF-PH
  inhibitors are the *wrong node*. Trap avoided.
- Meisel 2024 (*Cell*): the intra-complex suppressor **nuo-3(G60D)/NDUFA6** rescues CI mutants
  by the **same mechanism as hypoxia** — restoring forward electron flow at the **ubiquinone
  (CoQ) pocket**, HIF-independent, ROS-independent, specific to matrix-arm mutants; a
  "hypoxia-mimetic" mutation with **allosteric coupling** between an accessory subunit and the
  catalytic core.

## Step 4 — Turn the genetics into a drug concept
- Logic: *a point mutation on an accessory subunit allosterically re-opens the CoQ pocket and
  rescues catalysis* ⇒ *a small molecule at the same accessory-subunit/Q-module interface should
  reproduce it.*
- Name the class: **complex I positive allosteric modulator (CI-PAM)** = a "chemical
  hypoxia-mimetic."
- **Novelty check (hard):** searched ChEMBL for anything acting on complex I. Result — the
  target (CHEMBL2363065) and subunits are annotated with **inhibitors only** (rotenone
  CHEMBL1703, piericidin…). **No activator/PAM exists anywhere in ChEMBL.** Complex I has only
  ever been a poisoning target. The concept is genuinely unoccupied.
- Cross-check trials: complex I PAM → none; "methylene blue" in mito disease → **0 trials**.

## Step 5 — Physicochemical reasoning about *why the tried drugs also fail on delivery*
- Two independent liabilities, both diagnosable from structure:
  - **Δψm-dependence:** MitoQ is a permanent TPP⁺ cation — its mito uptake needs the membrane
    potential the disease destroys. Self-defeating in exactly this disease.
  - **CNS access:** CoQ10 (cLogP≈18) and EPI-743 (cLogP≈7.5) are far too lipophilic for a
    brain-predominant disease.
- Quantified with **Wager CNS MPO** (RDKit): MitoQ 2.0, CoQ10 3.0, EPI-743 3.3 — all sub-
  threshold. This became the second design constraint and a clean figure (Fig 2).

## Step 6 — Design the molecule to the mechanism-matched profile
- Four rules, each traceable to a finding above:
  1. neutral, Δψm-independent (vs MitoQ);
  2. brain-penetrant (MW<350, TPSA<90, cLogP 1–4, HBD≤3) — Leigh is neurological;
  3. non-quinone/chromanol — deliberately outside tried chemical space; bind-and-reshape, not
     carry electrons;
  4. a polar **"G60D-mimetic" H-bond arm** on a rigid scaffold to engage the accessory interface.
- Built 6 candidates, profiled vs 9 reference drugs in RDKit (MW, cLogP, TPSA, HBD/HBA, QED,
  charge, permanent-cation flag, redox-class SMARTS, CNS MPO, Ro5).
- **Lead = CI-PAM-1f**, _N_-(trans-4-hydroxycyclohexyl)quinoxaline-2-carboxamide:
  CNS MPO 5.5 (top of panel), QED 0.87, MW 271, cLogP 1.66, neutral, non-redox, 0 Ro5
  violations. Quinoxaline carboxamide = flat rigid Q-headgroup-complementary but redox-inert;
  hydroxycyclohexyl amide = the neutral polar G60D-mimetic contact.
- The other 5 candidates are the SAR starting series (vary anchor rigidity, arm polarity, ring
  system) — kept for the med-chem plan.

## Step 7 — Define the falsification-first experiment
- The whole idea hinges on one unknown: *can a small molecule induce the activating
  conformation?* G60D proves the conformation exists, not that it's druggable.
- So experiment 1 is the go/no-go: does CI-PAM-1f raise **forward CI activity + OCR** in
  *Ndufs4*-KO cells? Follow with Δψm/NAD⁺ rescue, rotenone-competition specificity, cryo-EM
  target engagement, then Leigh-mouse survival + brain pO₂ (the direct hypoxia-mimetic readout).

## Why I'm confident vs. where I'm exposed
- **Confident:** the *target rationale* is unusually strong — a genetic proof-of-concept in a
  real CI-disease model, from a top lab, plus a rigorous novelty gap (no CI activator exists).
  The delivery critique of incumbents is quantitative and reproducible.
- **Exposed:** the *specific molecule* is a computational hypothesis. No binding data; no
  docking this session (no GPU); the activating pocket's druggability is unproven. I've been
  explicit about this and designed the first experiment to expose it quickly and cheaply.

## Data/methods provenance
- Databases: Open Targets, ChEMBL, PubChem, UniProt/MyGene, ClinicalTrials.gov (all via MCP
  connectors; identifiers in sources.md).
- Primary lit: Meisel 2024 Cell (fetched + read), Jain 2016 Science, Jain 2019 Cell Metab.
- Compute: RDKit 2026.03.4 property/QED/SMARTS; Wager CNS MPO implemented in-kernel; matplotlib
  + figure-style for figures. No remote compute was available; all analysis ran locally.
