# Hackathon -- Built with Claude: Life Sciences (the Metascience Project)

> **Ground file / single source of truth for this project.** Every session, agent, and Claude Science run reads this first so all work points the same direction.
> **Source:** official Participant Guide (operator-provided 2026-07-08, authoritative). | **Last update:** 2026-07-08

---

## 0. Scope & separation (read first)

- **the Metascience Project is a standalone, independent project.** It is built from scratch for this hackathon.
- **No overspill with a separate project/a separate project or any other workspace project.** No cross-pollination of code, data, framing, or artifacts -- in either direction -- **except on an explicit, narrow operator instruction**. When unsure: keep separate, ask.
- This separation is also enforced by the hackathon's own **"New Work Only"** rule (see §4).

## 1. What this is (snapshot)

| Field | Value |
|---|---|
| Event | Built with Claude: Life Sciences |
| Organizer | Anthropic virtual hackathon, in partnership with **Gladstone Institutes**; hosted on the Cerebral Valley (CV) platform |
| Format | Global, **virtual / remote** |
| Our status | **ACCEPTED** |
| Our track | **Researcher Track** ("Build From the Bench", via **Claude Science**) |
| Our team | **Solo** (rules allow up to 2) |
| Prize pool | $100k in credits (see §8) |

**Why the work matters:** produce a discrete, reproducible scientific result (a finding, a trained model, or an analysis others can rerun) that starts from a real biological question and is answered end-to-end with Claude Science -- something judges trust and other researchers can build on.

## 2. Schedule (all times **ET**; today = Wed Jul 8)

| When (ET) | What |
|---|---|
| Tue Jul 7, 12:00 | Kickoff (rules/prizes/judging) + hacking begins |
| **Wed Jul 8, 12:00-13:00** | **Live Session 1 -- Claude Science overview** (A. Tarashansky, Anthropic) |
| Fri Jul 10, 12:00-13:00 | Live Session 2 -- genome-to-inference PPI screening (S. Silas, Gladstone) |
| daily, 17:00-18:00 | Anthropic office hours (`#office-hours`) |
| Sat-Sun Jul 11-12 | Hacking continues |
| **Mon Jul 13, 21:00** | **SUBMISSIONS DUE** via CV platform |
| Tue-Wed Jul 14-15 | Round 1 judging (async) |
| Thu Jul 16, 12:00 / 13:30 | Final judging (top 6) / closing ceremony (top 3) |

> ⏳ **Deadline in local time: Mon Jul 13, 21:00 ET = Tue Jul 14, 03:00 CEST** [conversion, ET+6h]. From today that is **~4.5 days**.

## 3. Our track -- Researcher Track: "Build From the Bench"

Using **Claude Science**, start from a biological question you have been thinking through, then find the existing datasets and tools needed to answer it. Submit something **discrete** -- a finding, a trained model, an analysis others can reproduce -- and **show how Claude Science got you there**.

**Optional Gladstone starting datasets (not required):**
1. New drug targets in CD4+ T-cell **Perturb-seq** data (A. Marson lab).
2. Predict a **noncoding variant's** effect on chromatin in a cell type of interest -- run Corces-lab pretrained brain models, or train your own with **ChromBPNet** on any ENCODE ATAC-seq experiment.
3. Genome regions **deeply conserved across mammals but rapidly changed in humans** -- Pollard-lab **Zoonomia** constraint scores + Human Accelerated Regions.

## 4. Rules (disqualification risks)

- **Open Source:** everything submitted must be open-sourced under an approved OSS license.
- **New Work Only:** built from scratch **during** the event, no prior work. *Researchers:* starting from an existing question + public datasets is fine, **but the analysis must happen during the event.**
- **Team size:** up to 2 members (we go solo).
- **Banned / disqualified:** anything violating legal, ethical, or platform policy; using code/data/assets you do not have rights to.

## 5. Deliverables (required for submission)

- **Demo video** -- 3 minutes **max** (YouTube / Loom / similar).
- **Open-source artifact** -- GitHub repo, notebook, **or** research write-up.
- **Written summary** -- 100-200 words.
- Submitted via the CV platform (submission page linked in the guide) by the **Jul 13, 21:00 ET** deadline.

## 6. Judging

**Stage 1 -- async (Jul 14-15):** judges score submissions independently on the criteria below; scores aggregate to the Top 3 per track for the final.
**Stage 2 -- live (Jul 16, 12:00 ET):** each finalist's 3-min pre-recorded demo plays; judges deliberate; winners announced at the 13:30 closing.

| Criterion | Weight | For a Researcher project |
|---|---|---|
| **Demo** | **30%** | Working, compelling, trustworthy result; genuinely cool to watch |
| **Impact** | 25% | Is this a finding/analysis others can build on? Fits the track's problem statement? |
| **Claude Use** | 25% | Creative, non-obvious use of Claude (Science/Code); surfaces surprising capability |
| **Depth & Execution** | 20% | Pushed past the first idea; sound, refined, real craft (not a quick hack) |

> Demo is the single largest weight -- budget real time for it. The written summary + repo/notebook must let a judge reproduce and trust the result.

## 7. Anthropic resources (curated; full list in the guide)

- **Claude Science:** Get Started + Docs + product overview + announcement blog.
- **Claude Code:** Quickstart + Docs + best-practices.
- **API / platform:** Claude API Quickstart, Models Overview, **MCP Docs**, **Agent Skills Docs**.
- **Method blogs:** Building Effective Agents; Building multi-agent systems (when/how); Effective Context Engineering; Extending Claude with skills + MCP servers.

## 8. Prizes

| Research Track (usage credits) | Amount |
|---|---|
| 1st | $30,000 |
| 2nd | $10,000 |
| 3rd | $5,000 |
| **Gladstone Institutes Award** | **$10,000** -- research project with the most potential to advance the field, hand-selected by Gladstone (we are eligible) |

*(Builder Track has an equivalent 30k/10k/5k in API credits -- not our track.)*

## 9. Community

- **Discord:** https://anthropic.com/discord -- get the **Hackathon Participant** role via `#hackathon-access` (ping `@CV` if not assigned).
- Channels: `#office-hours`, `#questions`, `#announcements`.

## 10. Open decisions (ours, not yet made)

1. **The biological question + (optional) dataset** for our Researcher deliverable.
2. **The discrete deliverable shape:** finding vs. trained model vs. reproducible analysis -- and its acceptance/reproducibility criteria.
3. **Open-source repo + license**, initialized from scratch during the event.
4. **Demo + 100-200w summary plan** (Demo = 30%; plan early, do not leave to the last hour).

---

*the Metascience Project ground file. Update this when the official guide changes or a project-level decision is locked.*
