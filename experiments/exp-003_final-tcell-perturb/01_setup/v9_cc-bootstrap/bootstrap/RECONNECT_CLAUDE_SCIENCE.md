<!-- v9. How a CC session (bootstrap OR driver) gets Claude Science running + logged in again after the session dies or
     the login link expires. Referenced from bootstrap/CLAUDE.md, driver/CLAUDE.md, and each run's CONNECTION.md
     ("How to resume"). This is host-operational knowledge for a Windows+WSL host; adapt the shell if the pre-flight
     found a different environment. It does NOT change any science or the loop — it only restores the CC↔CS channel. -->

# Reconnecting to Claude Science — for any CC session (bootstrap or driver)

**When you need this:** your CS browser tab shows **"login no longer valid"**, **"reconnecting…"**, or the tab/session
is simply dead. Nothing is broken — the login link is **single-use and expires in ~3 minutes**, and **any daemon
restart kills the open session**. The fix is always to mint a **fresh** link. **Never reuse an old link or a bookmark.**

## Get back in — 3 steps (Windows + WSL host)
1. Open **PowerShell**.
2. Run:
   ```powershell
   wsl -- bash -lc "claude-science url"
   ```
3. Copy the `http://localhost:8000/?nonce=…` it prints into **Chrome**, then click **Sign in** → you land on the
   dashboard. (Use your OWN new tab — never the account home, never another run's open tab.)

Then continue where you were: open your run's CS **project** (do **not** create a new one; do **not** re-attach the
folder — both already exist per this run's `CONNECTION.md`), send `reply OK`, confirm `OK` back → channel live.

## "login no longer valid" / "reconnecting"
Not a fault — your session just **expired**. Same fix: repeat steps 1–3 for a fresh link. Do not bookmark the URL; the
nonce is one-time.

## Is the daemon even up?
It now **auto-starts at login/unlock** (the `ClaudeScience-EnsureUp` scheduled task). To **force** it (harmless if it's
already running):
```powershell
wsl -- bash -lc "claude-science serve --port 8000 --no-browser --detached"
```
Then do steps 1–3 above to get a fresh login link.

## Notes
- The **port is 8000** on this host (matches the `URL:` field in this run's `CONNECTION.md`). If a pre-flight ever
  recorded a different port, use that port in both commands and in the URL.
- This restores the *connection only*. Your run's project, granted folder, Agent Context, and inputs are unchanged —
  they persist across reconnects; do not rebuild them.
- If `claude-science url` itself errors (command not found / WSL not responding), that is the one thing to escalate to
  the human — everything else here is self-service.
