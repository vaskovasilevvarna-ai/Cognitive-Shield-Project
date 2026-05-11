"""Unit tests for the ACP uncertainty propagator scaffold."""

from cognitive_shield.core.agent_communication_protocol_acp.contracts import (
    ACPMessage,
)
from cognitive_shield.core.agent_communication_protocol_acp.uncertainty_propagator import (
    build_uncertainty_preview,
)


def test_build_uncertainty_preview_returns_minimal_uncertainty_fields() -> None:
    """ACP uncertainty propagator scaffold returns uncertainty preview fields only."""
    message = ACPMessage(
        message_id="acp-msg-001",
        sender="analysis",
        recipient="arbiter",
        message_type="uncertainty_signal",
    )

    uncertainty_preview = build_uncertainty_preview(message)

    assert uncertainty_preview == {
        "message_id": "acp-msg-001",
        "message_type": "uncertainty_signal",
        "uncertainty_status": "preview_only",
    }
