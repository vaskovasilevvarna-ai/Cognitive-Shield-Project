"""Unit tests for the ACP contract boundary scaffold."""

from cognitive_shield.core.agent_communication_protocol_acp.contracts import (
    ACPBundle,
    ACPMessage,
)


def test_acp_message_can_be_created_with_required_fields() -> None:
    """ACPMessage can be constructed with required protocol envelope fields."""
    message = ACPMessage(
        message_id="acp-msg-001",
        sender="mds",
        recipient="analysis",
        message_type="analysis_request",
    )

    assert message.message_id == "acp-msg-001"
    assert message.sender == "mds"
    assert message.recipient == "analysis"
    assert message.message_type == "analysis_request"
    assert message.payload == {}
    assert message.uncertainty_flags == []
    assert message.trace_ref == ""


def test_acp_bundle_can_be_created_with_defaults() -> None:
    """ACPBundle can be constructed as a minimal future exchange container."""
    bundle = ACPBundle(
        bundle_id="acp-bundle-001",
        source_message_id="msg-001",
    )

    assert bundle.bundle_id == "acp-bundle-001"
    assert bundle.source_message_id == "msg-001"
    assert bundle.messages == []
    assert bundle.contradiction_notes == []
    assert bundle.uncertainty_notes == []
