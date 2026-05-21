"""
Core Input readiness scaffold for Cognitive Shield.

This module provides a minimal local Input-side readiness status helper.
It does not implement Message Decomposition Specification (MDS) behavior,
runtime pipeline execution, language routing, source-type inference, or
downstream pipeline logic.
"""

from cognitive_shield.core.input.contracts import InputMessage
from cognitive_shield.core.input.validator import is_valid_input_source


def build_input_readiness_status(message: InputMessage) -> dict[str, str]:
    """
    Build a minimal readiness status for an InputMessage.

    This helper checks whether the message is ready at the Input boundary only.
    It does not call MDS modules, route languages, infer source types, create
    decomposition fields, or execute downstream pipeline behavior.
    """
    if is_valid_input_source(message):
        return {
            "message_id": message.message_id,
            "language": message.language,
            "input_status": "ready",
            "reason": "minimal_input_source_valid",
        }

    return {
        "message_id": message.message_id,
        "language": message.language,
        "input_status": "blocked",
        "reason": "minimal_input_source_invalid",
    }


__all__ = [
    "build_input_readiness_status",
]
