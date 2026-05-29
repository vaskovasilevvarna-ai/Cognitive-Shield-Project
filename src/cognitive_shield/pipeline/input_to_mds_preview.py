"""
Input to MDS preview scaffold for Cognitive Shield.

This module is a Sprint 1 bounded preview scaffold. It does not implement
runtime pipeline execution, real Input to MDS execution, real Message
Decomposition Specification (MDS) behavior, downstream pipeline logic, or
end-to-end message processing.
"""

from cognitive_shield.core.input.contracts import InputMessage
from cognitive_shield.core.input.validator import is_valid_input_source

MDS_TARGET_STAGE = "message_decomposition_specification_mds"


def build_input_to_mds_preview(message: InputMessage) -> dict[str, str]:
    """
    Build a minimal preview of the future Input to MDS handoff.

    This helper validates only minimal InputMessage source fields and returns a
    preview dictionary. It does not call MDS services, create decomposition
    outputs, segment text, extract claims, infer relations, or execute pipeline
    behavior.
    """
    if not is_valid_input_source(message):
        return {
            "message_id": message.message_id,
            "language": message.language,
            "source_status": "invalid_input_source",
            "target_stage": MDS_TARGET_STAGE,
            "handoff_status": "blocked_preview",
        }

    return {
        "message_id": message.message_id,
        "language": message.language,
        "source_status": "valid_input_source",
        "target_stage": MDS_TARGET_STAGE,
        "handoff_status": "preview_only",
    }


__all__ = [
    "MDS_TARGET_STAGE",
    "build_input_to_mds_preview",
]
