"""
Agent Communication Protocol (ACP) router scaffold for Cognitive Shield.

This module is a Sprint 1 bounded scaffold. It does not implement real ACP
routing, agent orchestration, message dispatch, protocol state management,
analysis execution, governance behavior, or downstream pipeline logic.
"""

from cognitive_shield.core.agent_communication_protocol_acp.contracts import (
    ACPMessage,
)


def build_route_preview(message: ACPMessage) -> dict[str, str]:
    """
    Build a minimal route preview for an ACPMessage.

    This is a scaffold-level helper only. It does not route messages, dispatch
    agents, enforce scope, validate schemas, register contradictions, propagate
    uncertainty, or export synthesis.
    """
    return {
        "sender": message.sender,
        "recipient": message.recipient,
        "message_type": message.message_type,
    }


__all__ = [
    "build_route_preview",
]
