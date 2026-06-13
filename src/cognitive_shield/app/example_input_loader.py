"""Example input loader for the Functional Local Prototype Engine.

This module loads a controlled example JSON input and passes its message content
into the bounded Functional Local Prototype Engine entry wrapper.

It intentionally performs no analysis, no taxonomy classification, no risk
scoring, no confidence scoring, and no verdict production.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from cognitive_shield.app.functional_local_engine import run_functional_local_engine


EXPECTED_INPUT_TYPE = "single_message"


def load_single_message_example(path: str | Path) -> dict[str, Any]:
    """Load and validate a controlled single-message example input."""

    input_path = Path(path)
    payload = json.loads(input_path.read_text(encoding="utf-8"))

    if not isinstance(payload, dict):
        raise ValueError("Example input must be a JSON object.")

    input_type = payload.get("input_type")
    if input_type != EXPECTED_INPUT_TYPE:
        raise ValueError("Example input must have input_type='single_message'.")

    content = payload.get("content")
    if not isinstance(content, str) or not content.strip():
        raise ValueError("Example input must contain a non-empty string 'content' field.")

    return payload


def run_engine_from_example(path: str | Path) -> dict[str, Any]:
    """Run the bounded local engine entry wrapper from an example JSON input."""

    payload = load_single_message_example(path)
    result = run_functional_local_engine(payload["content"])

    return {
        "example_input_id": payload.get("id", ""),
        "example_language": payload.get("language", ""),
        "example_input_type": payload["input_type"],
        "example_loader_status": "loaded_single_message_example",
        "engine_result": result,
    }


__all__ = [
    "EXPECTED_INPUT_TYPE",
    "load_single_message_example",
    "run_engine_from_example",
]
