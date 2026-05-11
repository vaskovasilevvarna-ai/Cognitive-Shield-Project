"""Unit tests for the ACP contradiction registrar scaffold."""

from cognitive_shield.core.agent_communication_protocol_acp.contracts import (
    ACPMessage,
)
from cognitive_shield.core.agent_communication_protocol_acp.contradiction_registrar import (
    build_contradiction_preview,
)


def test_build_contradiction_preview_returns_minimal_contradiction_fields() -> None:
    """ACP contradiction registrar scaffold returns contradiction preview fields only."""
    message = ACPMessage(
        message_id="acp-msg-001",
        sender="evidence",
        recipient="arbiter",
        message_type="analysis_signal",
    )

    contradiction_preview = build_contradiction_preview(message)

    assert contradiction_preview == {
        "message_id": "acp-msg-001",
        "message_type": "analysis_signal",
        "contradiction_status": "preview_only",
    }
