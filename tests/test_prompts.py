"""The prompts live in config/prompts/*.yaml (compliance_agent/prompts.py loads them). No database, no models."""
from __future__ import annotations

import pytest

from compliance_agent import prompts
from compliance_agent.config import ConfigError

SYSTEM_PROMPTS = ("worker", "reviser", "screen", "router", "grader", "rewriter", "quick_answer", "reflect")


def test_every_prompt_the_code_uses_is_in_the_yaml_files():
    assert set(prompts.names()) == {*SYSTEM_PROMPTS, "reranker", "summary", "role_notes", "data_rule", "memory_rule"}
    assert set(prompts.get_map("role_notes")) == {"product_manager", "dpo"}
    for name in SYSTEM_PROMPTS:
        text = prompts.get(name)
        assert "{{" not in text and prompts.get("data_rule") in text, name          # every system prompt carries the data rule
    for name in ("worker", "reviser", "quick_answer"):
        assert prompts.get("memory_rule") in prompts.get(name), name                 # and these three the memory rule


def test_values_are_filled_in_and_single_braces_are_left_alone():
    assert "Return the indices of the 7 most relevant passages" in prompts.get("reranker", top_n=7)
    assert "{messages}" in prompts.get("summary")                                    # the summariser fills this one in itself


def test_a_missing_prompt_or_value_is_an_error_that_names_it():
    with pytest.raises(ConfigError, match="'no_such_prompt' is not defined"):
        prompts.get("no_such_prompt")
    with pytest.raises(ConfigError, match="top_n"):
        prompts.get("reranker")                                                      # the value the code must pass is missing
    with pytest.raises(ConfigError, match="use get_map"):
        prompts.get("role_notes")


def test_a_prompt_name_used_in_two_files_is_refused(tmp_path, monkeypatch):
    (tmp_path / "a.yaml").write_text("worker: one\n", encoding="utf-8")
    (tmp_path / "b.yaml").write_text("worker: two\n", encoding="utf-8")
    monkeypatch.setattr(prompts, "PROMPTS_DIR", tmp_path)
    prompts._all.cache_clear()
    try:
        with pytest.raises(ConfigError, match="defined twice: in a.yaml and in b.yaml"):
            prompts.get("worker")
    finally:
        monkeypatch.undo()
        prompts._all.cache_clear()
