"""
Canonical Message Object (CMO) builder scaffold for Cognitive Shield.

This module is a Sprint 1 bounded scaffold. It does not implement real CMO
construction, Message Decomposition Specification (MDS) output conversion,
claim graph construction, taxonomy logic, risk scoring, or downstream pipeline
logic.
"""

from cognitive_shield.core.canonical_message_object_cmo.contracts import (
    InputMessage,
)
from cognitive_shield.core.canonical_message_object_cmo.validator import (
    is_valid_cmo_source_message,
)


def can_build_from_input_message(message: InputMessage) -> bool:
    """
    Check whether an InputMessage can enter the future CMO builder boundary.

    This is a scaffold-level readiness check only. It delegates to the minimal
    CMO source-message validator and does not construct a Canonical Message
    Object.
    """
    return is_valid_cmo_source_message(message)


__all__ = [
    "can_build_from_input_message",
]
