"""
MDS surface unit boundary for Cognitive Shield.

This module provides a minimal single-surface-unit MDS behavior.

It does not implement segmentation into multiple units, claim extraction,
implicit inference, framing extraction, relation inference, full
DecompositionResult construction, CMO construction, ACP routing, Analysis
generation, runtime pipeline execution, or downstream pipeline logic.
"""

MDS_STAGE = "message_decomposition_specification_mds"
SURFACE_UNIT_TYPE = "surface_text"


def build_minimal_surface_unit(source_text: str) -> dict[str, str]:
    """
    Build one minimal surface unit from source_text.

    This function preserves the original source text and creates only a
    single surface-level unit. It does not split text, extract claims, infer
    relations, create framing units, or construct a DecompositionResult.
    """
    if not source_text.strip():
        return {
            "surface_unit_id": "surface-unit-001",
            "source_text": source_text,
            "unit_type": SURFACE_UNIT_TYPE,
            "mds_stage": MDS_STAGE,
            "surface_status": "invalid_surface_text",
        }

    return {
        "surface_unit_id": "surface-unit-001",
        "source_text": source_text,
        "unit_type": SURFACE_UNIT_TYPE,
        "mds_stage": MDS_STAGE,
        "surface_status": "surface_unit_created",
    }


__all__ = [
    "MDS_STAGE",
    "SURFACE_UNIT_TYPE",
    "build_minimal_surface_unit",
]
