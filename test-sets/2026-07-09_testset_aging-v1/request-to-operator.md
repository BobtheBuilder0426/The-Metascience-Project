<!-- WHAT THIS IS: a concrete, idiot-safe request to the operator (domain expert, aging biology) to confirm/replace the test-set
     questions the Experiment Loop will run on. HOW TO USE (the operator): read the 4 draft questions in README.md, then answer
     the short block below — inline is fine. This makes your later evaluation more meaningful (GOAL S4). Keep it lean. -->

# Request to the operator — confirm the test-set questions (5-minute ask)  [CS → the operator]

Hi the operator — the Experiment Loop needs a small, fixed set of **research questions** that both arms (the raw baseline and
the optimized loop) will answer *word-for-word identically*. Domain = your turf: **aging / metabolism / mitochondria**,
so your judgment of "novel + sensible" is the ground truth.

I've drafted **4 seed questions** (see `README.md` in this folder) spanning three difficulty tiers. They're
hypothesis-generation questions (not lookups), each answerable/gradeable against real literature, and each rewards a
system that uses many Claude Science databases well.

**What I need from you (pick whichever is least effort):**

1. **Fastest:** just reply **"Q1–Q4 look good"** (or which subset), and I'll freeze them.
2. **Better:** for any question, tweak the wording, or tell me the right *depth* (too easy / too hard for a real
   research contribution in your field).
3. **Best (if you have 5 min):** give me **1–3 questions from your own current thinking** — something where you
   genuinely don't know the answer and where a *truly novel, sensible* hypothesis would impress you or a reviewer.
   These make the "did the loop produce genuinely novel science?" test real. One sentence each is enough.

**Two quick calibration questions (one line each):**
- **A.** For a hypothesis in your field to count as **"genuinely novel, not just recombined"** — what's your bar? An
  example of something that *would* impress you vs. something that's obvious-but-dressed-up helps me calibrate the metric.
- **B.** For **"plausible / sensible"** — what instantly makes you distrust an AI hypothesis (the tells of AI-slop in
  aging biology)? I'll encode these as automatic plausibility red-flags.

**Format:** reply inline here or wherever is easy; I only need text. No data downloads needed for this step. If you'd
rather I just run with Q1–Q4, say so and I'll proceed — you can still adjust after seeing exp-001.

*(Why this matters: your questions + your novelty bar become the yardstick the whole loop is optimized against, and
your qualitative feedback — not just scores — is what we capture per GOAL success-dimension 5.)*
