"""
MDS explicit claim unit bundle boundary for Cognitive Shield.

This module provides a minimal MDS-local claim unit bundle behavior.

It bundles existing explicit claim units without creating new claim units,
performing implicit inference, truth assessment, evidence assessment, framing
extraction, relation inference, DecompositionResult construction, CMO
construction, ACP routing, Analysis generation, runtime pipeline execution, or
downstream pipeline logic.
"""

from cognitive_shield.core.message_decomposition_specification_mds.claim_units import (
    EXPLICIT_CLAIM_UNIT_TYPE,
)
from cognitive_shield.core.message_decomposition_specification_mds.surface_preparation import (
    MDS_STAGE,
)


def build_explicit_claim_unit_bundle(
    claim_units: list[dict[str, str]],
) -> dict[str, object]:
    """
    Build a minimal MDS-local bundle from existing explicit claim units.

    This function preserves explicit claim unit records and their order. It
    does not create new claim units, infer meaning, assess truth, assess
    evidence, extract relations, or construct a DecompositionResult.
    """
    bundled_claim_units = []

    for claim_unit in claim_units:
        if claim_unit.get("unit_type") != EXPLICIT_CLAIM_UNIT_TYPE:
            continue

        if claim_unit.get("claim_unit_status") != "claim_unit_created":
            continue

        if not claim_unit.get("source_text", "").strip():
            continue

        bundled_claim_units.append(
            {
                "claim_unit_id": claim_unit.get("claim_unit_id", ""),
                "source_claim_candidate_id": claim_unit.get(
                    "source_claim_candidate_id",
                    "",
                ),
                "source_surface_unit_id": claim_unit.get(
                    "source_surface_unit_id",
                    "",
                ),
                "source_text": claim_unit.get("source_text", ""),
                "unit_type": EXPLICIT_CLAIM_UNIT_TYPE,
                "claim_unit_status": "claim_unit_created",
                "order_index": claim_unit.get("order_index", ""),
            }
        )

    bundle_status = (
        "claim_unit_bundle_created"
        if bundled_claim_units
        else "no_claim_units"
    )

    return {
        "mds_stage": MDS_STAGE,
        "bundle_status": bundle_status,
        "claim_units": bundled_claim_units,
    }


__all__ = [
    "build_explicit_claim_unit_bundle",
]
