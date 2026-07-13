# the Metascience Project -- Resources (what CS + the Agentic Loop may use)

<!-- WHAT THIS FILE IS: the catalog of everything available to Claude Science (CS) and to the Claude Code setups it
     builds -- tools, compute, access, and the humans/agents that can help. This resources/ folder is ALSO where the operator
     puts things CS asks him for (papers, data, profiles). HOW TO USE: read this to know what you can rely on and how to
     request more. Self-contained; nothing here points outside this repo. English. -->

## 1. Compute / environment (the machine everything runs on)

| | |
|---|---|
| Host OS | Windows 10 Pro (build 19045) |
| CPU | Intel i5-1135G7 -- 4 cores / 8 threads |
| RAM | **7.7 GB total** -- free fluctuates (~1-3 GB); measured 2.64 GB free @ 2026-07-08 18:09 |
| GPU | Intel Iris Xe (integrated) -- **no dedicated GPU** |
| Disk | ~350 GB free (ample) |
| Linux side | WSL (Ubuntu), shares the host CPU/RAM; python3 available |

**Hard constraints (design around these):** RAM is tight and shared -- CS, Claude Code, and a browser all run on this
one machine. So: **bounded concurrency** (do not spawn many heavy sessions at once), **lean local footprint**, **no
heavy local ML training** (integrated GPU). Lean on the cloud/API/web for heavy lifting. **Do not crash the machine** --
it is the same machine CS and Claude Code run on.

## 2. Infrastructure / topology (so you can design realistically)

- **Claude Science runs on Linux; Claude Code runs on Windows.** They share ONE folder -- **this repo** -- through a
  bridge, so both read and write the same files. CS reaches it natively; Claude Code reaches it through a Windows bridge.
- **Heavy execution does not run in-place from the shared folder** (it is a slow network mount). Claude Code pulls a
  setup OUT to a local runtime area on the Windows side, runs it there, and copies results back into this repo.
- **The labbook (`../LABBOOK.md`) is the top ground truth**; everything is documented crash-recovery-proof.

## 3. Tools & access available

- **Claude Code (Max 20x subscription)** -- the agentic coding environment; runs the setups; can spawn sub-agents/panels.
- **Claude Science** -- the analysis platform (see `claude-science-handbook.md` in this folder for full capabilities).
- **Claude Chrome plugin (Claude Code side)** -- lets **Claude Code** control a real browser; this is **how CC drives the Claude Science tab** (the drive channel). It is a Claude Code capability, not a Claude Science one.
- **Full web access** -- CS, Claude Code, and all their agents can browse the web.
- **`claude -p`** (headless Claude Code) -- usable only within the subscription's free monthly allowance.
- **$200 Claude API credits** (Claude Console, verified) -- for API-based calls; relevant only if Claude Science chooses to use the API.
- **Codex (Claude Code side only)** -- a 2nd, different AI model available to Claude Code (not to Claude Science); can be switched on any time (e.g. for panels / cross-model review / multi-subagent spawns). **Start angles worth exploring here:** Karpathy's "LLM council" (several models deliberate together) + OpenRouter's model-fusion approach.
- **Claude Deep-Research** (the chat research tool) -- the operator can run as many as help; just ask him with a precise question.

## 4. Literature & data

- **`claude-science-handbook.md`** (this folder) -- the full Claude Science documentation, assembled.
- **Publications:** the operator can download publications/supplements that are allowed for research use and NOT behind a
  paywall, when they are not otherwise reachable. Ask him.
- **Starter papers:** a small starter knowledge base of papers will be added to this folder (pending -- the operator provides
  them; each will be registered in `../SOURCES.md`).
- Every source used must be registered in `../SOURCES.md` (S-NNN) and cited by number.

## 5. People / agents you can task

- **the operator (human, domain expert).** Profile: `operator-profile.md` in this folder (pending). Expertise: PhD aging research;
  wet-lab + in-vivo; molecular metabolism, mitochondria, exercise + aging biology; molecular medicine; translation to
  the clinic; drug discovery. CS should think about how to use the operator best for this goal -- not only number-ratings, but
  real qualitative input + feedback. the operator can also **copy-paste** things in when told exactly what/when/where
  (idiot-safe, not excessive).
- **the assistant (the Mission-Control Claude Code).** CS can task the assistant to **prepare/work up data** and to **help analyse the
  blank-CC runs** (the assistant investigates a run and pulls the data back into this repo). the assistant analyses + reports; he does
  not evaluate.

## 6. How to request something from the operator

CS can ask the operator anything it needs. the operator provides it by (a) downloading allowed, non-paywalled material, (b) copy-pasting
exactly what is asked for (tell him precisely what, when, and where -- keep it idiot-safe and not excessive), or (c)
answering as the domain expert.

---
*This folder also holds: `claude-science-handbook.md` (the CS docs), `operator-profile.md` (pending), and starter papers (pending).*
