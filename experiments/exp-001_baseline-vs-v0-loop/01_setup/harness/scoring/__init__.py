"""the Metascience Project scoring harness — implements rubric.json + creativity-metric.md.

Pure scoring core (extract, novelty, citations, judge, composite, elo) with
dependency-injected LLM/connector functions, so it runs offline in dry-run and
against host.llm + host.mcp in a real CS session. See harness/README.md.
"""
from . import extract, novelty, citations, judge, composite, elo  # noqa: F401

__all__ = ["extract", "novelty", "citations", "judge", "composite", "elo"]
__version__ = "0.1.0"
