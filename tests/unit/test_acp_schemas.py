"""Unit tests for the ACP schema boundary scaffold."""

from cognitive_shield.core.agent_communication_protocol_acp.schemas import (
    ACP_SCHEMA_NAME,
    ACP_SCHEMA_VERSION,
)


def test_acp_schema_identity_constants_are_defined() -> None:
    """ACP schema boundary exposes stable schema identity constants."""
    assert ACP_SCHEMA_NAME == "agent_communication_protocol_acp"
    assert ACP_SCHEMA_VERSION == "0.1"
