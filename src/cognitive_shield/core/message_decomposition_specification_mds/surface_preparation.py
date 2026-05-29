"""
MDS surface preparation for Cognitive Shield.

This module provides the first admitted Sprint 2 MDS-side behavior:
surface-level preparation only.

It does not implement claim extraction, implicit inference, framing extraction,
relation inference, full DecompositionResult construction, CMO construction,
ACP routing, Analysis generation, runtime pipeline execution, or downstream
pipeline logic.
"""

from cognitive_shield.core.message_decomposition_specification_mds.contracts import (
    InputMessage,
)
from cognitive_shield.core.message_decomposition_specification_mds.validator import (
    is_valid_input_message,
)

MDS_STAGE = "message_decomposition_specification_mds"


def prepare_mds_surface_minimal(message: InputMessage) -> dict[str, str]:
    """
    Prepare minimal surface-level MDS input.

    This function preserves the original surface text and reports whether the
    message can enter the first MDS surface-preparation boundary. It does not
    segment text, extract claims, infer relations, create framing units, or
    construct a DecompositionResult.
    """
    if not is_valid_input_message(message) or not message.raw_text.strip():
        return {
            "message_id": message.message_id,
            "source_text": message.raw_text,
            "mds_stage": MDS_STAGE,
            "preparation_status": "blocked",
            "surface_status": "invalid_surface_text",
        }

    return {
        "message_id": message.message_id,
        "source_text": message.raw_text,
        "mds_stage": MDS_STAGE,
        "preparation_status": "prepared",
        "surface_status": "surface_text_preserved",
    }


__all__ = [
    "MDS_STAGE",
    "prepare_mds_surface_minimal",
]
