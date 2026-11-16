"""The prompts, kept apart from the code: every prompt the application sends to a model is text in
config/prompts/*.yaml, one file per part of the app.

    prompts.get("worker")                    -> the worker's system prompt
    prompts.get("reranker", top_n=5)         -> a prompt with a value filled in
    prompts.get_map("role_notes")            -> a group of short texts, by key

A prompt can include another text with {{name}}: {{data_rule}} and {{memory_rule}} (shared.yaml) are filled
in from the files, any other name from the values the caller passes. Single braces such as {messages} are left
alone (they belong to the library that uses the prompt). A missing prompt, a name used in two files, or a
{{name}} nobody fills in stops the app at start with a message that names the file.
"""
from __future__ import annotations

import re
from functools import lru_cache
from typing import Any

import yaml

from .config import CONFIG_DIR, ConfigError

PROMPTS_DIR = CONFIG_DIR / "prompts"
SHARED = ("data_rule", "memory_rule")              # texts other prompts may include
_PLACEHOLDER = re.compile(r"\{\{(\w+)\}\}")


@lru_cache(maxsize=1)
def _all() -> dict[str, Any]:
    files = sorted(PROMPTS_DIR.glob("*.yaml"))
    if not files:
        raise ConfigError(f"No prompt files found in {PROMPTS_DIR}")
    out: dict[str, Any] = {}
    source: dict[str, str] = {}
    for path in files:
        with path.open("r", encoding="utf-8") as fh:
            data = yaml.safe_load(fh) or {}
        for name, value in data.items():
            if name in out:
                raise ConfigError(f"Prompt '{name}' is defined twice: in {source[name]} and in {path.name}")
            out[name], source[name] = value, path.name
    return out


def _raw(name: str) -> Any:
    prompts = _all()
    if name not in prompts:
        raise ConfigError(f"Prompt '{name}' is not defined in {PROMPTS_DIR} (known: {', '.join(sorted(prompts))})")
    return prompts[name]


def _fill(name: str, text: str, values: dict[str, Any]) -> str:
    def put(m: re.Match) -> str:
        key = m.group(1)
        if key in values:
            return str(values[key])
        if key in SHARED and key != name:
            return str(_raw(key))
        raise ConfigError(f"Prompt '{name}' uses {{{{{key}}}}}, which is neither a shared text nor a value passed by the code")

    return _PLACEHOLDER.sub(put, text)


def get(name: str, **values: Any) -> str:
    """The prompt `name` as text, with its {{...}} parts filled in."""
    raw = _raw(name)
    if not isinstance(raw, str):
        raise ConfigError(f"Prompt '{name}' is a group of texts; use get_map")
    return _fill(name, raw, values)


def get_map(name: str) -> dict[str, str]:
    """A group of short texts by key, e.g. the note per role."""
    raw = _raw(name)
    if not isinstance(raw, dict):
        raise ConfigError(f"Prompt '{name}' is a single text; use get")
    return {str(k): _fill(name, str(v), {}) for k, v in raw.items()}


def names() -> list[str]:
    return sorted(_all())
