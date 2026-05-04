"""Unit tests for shared input contracts."""

from cognitive_shield.shared.contracts.input_contracts import InputMessage


def test_input_message_can_be_created_with_minimal_fields() -> None:
    """InputMessage can be constructed with the required minimal fields."""
    message = InputMessage(
        message_id="msg-001",
        raw_text="This is a minimal test message.",
        language="en",
    )

    assert message.message_id == "msg-001"
    assert message.raw_text == "This is a minimal test message."
    assert message.language == "en"
    assert message.source_type is None
    assert message.timestamp is None
    assert message.metadata == {}
