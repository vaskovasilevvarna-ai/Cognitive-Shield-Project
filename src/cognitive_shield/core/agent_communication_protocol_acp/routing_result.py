"""
Minimal non-dispatch routing result boundary for Cognitive Shield.

This module provides a controlled Agent Communication Protocol (ACP) routing
result boundary for Sprint 4 MVP functional proof.

It creates only a minimal non-dispatch routing result from an existing Protocol
Router readiness result. It does not create real routing decisions, dispatch
targets, agent instructions, selected agents, route tables, Analysis, runtime
pipeline behavior, or downstream pipeline logic.
"""

from cognitive_shield.core.agent_communication_protocol_acp.cmo_boundary import (
    SOURCE_STAGE,
    TARGET_STAGE,
)


def build_minimal_routing_result(
    protocol_router_readiness: dict[str, object],
) -> dict[str, object]:
    """
    Build a minimal non-dispatch routing result from Protocol Router readiness.

    This function preserves the original bounded MDS DecompositionResult and
    CMO field envelope. It returns only a bounded routing-result status. It does
    not route, dispatch, select agents, create route tables, generate Analysis,
    or execute downstream pipeline behavior.
    """
    readiness_status = protocol_router_readiness.get(
        "protocol_router_readiness_status",
        "",
    )
    acp_scope_status = protocol_router_readiness.get("acp_scope_status", "")
    schema_status = protocol_router_readiness.get(
        "acp_schema_validation_status",
        "",
    )
    acp_message_status = protocol_router_readiness.get("acp_message_status", "")
    acp_bundle_status = protocol_router_readiness.get("acp_bundle_status", "")

    routing_result_status = (
        "route_ready_no_dispatch"
        if readiness_status == "protocol_router_ready"
        else "not_ready_for_routing"
    )

    return {
        "routing_result_status": routing_result_status,
        "source_stage": protocol_router_readiness.get("source_stage", SOURCE_STAGE),
        "target_stage": protocol_router_readiness.get("target_stage", TARGET_STAGE),
        "protocol_router_readiness_status": readiness_status,
        "acp_scope_status": acp_scope_status,
        "acp_schema_validation_status": schema_status,
        "acp_message_status": acp_message_status,
        "acp_bundle_status": acp_bundle_status,
        "decomposition_result": protocol_router_readiness.get(
            "decomposition_result",
            {},
        ),
        "field_envelope": protocol_router_readiness.get("field_envelope", {}),
    }


__all__ = [
    "build_minimal_routing_result",
]
