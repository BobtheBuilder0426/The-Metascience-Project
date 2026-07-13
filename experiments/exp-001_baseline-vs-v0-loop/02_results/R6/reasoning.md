# Reasoning: how I arrived at the Cofactor Ratchet

This document is the line of thought, including the wrong turns. The polished case is in `result.md`; this is the workshop floor.

---

## 1. Framing the problem so it is answerable

The prompt — "how did a soup of lifeless molecules organise into the first self-replicating cell?" — is the biggest open question in biology, and it will not be *solved* in a session. So I set a reachable target: produce a **novel, plausible, mechanistically specific, and testable** hypothesis, argued from real and current chemistry, with the quantitative claims actually computed rather than asserted.

"Novel" needed a definition I could hold myself to. Restating the RNA world, or the lipid world, or hydrothermal vents, is not novel. Novelty here means a **new architecture connecting known parts**, plus **at least one new, timed, falsifiable transition** the existing models don't articulate.

I began by surveying the current literature (2018–2025) across five sub-areas: active/proliferating coacervates, compositional inheritance (GARD), the coacervate→vesicle transition, cofactor "molecular fossils," and in-droplet nucleotide chemistry. Two observations from that survey did the most work:

- Active coacervate droplets **already** grow and divide by physics alone — compartment + a growth cycle come essentially for free.
- The old "chicken-and-egg" framing (heredity vs metabolism vs compartment) quietly assumes they are *separate objects*. A droplet is a counterexample: it is all three at once, trivially, when it is simple.

That reframing is the hinge of the whole hypothesis. The moment you stop asking "how do three things arise and combine?" and start asking "how does *one* droplet grow a heredity channel?", the problem shrinks to a single hard step.

## 2. Locating the single hard step

If compartment and metabolism are cheap (a fuelled droplet has both), the expensive thing is **heritable information that can grow without bound** — a genome. So I asked: what is the *cheapest* heredity a droplet can have, and why isn't it enough?

The cheapest heredity is **compositional** (GARD): mutually-catalytic contents settle into attractor states that survive division. This is real and gives selection with no polymer. But the literature (Vasas & Szathmáry 2010) says compositional systems have limited evolvability. If that limitation is real and quantifiable, then it *defines the moment* a sequence-based heredity becomes worth having — and that moment is my candidate for the one genuine transition.

This is where the hypothesis stopped being a list of ingredients and became an argument with a shape: **a ceiling, and a handoff at the ceiling.**

## 3. Choosing the pivot molecule

For the handoff to be more than "and then RNA showed up," I needed a physical reason the droplet's own chemistry would *produce* templates. The cleanest answer: make the metabolic catalysts themselves be nucleotides. Then templates are a natural side-product of concentrating the metabolism.

This is where cofactors became irresistible. The fact that ATP, NAD, FAD, CoA, SAM all carry a nucleotide (usually adenosine) that does no chemical work is a classic "molecular fossil" argument (White 1976; Goldman & Kaçar 2021). I had been treating cofactors as a side-topic; I realised they are the **bridge**: the same molecule is metabolism (it catalyses), compartment-growth (its reactions build the droplet), and heredity-raw-material (it is a nucleotide). One molecule class ties all three faces together. That is the novel core, and it named the hypothesis.

## 4. Deciding to compute, not assert

Three claims in the argument are quantitative and therefore had to be *shown*, or the hypothesis is just a story:

1. Composition is genuinely heritable across division. → simulate GARD, measure parent–offspring similarity vs a random-assembly null.
2. Compositional heredity has a **ceiling** that a sequence does not. → census the number of distinct composomes vs repertoire size; compare to 2N sequence bits.
3. A sequence handoff **breaks** that ceiling. → an evolving-population simulation with a control that never gets the handoff.

I made a deliberate methodological choice: keep the models **abstract and transparent** rather than pseudo-realistic. The point is to isolate the *logic* (does a ceiling exist? does a sequence channel break it?), and an abstract model that clearly does or doesn't show the effect is more honest than an elaborate one whose result depends on buried parameter choices.

## 5. The wrong turns (kept on the record)

**Wrong turn A — parallelism.** My first census run tried to parallelise with functions defined in the interactive kernel; they can't be pickled, so the pool died. Fix: move the model into an importable module (`gard_model.py`). Then the kernel couldn't find the module because its working directory wasn't the workspace; fix: add the workspace to `sys.path`. Mundane, but it is part of the actual record.

**Wrong turn B — a bad channel model.** For the handoff I first built a "compositional information channel" that stored bits as independent enriched/baseline molecular features and computed a transmitted-information capacity. The numbers came out non-monotone and noisy (bits going up and down with feature count) because the abstraction — independent binary features sharing a molecular budget, read through a binary-symmetric-channel capacity formula — was simply the wrong model for weak, correlated compositional features. I **discarded it** rather than dress it up. The honest ceiling was already sitting in the census result (number of attractors ≈ a few, not growing with N), which is exactly the Segré/Lancet/Vasas finding. So I rebuilt the handoff on the census-derived ceiling plus a proper temporal population simulation. Lesson I applied: when a model misbehaves, prefer the result that coincides with an independently-established literature finding, and don't ship a metric you can't defend.

**Course-correction C — the census was noisy.** With only 2 catalytic matrices per repertoire size, the exact composome counts jumped around (1–9). Rather than over-claim precise numbers, I present the robust qualitative fact — the count stays in the single digits and does **not** scale with N — which is all the argument needs and all the data supports.

## 6. Why the pieces reinforce each other

Once the ceiling and handoff were solid, the rest of the chain assembled itself, and each classic objection turned into a *feature*:

- "Copying is too error-prone for a genome" (Eigen) → true for a *long* genome, but the first template only needs a few sites to beat the compositional ceiling, and a few-site template survives even sloppy copying (Figure 4). The Eigen threshold, usually cited as an obstacle, becomes the **ratchet's escapement**: better copying → longer genome → better copiers → better copying.
- "You still need a membrane" → the active coacervate already has an interface, so the membrane is a late *upgrade* selected by dilution/rain stress, not a prerequisite. This is why I put it last.
- "Which camp is right, replicator-first or metabolism-first?" → both, at different clicks of the same ratchet (Table 2).

## 7. Guarding against confabulation

A hypothesis paper lives or dies on whether its citations are real. I did not trust remembered DOIs. Every identifier was either returned by an OpenAlex search or verified by a direct DOI lookup whose returned title I checked against the paper I intended to cite. Two DOIs I guessed from memory (an Oparin and an Eschenmoser reference) came back as unrelated papers — the check caught them, and I dropped them rather than cite blind. Oparin (1938) and Haldane (1929) have no clean DOIs and are cited as the classic monograph/essay they are.

## 8. What I chose *not* to claim

I resisted three temptations that would have made the story cleaner but less honest:

- I did not name a specific first cofactor-catalysed growth reaction. I don't know it; I argue only that it is prebiotically reachable.
- I did not present the simulations as realistic chemistry. They are logic demonstrations, and I say so.
- I did not hide the handoff as the weakest-constrained link. I flagged it as *the* experiment to do, because a hypothesis is more valuable when it points at its own soft spot.

The result is a hypothesis whose one hard step is small, timed, and testable — which is the most one can honestly ask of an origin-of-life proposal today.
