<!--
CLAUDE SCIENCE HANDBOOK - assembled reference
=============================================
WHAT THIS FILE IS:
  A single, self-contained handbook assembled from the 24 official Claude Science
  documentation pages (claude.com/docs/claude-science/*), condensed into a usable
  operator reference for scientific work with Claude Science + Claude Code.
  Content is faithful to the official docs as fetched on 2026-07-08. Nothing is invented.

HOW TO USE:
  - Start at the Table of Contents and jump to the section you need.
  - Flow: what it is -> setup -> data/artifacts -> tools -> connectors/skills ->
    literature -> compute -> reviewer -> ops -> admin/legal -> limits -> glossary -> changelog.
  - Commands, flags, connector names, and tables are preserved where they matter operationally.
  - This is a SNAPSHOT. For authoritative, current docs see the URLs in the Sources section.
  - Self-contained: references only Claude Science's own docs and app paths
    (e.g. ~/.claude-science); nothing outside this repository.

CRASH RECOVERY: If a session is interrupted, this file is the complete reference -
  no other files are needed to understand Claude Science's capabilities and setup.
-->

# Claude Science Handbook

An assembled, condensed reference for Claude Science - Anthropic's local AI workbench for scientific research. Compiled from the official documentation (fetched 2026-07-08).

## Table of Contents

1. [What Claude Science Is + Core Concepts](#1-what-claude-science-is--core-concepts)
2. [Setup: Enable, Install, Windows/WSL](#2-setup-enable-install-windowswsl)
3. [How It Works With Your Data (Artifacts, Annotations, Provenance)](#3-how-it-works-with-your-data-artifacts-annotations-provenance)
4. [Tools & Environments](#4-tools--environments)
5. [Connectors & Skills (+ Custom Connectors)](#5-connectors--skills--custom-connectors)
6. [Literature Access](#6-literature-access)
7. [Compute: Local GPU, Cloud Storage, Providers, Remote Clusters](#7-compute-local-gpu-cloud-storage-providers-remote-clusters)
8. [The Reviewer](#8-the-reviewer)
9. [Usage & Operations: Monitoring, CLI, Device Management](#9-usage--operations-monitoring-cli-device-management)
10. [Admin, Legal & Compliance](#10-admin-legal--compliance)
11. [Limits: What's Not Available Yet](#11-limits-whats-not-available-yet)
12. [Glossary](#12-glossary)
13. [Changelog](#13-changelog)
14. [Sources](#sources)

---

## 1. What Claude Science Is + Core Concepts

### What it is

Claude Science is Anthropic's AI workbench, available in **beta for macOS and Linux** (Windows runs via WSL - see Section 2). It pairs Claude with an analysis environment on your computer: you describe research tasks and Claude executes **Python, R, or shell** code in a sandbox. Although it opens in a browser tab, **it is a local application, not a website**.

### Key capabilities

- Write and execute code in an isolated environment.
- Access only folders you explicitly authorize.
- Query scientific databases through connectors.
- Generate versioned artifacts with complete provenance tracking.
- Have a reviewer verify Claude's claims against the actual execution record.

### Important limitations

- Claude can make mistakes.
- The reviewer checks claims against the execution record; it does **not** re-run analyses.
- Unsuitable for clinical or diagnostic applications.
- Results require verification before publication or critical decisions.

### System requirements

- A Claude account on **Pro, Max, Team, or Enterprise** (Free is not supported).
- **macOS 13+** or **Linux x64**.
- ~5 GB available disk space.
- On Linux: `socat`, `bubblewrap` 0.8.0+, and enabled unprivileged user namespaces.

Files stay local; all code execution happens in a sandbox requiring your approval for new folder access, network hosts, and remote jobs.

### Core concepts

**Projects and sessions.** A *project* groups related sessions and the artifacts they produce. Projects can carry custom instructions Claude reads at the start of each conversation, and folder permissions you grant persist across sessions. A *session* is a single conversation thread with its own dedicated workspace folder and one or more running kernels.

**File storage.** Files stay on your computer; Claude reads and writes them in place inside folders you authorize. Anthropic does not host or store your files, though file content sent to the API during conversations follows Anthropic's standard retention policy. Files, artifacts, and conversation history are device-specific - they do not transfer if you sign in elsewhere. Exception: files attached through the composer are copied into the app's local data folder to persist with the conversation. **Do not manually move, rename, or delete files in `~/.claude-science`** - it can break artifact links and version history. Manage artifacts through the app.

**Permission cards.** Appear whenever Claude needs a new access type; each card shows exactly what is being requested. Scope options differ by action: folder access is read-only or read & write; code execution is once or always; connector tools offer once, per-conversation, per-project, or global.

**Plans, sandbox, delegation.** Claude may propose plans for multi-step work that you approve or refine. All code runs in an OS sandbox restricted to authorized folders, with network **deny-by-default** except package managers and approved hosts. Delegation lets Claude parallelize independent work tracks within a session, with status markers shown in the conversation.

**Memory and shortcuts.** Memory (disabled by default) lets Claude retain facts across sessions in your local database. Composer shortcuts: `@` for artifacts, `#` for past sessions, `/` for skills.

---

## 2. Setup: Enable, Install, Windows/WSL

### 2.1 Enable Claude Science (Team/Enterprise admins)

Availability by plan:

| Plan | Status |
|------|--------|
| Pro, Max | Automatically enabled |
| Team, Enterprise | **Disabled by default**; requires admin activation |
| Free | Not supported |
| HIPAA-enabled orgs | Disabled by default; usage falls **outside BAA** coverage |

Activation (Owner or Primary Owner):

1. Go to **Organization settings > Capabilities**.
2. Find the Claude Science toggle and activate it.
3. Complete the setup wizard (covers unsupported features, role permissions, connector configuration).
4. Select **Enable Claude Science**.

Two layers of control: the **org-level toggle** decides whether Claude Science is available at all; **role-based entitlements** decide which members get access. Built-in roles are entitled automatically; custom roles (Enterprise only) need explicit capability assignment. The wizard also configures data sources (Anthropic-built featured connectors, local connectors, and Directory connectors). To disable: toggle off in Capabilities - locally stored data remains on member devices.

### 2.2 Install and get started

**macOS.** Download the installer from `claude.com/product/claude-science` and double-click. First launch sets up the runtime plus starter Python and R environments (a few minutes), then opens a browser tab. If none appears, choose **Open** from the menu bar icon.

**Linux.**

```bash
curl -fsSL https://claude.ai/install-claude-science.sh | bash
claude-science serve
```

First launch prints progress and ends with a local URL. On a remote server, start with `--no-browser`, forward the port over SSH, and open the URL from your laptop.

**Sign in.** Sign in with your Claude account. If the OAuth redirect can't return (e.g., through an SSH tunnel), use the **Paste a code** option. No API key required. A setup wizard walks through connectors, skills, and which websites Claude can access (change anytime in Settings). Everything installs to a single folder `~/.claude-science`; deleting it removes all projects, artifacts, and conversation history.

**Run your first analysis.**

1. Open the **Example** project, or create a new one.
2. Start a conversation. Reference a folder by typing its path or using the `@` picker.
3. Review the **folder-access** card and allow or deny.
4. Review the **code-execution** card when Claude proposes running code.
5. Results appear as artifacts in the **Files** panel.

**First-launch troubleshooting.**

- macOS says the app isn't supported / icon crossed out: wrong processor build. Re-download choosing **Mac (Intel)** or **Mac (Apple Silicon)** (check Apple menu > About This Mac > Chip/Processor).
- No browser tab: macOS - choose **Open** from menu bar icon; Linux - copy the printed URL into a browser on the same machine, or run `claude-science url`.
- Linux refuses to start: install bubblewrap 0.8.0+ and confirm unprivileged user namespaces are enabled (`bwrap --version`).
- Sign-in stops at claude.ai: account is on Free (upgrade), or the redirect couldn't return (use **Paste a code**).

### 2.3 Run on Windows with WSL

No native Windows build yet; the Linux binary runs well under **WSL 2**. ~5 minutes.

**Enable WSL** (PowerShell as Administrator):

```powershell
wsl --install -d Ubuntu-24.04
```

Reboot if prompted, open **Ubuntu 24.04**, create your Linux user. Use **Ubuntu 24.04 or newer** (the sandbox needs bubblewrap 0.8.0+; Ubuntu 22.04 ships an older version). **WSL 2 is required** (WSL 1 can't run the sandbox); `wsl --install` sets up WSL 2 by default. Check with `wsl -l -v`; upgrade with `wsl --set-version Ubuntu-24.04 2`.

**Install dependencies** (inside Ubuntu):

```bash
sudo apt update && sudo apt install -y curl bubblewrap socat
```

**Install Claude Science** (inside Ubuntu - do not copy a Windows-downloaded binary across):

```bash
curl -fsSL https://claude.ai/install-claude-science.sh | bash
. ~/.profile
claude-science --version
```

**Run it:**

```bash
claude-science serve --port 8765 --no-browser
```

Copy the printed URL into any Windows browser - WSL 2 forwards `localhost` automatically. The URL holds a one-time sign-in token; print a fresh one with `claude-science url`.

**Keep it running.** The app lives in the WSL VM and stops when WSL shuts down. Closing your last Ubuntu terminal shuts the VM down after a short idle period; `wsl --shutdown` stops it immediately. To start from PowerShell without opening Ubuntu:

```powershell
wsl -d Ubuntu-24.04 -- ~/.local/bin/claude-science serve --port 8765 --no-browser
```

Leave that PowerShell window open to keep the VM alive. To background it inside an existing Ubuntu session, add `--detached`.

**WSL troubleshooting.**

| Symptom | What it means |
|---------|---------------|
| `command not found: claude-science` | `~/.local/bin` not on PATH yet. Run `. ~/.profile` or open a new terminal. |
| Error mentioning `bwrap too old` | Ubuntu ships an older bubblewrap. Use Ubuntu 24.04+. |
| `daemon already running on port 8765` | Already running. Run `claude-science url` and open the link. |
| `port 8765 is already in use` | Another program holds that port. Pick another with `--port 8080`. |
| Browser can't reach `localhost:8765` | Confirm the daemon is still running in WSL. With a custom `.wslconfig` network mode, try the WSL address instead of `localhost`. |

---

## 3. How It Works With Your Data (Artifacts, Annotations, Provenance)

### 3.1 Data handling

Claude Science is **local-first**: conversation history and artifacts stay on your device; there is no Anthropic-hosted session store. When the app sends prompts and responses to Anthropic's servers, that traffic follows Anthropic's **standard retention policy** for model traffic (same as other Claude products); orgs with CMEK get equivalent encryption. The app also sends product-usage telemetry (event counts and timing, **not** conversation content), which you can disable via device configuration.

- **Remote compute**: when you connect remote compute you control, code and data go **directly to that destination**, not through Anthropic. Admins cannot restrict this yet.
- **Directory connectors** route through Anthropic's hosted connector service (existing permission and tunnel controls). **Locally-added connectors** talk directly to the app.
- Because local data lives on devices, server-side controls (Custom Data Retention, Org Data Export, Compliance API) cannot reach it - **device management is the primary governance mechanism**. Identity controls (SSO, SCIM, roles) work via claude.ai authentication.

### 3.2 Artifacts

An **artifact** is a file Claude saves into the project (figure, processed dataset, report, notebook, other output). Artifacts persist until you delete them. Other files Claude writes during a session are temporary and cleared a few hours after the session ends - ask Claude to save a scratch file to keep it.

**Working with artifacts.** Click a linked file to open it in a tab beside the chat. HTML artifacts have zoom controls (including fit-to-width); images zoom to native resolution. Open **Files** in the sidebar for a searchable grid of every artifact. Artifact menu: **Open, Open beside session, View in context, Provenance, Versions, Copy link, Star, Rename, Download, Delete**. Renaming doesn't break links; **Delete removes all versions permanently**. Attached/dropped files are listed under **Your uploads**. To copy artifacts out, use **Download** for a single file, or open the project folder under `~/.claude-science` and copy directly.

**Versions.** Saving the same filename again in the same session creates a new version. You can edit text-based artifacts (Markdown, code, plain text) directly: **Edit content > Save** creates a new version. Images, PDFs, HTML, and tables can't be edited in place. When an artifact is open, a version stepper and diff toggle appear (previous version is the default comparison). Older versions are read-only; to restore one, ask Claude to save it again. Links in the conversation point to the specific version that existed at the time.

**Provenance.** Every artifact version records how it was made. Open **Provenance** for five tabs:

- **Messages** - the conversation around the save.
- **Code** - a reproducible script, downloadable as script or notebook.
- **Execution Log** - every command that ran.
- **Environment** - environment name, language version, and every installed package with its version.
- **Review** - findings from the reviewer.

The **Execution Log is authoritative**. If the Code tab and the log disagree, trust the log.

**Deleting.** Deleting a session keeps its artifacts and provenance. Deleting a project deletes all its sessions, artifacts, and project-scoped memory.

### 3.3 Annotations

Attach comments to specific parts of artifacts instead of describing locations in prose. You can: select text in Markdown, plain-text, LaTeX, or code; highlight text in PDFs (single page only); click points on images/figures; or use **Annotate** mode to click elements in rendered HTML reports. Tables (and some other types) can't be annotated; session transcripts are supported.

- **Leave one**: select content, click the **Annotate** pill, type the comment, press Cmd/Ctrl+Enter (or **Save**). It appears as a highlighted badge (text) or numbered pin (images); hover to read, click to Edit/Delete.
- **Send to Claude**: saving does **not** auto-send. Pending annotations accumulate in an **N comments** chip on the composer and go with your next message (batch or individually). Claude receives each with its filename, the quoted selection (or marked image), and your note. Once sent they are consumed, leave the artifact, and appear as cards on the message. No threads or resolve states; to revise after an update, annotate the new version.
- **Limits**: 1,000-character max per annotation; PDF selections can't cross page breaks; annotations are excluded from downloads and don't show in the Files grid.

---

## 4. Tools & Environments

Claude can execute **Python, R, and shell** commands. Python and R keep variables across steps during a session; **kernels persist ~30 minutes of inactivity**, or until a package installation or session termination.

**Starter environments.** Initial setup provides two **read-only conda environments** in `~/.claude-science`:

- **Python**: numpy, pandas, scipy, matplotlib, seaborn, pillow
- **R**: tidyverse, ggplot2, jsonlite

**Task environments.** For packages beyond the starters, Claude either reuses an existing named environment or suggests a new specialized one. A permission card shows the environment name and initial packages. These environments are available **across all projects on the machine**. There is no settings UI - manage environments by asking Claude.

**Installing packages.** Default sources:

- **Conda**: micromamba from conda-forge, bioconda, defaults, pytorch channels
- **Python**: pip via PyPI
- **R**: CRAN and Bioconductor

Packages installed **to an environment** are permanent across sessions and projects. **Inline installs** (`pip install`, `install.packages()`) expire on kernel restart - request environment-level installation for permanence. Tools lacking packages are handled via source downloads, sandbox compilation with conda-forge compilers, and artifact storage for reuse. The sandbox has **no root and no system package managers** - `apt` and `sudo` don't work; use conda-forge or source builds. Package sources can't be redirected to alternate servers.

**GPUs.** On Linux machines with GPU hardware (including multi-GPU), GPUs are accessible to code execution once **enabled in Settings > Compute**. Machines without GPUs can use remote compute connections or external providers (Section 7).

---

## 5. Connectors & Skills (+ Custom Connectors)

**Connectors** give Claude access to external databases during analysis. **Skills** are instructional frameworks Claude deploys contextually (methods, tools, verification procedures). Both are configured in Settings and work globally across projects.

### 5.1 Featured connectors

Pre-enabled, connect to **public life-sciences databases**, require no authentication, and are **read-only**. Review individual source licenses - some underlying databases have non-commercial or attribution terms.

| Category | Connectors |
|----------|-----------|
| Genomic data | Ensembl, UCSC |
| Gene information | MyGene, UniProt, GO, Reactome, OLS |
| Variant databases | gnomAD, ClinVar, dbSNP |
| Human genetics | GWAS Catalog, eQTL Catalogue, FinnGen, BioBank Japan |
| Clinical genomics | ClinGen, CIViC, Open Targets |
| Expression | GTEx |
| Regulatory data | ENCODE, JASPAR, UniBind |
| Protein resources | InterPro, Pfam, Human Protein Atlas, STRING |
| Structural data | PDB, AlphaFold, EMDB, Complex Portal, IntAct |
| RNA | Rfam |
| Omics archives | GEO, ArrayExpress, PRIDE, MGnify, MetaboLights |
| Cancer data | cBioPortal |
| Chemistry | PubChem, ChEBI, Rhea, BindingDB |
| Drug information | FDA data, openFDA |
| Literature | OpenAlex, arXiv |
| Research resources | Grants.gov, Antibody Registry |
| Additional | BioMart, CellGuide, ZINC, Ketcher Chemistry |

### 5.2 Directory connectors

Four Directory connectors - **PubMed, Clinical Trials, ChEMBL, bioRxiv** - are available separately, with **restricted access on Team and Enterprise** plans requiring administrative approval.

### 5.3 Skills

Featured science skills cover literature review, indication dossiers, and protein modeling tools including **AlphaFold2, Boltz-2, Chai-1**, and others. Create custom skills via chat, manual composition, uploads, or GitHub integration.

### 5.4 Custom connectors

Integrate **Model Context Protocol (MCP)** servers - either remote HTTPS web servers or local programs.

**Add** at **Settings > Connectors > Add connector**:

- **Remote**: provide a server URL.
- **Local command**: specify a program to run.

Both need a **Name** using only lowercase letters, digits, and hyphens.

- **Remote config**: transport (SSE or Streamable HTTP), OAuth client settings, headers helper command. Servers requiring auth redirect through the provider's sign-in flow.
- **Local config**: runs in a sandbox with the **same network restrictions** as code execution; configure command arguments and environment variables.
- **Tool permissions**: default **Ask each time**. Per-tool, set **Always allow** or **Block** under the connector's **Tools**. **Skip approvals** bypasses confirmations for all tools on that connector - *only use connectors from developers you trust*.
- **Note**: local connector environment variables are stored **unencrypted** in config files (accessible only to your account) - avoid storing sensitive credentials. A public **Connectors Directory** exists for browsing community connectors.

---

## 6. Literature Access

Claude can retrieve **open-access** literature without credentials. Add publisher keys or institutional library proxies via **Settings > Credentials** for paywalled content you're authorized to use.

**Retrieval sequence** (given a DOI or title):

1. Open-access sources (Unpaywall, Semantic Scholar, PubMed Central)
2. Publisher routes where you hold credentials
3. Your institutional library proxy
4. Publisher's public page

Retrieved files (PDF, XML, or text) are stored within the session.

**Supported credentials:**

| Credential | Capability |
|------------|-----------|
| Elsevier API key + institutional token | Access Elsevier subscription content |
| Springer Nature API key | Access Springer Nature materials |
| Semantic Scholar API key | Accelerates Semantic Scholar searches |
| NCBI API key | Increases PubMed rate limits (3 -> 10 requests/second) |
| EZproxy URL + session cookie | Routes requests through institutional library |

**Contact email.** NCBI, EBI, and OurResearch (Unpaywall) require a contact email. A sharing prompt appears on first use; enable via **Settings > General > Contact email**.

**Technical notes.** Claude enforces one request per second per provider, respects rate-limit directives, and includes identification headers. Paywalled HTML content is **not** scraped.

---

## 7. Compute: Local GPU, Cloud Storage, Providers, Remote Clusters

### 7.1 Local GPU

Enable in **Settings > Compute** (see Section 4). Multi-GPU supported on Linux.

### 7.2 Cloud storage

Connect **Amazon S3, Google Cloud Storage, or Azure Blob Storage** so Claude reads data and writes results in place, with your permission.

**Setup.** In **Settings > Credentials**, choose **AWS**, **Google Cloud**, or **Microsoft Azure** and Connect. Credentials:

- AWS: access key
- Google Cloud: service-account JSON or HMAC key
- Azure: connection string or service principal

List the bucket names (AWS, GCP) or **Blob containers** (Azure) the credential covers. S3-compatible stores use the AWS form plus the **S3-compatible endpoint** field (allowlist that endpoint host separately).

**How it works.** Listing a bucket adds its address to the sandbox network allowlist so code reaches it without a per-call card; access stays limited to the credential's permissions. Credentials are encrypted locally and sent only to their provider. Claude reads/writes objects with each provider's Python library (`boto3`, Azure SDK). **Settings > Storage** shows connected credentials and lets you browse, import (up to 100 GB), or export objects.

**Notes.** Reach GCS with an **HMAC key** via `boto3`, or use import/export (alternative GCS tools use path-style addresses unavailable from the sandbox). Any code Claude writes can use credentials you add here - **never add credentials for buckets that should remain inaccessible** during sessions.

### 7.3 Compute providers (Modal + model endpoints)

**Modal.** Run jobs on **Modal** using your own account; Modal bills you directly (Anthropic never processes payments or accesses payment info).

- **Setup**: Settings > Compute > Cloud providers > Connect on the Modal card. If you've run `modal token new` (Modal CLI), it reads `~/.modal.toml` automatically; otherwise enter **Token ID** and **Token secret** in Settings > Credentials > Modal. Tokens are stored encrypted and never shown to Claude.
- **Job execution**: when a task needs GPU or exceeds local memory, Claude proposes a cloud job. The modal card shows Profile, machine spec (e.g., **H100, 8 CPUs, 32 GiB**), per-second billing, and max billable duration (links to Modal pricing). Approve individual jobs or all jobs in a conversation/project. Input files max **1 GiB per submission**; larger data can be staged to **Modal Volumes** and mounted. Outputs written to `./out/` (max **5 GiB**) return with logs.
- **Warning**: closing the app does **not** cancel a running Modal job - it keeps billing until it finishes or times out.
- **Cost management**: no automatic spend ceiling. **Concurrent jobs** default 10; **Default container timeout** 12 hours (max 23 hours, enforced by Modal). Monitor spend via Modal's dashboard. Configure Modal environment and default app name in Settings > Compute.
- **Container images**: auto-generated to match job requirements, built once on Modal, reused until dependencies change (view in the Details doc from Settings > Compute).

**Model endpoints - NVIDIA BioNeMo NIM.** In **Settings > Compute > Model endpoints**: import BioNeMo Agent Toolkit skills, add your NVIDIA NGC API credential, and select the NVIDIA-hosted endpoint or a local container deployment (requires an NVIDIA GPU). Ask Claude to launch local Docker NIM containers or configure remote connections for specific BioNeMo skills.

### 7.4 Remote compute clusters (SSH)

Connect a machine reachable over SSH (lab workstation or HPC login node) so Claude can run jobs on it. Claude Science uses your existing `~/.ssh/config`, authenticates with your key or `ssh-agent`, and **installs nothing on the host**.

**Add a host.** Settings > Compute > **SSH hosts** > **Add SSH host**. Choose/type an alias from `~/.ssh/config` (address, user, port, and any `ProxyJump` come from that file). Optionally add notes (partition, account code, module loads, whether software can be installed) - Claude reads these before the first job. Optionally override **User**, **Port**, or **Identity file** under **Advanced**. Click **Add**. Adding a host runs a **read-only probe** recording CPUs, memory, GPUs, CUDA driver, presence of conda/modules/Apptainer, scratch directories, and whether `sbatch` exists (on SLURM it reads partitions). Results are saved as editable notes; re-run with **Probe**.

**Running jobs.** Workstations run jobs as **detached processes**; SLURM clusters receive jobs via **`sbatch`**. Jobs survive connection loss. On the host page, set **Scratch directory** (must be on a shared filesystem for SLURM) and **Concurrent job limit** (default 100). When Claude proposes a job, a **"Run this job on `<host>`?"** card shows the command and script; approve with **Once, This conversation, This project, or Global**. On approval the script and inputs are copied to a job directory under the scratch directory.

- **Remote jobs run outside the sandbox**, as your user on the host, with full access to what your account can read/write there.
- Default job timeout is **30 minutes** - tell Claude before submitting longer work. On finish, outputs are pulled back into the session; files over ~100 MB (default threshold) stay on the host and Claude records their paths.

**Host details.** Claude reads host-specific instructions from the **Details document** on the host page (how environments are activated, where data/packages live, scheduling conventions). Claude updates these as it works; you can edit anytime.

---

## 8. The Reviewer

A built-in verification step that independently re-reads Claude's recent responses, the approved plan, saved artifacts, and the execution record, then checks whether claims match what actually ran. It runs automatically after responses and periodically during long work; trigger it anytime with **Request review**. Auto-review is **on by default on Max, Team, and Enterprise**; on **Pro** it starts off (enable per session).

**What it checks (examples, not exhaustive):**

- A result reported as computed when nothing ran.
- A value that contradicts the file it came from.
- A citation that doesn't support the claim attributed to it.
- A reference whose DOI resolves to a different article.
- An approved plan step that wasn't completed.
- A conclusion not supported by the method used.

It checks whether **claims match the record**; it does **not re-run analyses**. It can flag a conclusion that doesn't follow from the method that ran, but it doesn't judge whether that method was the right choice.

**Findings.** A **Reviewer - N findings** card appears with each finding's claim, evidence, and a link into the transcript. Claude reads and addresses them in its next message (correct the work or explain why the finding doesn't apply). Open the reviewer's full reasoning from the card.

**Custom criteria.** In **Settings > Specialists > Reviewer**, add checks in the **Instructions** field - they are added to every review and cannot remove or weaken built-in checks. You can also create your own specialist for additional customized reviews.

**Controls.** Auto-review is a per-session toggle in the session settings menu (on for Max/Team/Enterprise, off for Pro). Reviews run against your plan's usage.

---

## 9. Usage & Operations: Monitoring, CLI, Device Management

### 9.1 Monitor usage

Claude Science consumption applies to the standard weekly quota and uses the same seat as claude.ai.

- **Org dashboard**: Organization settings > Analytics > All Activity, filter by **Claude Science** (shows active users, sessions, spend). A direct **Monitor usage** link is on the Claude Science row under Organization settings > Capabilities.
- **Enterprise Admin API**: `GET /v1/organizations/analytics/users`. The `science_metrics` object:

| Metric | Purpose |
|--------|---------|
| `distinct_session_count` | Distinct Claude Science sessions (null for aggregated data) |
| `message_count` | Messages within Claude Science sessions |
| `delegation_count` | Handoffs to specialized agents |
| `remote_compute_job_count` | Remote compute job launches |
| `skills_used_count` | Skill invocations across sessions |

### 9.2 Command-line settings

`claude-science serve` starts the app and opens the web app at a single-use login link.

| Command | Purpose |
|---------|---------|
| `claude-science serve` | Launch the background program; access the web UI via a temporary login URL |
| `claude-science open` | Generate a fresh login link and open it in your browser |
| `claude-science url` | Print a new login link to stdout only |
| `claude-science status` | Show status, version, and port as JSON |
| `claude-science logs` | Show the latest log file; `--tail` for live monitoring |
| `claude-science stop` | Cleanly shut down the running program |
| `claude-science update` | Install updates (`--check` to preview, `--to <version>` for a specific version) |
| `claude-science import <path>` | Merge another data directory/database into the current one |
| `claude-science --version` | Print the current version |

**Global flags:** `--data-dir <dir>` (default `~/.claude-science`), `--config <file>` (default `~/.claude-science/config.toml`).

**`serve` flags:** `--port <n>` (8000), `--no-browser` (off), `--detached` (off), `--no-auto-update` (off), `--host <address>` (127.0.0.1), `--base-path </prefix>` (unset, for reverse proxy), `--allow-origin <url>` (unset), `--sandbox-port <n>` (port+1, HTML preview isolation), `--verbose` (off).

**Auth:** login links contain a single-use nonce valid ~3 minutes. **`import` has no preview and no undo** - back up the data directory first. **Env vars:** `DO_NOT_TRACK` disables usage analytics; `GITHUB_TOKEN` optionally raises API rate limits for GitHub-based skill installs.

### 9.3 Manage on devices (IT / endpoint teams)

All member content is stored **locally**. Two on-disk locations:

- **Configuration**: `~/.claude-science/config.toml` holds all app settings (every key optional; app starts with no file). This is the file to deploy via device management.
- **Data directory**: conversations, artifacts, delegation configs, and workspace files in a per-org subfolder `orgs/<organization-id>/`, as a local database plus files.

Auth tokens and the shared package environment live under `~/.claude-science/` regardless of the data directory, so backup/wipe policies targeting the data directory don't affect sign-in state. There is no Anthropic-hosted copy, so Custom Data Retention, Org Data Export, and the Compliance API don't reach these folders.

**Deploy config via MDM.** Claude Science reads no system-level managed-preferences file; deploy the per-member `config.toml`. Keys most relevant to admins:

| Key | Effect |
|-----|--------|
| `disable_telemetry = true` | Stops product-usage telemetry to Anthropic |
| `data_dir = "<path>"` | Moves conversations, artifacts, workspaces to a managed location |
| `[update] auto_update = false` | Prevents self-update; pair with your own distribution channel |
| `[sandbox] network_isolated = true` | Blocks network access from the local code-execution sandbox |

**Telemetry.** Event counts and timings, not conversation content. No in-app setting; disable with `disable_telemetry = true` or the `DO_NOT_TRACK` env var (both device-level; no per-member/org toggle).

**EDR.** On macOS, sandboxed analysis processes run as ordinary child processes visible to host EDR. On Linux, they run in a separate PID namespace with an isolated process view, so host EDR won't see them as ordinary children.

**Required updates.** Anthropic may set a minimum supported version. Below that floor, the app shows a full-page notice and blocks use until the member updates. Admins don't configure the floor; if you distribute via your own channel with auto-update disabled, push updates promptly when Anthropic raises it.

---

## 10. Admin, Legal & Compliance

### 10.1 Admin controls (Claude Science beta)

Members sign in with their Claude account, so identity and billing controls apply automatically. Because conversations are stored **locally**, most data-handling controls don't cover that data. Status legend: **Supported / Partial / Not available / Not applicable**.

**Identity and access:** SSO (SAML/OIDC) - Supported (via claude.ai). SCIM/Directory Sync - Supported (deprovisioning revokes access). Domain capture - Supported. Members management - Supported. Built-in roles - Supported. Custom roles - Supported. Groups - Supported. **IP allowlisting - Partial** (Claude inference is IP-gated; gating remote compute is on the roadmap; custom/local connectors out of scope). **Session duration - Partial** (limits the browser sign-in step only; app stays signed in after).

**Capability toggles:** Org enable toggle - Supported (off by default for Team/Enterprise). Completion feedback (thumbs) - Supported. Org custom instructions - Supported. **Skills allowlist - Partial** (org-published skills appear, but members can install local skills; admin control on roadmap). **Web search - Not available** (app offers it regardless; roadmap). **Code execution - Not available** (that setting controls Chat's hosted sandbox; Science runs code locally by design). **Code execution network allowlist - Not available** (Science's local sandbox keeps its own member-maintained allowlist; roadmap). Location metadata - Not applicable (no geolocation). Memory - Not applicable (own local memory, off by default). Projects - Not applicable (uses local workspaces).

**Connectors:** Org-published Directory connectors - Supported. **Per-role connector restrictions - Partial** (Directory connectors only). **Org plugin allowlist - Partial** (members can still add local skills/connectors; roadmap). **Connector tunnels - Partial** (Directory connectors reach the app through tunnels; local and custom remote connectors don't route through them). **Custom connector restrictions - Not available** (members can add custom connectors regardless; roadmap). Desktop Extension allowlist - Not applicable.

**Data and privacy:** CMEK - Supported (model traffic, same as Chat). **Data processing geography - Partial** (covers Anthropic-hosted processing, not remote compute you configure or the member's computer). **HIPAA - Partial** (HIPAA-ready orgs can enable the beta, but usage isn't covered under the BAA). **Custom Data Retention - Not available** (auto-delete doesn't cover local data or the usage logs Anthropic keeps).

**Audit and compliance:** Audit log - Not available (roadmap). Compliance API - Not available. Org data export - Not available (excludes member-computer data).

**Usage, models, and billing:** Usage limits - Supported (same 5-hour and weekly limits as Claude Code and Cowork). Billing and seats - Supported (same seat as claude.ai). Model access controls - Supported (standard model API; allowed-model list and grants apply). Usage analytics - Supported (spend filterable by product).

**Offboarding and local data:** Offboarding (local data) - Not available (removing a member doesn't wipe data already on their computer). Local deletion signal - Not available (deleting local data doesn't notify Anthropic to drop the matching server-side record early; roadmap).

### 10.2 Legal and compliance

- **Terms**: **Commercial Terms** apply to Team and Enterprise; **Consumer Terms of Service** govern Pro and Max.
- **Usage Policy**: the Anthropic Usage Policy applies. Advertised usage limits for Pro and Max assume ordinary, individual usage.
- **Authentication**: OAuth tokens authenticate users on **paid subscription tiers only**, for standard application usage; Anthropic maintains enforcement rights (contact sales with questions about permitted authentication methods).
- **Security**: trust and security information via Anthropic's **Trust Center** and **Transparency Hub**; vulnerability reporting via **HackerOne**.

---

## 11. Limits: What's Not Available Yet

- **Audit and compliance**: audit logs for Claude Science events aren't yet integrated into the org audit log (planned). The Compliance API can't export or delete Claude Science data (conversations are local). Org data exports don't include locally stored data.
- **Data retention**: auto-delete windows apply only to server-stored content; local content isn't covered. Deleting local data sends **no** signal to Anthropic to drop corresponding server-side model-traffic logs early - they expire on standard schedules.
- **Connector and domain allowlists**: org allowlists govern centrally published Directory connectors but don't restrict locally installed or custom (private-URL) connectors (admin controls planned). Skills allowlists behave similarly - org-published skills are accessible, but there's no admin control over which featured skills members can activate.
- **Session duration**: controls browser sign-in timing only; after auth the app keeps its own token and stays active beyond that window.
- **Offboarding**: removing members prevents sign-in but doesn't delete Claude Science data already on their computers - use device management to remove local data.

---

## 12. Glossary

- **Annotation** - a comment you pin to part of an artifact by selecting it; Claude reads pending annotations as instructions on its next turn.
- **Artifact** - any file Claude makes and saves for you, listed in its session's Files view.
- **Cell** - a code block executed in a kernel; the cell, its output, and runtime environment are recorded in the session's Notebook.
- **Cloud provider** - your account at a cloud service where Claude can initiate jobs; you pay the provider directly.
- **Connector** - an outside data source or tool wired into Claude over MCP; includes a featured set, partner connectors from the Connectors Directory, and your own under Settings > Connectors.
- **Data directory** - the `~/.claude-science` folder holding the database, artifacts, session workspaces, and logs.
- **Environment** - a named set of installed packages (conda) that a kernel runs in, reused across sessions.
- **Execution log** - the slice of a session's Notebook cells that produced a given artifact version, shown as a tab in its Provenance pane.
- **Kernel** - the live Python or R process that runs a session's cells and keeps variables in memory between them.
- **Memory** - notes Claude keeps about you and your projects across sessions, which you can review and edit.
- **Model endpoint** - a scientific domain-specific model server you register under Settings > Compute (local or vendor-hosted) that Claude sends single prediction requests to.
- **Network allowlist** - the list under Settings of every outside host that sandboxed code may reach.
- **Permission card** - the card that replaces the message box when Claude needs permission (running code, a job, a network host, a folder, a connector tool, or reconfiguring Claude Science); you allow or deny it.
- **Provenance** - the panel behind every artifact version showing the code, cells, conversation, environment, and findings that produced it.
- **Reviewer** - the independent agent that re-examines Claude's claims and artifacts at checkpoints, recording each issue as a finding on the artifact's Review tab; runs automatically on some plans.
- **Sandbox** - the isolated environment all of Claude's code runs in; reaching outside it needs your approval.
- **Scope** - how long an approval lasts (Once, This conversation, This project, or Global); every standing grant is listed and revocable under Settings > Permissions.
- **Session** - one conversation thread inside a project, with its own kernel and workspace.
- **Skill** - an installable package of instructions and helper code that teaches Claude a method or tool.
- **Specialist** - a named set of skills, connectors, and instructions that a session answers as.
- **SSH host** - a remote machine (server, cluster node, or job-submission host) added by its SSH name, that Claude can run jobs on or dispatch jobs from.
- **Version** - one immutable save of an artifact; saving again adds a new version instead of overwriting.
- **Workspace** - the per-session folder on disk where Claude's code reads and writes files before they are saved as artifacts.

---

## 13. Changelog

Release notes for Claude Science (newest first). See the changelog source URL for the full, current list.

**v0.1.16 (July 7, 2026)** - Features: auto-review now available on the **Pro** plan (turn on from session settings); artifact previews with zoom for HTML/images plus version comparison; import skills from **private GitHub repositories** using your own credentials; LaTeX cross-reference resolution (`\ref`, `\eqref`, section numbering); dashboard enhancements (project switcher, live status, Cmd-K search); faster artifact annotation with drag-and-drop pins and `@`/`#` mentions. Fixes: pasted attachments, large-preview freezing, stale usage banners; repo cloning/archive unpacking no longer floods chats with images; reviewer stability and findings tray; connector tool calls now retry read-only operations automatically; corrupt-image handling, database-upgrade stability, auto-translate crashes.

**v0.1.15 (July 1, 2026)** - Corporate network support for **TLS-inspecting proxies** (e.g., Zscaler, Netskope); package mirror configuration for conda and pip via internal mirrors; **OpenAlex** now requires a free API key for full-text access; new **Context usage** view showing token allocation within a session; additional fixes.

**v0.1.14 (June 30, 2026)** - Public launch of Claude Science.

---

## Sources

All pages fetched 2026-07-08 from the official Claude Science documentation:

- https://claude.com/docs/claude-science/overview.md
- https://claude.com/docs/claude-science/core-concepts.md
- https://claude.com/docs/claude-science/get-started.md
- https://claude.com/docs/claude-science/enable-claude-science.md
- https://claude.com/docs/claude-science/run-on-windows-wsl.md
- https://claude.com/docs/claude-science/how-claude-science-works-with-your-data.md
- https://claude.com/docs/claude-science/artifacts.md
- https://claude.com/docs/claude-science/annotations.md
- https://claude.com/docs/claude-science/tools-and-environments.md
- https://claude.com/docs/claude-science/connectors-and-skills.md
- https://claude.com/docs/claude-science/custom-connectors.md
- https://claude.com/docs/claude-science/literature-access.md
- https://claude.com/docs/claude-science/cloud-storage.md
- https://claude.com/docs/claude-science/compute-providers.md
- https://claude.com/docs/claude-science/remote-compute-clusters.md
- https://claude.com/docs/claude-science/the-reviewer.md
- https://claude.com/docs/claude-science/monitor-usage.md
- https://claude.com/docs/claude-science/command-line-settings.md
- https://claude.com/docs/claude-science/manage-on-devices.md
- https://claude.com/docs/claude-science/admin-controls.md
- https://claude.com/docs/claude-science/legal-and-compliance.md
- https://claude.com/docs/claude-science/whats-not-available-yet.md
- https://claude.com/docs/claude-science/glossary.md
- https://claude.com/docs/claude-science/changelog.md
