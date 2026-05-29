"""Unit tests for the ACP schema validator scaffold."""

from cognitive_shield.core.agent_communication_protocol_acp.contracts import (
    ACPMessage,
)
from cognitive_shield.core.agent_communication_protocol_acp.schema_validator import (
    build_schema_validation_preview,
)


def test_build_schema_validation_preview_returns_minimal_validation_fields() -> None:
    """ACP schema validator scaffold returns validation preview fields only."""
    message = ACPMessage(
        message_id="acp-msg-001",
        sender="mds",
        recipient="analysis",
        message_type="analysis_request",
    )

    validation_preview = build_schema_validation_preview(message)

    assert validation_preview == {
        "message_id": "acp-msg-001",
        "message_type": "analysis_request",
        "validation_status": "preview_only",
    }
