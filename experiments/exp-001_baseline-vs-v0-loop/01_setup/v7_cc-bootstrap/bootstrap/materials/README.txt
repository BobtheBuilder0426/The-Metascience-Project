# materials/ — files shipped inside the bootstrap folder.
#
# THIS FOLDER SHIPS ONE THING: a dummy CHANNEL-CHECK FILE.
#
#   bridge_test.pdf  — a 2-page dummy PDF with NO research content. Its only job is to
#   prove, during PART B channel verification, that a real file placed in a run's dedicated
#   folder actually reaches Claude Science and can be read by it. It carries a known title
#   ("BRIDGE TEST DOCUMENT") and a sentinel line ("BRIDGE-OK-7F3A2C") so the CC can
#   confirm CS read the true content, not a cached guess.
#
# HOW IT IS USED (PART B step 12b — channel verification, NOT research input):
#   The CC copies bridge_test.pdf into THIS run's dedicated-folder inputs/ (<cs-workspaces>/
#   AL-<name>/inputs/), then asks Claude Science to OPEN it from the granted folder and report
#   its title + page count (or the sentinel line). If CS returns the known values, the data
#   channel is proven end-to-end. This file is a TRANSPORT TEST ONLY — it is never digested,
#   never treated as research material, and never fed to the driver as context.
#
# WHAT IS *NOT* HERE: real research inputs (papers/data).
#   Real inputs are supplied by the human LATER, per question, at INTAKE (bootstrap CLAUDE.md
#   PART B step 8), together with the research question — the CC explicitly asks "do you have
#   any publications/files to attach for context?" at that point. Only those intake files are
#   run through the pdf-digest subagents (PART B step 14) into driver/AL-<name>/context/<filename>.digest.md.
#   Do NOT ship research papers in this folder; keep the setup channel-check separate from
#   the research inputs so the bridge test never contaminates the run material.
#
# SWAPPING THE DUMMY: any small file the CC can verify works (e.g. a tiny channel_check.txt
# with one known line). A PDF is used here so the check also exercises the PDF path.
