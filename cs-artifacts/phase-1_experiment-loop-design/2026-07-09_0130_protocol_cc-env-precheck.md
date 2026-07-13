<!-- WHAT THIS FILE IS: the Phase-1 environment PRE-CHECK PROMPT that Claude Science (CS) hands to a BLANK Claude Code
     (CC). The operator pastes the fenced block below into a fresh CC session opened on the shared folder. CC runs the
     read-only probes and writes back a structured report + a labbook entry, which CS needs before designing the
     Agentic Loop's runnable core. HOW TO USE (operator): open a blank Claude Code in the shared folder, paste the
     block between the ==== markers, let it run, then tell CS "CC pre-check done". CS reads the report file. -->

# exp-pre — CC-side environment pre-check prompt  [CS-authored, CC-run]

**Why this exists.** The Agentic Loop is a blank Claude Code (CC) that drives Claude Science (CS) in a closed cycle by
**controlling the CS browser tab (Chrome control)**, pulling each experiment setup out to a local runtime area, running
it, and reporting back. Before CS can design that runnable core, CS must know what the CC side can actually do. This
prompt makes a blank CC characterize its own environment and report back. It is **read-only and bounded** — no installs,
no heavy jobs, no secrets printed, and it must not crash the shared 7.7 GB machine.

**Operator:** open a fresh Claude Code session **in the shared folder**, then paste everything between the `====` lines.

```
==================== PASTE INTO A BLANK CLAUDE CODE ====================
You are a blank Claude Code (CC) doing a one-time ENVIRONMENT PRE-CHECK for a partner system, "Claude Science" (CS),
in this shared project folder (the Metascience Project). CS will read your report to design an automated research loop in which a
Claude Code like you DRIVES Claude Science by controlling its browser tab. Your job now is ONLY to characterize this
environment and report back. Be precise, honest, and concise. If something is unavailable or you are unsure, say so —
"unknown / could not verify" is a valid and useful answer. Do NOT guess.

HARD RULES (obey all):
- READ-ONLY probing. Do NOT install packages, clone repos, download models, or run heavy/long jobs.
- Do NOT print, echo, or write any secret (API keys, tokens, cookies). Report only PRESENT / ABSENT and where it lives.
- Keep it light — this is a shared ~7.7 GB machine also running a browser and CS. No parallel heavy work.
- Prefer built-in checks (version flags, `which`, a trivial round-trip). Time-box the whole thing to a few minutes.
- Everything in ENGLISH.

RUN THESE PROBES and record the result of each (command tried + what you observed):

A. CLAUDE CODE ITSELF
   1. `claude --version` (or equivalent); which model is active (Sonnet/Opus/other); is this a Max/Max-20x plan?
   2. Can you spawn parallel sub-agents / a sub-agent panel (Task tool)? How many, realistically, on this machine?
   3. Which skills are available to you (`/`), and which MCP servers/connectors are configured on the CC side?
   4. Is headless `claude -p` available? Does a trivial `claude -p "reply OK"` work? Rough sense of remaining
      free-allowance (fine to say "unknown", just note if it ran or was blocked).

B. THE DRIVE CHANNEL — CHROME CONTROL OF THE CS TAB  (THE LOAD-BEARING CAPABILITY)
   5. Is the Claude Chrome plugin/extension installed and connected to this Claude Code? How is browser control invoked?
   6. Can you actually: (i) see/read the Claude Science browser tab, (ii) locate the message composer, (iii) type text
      into it, (iv) submit (Enter/Send), and (v) read CS's response back? Test what you safely can against the CS tab
      (e.g. type a harmless "ping — reply with PONG" and read the reply). Report which of (i)-(v) worked.
   7. TURN-COMPLETION: how do you tell when CS has FINISHED responding (so you read the whole answer, not a partial
      stream)? Describe the signal you'd use and whether it's reliable.
   8. APPROVAL CARDS: when CS's UI shows a permission card (folder access / network host / run-code / plan approval),
      can you SEE it and CLICK approve? This is critical for an unattended loop — report yes/no/partial + any limits.
   9. Rough round-trip latency for one send→receive cycle, and any reliability caveats or failure modes you hit.

C. LOCAL RUNTIME AREA  (where you pull a setup OUT to run it — NOT the shared network mount)
   10. Are you on Windows-native, or inside WSL (Ubuntu)? `uname -a` / `ver`. Give a concrete path to a local runtime
       area OUTSIDE the shared folder that you can use.
   11. Versions present: python3 (+ can you make a venv & pip install?), node, git. Disk free + rough RAM headroom.
   12. Internet from the runtime: can you reach the web / pip / a public API? (Test one lightweight GET; don't download.)
   13. Can you read the shared folder AND write a file back into it that CS will see? Create a tiny test file
       `phase1-cc-bridge-test.txt` at the repo root with one line, confirm it's there, then delete it.
   14. Can you append to `LABBOOK.md` atomically (the repo asks for a Linux-native append via WSL rather than writing
       over the file-share)? Confirm the method you'd use — do NOT append a real entry yet except the one in step 18.

D. CODEX (2nd model — an improvement category CS will test)
   15. Is Codex available to you? How is it invoked (CLI command / API / IDE)? Is it authenticated?
   16. Trivial round-trip: ask Codex to "reply with the word CODEX-OK". Did it work? Note latency / any auth blocker.

E. API ACCESS (the $200 credits — availability only)
   17. Is an Anthropic API key present in the environment (e.g. an env var)? Report PRESENT/ABSENT and where — do NOT
       print it. Note whether a trivial API call would be possible if CS later chooses to use it.

WRITE YOUR REPORT:
- Create ONE file at the repo root named EXACTLY: `2026-07-09_report_cc-env-precheck.md`
- Use this structure, with a short verdict per line — WORKS / PARTIAL / FAILS / UNKNOWN — plus one line of evidence:
    # CC-side environment pre-check report  [CC] — <date/time CEST>
    ## A. Claude Code itself
    ## B. Drive channel (Chrome control of the CS tab)   <-- most important; be specific
    ## C. Local runtime area
    ## D. Codex
    ## E. API access
    ## Blockers / risks for an unattended CS-driving loop
    ## Anything surprising or better than expected
- Then append ONE labbook entry to `LABBOOK.md` (append-only; newest at the bottom; do not edit past entries), tagged
  [CC], next id after the last LB-NNN, headed "CC-side environment pre-check", with fields Goal / What & how / Outcome /
  Data-artifacts (name this report file) / Sources (none). Keep it to a few lines.
- Finally, in your chat reply to the operator, give a 5-line summary + the single biggest blocker (if any), and say
  "CC pre-check done — CS can read 2026-07-09_report_cc-env-precheck.md".
======================================================================
```

## What CS will do with this
CS reads `2026-07-09_report_cc-env-precheck.md` and uses it to fix the **runnable core** of the v0 Agentic Loop:
whether the drive channel can run unattended (approval-card handling is the key risk), what the local runtime can
execute, whether Codex and `claude -p` are real (they gate two improvement categories), and which connectors a test
set may assume. If the drive channel is only PARTIAL (e.g. CC cannot clear CS approval cards autonomously), CS will
design the loop with explicit human-relayed hand-offs at those points (per DOCUMENTATION.md §4b) rather than assume
full autonomy.
