#!/usr/bin/env bash
# make_shortcut.sh — create a human-visible, clickable shortcut ("Verknüpfung") to the shared bridge folder,
# in whatever environment the blank Claude Code is actually running in.
#
# The bootstrap must NOT assume WSL. This script DETECTS the environment and picks the right native mechanism:
#   • WSL (Linux kernel under Windows)      → Windows .lnk on the Windows Desktop, target = <wsl>\... (via wslpath)
#   • native Windows (Git-Bash/MSYS/Cygwin) → Windows .lnk on the Windows Desktop, target = the Windows path
#   • macOS                                 → Finder alias on ~/Desktop (osascript); fallback = symlink
#   • plain Linux                           → .desktop launcher on ~/Desktop (+ a symlink); fallback = symlink
# In every case the fallback of last resort is a symlink on the Desktop, and the bridge itself still works via the
# paths recorded in CONNECTION.md — the shortcut is a convenience/visibility layer, never the bridge itself.
#
# Usage:
#   bash skills/bridge-shortcut/make_shortcut.sh "<bridge-folder>" ["<shortcut-name>"] ["<env-hint>"] ["<dest-dir>"]
#     <bridge-folder>  path to the folder to point at (as THIS shell sees it)   (default: $PWD)
#     <shortcut-name>  base name of the shortcut (no extension)                 (default: the folder's own name)
#     <env-hint>       force the environment: wsl | windows | macos | linux     (default: auto-detect)
#     <dest-dir>       where to put the shortcut (native path for that env)      (default: the Desktop)
set -euo pipefail

FOLDER="${1:-$PWD}"; FOLDER="$(cd "$FOLDER" && pwd)"
NAME="${2:-$(basename "$FOLDER")}"
ENV_HINT="${3:-auto}"
DEST_OVERRIDE="${4:-}"

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
  if [ -z "$dest_win" ]; then
    dest_win="$("$PS" -NoProfile -Command '[Environment]::GetFolderPath("Desktop")' | tr -d '\r')"
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
    echo "recreate: bash skills/bridge-shortcut/make_shortcut.sh \"$FOLDER\" \"$nm\" $ENV"
    return 0
  fi
  echo "SHORTCUT-FAIL: $res"; return 1
}

case "$ENV" in
  wsl)
    have wslpath || { echo "SHORTCUT-FAIL: wslpath missing though env=wsl"; exit 3; }
    WIN_TARGET="$(wslpath -w "$FOLDER")"
    echo "target_folder_win:  $WIN_TARGET"
    make_win_lnk "$WIN_TARGET" "$NAME" "$DEST_OVERRIDE" || {
      echo "Fallback: right-click Desktop → New → Shortcut → paste:  $WIN_TARGET"; }
    ;;
  windows)
    # Git-Bash path → Windows path. cygpath if present, else assume caller passed a Windows-usable path.
    if have cygpath; then WIN_TARGET="$(cygpath -w "$FOLDER")"; else WIN_TARGET="$FOLDER"; fi
    echo "target_folder_win:  $WIN_TARGET"
    make_win_lnk "$WIN_TARGET" "$NAME" "$DEST_OVERRIDE" || {
      echo "Fallback: right-click Desktop → New → Shortcut → paste:  $WIN_TARGET"; }
    ;;
  macos)
    DEST="${DEST_OVERRIDE:-$HOME/Desktop}"; mkdir -p "$DEST"
    ALIAS="$DEST/$NAME"
    # Prefer a real Finder alias (double-clickable, shows as an alias). Fall back to a symlink.
    if have osascript && osascript -e "tell application \"Finder\" to make alias file to POSIX file \"$FOLDER\" at POSIX file \"$DEST\"" \
         -e "tell application \"Finder\" to set name of result to \"$NAME\"" >/dev/null 2>&1; then
      echo "shortcut_placed: $DEST/$NAME (Finder alias)"
      echo "SHORTCUT-OK"; echo "recreate: bash skills/bridge-shortcut/make_shortcut.sh \"$FOLDER\" \"$NAME\" macos"
    else
      ln -sfn "$FOLDER" "$ALIAS"
      echo "shortcut_placed: $ALIAS (symlink — osascript alias unavailable)"
      echo "SHORTCUT-OK"; echo "recreate: ln -sfn \"$FOLDER\" \"$ALIAS\""
    fi
    ;;
  linux)
    DEST="${DEST_OVERRIDE:-$HOME/Desktop}"; mkdir -p "$DEST"
    DESKTOP="$DEST/$NAME.desktop"
    cat > "$DESKTOP" <<DEOF
[Desktop Entry]
Type=Link
Name=$NAME
URL=file://$FOLDER
Icon=folder
DEOF
    chmod +x "$DESKTOP" 2>/dev/null || true
    ln -sfn "$FOLDER" "$DEST/$NAME" 2>/dev/null || true   # plain symlink too (works in any file manager / terminal)
    echo "shortcut_placed: $DESKTOP (+ symlink $DEST/$NAME)"
    echo "SHORTCUT-OK"
    echo "recreate: bash skills/bridge-shortcut/make_shortcut.sh \"$FOLDER\" \"$NAME\" linux"
    ;;
  *) echo "SHORTCUT-FAIL: unknown env '$ENV' (use env-hint: wsl|windows|macos|linux)"; exit 3;;
esac
