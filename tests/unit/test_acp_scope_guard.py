"""Unit tests for the ACP scope guard scaffold."""

from cognitive_shield.core.agent_communication_protocol_acp.contracts import (
    ACPMessage,
)
from cognitive_shield.core.agent_communication_protocol_acp.scope_guard import (
    build_scope_preview,
)


def test_build_scope_preview_returns_minimal_scope_fields() -> None:
    """ACP scope guard scaffold returns scope preview fields only."""
    message = ACPMessage(
        message_id="acp-msg-001",
        sender="mds",
        recipient="analysis",
        message_type="analysis_request",
    )

    scope_preview = build_scope_preview(message)

    assert scope_preview == {
        "sender": "mds",
        "recipient": "analysis",
        "message_type": "analysis_request",
        "scope_status": "preview_only",
    }
