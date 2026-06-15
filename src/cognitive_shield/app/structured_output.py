"""Structured output envelope for the Functional Local Prototype Engine.

This module creates a bounded prototype output envelope around the local runner
result.

It intentionally does not implement the final Canonical Output Schema, risk
scoring, confidence scoring, Shield Decision output, governance decisions, or
educational behavior.
"""

from __future__ import annotations

from typing import Any

from cognitive_shield.app.local_runner import run_default_local_prototype


OUTPUT_STATUS = "created"
OUTPUT_FORMAT_VERSION = "0.1"
PROTOTYPE_PHASE = "functional_local_prototype_engine"


def build_structured_output() -> dict[str, Any]:
    """Build a bounded structured output envelope for the local prototype."""

    runner_output = run_default_local_prototype()

    return {
        "output_status": OUTPUT_STATUS,
        "output_format_version": OUTPUT_FORMAT_VERSION,
        "prototype_phase": PROTOTYPE_PHASE,
        "runner_output": runner_output,
    }


__all__ = [
    "OUTPUT_FORMAT_VERSION",
    "OUTPUT_STATUS",
    "PROTOTYPE_PHASE",
    "build_structured_output",
]
