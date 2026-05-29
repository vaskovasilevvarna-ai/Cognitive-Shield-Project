"""
Agent Communication Protocol (ACP) contradiction registrar scaffold for Cognitive Shield.

This module is a Sprint 1 bounded scaffold. It does not implement real
contradiction registration, conflict detection, comparison logic, routing,
or downstream pipeline behavior.
"""

from cognitive_shield.core.agent_communication_protocol_acp.contracts import (
    ACPMessage,
)


def build_contradiction_preview(message: ACPMessage) -> dict[str, str]:
    """
    Build a minimal contradiction preview for an ACPMessage.

    This is a scaffold-level helper only. It does not detect contradictions,
    compare messages, build conflict maps, propagate uncertainty, export
    synthesis, or execute downstream analysis.
    """
    return {
        "message_id": message.message_id,
        "message_type": message.message_type,
        "contradiction_status": "preview_only",
    }


__all__ = [
    "build_contradiction_preview",
]
