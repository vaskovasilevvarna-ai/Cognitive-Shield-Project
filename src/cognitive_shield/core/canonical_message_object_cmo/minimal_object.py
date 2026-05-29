"""
Minimal CMO object boundary for Cognitive Shield.

This module provides a controlled minimal Canonical Message Object (CMO)
object boundary.

It creates only a minimal CMO object from an existing CMO field envelope. It
does not construct a full Canonical Message Object, populate a CMO schema, map
fields, normalize content, enrich content, route to ACP, generate Analysis,
execute runtime pipeline behavior, or introduce downstream pipeline logic.
"""

from cognitive_shield.core.canonical_message_object_cmo.mds_boundary import (
    SOURCE_STAGE,
    TARGET_STAGE,
)


def build_minimal_cmo_object(
    cmo_field_envelope: dict[str, object],
) -> dict[str, object]:
    """
    Build a minimal CMO object from an existing CMO field envelope.

    This function preserves the original DecompositionResult and field envelope.
    It does not construct a full Canonical Message Object, populate schema
    fields, map data, normalize content, enrich content, route to ACP, generate
    Analysis, or execute downstream pipeline behavior.
    """
    envelope_status = cmo_field_envelope.get(
        "cmo_field_envelope_status",
        "",
    )

    object_status = (
        "minimal_cmo_object_created"
        if envelope_status == "cmo_field_envelope_created"
        else "not_ready_for_minimal_cmo_object"
    )

    return {
        "minimal_cmo_object_status": object_status,
        "source_stage": cmo_field_envelope.get("source_stage", SOURCE_STAGE),
        "target_stage": cmo_field_envelope.get("target_stage", TARGET_STAGE),
        "cmo_field_envelope_status": envelope_status,
        "decomposition_result": cmo_field_envelope.get(
            "decomposition_result",
            {},
        ),
        "field_envelope": cmo_field_envelope.get("field_envelope", {}),
    }


__all__ = [
    "build_minimal_cmo_object",
]
