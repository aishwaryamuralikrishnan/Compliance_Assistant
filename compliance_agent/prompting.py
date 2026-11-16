"""Trust boundaries in prompts.

Every piece of text that comes from a person or from a retrieved document reaches a model inside a named tag,
and every system prompt carries DATA_RULE. System prompts themselves are static: nothing that changes per
request (memory, the user's text, a DPO comment) is ever concatenated into one.

    tag("user_message", text)                      -> <user_message>\n...\n</user_message>
    passages([(citation, text), ...])              -> <passages><passage n="1" citation="...">...</passage></passages>

Text placed inside a tag cannot close it: an opening or closing tag of ours that appears in the text is
neutralised first (`<` becomes `&lt;`).
"""
from __future__ import annotations

import re
from typing import Iterable

from . import prompts

TAGS = (
    "user_message", "question", "passages", "passage", "org_memory", "user_preferences", "note", "queries_tried",
    "missing", "requested_changes", "change", "dpo_request", "pm_response", "dpo_comment", "original_description",
    "revised_description", "assessment_v1",
)

DATA_RULE = prompts.get("data_rule")         # config/prompts/shared.yaml

# For the two agents and the quick answer, which also receive long-term memory.
MEMORY_RULE = prompts.get("memory_rule")

_TAG_RX = re.compile(r"<(?=\s*/?\s*(?:%s)\b)" % "|".join(TAGS), re.I)


def neutralise(text: str) -> str:
    """Make sure the text cannot open or close one of our tags."""
    return _TAG_RX.sub("&lt;", str(text or ""))


def _attr(value: object) -> str:
    return neutralise(str(value)).replace('"', "'").replace("\n", " ")


def tag(name: str, text: str, **attrs: object) -> str:
    """The text inside <name ...>...</name>, on its own lines."""
    head = name + "".join(f' {k}="{_attr(v)}"' for k, v in attrs.items() if v is not None)
    return f"<{head}>\n{neutralise(text)}\n</{name}>"


def passages(items: Iterable[tuple[str, str]], *, start: int = 1) -> str:
    """Retrieved passages as <passages><passage n="1" citation="GDPR Art. 22(1)">...</passage></passages>.
    `items` are (citation or heading, text); `start` is the number of the first passage."""
    body = "\n".join(tag("passage", text, n=i, citation=label or None) for i, (label, text) in enumerate(items, start=start))
    return f"<passages>\n{body}\n</passages>"
