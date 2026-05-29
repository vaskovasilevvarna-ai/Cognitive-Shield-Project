"""
CMO structural contract boundary for Cognitive Shield.

This module provides a controlled Canonical Message Object (CMO) structural
contract boundary.

It checks whether a minimal CMO shell is ready for a future CMO construction
step. It does not construct a full Canonical Message Object, populate a CMO
schema, map CMO fields, normalize content, enrich content, route to ACP,
generate Analysis, execute runtime pipeline behavior, or introduce downstream
pipeline logic.
"""

from cognitive_shield.core.canonical_message_object_cmo.mds_boundary import (
    SOURCE_STAGE,
    TARGET_STAGE,
)


def build_cmo_structural_contract(
    cmo_shell: dict[str, object],
) -> dict[str, object]:
    """
    Build a minimal CMO structural contract from an existing CMO shell.

    This function preserves the original decomposition result and shell status.
    It does not construct a full Canonical Message Object, populate schema
    fields, map data, enrich content, route to ACP, generate Analysis, or
    execute downstream pipeline behavior.
    """
    cmo_shell_status = cmo_shell.get("cmo_shell_status", "")

    cmo_contract_status = (
        "cmo_structural_contract_ready"
        if cmo_shell_status == "cmo_shell_created"
        else "not_ready_for_cmo_structural_contract"
    )

    return {
        "cmo_contract_status": cmo_contract_status,
        "source_stage": cmo_shell.get("source_stage", SOURCE_STAGE),
        "target_stage": cmo_shell.get("target_stage", TARGET_STAGE),
        "cmo_shell_status": cmo_shell_status,
        "decomposition_result": cmo_shell.get("decomposition_result", {}),
    }


__all__ = [
    "build_cmo_structural_contract",
]
