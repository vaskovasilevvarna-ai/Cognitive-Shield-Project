"""
Agent Communication Protocol (ACP) scope guard scaffold for Cognitive Shield.

This module is a Sprint 1 bounded scaffold. It does not implement real scope
enforcement, routing, orchestration, governance behavior, analysis execution,
or downstream pipeline logic.
"""

from cognitive_shield.core.agent_communication_protocol_acp.contracts import (
    ACPMessage,
)


def build_scope_preview(message: ACPMessage) -> dict[str, str]:
    """
    Build a minimal scope preview for an ACPMessage.

    This is a scaffold-level helper only. It does not enforce scope, block
    messages, route agents, validate schemas, register contradictions,
    propagate uncertainty, or export synthesis.
    """
    return {
        "sender": message.sender,
        "recipient": message.recipient,
        "message_type": message.message_type,
        "scope_status": "preview_only",
    }


__all__ = [
    "build_scope_preview",
]
