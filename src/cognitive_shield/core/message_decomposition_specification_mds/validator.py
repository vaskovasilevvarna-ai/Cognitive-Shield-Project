"""
Message Decomposition Specification (MDS) validator scaffold for Cognitive Shield.

This module is a Sprint 1 bounded scaffold. It does not implement real MDS
validation, message decomposition behavior, claim extraction, or downstream
pipeline logic.
"""

from cognitive_shield.core.message_decomposition_specification_mds.contracts import (
    InputMessage,
)


def is_valid_input_message(message: InputMessage) -> bool:
    """
    Check whether an InputMessage has the minimal required surface fields.

    This is a scaffold-level check only. It does not validate decomposition,
    claims, framing, relations, context, taxonomy, risk, or policy behavior.
    """
    return bool(
        message.message_id
        and message.raw_text
        and message.language
    )


__all__ = [
    "is_valid_input_message",
]
