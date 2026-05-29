"""
Message Decomposition Specification (MDS) mapper scaffold for Cognitive Shield.

This module is a Sprint 1 bounded scaffold. It does not implement real message
decomposition, surface segmentation, claim extraction, relation inference,
taxonomy logic, risk scoring, or downstream pipeline logic.
"""

from cognitive_shield.core.message_decomposition_specification_mds.contracts import (
    InputMessage,
)


def build_input_trace_map(message: InputMessage) -> dict[str, str]:
    """
    Build a minimal trace map for an InputMessage.

    This is a scaffold-level mapping helper only. It does not create surface
    segments, claims, framing units, relations, context carriers, taxonomy
    labels, risk signals, or output structures.
    """
    return {
        "message_id": message.message_id,
        "language": message.language,
    }


__all__ = [
    "build_input_trace_map",
]
