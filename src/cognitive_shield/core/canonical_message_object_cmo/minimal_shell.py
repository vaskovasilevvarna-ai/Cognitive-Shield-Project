"""
Minimal CMO shell for Cognitive Shield.

This module provides a controlled Canonical Message Object (CMO) shell boundary.

It creates only a minimal CMO shell from an eligible MDS-to-CMO boundary result.
It does not construct a full Canonical Message Object, populate a CMO schema,
map CMO fields, route to ACP, generate Analysis, execute runtime pipeline
behavior, or introduce downstream pipeline logic.
"""

from cognitive_shield.core.canonical_message_object_cmo.mds_boundary import (
    SOURCE_STAGE,
    TARGET_STAGE,
)


def build_minimal_cmo_shell(
    mds_boundary_result: dict[str, object],
) -> dict[str, object]:
    """
    Build a minimal CMO shell from an eligible MDS-to-CMO boundary result.

    This function preserves the original MDS DecompositionResult and boundary
    status. It does not construct a full Canonical Message Object, map fields,
    enrich content, route to ACP, generate Analysis, or execute downstream
    pipeline behavior.
    """
    boundary_status = mds_boundary_result.get("boundary_status", "")

    cmo_shell_status = (
        "cmo_shell_created"
        if boundary_status == "eligible_for_cmo_boundary"
        else "not_eligible_for_cmo_shell"
    )

    return {
        "cmo_shell_status": cmo_shell_status,
        "source_stage": mds_boundary_result.get("source_stage", SOURCE_STAGE),
        "target_stage": mds_boundary_result.get("target_stage", TARGET_STAGE),
        "boundary_status": boundary_status,
        "decomposition_result": mds_boundary_result.get(
            "decomposition_result",
            {},
        ),
    }


__all__ = [
    "build_minimal_cmo_shell",
]
