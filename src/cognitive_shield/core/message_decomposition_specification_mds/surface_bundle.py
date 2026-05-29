"""
MDS surface bundle boundary for Cognitive Shield.

This module provides a minimal surface bundle MDS behavior.

It combines surface-level preparation and one single surface unit without
introducing segmentation, claim extraction, implicit inference, framing
extraction, relation inference, full DecompositionResult construction,
CMO construction, ACP routing, Analysis generation, runtime pipeline execution,
or downstream pipeline logic.
"""

from cognitive_shield.core.message_decomposition_specification_mds.surface_preparation import (
    MDS_STAGE,
    prepare_mds_surface_minimal,
)
from cognitive_shield.core.message_decomposition_specification_mds.surface_units import (
    build_minimal_surface_unit,
)


def build_mds_surface_bundle(message) -> dict[str, object]:
    """
    Build a minimal MDS surface bundle.

    This function combines the existing surface preparation result and one
    minimal surface unit. It does not split text, extract claims, infer
    relations, create framing units, or construct a DecompositionResult.
    """
    surface_preparation = prepare_mds_surface_minimal(message)

    if surface_preparation["preparation_status"] != "prepared":
        return {
            "mds_stage": MDS_STAGE,
            "bundle_status": "blocked_invalid_surface_text",
            "surface_preparation": surface_preparation,
            "surface_unit": {},
        }

    surface_unit = build_minimal_surface_unit(
        surface_preparation["source_text"]
    )

    return {
        "mds_stage": MDS_STAGE,
        "bundle_status": "surface_bundle_created",
        "surface_preparation": surface_preparation,
        "surface_unit": surface_unit,
    }


__all__ = [
    "build_mds_surface_bundle",
]
