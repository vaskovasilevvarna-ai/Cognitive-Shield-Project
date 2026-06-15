"""JSON output rendering for the Functional Local Prototype Engine.

This module converts the bounded structured output envelope into a stable JSON
string suitable for local prototype display or future CLI output.

It intentionally does not implement file writing, full CLI behavior, risk
scoring, confidence scoring, verdict production, Shield Decision output,
governance decisions, or educational behavior.
"""

from __future__ import annotations

import json
from typing import Any

from cognitive_shield.app.structured_output import build_structured_output


JSON_OUTPUT_STATUS = "rendered"
JSON_OUTPUT_FORMAT = "json"
JSON_OUTPUT_FORMAT_VERSION = "0.1"


def build_json_output() -> str:
    """Build a stable JSON string from the bounded structured output envelope."""

    structured_output: dict[str, Any] = build_structured_output()

    json_ready_output: dict[str, Any] = {
        "json_output_status": JSON_OUTPUT_STATUS,
        "json_output_format": JSON_OUTPUT_FORMAT,
        "json_output_format_version": JSON_OUTPUT_FORMAT_VERSION,
        "structured_output": structured_output,
    }

    return json.dumps(
        json_ready_output,
        indent=2,
        sort_keys=True,
    )


__all__ = [
    "JSON_OUTPUT_FORMAT",
    "JSON_OUTPUT_FORMAT_VERSION",
    "JSON_OUTPUT_STATUS",
    "build_json_output",
]
