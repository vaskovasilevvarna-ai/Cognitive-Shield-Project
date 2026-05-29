"""
Message Decomposition Specification (MDS) service scaffold for Cognitive Shield.

This module is a Sprint 1 bounded scaffold. It does not implement real message
decomposition behavior, claim extraction, relation inference, taxonomy logic,
risk scoring, or downstream pipeline logic.
"""

from cognitive_shield.core.message_decomposition_specification_mds.contracts import (
    InputMessage,
)
from cognitive_shield.core.message_decomposition_specification_mds.validator import (
    is_valid_input_message,
)


def can_accept_input_message(message: InputMessage) -> bool:
    """
    Check whether an InputMessage can enter the future MDS service boundary.

    This is a scaffold-level readiness check only. It delegates to the minimal
    InputMessage surface validator and does not perform decomposition.
    """
    return is_valid_input_message(message)


__all__ = [
    "can_accept_input_message",
]
