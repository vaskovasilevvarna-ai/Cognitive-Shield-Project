"""Unit tests for the ACP synthesis exporter scaffold."""

from cognitive_shield.core.agent_communication_protocol_acp.contracts import (
    ACPMessage,
)
from cognitive_shield.core.agent_communication_protocol_acp.synthesis_exporter import (
    build_synthesis_preview,
)


def test_build_synthesis_preview_returns_minimal_synthesis_fields() -> None:
    """ACP synthesis exporter scaffold returns synthesis preview fields only."""
    message = ACPMessage(
        message_id="acp-msg-001",
        sender="analysis",
        recipient="arbiter",
        message_type="synthesis_signal",
    )

    synthesis_preview = build_synthesis_preview(message)

    assert synthesis_preview == {
        "message_id": "acp-msg-001",
        "message_type": "synthesis_signal",
        "synthesis_status": "preview_only",
    }
