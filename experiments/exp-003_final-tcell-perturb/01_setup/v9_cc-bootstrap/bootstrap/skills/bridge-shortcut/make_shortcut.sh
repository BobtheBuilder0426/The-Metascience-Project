#!/usr/bin/env bash
# make_shortcut.sh — create a human-visible, clickable shortcut ("Verknüpfung") to the shared bridge folder,
# in whatever environment the blank Claude Code is actually running in.
#
# ⚠️ SAFETY RULE (v7 — do NOT relax): the shortcut is placed ONLY inside the CC's own WORKSPACE folder.
#    It is NEVER written to the Desktop or anywhere outside the workspace. The CC has no business touching the
#    human's Desktop or any path outside the workspace it was given. The shortcut's sole purpose is to let the
#    human + any future session, browsing INSIDE the workspace, find the shared CS/bridge folder reliably.
#    The <workspace-root> argument is REQUIRED; if it is missing or not inside it, the script FAILS rather than
#    guessing a location.
#
# The bootstrap must NOT assume WSL. This script DETECTS the environment and picks the right native mechanism,
# always placing the shortcut inside <workspace-root>:
#   • WSL (Linux kernel under Windows)      → Windows .lnk in the workspace, target = <wsl>\... (via wslpath)
#   • native Windows (Git-Bash/MSYS/Cygwin) → Windows .lnk in the workspace, target = the Windows path
#   • macOS                                 → Finder alias in the workspace (osascript); fallback = symlink
#   • plain Linux                           → .desktop launcher in the workspace (+ a symlink); fallback = symlink
# In every case the fallback of last resort is a symlink inside the workspace, and the bridge itself still works via
# the paths recorded in CONNECTION.md — the shortcut is a convenience/visibility layer, never the bridge itself.
#
# Usage:
#   bash skills/bridge-shortcut/make_shortcut.sh "<bridge-folder>" "<workspace-root>" ["<shortcut-name>"] ["<env-hint>"]
#     <bridge-folder>  path to the folder to POINT AT (the shared CS folder, as THIS shell sees it)   (required)
#     <workspace-root> the CC's OWN workspace folder — the shortcut is placed HERE, never elsewhere    (required)
#     <shortcut-name>  base name of the shortcut (no extension)                 (default: the bridge folder's name)
#     <env-hint>       force the environment: wsl | windows | macos | linux     (default: auto-detect)
set -euo pipefail

FOLDER="${1:-}"
WORKSPACE_ROOT="${2:-}"
if [ -z "$FOLDER" ] || [ -z "$WORKSPACE_ROOT" ]; then
  echo "SHORTCUT-FAIL: usage: make_shortcut.sh <bridge-folder> <workspace-root> [name] [env-hint]"
  echo "  (both <bridge-folder> and <workspace-root> are REQUIRED — the shortcut is placed inside the workspace,"
  echo "   NEVER on the Desktop; refusing to guess a location.)"
  exit 2
fi
FOLDER="$(cd "$FOLDER" && pwd)"
[ -d "$WORKSPACE_ROOT" ] || { echo "SHORTCUT-FAIL: workspace-root '$WORKSPACE_ROOT' is not a directory"; exit 2; }
WORKSPACE_ROOT="$(cd "$WORKSPACE_ROOT" && pwd)"
NAME="${3:-$(basename "$FOLDER")}"
ENV_HINT="${4:-auto}"
# Destination is ALWAYS the workspace root. No Desktop, no free override. This is the v7 safety fix.
DEST_OVERRIDE="$WORKSPACE_ROOT"

# ---- 1. detect environment (unless the caller forced one from the pre-flight result) ----
detect_env() {
  local u; u="$(uname -a 2>/dev/null || echo unknown)"
  if grep -qiE 'microsoft|wsl' /proc/version 2>/dev/null || [ -n "${WSL_DISTRO_NAME:-}" ]; then echo wsl; return; fi
  case "$u" in
    *Darwin*) echo macos; return;;
    *CYGWIN*|*MINGW*|*MSYS*) echo windows; return;;
    *Linux*) echo linux; return;;
  esac
  # Windows native running this via Git-Bash sometimes reports MINGW in $OSTYPE
  case "${OSTYPE:-}" in msys*|cygwin*|win*) echo windows; return;; darwin*) echo macos; return;; esac
  echo linux
}
ENV="$ENV_HINT"; [ "$ENV" = "auto" ] && ENV="$(detect_env)"

echo "env: $ENV"
echo "target_folder_shell: $FOLDER"

have() { command -v "$1" >/dev/null 2>&1; }
ps_exe() { command -v powershell.exe 2>/dev/null || echo /mnt/c/Windows/System32/WindowsPowerShell/v1.0/powershell.exe; }

# ---- shared: make a Windows .lnk given a Windows target path + a Windows dest dir (used by wsl + windows) ----
make_win_lnk() {  # $1=win_target  $2=name  $3=dest_win(optional)
  local win_target="$1" nm="$2" dest_win="${3:-}" PS; PS="$(ps_exe)"
  [ -x "$PS" ] || { echo "SHORTCUT-FAIL: no powershell.exe found for a Windows .lnk"; return 3; }
  # dest_win MUST be provided by the caller (the Windows form of the workspace root). We never default to the
  # Desktop — that was the v6.1 bug. If it's missing, fail loudly rather than write outside the workspace.
  if [ -z "$dest_win" ]; then
    echo "SHORTCUT-FAIL: no workspace destination resolved (refusing to fall back to the Desktop)"; return 3
  fi
  local lnk_win="${dest_win}\\${nm}.lnk"
  local esc_lnk esc_tgt esc_desc
  esc_lnk="$(printf "%s" "$lnk_win"    | sed "s/'/''/g")"
  esc_tgt="$(printf "%s" "$win_target" | sed "s/'/''/g")"
  esc_desc="$(printf "%s" "$FOLDER"    | sed "s/'/''/g")"
  local ps1; ps1="$(mktemp --suffix=.ps1 -p "$FOLDER" .mkshortcut.XXXXXX)"
  cat > "$ps1" <<PSC
\$ErrorActionPreference='Stop'
\$sh=New-Object -ComObject WScript.Shell
\$lnk=\$sh.CreateShortcut('${esc_lnk}')
\$lnk.TargetPath='${esc_tgt}'
\$lnk.Description='Shared bridge folder for the loop run (${esc_desc})'
\$lnk.Save()
if(Test-Path -LiteralPath '${esc_lnk}'){Write-Output 'PS-OK'}else{Write-Output 'PS-MISSING'}
PSC
  local win_ps1; win_ps1="$(wslpath -w "$ps1" 2>/dev/null || printf "%s" "$ps1")"
  local res; res="$("$PS" -NoProfile -ExecutionPolicy Bypass -File "$win_ps1" 2>&1 | tr -d '\r' || true)"
  rm -f "$ps1"
  echo "shortcut_placed: $lnk_win"
  if printf "%s" "$res" | grep -q 'PS-OK'; then
    echo "SHORTCUT-OK"
    echo "recreate: bash skills/bridge-shortcut/make_shortcut.sh \"$FOLDER\" \"$WORKSPACE_ROOT\" \"$nm\" $ENV"
    return 0
  fi
  echo "SHORTCUT-FAIL: $res"; return 1
}

case "$ENV" in
  wsl)
    have wslpath || { echo "SHORTCUT-FAIL: wslpath missing though env=wsl"; exit 3; }
    WIN_TARGET="$(wslpath -w "$FOLDER")"
    WIN_DEST="$(wslpath -w "$WORKSPACE_ROOT")"   # place the .lnk INSIDE the workspace, not the Desktop
    echo "target_folder_win:  $WIN_TARGET"
    echo "shortcut_dest_win:  $WIN_DEST"
    make_win_lnk "$WIN_TARGET" "$NAME" "$WIN_DEST" || {
      echo "Fallback: in your workspace folder, right-click → New → Shortcut → paste:  $WIN_TARGET"; }
    ;;
  windows)
    # Git-Bash path → Windows path. cygpath if present, else assume caller passed a Windows-usable path.
    if have cygpath; then
      WIN_TARGET="$(cygpath -w "$FOLDER")"; WIN_DEST="$(cygpath -w "$WORKSPACE_ROOT")"
    else
      WIN_TARGET="$FOLDER"; WIN_DEST="$WORKSPACE_ROOT"
    fi
    echo "target_folder_win:  $WIN_TARGET"
    echo "shortcut_dest_win:  $WIN_DEST"
    make_win_lnk "$WIN_TARGET" "$NAME" "$WIN_DEST" || {
      echo "Fallback: in your workspace folder, right-click → New → Shortcut → paste:  $WIN_TARGET"; }
    ;;
  macos)
    DEST="$WORKSPACE_ROOT"; mkdir -p "$DEST"   # inside the workspace, never ~/Desktop
    ALIAS="$DEST/$NAME"
    # Prefer a real Finder alias (double-clickable, shows as an alias). Fall back to a symlink.
    if have osascript && osascript -e "tell application \"Finder\" to make alias file to POSIX file \"$FOLDER\" at POSIX file \"$DEST\"" \
         -e "tell application \"Finder\" to set name of result to \"$NAME\"" >/dev/null 2>&1; then
      echo "shortcut_placed: $DEST/$NAME (Finder alias)"
      echo "SHORTCUT-OK"; echo "recreate: bash skills/bridge-shortcut/make_shortcut.sh \"$FOLDER\" \"$WORKSPACE_ROOT\" \"$NAME\" macos"
    else
      ln -sfn "$FOLDER" "$ALIAS"
      echo "shortcut_placed: $ALIAS (symlink — osascript alias unavailable)"
      echo "SHORTCUT-OK"; echo "recreate: ln -sfn \"$FOLDER\" \"$ALIAS\""
    fi
    ;;
  linux)
    DEST="$WORKSPACE_ROOT"; mkdir -p "$DEST"   # inside the workspace, never ~/Desktop
    LINKFILE="$DEST/$NAME.desktop"             # a .desktop launcher FILE placed in the workspace (not the OS Desktop)
    cat > "$LINKFILE" <<DEOF
[Desktop Entry]
Type=Link
Name=$NAME
URL=file://$FOLDER
Icon=folder
DEOF
    chmod +x "$LINKFILE" 2>/dev/null || true
    ln -sfn "$FOLDER" "$DEST/$NAME" 2>/dev/null || true   # plain symlink too (works in any file manager / terminal)
    echo "shortcut_placed: $LINKFILE (+ symlink $DEST/$NAME)"
    echo "SHORTCUT-OK"
    echo "recreate: bash skills/bridge-shortcut/make_shortcut.sh \"$FOLDER\" \"$WORKSPACE_ROOT\" \"$NAME\" linux"
    ;;
  *) echo "SHORTCUT-FAIL: unknown env '$ENV' (use env-hint: wsl|windows|macos|linux)"; exit 3;;
esac
