# resources/papers -- starter knowledge base

<!-- WHAT THIS IS: the 4 starter papers the operator provided as the explicit STARTING POINT for the project. HOW TO USE (CS):
     read these FULLY first and work forward from them. Three are the state-of-the-art agentic-science systems (the
     closest prior art to the Agentic Loop we are building); one is the engineering survey for the harness layer. Each
     is registered in ../SOURCES.md (S-002..S-005). -->

**CS: read all four in full as the starting point, then build forward.**

- **S-002 -- ERA: "An AI system to help scientists write expert-level empirical software."** Google DeepMind, *Nature* 654 (2026), DOI 10.1038/s41586-026-10658-6. LLM code-mutation + **tree search** + research-idea injection that self-improves against a quality metric; demos in single-cell RNA-seq batch integration + COVID forecasting. -> `s41586-026-10658-6.pdf`
- **S-003 -- Robin: "A multi-agent system for automating scientific discovery."** FutureHouse et al., *Nature* 655 (2026), DOI 10.1038/s41586-026-10652-y. Multi-agent **lab-in-the-loop** (literature agents + a data-analysis agent); autonomously proposed + validated ripasudil for dry AMD. -> `s41586-026-10652-y.pdf`
- **S-004 -- AI Co-Scientist: "Accelerating scientific discovery with Co-Scientist."** Google (Gemini), *Nature* 655 (2026), DOI 10.1038/s41586-026-10644-y. Multi-agent **tournament-evolution + meta-review** self-improving loop with test-time-compute scaling; scientist-in-the-loop; biomedical validations. -> `s41586-026-10644-y.pdf`
- **S-005 -- "Agent Harness for Large Language Model Agents: A Survey."** Meng et al., 2026 preprint (no DOI/arXiv printed). Six-component harness framework **H = (E, T, C, S, L, V)**; argues the **harness > the model** for long-horizon reliability. -> `Agent_Harness_for_LLM_Agents__A_Survey_0408.pdf`
