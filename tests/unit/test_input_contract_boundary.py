"""Unit tests for the Input contract boundary scaffold."""

from cognitive_shield.core.input.contracts import InputMessage


def test_input_contract_boundary_exports_input_message() -> None:
    """Input contract boundary exposes the shared InputMessage contract."""
    message = InputMessage(
        message_id="msg-001",
        raw_text="Minimal input boundary test message.",
        language="en",
    )

    assert message.message_id == "msg-001"
    assert message.raw_text == "Minimal input boundary test message."
    assert message.language == "en"
