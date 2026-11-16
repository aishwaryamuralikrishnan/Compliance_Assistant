"""direct_answer: the quick path. One retrieval pass, the quick worker model, no tools."""
from __future__ import annotations

import logging
from typing import Any

from langgraph.config import get_config, get_stream_writer
from langgraph.runtime import Runtime

from .. import memory, models, prompts
from ..prompting import passages, tag
from ..retrieval.loop import search_with_loop
from ..state import GraphState

log = logging.getLogger(__name__)

_SYSTEM = prompts.get("quick_answer")            # config/prompts/answers.yaml


def direct_answer(state: GraphState, runtime: Runtime) -> dict[str, Any]:
    say = get_stream_writer()
    cfg = get_config().get("configurable", {})
    question = state.get("input", "")
    res = search_with_loop(question, k=6, max_attempts=1, use_grader=False, emit=say)
    sources = [c.as_dict() for c in res.chunks]
    mem_text = memory.format_as_context({})
    if runtime.store is None:
        say({"node": "direct_answer", "event": "memory_unavailable", "error": "no store attached to this run"})
    else:
        try:
            mem_text = memory.format_as_context(memory.recall(runtime.store, cfg.get("user_id", ""), question, facts_k=4, lessons_k=2))
        except Exception as exc:
            # Never silently answer without memory: log the real error and say so in the trace.
            log.warning("memory recall failed for user %s: %s: %s", cfg.get("user_id", ""), type(exc).__name__, exc)
            say({"node": "direct_answer", "event": "memory_unavailable", "error": f"{type(exc).__name__}: {str(exc)[:160]}"})
            mem_text = memory.format_as_context({}, unavailable="Long-term memory could not be read for this answer.")
    # The system prompt is static. Memory, the question and the sources are data and travel in the human message, tagged.
    context = passages((c.citation, c.text[:1500]) for c in res.chunks)
    msgs = [("system", _SYSTEM), ("human", f"{mem_text}\n\n{tag('question', question)}\n\n{context}")]
    say({"node": "direct_answer", "event": "model_call", "model": models.resolved_model_ids().get("worker_quick"), "sources": [c.citation for c in res.chunks]})
    reply = models.chat("worker_quick").invoke(msgs)
    text = reply.content if isinstance(reply.content, str) else str(reply.content)
    if not text.strip():
        # a reasoning model can spend its whole output budget before writing the answer; report it, never hide it
        usage = getattr(reply, "usage_metadata", None) or {}
        log.warning("direct_answer: the model returned no text (output tokens %s, max_tokens %s)", usage.get("output_tokens"), models.slot_spec("worker_quick").get("max_tokens"))
        say({"node": "direct_answer", "event": "empty_answer", "tokens_out": usage.get("output_tokens"),
             "max_tokens": models.slot_spec("worker_quick").get("max_tokens")})
    reply.content = text
    return {"answer": text, "sources": sources, "messages": [reply]}
