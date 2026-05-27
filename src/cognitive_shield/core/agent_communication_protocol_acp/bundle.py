"""
ACP bundle boundary for Cognitive Shield.

This module provides a controlled Agent Communication Protocol (ACP) bundle
boundary.

It creates only a minimal ACPBundle-like structural object from an existing ACP
minimal envelope. It does not create an ACPMessage, route to agents, dispatch
messages, orchestrate agent communication, generate Analysis, execute runtime
pipeline behavior, or introduce downstream pipeline logic.
"""

from cognitive_shield.core.agent_communication_protocol_acp.cmo_boundary import (
    SOURCE_STAGE,
    TARGET_STAGE,
)


def build_acp_bundle(
    acp_minimal_envelope: dict[str, object],
) -> dict[str, object]:
    """
    Build a minimal ACPBundle from an existing ACP minimal envelope.

    This function preserves the original bounded MDS DecompositionResult and
    CMO field envelope. It returns only a minimal ACPBundle status. It does not
    create ACP messages, route, dispatch, orchestrate, generate Analysis, or
    execute downstream pipeline behavior.
    """
    acp_envelope_status = acp_minimal_envelope.get("acp_envelope_status", "")

    acp_bundle_status = (
        "acp_bundle_created"
        if acp_envelope_status == "acp_minimal_envelope_created"
        else "not_ready_for_acp_bundle"
    )

    return {
        "acp_bundle_status": acp_bundle_status,
        "source_stage": acp_minimal_envelope.get("source_stage", SOURCE_STAGE),
        "target_stage": acp_minimal_envelope.get("target_stage", TARGET_STAGE),
        "acp_envelope_status": acp_envelope_status,
        "decomposition_result": acp_minimal_envelope.get(
            "decomposition_result",
            {},
        ),
        "field_envelope": acp_minimal_envelope.get("field_envelope", {}),
    }


__all__ = [
    "build_acp_bundle",
]
