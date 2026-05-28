"""
Minimal ACP schema validator boundary for Cognitive Shield.

This module provides a controlled Agent Communication Protocol (ACP) schema
validation boundary.

It validates only the minimal structural shape of an existing ACPMessage-like
object. It does not route to agents, dispatch messages, enforce scope,
orchestrate agent communication, generate Analysis, execute runtime pipeline
behavior, or introduce downstream pipeline logic.
"""

from cognitive_shield.core.agent_communication_protocol_acp.cmo_boundary import (
    SOURCE_STAGE,
    TARGET_STAGE,
)


REQUIRED_ACP_MESSAGE_FIELDS = {
    "acp_message_status",
    "source_stage",
    "target_stage",
    "acp_bundle_status",
    "decomposition_result",
    "field_envelope",
}


def validate_acp_message_schema(
    acp_message: dict[str, object],
) -> dict[str, object]:
    """
    Validate the minimal structural shape of an ACPMessage-like object.

    This function preserves the original bounded MDS DecompositionResult and
    CMO field envelope. It returns only a schema validation status. It does not
    route, dispatch, enforce scope, orchestrate, generate Analysis, or execute
    downstream pipeline behavior.
    """
    acp_message_status = acp_message.get("acp_message_status", "")
    acp_bundle_status = acp_message.get("acp_bundle_status", "")

    has_required_fields = REQUIRED_ACP_MESSAGE_FIELDS.issubset(acp_message.keys())

    validation_status = (
        "acp_schema_valid"
        if acp_message_status == "acp_message_created" and has_required_fields
        else "acp_schema_invalid"
    )

    return {
        "acp_schema_validation_status": validation_status,
        "source_stage": acp_message.get("source_stage", SOURCE_STAGE),
        "target_stage": acp_message.get("target_stage", TARGET_STAGE),
        "acp_message_status": acp_message_status,
        "acp_bundle_status": acp_bundle_status,
        "decomposition_result": acp_message.get("decomposition_result", {}),
        "field_envelope": acp_message.get("field_envelope", {}),
    }


__all__ = [
    "REQUIRED_ACP_MESSAGE_FIELDS",
    "validate_acp_message_schema",
]
