"""Rewrite the retrieval query after a grader miss (cheap slot)."""
from __future__ import annotations

from langsmith import traceable
from pydantic import BaseModel, Field

from .. import models, prompts
from ..prompting import tag


class _Rewrite(BaseModel):
    """A better search query for the legal corpus."""

    query: str = Field(description="Rewritten search query using the regulation's own vocabulary")
    rationale: str = Field(default="", description="One sentence on what changed and why")


_SYSTEM = prompts.get("rewriter")                # config/prompts/retrieval.yaml


@traceable(name="rewrite_query", run_type="chain")
def rewrite_query(original: str, previous_queries: list[str], missing: str) -> tuple[str, str]:
    """Returns (new_query, rationale). Falls back to the original with a generic suffix on error."""
    history = "\n".join(f"- {q}" for q in previous_queries)
    msgs = [
        ("system", _SYSTEM),
        ("human", f"{tag('question', original)}\n\n{tag('queries_tried', history)}\n\n{tag('missing', missing or 'unclear')}"),
    ]
    try:
        r = models.invoke_structured("cheap", _Rewrite, msgs)
        new_q = r.query.strip()
        if not new_q or new_q.lower() in {q.lower() for q in previous_queries}:
            raise ValueError("rewrite repeated an earlier query")
        return new_q, r.rationale
    except Exception as exc:
        return f"{original} {missing}".strip(), f"rewrite fallback ({exc})"
