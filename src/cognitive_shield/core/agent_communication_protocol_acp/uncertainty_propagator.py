"""
Agent Communication Protocol (ACP) uncertainty propagator scaffold for Cognitive Shield.

This module is a Sprint 1 bounded scaffold. It does not implement real
uncertainty propagation, confidence evaluation, aggregation, routing,
or downstream pipeline behavior.
"""

from cognitive_shield.core.agent_communication_protocol_acp.contracts import (
    ACPMessage,
)


def build_uncertainty_preview(message: ACPMessage) -> dict[str, str]:
    """
    Build a minimal uncertainty preview for an ACPMessage.

    This is a scaffold-level helper only. It does not propagate uncertainty,
    calculate confidence, aggregate signals, escalate conflicts, export
    synthesis, or execute downstream analysis.
    """
    return {
        "message_id": message.message_id,
        "message_type": message.message_type,
        "uncertainty_status": "preview_only",
    }


__all__ = [
    "build_uncertainty_preview",
]
