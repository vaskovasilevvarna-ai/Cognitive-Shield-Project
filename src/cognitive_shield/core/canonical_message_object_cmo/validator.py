"""
Canonical Message Object (CMO) validator scaffold for Cognitive Shield.

This module is a Sprint 1 bounded scaffold. It does not implement real CMO
validation, CMO construction, Message Decomposition Specification (MDS) output
conversion, claim graph construction, taxonomy logic, risk scoring, or
downstream pipeline logic.
"""

from cognitive_shield.core.canonical_message_object_cmo.contracts import (
    InputMessage,
)


def is_valid_cmo_source_message(message: InputMessage) -> bool:
    """
    Check whether an InputMessage has minimal fields for future CMO processing.

    This is a scaffold-level check only. It does not validate a Canonical
    Message Object, construct a CMO, convert MDS output, or inspect analytical
    units.
    """
    return bool(
        message.message_id
        and message.raw_text
        and message.language
    )


__all__ = [
    "is_valid_cmo_source_message",
]
