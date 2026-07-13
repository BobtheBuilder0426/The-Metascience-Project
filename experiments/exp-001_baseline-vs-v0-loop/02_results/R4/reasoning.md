# Reasoning: how the Partition-Ratchet hypothesis was reached

This document traces the line of thought behind the hypothesis in `result.md`, and then makes the explicit case for why its central claim is novel and not obvious.

---

## 1. Starting constraint: the target is a *cell*, not a molecule

The question is not "where did the first replicator come from" but "how did lifeless organics organize into the first self-replicating **cell**." That word forces three simultaneous requirements — heritable information, energy/matter-flux capture, and a growing/dividing compartment — and, critically, a mechanism by which all three reproduce *together*. Any answer that solves one requirement and imports the other two has not answered the question; it has relocated it. This reframing did most of the work: it turns "pick the winning camp" into "find the coupling none of the camps supplies."

## 2. Mapping the camps to find the true gap

Reading the major frameworks against those three legs (the scoring in `figures/camp_comparison_table.csv`) showed a consistent pattern: every framework is strong on one or two legs and *assumes* the rest.

- RNA-world / ribozymes: information, but monomers and compartment imported.
- Fe–S / metabolism-first: flux capture, but no heredity, and a proven evolvability ceiling.
- Alkaline-vent / chemiosmotic: a genuine, sustained, geochemically-supplied energy source and the closest tie to LUCA's reconstructed physiology — but the "leaving-home" problem when a closed organic membrane loses the free proton gradient.
- Szostak protocell: an elegant genome→division coupling, but both nucleotides and lipids fed from outside.
- GARD / compositional genome: heritable composition, but no fitness readout, hence no open-ended evolution.
- Gánti chemoton: the correct *formal* three-way coupling, but with the coupling coefficients postulated rather than explained.

The gap that survived this mapping was not "which molecule came first." It was **the coupling itself** — and specifically two under-examined tensions:

1. **Synchronization is inserted by hand.** Growth-and-division models need genome-replication rate and membrane-growth rate to match, or the protocell dilutes to death or bursts. Current models supply that balance as a parameter or an assumed external lipid feed (Taneja & Higgs 2025). Nobody gives a physical reason the two rates track each other.
2. **The compositional genome cannot be selected on.** Compositional inheritance is heritable but has no quantitative fitness readout, which is exactly why it caps evolvability (Vasas et al. 2010).

## 3. The honest pre-emption check that redirected the idea

An early candidate "novel" idea was a shared thioester → acetyl-phosphate node feeding both genome activation and membrane growth. A direct check of the literature showed this is **already published**, and it would have been a mistake to claim it:

- Whicher et al. (2018) already proposed acetyl phosphate as a primordial currency "coupling carbon and energy flux," showed it forms from thioacetate in water, and showed it phosphorylates ribose→R5P, adenosine→AMP and ADP→ATP — while explicitly reporting that it did **not** polymerise amino acids or nucleotides.
- de Duve (2003) had already placed thioesters at the centre of primitive energy transactions.
- Cho et al. (2024) already demonstrated the thioester→membrane branch experimentally (cysteine + short-chain thioesters → diacyl lipids → vesicles).
- Kitadai et al. (2021) already showed thioester formation from CO + methanethiol on nickel sulfide under vent-like conditions.

So "one shared acetyl currency feeds genome + membrane" was **not** available as a novel claim. Rather than dress it up, I took the shared currency as *given* and asked what, given it, is still unsolved. The answer was the two tensions above — and they suggested their own resolution.

## 4. The move: fuse the two tensions into one variable

The two open tensions have a common shape. Tension 1 asks for a *physical* reason two rates track; tension 2 asks for a *fitness readout* on composition. Both are solved at once if the compositional genome is made to **physically control the branch point of the shared currency**:

- Define **r = (flux to membrane) / (flux to genome activation)** at the shared acetyl node.
- Let membrane composition set *r* (composition is what GARD already inherits).
- Then *r* has a fitness readout — **division success** — because a mistuned *r* either dilutes the cell's contents or bursts it. That directly supplies what compositional inheritance lacked (tension 2).
- Let membrane tension/pH — quantities the growing polyanionic genome itself drives, via the Szostak osmotic ratchet — feed **back** on the branch ratio. Then flux is automatically routed to whichever subsystem is rate-limiting, and synchronization becomes an emergent attractor rather than an assumed constant (tension 1).

Sequence heredity then has a clear reason to appear *after* this system is already alive-ish and under selection: it stabilizes the already-selectable partition phenotype against the low fidelity of compositional inheritance. This inverts the usual "genome-first" ordering into "genome recruited to protect a working metabolic phenotype."

## 5. Grounding the fossil prediction

If the shared acetyl node is real ancient chemistry, its logic should be fossilized in conserved metabolism. This was checked against sequence/annotation databases rather than asserted: the thioester ⇌ acyl-phosphate ⇌ phosphoanhydride relay is carried today by phosphotransacetylase (Pta, UniProt P0A9M8, EC 2.3.1.8), acetate kinase (AckA, UniProt P0A6A3, EC 2.7.2.1) — both with experimental (IDA) activity annotations — and CO-dehydrogenase/acetyl-CoA synthase (UniProt P27988, EC 2.3.1.169) in the Wood–Ljungdahl pathway, with the acetyl/thiolase hub sitting at the TCA core in Reactome (R-HSA-71403). The prediction is therefore anchored in extant biochemistry, not invented.

---

## 6. Why the central claim is novel and not obvious

**The central claim:** the first heritable, selectable information was the *flux-partition ratio* of a shared metabolic currency, stored in membrane composition and read out as division timing; and the protocell's own membrane mechanics synchronize genome replication with compartment division.

**Why it is novel.** Every component idea exists in the literature, but the specific identification at the heart of the claim does not. The novelty is an *identity statement* between four things the field keeps separate:

> Gánti's coupling coefficient  =  the flux-partition ratio *r* of a shared currency  =  GARD's compositional "genome"  =  the trait selection acts on.

- The **thioester/acetyl-phosphate literature** (de Duve; Whicher; Pinna) treats the shared currency purely as *energy*. It never treats its branch ratio as *information*. Making *r* the genome is not a rephrasing of their claim; it assigns a role (heritable set-point) to a quantity they only ever treated as a throughput.
- The **GARD literature** (Segré; Lancet) treats composition as a self-templating genome but is stuck on its lack of evolvability (Vasas et al. 2010). The novel move supplies the missing fitness readout by coupling composition to metabolic flux and division timing — a coupling GARD does not contain.
- The **chemoton** (Gánti) has the correct three-way coupling but leaves its coupling coefficients as free parameters. Deriving one of them from membrane mechanics is exactly the step Gánti did not take.
- The **Szostak protocell** work has the osmotic ratchet that couples genome to division, but uses it only to drive *growth*; feeding it *back* onto a metabolic branch point to control *partition* — and thereby to synchronize the subsystems — is not part of that program.

**Why it is not obvious.** The obvious paths are the ones the field actually took: pick a molecule to come first (RNA, metabolism, membrane) and bolt the rest on; or, having accepted a shared currency, treat it as an energy-supply detail. Both of those keep information, energy and compartment as *separate* modules to be connected later. The non-obvious step is to refuse that modularity and instead let a *single physical variable* — where the flux goes — simultaneously be the genome, the metabolic control point, and the thing division timing selects on. It is counterintuitive because it puts the "genome" in the membrane's composition and the "readout" in the cell's mechanical state, rather than in a sequence; and it makes synchronization — usually the hardest thing to arrange — fall out for free as a consequence of the growth it is trying to synchronize. That inversion is the content of the hypothesis, and it is not entailed by any single camp's premises.

**What would make it wrong.** The claim is not safe: it rests entirely on membrane tension/pH being able to bias the acetyl branch ratio. If that gating does not exist (the kill criterion in `result.md` §6), the identity statement breaks and the picture reverts to the published shared-currency account. That exposure is deliberate — it is what makes the claim a hypothesis rather than a synthesis.
