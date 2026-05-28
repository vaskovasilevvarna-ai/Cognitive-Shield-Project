"""
Protocol Router readiness boundary for Cognitive Shield.

This module provides a controlled Agent Communication Protocol (ACP) Protocol
Router readiness boundary.

It checks only whether an existing ACP Scope Guard result is minimally ready
for a future Protocol Router layer. It does not create routing decisions,
dispatch targets, agent instructions, selected agents, route tables, Analysis,
runtime pipeline behavior, or downstream pipeline logic.
"""

from cognitive_shield.core.agent_communication_protocol_acp.cmo_boundary import (
    SOURCE_STAGE,
    TARGET_STAGE,
)


def check_protocol_router_readiness(
    acp_scope_guard_result: dict[str, object],
) -> dict[str, object]:
    """
    Check minimal Protocol Router readiness from an ACP Scope Guard result.

    This function preserves the original bounded MDS DecompositionResult and
    CMO field envelope. It returns only a router readiness status. It does not
    route, dispatch, select agents, create route tables, generate Analysis, or
    execute downstream pipeline behavior.
    """
    acp_scope_status = acp_scope_guard_result.get("acp_scope_status", "")
    schema_status = acp_scope_guard_result.get(
        "acp_schema_validation_status",
        "",
    )
    acp_message_status = acp_scope_guard_result.get("acp_message_status", "")
    acp_bundle_status = acp_scope_guard_result.get("acp_bundle_status", "")

    readiness_status = (
        "protocol_router_ready"
        if acp_scope_status == "acp_scope_allowed"
        else "protocol_router_not_ready"
    )

    return {
        "protocol_router_readiness_status": readiness_status,
        "source_stage": acp_scope_guard_result.get("source_stage", SOURCE_STAGE),
        "target_stage": acp_scope_guard_result.get("target_stage", TARGET_STAGE),
        "acp_scope_status": acp_scope_status,
        "acp_schema_validation_status": schema_status,
        "acp_message_status": acp_message_status,
        "acp_bundle_status": acp_bundle_status,
        "decomposition_result": acp_scope_guard_result.get(
            "decomposition_result",
            {},
        ),
        "field_envelope": acp_scope_guard_result.get("field_envelope", {}),
    }


__all__ = [
    "check_protocol_router_readiness",
]
