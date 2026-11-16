"""The reviser agent's instructions and the message that briefs it.

The reviser runs when the DPO has requested changes to a feature and the product manager has revised the
description. It does not re-assess from scratch: it works out the legal consequence of what changed, one
requested change at a time, and carries everything else over from v1 unchanged. The agent itself is built in
worker.py (`build_reviser`) from the same model slot, tools, middleware and gate as the worker.
"""
from __future__ import annotations

import json
from typing import Any

from .. import prompts
from ..prompting import tag

REVISER_PROMPT = prompts.get("reviser")          # config/prompts/agents.yaml


def revision_brief(revision: dict[str, Any], revised_description: str) -> str:
    """The first message of a revision run: everything the reviser needs, so it never has to look it up."""
    v1 = revision.get("v1") or {}
    responses = revision.get("responses") or []
    changes = []
    for i, req in enumerate(revision.get("requests") or [], 1):
        r = responses[i - 1] if i - 1 < len(responses) else {}
        note = (r.get("note") or "").strip() or "(no note)"
        changes.append(f'<change n="{i}">\n{tag("dpo_request", req)}\n{tag("pm_response", note, status=r.get("status", "done"))}\n</change>')
    lines = [
        f"Assessment v1 to revise: {tag('assessment_v1', json.dumps(_slim(v1), ensure_ascii=False, indent=1), id=revision.get('revises'))}",
        "",
        "Requested changes by the DPO, with the product manager's answers:",
        "<requested_changes>\n" + "\n".join(changes) + "\n</requested_changes>",
    ]
    if revision.get("comment"):
        lines += ["", "The DPO's comment:", tag("dpo_comment", revision["comment"])]
    lines += ["", "Original feature description (assessed in v1):", tag("original_description", revision.get("previous_description") or "(not recorded)"),
              "", "Revised feature description (assess this):", tag("revised_description", revised_description),
              "", "Produce assessment v2 now, following your instructions."]
    return "\n".join(lines)


def _slim(a: dict[str, Any]) -> dict[str, Any]:
    keep = ("assessment_id", "title", "verdict", "risk_level", "summary", "high_risk_ai", "dpia_required", "findings", "next_steps")
    return {k: a[k] for k in keep if k in a}
