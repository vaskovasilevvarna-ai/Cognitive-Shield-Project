"""Unit tests for the ACP router scaffold."""

from cognitive_shield.core.agent_communication_protocol_acp.contracts import (
    ACPMessage,
)
from cognitive_shield.core.agent_communication_protocol_acp.router import (
    build_route_preview,
)


def test_build_route_preview_returns_minimal_route_fields() -> None:
    """ACP router scaffold returns route preview fields only."""
    message = ACPMessage(
        message_id="acp-msg-001",
        sender="mds",
        recipient="analysis",
        message_type="analysis_request",
    )

    route_preview = build_route_preview(message)

    assert route_preview == {
        "sender": "mds",
        "recipient": "analysis",
        "message_type": "analysis_request",
    }
