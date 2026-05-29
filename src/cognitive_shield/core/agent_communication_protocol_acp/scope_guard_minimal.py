"""
Minimal ACP Scope Guard boundary for Cognitive Shield.

This module provides a controlled Agent Communication Protocol (ACP) Scope
Guard boundary.

It checks only whether an existing ACP schema validation result is minimally
in-scope for future ACP processing. It does not route to agents, dispatch
messages, create agent instructions, call Protocol Router behavior, generate
Analysis, execute runtime pipeline behavior, or introduce downstream pipeline
logic.
"""

from cognitive_shield.core.agent_communication_protocol_acp.cmo_boundary import (
    SOURCE_STAGE,
    TARGET_STAGE,
)


def check_acp_scope_guard(
    acp_schema_validation: dict[str, object],
) -> dict[str, object]:
    """
    Check minimal ACP scope from an existing schema validation result.

    This function preserves the original bounded MDS DecompositionResult and
    CMO field envelope. It returns only a minimal scope status. It does not
    route, dispatch, create agent instructions, orchestrate, generate Analysis,
    or execute downstream pipeline behavior.
    """
    schema_status = acp_schema_validation.get(
        "acp_schema_validation_status",
        "",
    )
    acp_message_status = acp_schema_validation.get("acp_message_status", "")
    acp_bundle_status = acp_schema_validation.get("acp_bundle_status", "")

    scope_status = (
        "acp_scope_allowed"
        if schema_status == "acp_schema_valid"
        else "acp_scope_rejected"
    )

    return {
        "acp_scope_status": scope_status,
        "source_stage": acp_schema_validation.get("source_stage", SOURCE_STAGE),
        "target_stage": acp_schema_validation.get("target_stage", TARGET_STAGE),
        "acp_schema_validation_status": schema_status,
        "acp_message_status": acp_message_status,
        "acp_bundle_status": acp_bundle_status,
        "decomposition_result": acp_schema_validation.get(
            "decomposition_result",
            {},
        ),
        "field_envelope": acp_schema_validation.get("field_envelope", {}),
    }


__all__ = [
    "check_acp_scope_guard",
]
