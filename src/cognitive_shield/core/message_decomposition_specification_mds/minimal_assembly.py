"""
MDS minimal assembly boundary for Cognitive Shield.

This module provides a minimal MDS-local assembly behavior.

It assembles already admitted MDS-local structures without constructing a full
DecompositionResult, preparing a Canonical Message Object (CMO), routing to ACP,
generating Analysis, performing inference, or executing downstream pipeline
logic.
"""

from cognitive_shield.core.message_decomposition_specification_mds.surface_preparation import (
    MDS_STAGE,
)


def build_mds_minimal_assembly(
    surface_bundle: dict[str, object],
    claim_unit_bundle: dict[str, object],
) -> dict[str, object]:
    """
    Build a minimal MDS-local assembly from existing bounded structures.

    This function groups an existing surface bundle and an existing claim unit
    bundle. It does not create new surface units, create new claim units, infer
    meaning, assess truth, assess evidence, construct a DecompositionResult,
    or prepare downstream handoff objects.
    """
    has_surface_bundle = bool(surface_bundle)
    has_claim_unit_bundle = bool(claim_unit_bundle)

    assembly_status = (
        "mds_minimal_assembly_created"
        if has_surface_bundle or has_claim_unit_bundle
        else "no_mds_structures"
    )

    return {
        "mds_stage": MDS_STAGE,
        "assembly_status": assembly_status,
        "surface_bundle": surface_bundle,
        "claim_unit_bundle": claim_unit_bundle,
    }


__all__ = [
    "build_mds_minimal_assembly",
]
