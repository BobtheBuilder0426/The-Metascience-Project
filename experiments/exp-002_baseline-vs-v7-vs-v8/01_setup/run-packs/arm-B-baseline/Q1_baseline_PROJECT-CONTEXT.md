<!-- exp-002 · Arm B (baseline blank CS) · Q1 PROJECT CONTEXT (paste into the CS project's Agent Context).
     The block between the ``` fences is what you paste. It is the exp-002 safety guardrail (byte-identical fixed text,
     shared with the L7/L8 CS projects) PLUS a delivery-only output-location stanza. Fill the ONE folder path, paste,
     then paste the question (arm-B-baseline/Q1_baseline_PASTE-question.txt) into the chat and attach any materials. -->

# exp-002 — Arm B (baseline) — Q1 — CS project context (guardrail + delivery)

**What this is.** The Agent Context for the blank-CS baseline session that answers Q1 (category 1 — 1C-metabolite / muscle-rejuvenation method (paper attached)).
Paste the fenced block below verbatim into the Claude Science project's **Agent Context / project instructions**.

**Before you paste — fill ONE thing:** the absolute path of the folder you created and granted to this project
(replace the `<<FILL IN …>>` slot). Everything else is fixed and must not be edited — the guardrail text is
byte-identical across all three arms (B / L7 / L8); only this run's identity slot differs, exactly as the loop arms
fill their own `AL-<name>` identity.

**Fairness note.** The **safety guardrail** (the `# Scope & Safety` section) is the byte-identical fixed guardrail every
arm receives. The **`# Where to deliver your results`** stanza is *delivery only* — it is the baseline's equivalent of
the file-placement a loop driver performs automatically for L7/L8 (which write `presentation/` into their own granted
run folder). It carries no performance tips and no hint about the answer, so it cannot advantage the baseline; it only
ensures the output lands where the operator can collect it.

```
# Scope & Safety — applies to every response in this project

You operate inside ONE Claude Science project and ONE attached folder — and nothing else.

This run's scope →  project "exp002-baseline-Q1"  ·  folder "exp002-baseline-Q1" (<<FILL IN: absolute path to the folder you created + granted for this baseline run, e.g. ~/cs-workspaces/exp002-baseline-Q1>>)

- Stay in scope. Do all work in THIS project. Read and write only the ONE folder named above;
  it is your only file destination.
- Everything else is off-limits. Never open, read, edit, list, or reason about any other project,
  any other attached folder (even if it is visible), any other chat or session, or any file outside
  the folder above. Visible ≠ yours.
- Do not change attachments. Never add, remove, rename, or re-point a folder grant; use the one
  already attached.
- When in doubt, ask. If a task seems to need anything outside this scope, stop and ask the human
  in chat instead of reaching outside it.

# Where to deliver your results (file-location only — says nothing about what to answer)

When you produce the "presentation folder" the question asks for, create it INSIDE the one folder
named above (your only file destination), with exactly this shape:

    <the folder named above>/presentation/
        result.md
        reasoning.md
        figures/
        sources.md
        process_trace.json

Write your deliverables only there, so they can be collected. This is a delivery/location note — it
neither adds to, nor changes, what the question asks or how it should be answered.
```
