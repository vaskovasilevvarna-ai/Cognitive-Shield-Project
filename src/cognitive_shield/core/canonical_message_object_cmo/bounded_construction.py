"""
CMO bounded construction boundary for Cognitive Shield.

This module provides a controlled Canonical Message Object (CMO) bounded
construction candidate.

It creates only a bounded construction candidate from an existing minimal CMO
object. It does not construct a full Canonical Message Object, populate a CMO
schema, map fields, normalize content, enrich content, route to ACP, generate
Analysis, execute runtime pipeline behavior, or introduce downstream pipeline
logic.
"""

from cognitive_shield.core.canonical_message_object_cmo.mds_boundary import (
    SOURCE_STAGE,
    TARGET_STAGE,
)


def build_bounded_cmo_construction(
    minimal_cmo_object: dict[str, object],
) -> dict[str, object]:
    """
    Build a bounded CMO construction candidate from a minimal CMO object.

    This function preserves the original DecompositionResult and field envelope.
    It does not create a full Canonical Message Object, populate schema fields,
    map semantic fields, normalize content, enrich content, route to ACP,
    generate Analysis, or execute downstream pipeline behavior.
    """
    minimal_object_status = minimal_cmo_object.get(
        "minimal_cmo_object_status",
        "",
    )

    construction_status = (
        "bounded_cmo_construction_created"
        if minimal_object_status == "minimal_cmo_object_created"
        else "not_ready_for_bounded_cmo_construction"
    )

    return {
        "bounded_cmo_construction_status": construction_status,
        "source_stage": minimal_cmo_object.get("source_stage", SOURCE_STAGE),
        "target_stage": minimal_cmo_object.get("target_stage", TARGET_STAGE),
        "minimal_cmo_object_status": minimal_object_status,
        "decomposition_result": minimal_cmo_object.get(
            "decomposition_result",
            {},
        ),
        "field_envelope": minimal_cmo_object.get("field_envelope", {}),
    }


__all__ = [
    "build_bounded_cmo_construction",
]
