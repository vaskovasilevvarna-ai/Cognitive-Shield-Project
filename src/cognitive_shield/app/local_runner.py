"""Local runner for the Functional Local Prototype Engine.

This module provides a small local execution entry point for the Functional
Local Prototype Engine phase.

It runs the controlled example input through the existing example input loader
and returns a structured bounded result.

It intentionally does not implement a full CLI interface, full runtime pipeline,
taxonomy classification, risk scoring, confidence scoring, governance decisions,
Shield Decision output, or educational behavior.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from cognitive_shield.app.example_input_loader import run_engine_from_example


RUNNER_MODE = "local_prototype"
RUNNER_STATUS = "completed"
DEFAULT_EXAMPLE_INPUT = Path("examples/single_message_inputs/minimal_message.json")


def _repo_root() -> Path:
    """Return the repository root based on this module location."""

    return Path(__file__).resolve().parents[3]


def default_example_input_path() -> Path:
    """Return the default controlled example input path."""

    return _repo_root() / DEFAULT_EXAMPLE_INPUT


def run_default_local_prototype() -> dict[str, Any]:
    """Run the bounded local prototype using the default example input."""

    input_path = default_example_input_path()
    engine_output = run_engine_from_example(input_path)

    return {
        "runner_status": RUNNER_STATUS,
        "runner_mode": RUNNER_MODE,
        "input_source": str(DEFAULT_EXAMPLE_INPUT),
        "engine_output": engine_output,
    }


__all__ = [
    "DEFAULT_EXAMPLE_INPUT",
    "RUNNER_MODE",
    "RUNNER_STATUS",
    "default_example_input_path",
    "run_default_local_prototype",
]
