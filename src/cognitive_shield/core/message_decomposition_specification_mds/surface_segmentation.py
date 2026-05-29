"""
MDS explicit surface segmentation for Cognitive Shield.

This module provides a minimal explicit surface segmentation behavior.

It splits source text only by visible line / paragraph boundaries. It does not
implement claim extraction, implicit inference, framing extraction, relation
inference, full DecompositionResult construction, CMO construction, ACP routing,
Analysis generation, runtime pipeline execution, or downstream pipeline logic.
"""

from cognitive_shield.core.message_decomposition_specification_mds.surface_preparation import (
    MDS_STAGE,
)

SURFACE_UNIT_TYPE = "surface_text"


def segment_surface_text_explicit(source_text: str) -> dict[str, object]:
    """
    Segment source_text by explicit visible line boundaries only.

    This function preserves segment text and order. It does not infer meaning,
    extract claims, create framing units, create relation objects, or construct
    a DecompositionResult.
    """
    if not source_text.strip():
        return {
            "mds_stage": MDS_STAGE,
            "segmentation_status": "blocked_invalid_surface_text",
            "surface_units": [],
        }

    surface_lines = [
        line.strip()
        for line in source_text.splitlines()
        if line.strip()
    ]

    if not surface_lines:
        return {
            "mds_stage": MDS_STAGE,
            "segmentation_status": "blocked_invalid_surface_text",
            "surface_units": [],
        }

    surface_units = [
        {
            "surface_unit_id": f"surface-unit-{index:03d}",
            "source_text": line,
            "unit_type": SURFACE_UNIT_TYPE,
            "mds_stage": MDS_STAGE,
            "surface_status": "surface_unit_created",
            "order_index": str(index),
        }
        for index, line in enumerate(surface_lines, start=1)
    ]

    return {
        "mds_stage": MDS_STAGE,
        "segmentation_status": "surface_segments_created",
        "surface_units": surface_units,
    }


__all__ = [
    "SURFACE_UNIT_TYPE",
    "segment_surface_text_explicit",
]
