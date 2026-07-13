# materials/ — OPTIONAL starter files shipped inside the bootstrap folder.
#
# Two uses:
#
# 1) CHANNEL-CHECK FILE (used by SETUP step 9b).
#    During setup the CC copies one file from here into the shared workspace's
#    inputs/ folder, then asks Claude Science to OPEN it from the attached folder
#    and report a concrete detail (e.g. a PDF's title + page count). This proves
#    end-to-end that CS actually received AND can read a real file over the shared
#    folder — not just that a folder is attached.
#      - Right now this ships a REAL PDF, so the check tests true document transport.
#      - It is TRIVIALLY SWAPPABLE: to make the folder generic for other users, drop
#        in a small dummy file instead (e.g. a tiny  channel_check.txt  with one known
#        line) and remove the PDFs. The CC just needs SOME file here it can verify.
#
# 2) STARTER INPUTS for the run (staged during SETUP, digested during INTAKE).
#    Any real input files the run should begin from can travel with the bootstrap
#    folder here; the CC copies them into the workspace inputs/ folder so CS can read
#    them from the attached folder. During INTAKE (bootstrap CLAUDE.md step 14) each
#    input is turned into an agent-optimized digest at driver/context/<filename>.digest.md
#    (see DIGEST.md for the method). The human can also just drop files into the
#    workspace inputs/ folder at intake time instead of shipping them here.
#
# materials/ is OPTIONAL. The normal way to supply inputs is to drop them into the
# workspace  inputs/  folder at setup time (see SETUP.txt / START_HERE.md). If you
# need neither a shipped channel-check file nor shipped inputs, this folder can hold
# just a tiny dummy check file, or be empty (the CC will still verify the token
# round-trip in step 9a).
#
# If you ship files here and want their identity recorded in meta.json, add a
# manifest.txt next to them with, per file, the claimed:  title / authors / source.
# (State it as CLAIMED — the CC does not independently verify file contents.)
