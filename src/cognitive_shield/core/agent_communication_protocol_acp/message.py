"""
ACP message boundary for Cognitive Shield.

This module provides a controlled Agent Communication Protocol (ACP) message
boundary.

It creates only a minimal ACPMessage-like structural object from an existing
ACPBundle. It does not route to agents, dispatch messages, orchestrate agent
communication, generate Analysis, execute runtime pipeline behavior, or
introduce downstream pipeline logic.
"""

from cognitive_shield.core.agent_communication_protocol_acp.cmo_boundary import (
    SOURCE_STAGE,
    TARGET_STAGE,
)


def build_acp_message(
    acp_bundle: dict[str, object],
) -> dict[str, object]:
    """
    Build a minimal ACPMessage from an existing ACPBundle.

    This function preserves the original bounded MDS DecompositionResult and
    CMO field envelope. It returns only a minimal ACPMessage status. It does not
    route, dispatch, orchestrate, generate Analysis, or execute downstream
    pipeline behavior.
    """
    acp_bundle_status = acp_bundle.get("acp_bundle_status", "")

    acp_message_status = (
        "acp_message_created"
        if acp_bundle_status == "acp_bundle_created"
        else "not_ready_for_acp_message"
    )

    return {
        "acp_message_status": acp_message_status,
        "source_stage": acp_bundle.get("source_stage", SOURCE_STAGE),
        "target_stage": acp_bundle.get("target_stage", TARGET_STAGE),
        "acp_bundle_status": acp_bundle_status,
        "decomposition_result": acp_bundle.get("decomposition_result", {}),
        "field_envelope": acp_bundle.get("field_envelope", {}),
    }


__all__ = [
    "build_acp_message",
]
