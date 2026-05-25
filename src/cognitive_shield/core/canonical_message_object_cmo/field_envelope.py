"""
CMO field envelope boundary for Cognitive Shield.

This module provides a controlled Canonical Message Object (CMO) field envelope
boundary.

It creates only a minimal field envelope from an existing CMO structural
contract. It does not construct a full Canonical Message Object, populate a CMO
schema, map fields, normalize content, enrich content, route to ACP, generate
Analysis, execute runtime pipeline behavior, or introduce downstream pipeline
logic.
"""

from cognitive_shield.core.canonical_message_object_cmo.mds_boundary import (
    SOURCE_STAGE,
    TARGET_STAGE,
)


def build_cmo_field_envelope(
    cmo_structural_contract: dict[str, object],
) -> dict[str, object]:
    """
    Build a minimal CMO field envelope from an existing structural contract.

    This function preserves the original DecompositionResult and exposes only a
    bounded placeholder field envelope. It does not construct a full CMO, map
    fields, populate schema fields, normalize content, enrich content, route to
    ACP, generate Analysis, or execute downstream pipeline behavior.
    """
    cmo_contract_status = cmo_structural_contract.get(
        "cmo_contract_status",
        "",
    )

    envelope_status = (
        "cmo_field_envelope_created"
        if cmo_contract_status == "cmo_structural_contract_ready"
        else "not_ready_for_cmo_field_envelope"
    )

    field_envelope = (
        {
            "source_reference": "bounded_decomposition_result",
            "structural_status": "field_envelope_placeholder",
        }
        if envelope_status == "cmo_field_envelope_created"
        else {}
    )

    return {
        "cmo_field_envelope_status": envelope_status,
        "source_stage": cmo_structural_contract.get("source_stage", SOURCE_STAGE),
        "target_stage": cmo_structural_contract.get("target_stage", TARGET_STAGE),
        "cmo_contract_status": cmo_contract_status,
        "decomposition_result": cmo_structural_contract.get(
            "decomposition_result",
            {},
        ),
        "field_envelope": field_envelope,
    }


__all__ = [
    "build_cmo_field_envelope",
]
