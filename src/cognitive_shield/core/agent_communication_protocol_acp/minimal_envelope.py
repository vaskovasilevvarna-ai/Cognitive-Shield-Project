"""
ACP minimal envelope boundary for Cognitive Shield.

This module provides a controlled Agent Communication Protocol (ACP) minimal
envelope.

It creates only a minimal ACP envelope from an existing ACP boundary eligibility
result. It does not create an ACPBundle, create an ACPMessage, route to agents,
dispatch messages, orchestrate agent communication, generate Analysis, execute
runtime pipeline behavior, or introduce downstream pipeline logic.
"""

from cognitive_shield.core.agent_communication_protocol_acp.cmo_boundary import (
    SOURCE_STAGE,
    TARGET_STAGE,
)


def build_acp_minimal_envelope(
    acp_boundary_result: dict[str, object],
) -> dict[str, object]:
    """
    Build a minimal ACP envelope from an eligible ACP boundary result.

    This function preserves the original bounded MDS DecompositionResult and
    CMO field envelope. It returns only a minimal ACP envelope status. It does
    not create ACP bundles, create ACP messages, route, dispatch, orchestrate,
    generate Analysis, or execute downstream pipeline behavior.
    """
    acp_boundary_status = acp_boundary_result.get("acp_boundary_status", "")

    acp_envelope_status = (
        "acp_minimal_envelope_created"
        if acp_boundary_status == "eligible_for_acp_boundary"
        else "not_ready_for_acp_minimal_envelope"
    )

    return {
        "acp_envelope_status": acp_envelope_status,
        "source_stage": acp_boundary_result.get("source_stage", SOURCE_STAGE),
        "target_stage": acp_boundary_result.get("target_stage", TARGET_STAGE),
        "acp_boundary_status": acp_boundary_status,
        "decomposition_result": acp_boundary_result.get(
            "decomposition_result",
            {},
        ),
        "field_envelope": acp_boundary_result.get("field_envelope", {}),
    }


__all__ = [
    "build_acp_minimal_envelope",
]
