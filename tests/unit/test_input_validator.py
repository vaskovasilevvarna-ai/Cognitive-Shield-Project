"""Unit tests for the Input validator scaffold."""

from cognitive_shield.core.input.contracts import InputMessage
from cognitive_shield.core.input.validator import is_valid_input_source


def test_is_valid_input_source_accepts_minimal_input_message() -> None:
    """Input validator scaffold accepts InputMessage objects with required fields."""
    message = InputMessage(
        message_id="msg-001",
        raw_text="Minimal message for Input validator scaffold.",
        language="en",
    )

    assert is_valid_input_source(message) is True


def test_is_valid_input_source_rejects_empty_required_fields() -> None:
    """Input validator scaffold rejects empty required source fields."""
    message = InputMessage(
        message_id="",
        raw_text="",
        language="",
    )

    assert is_valid_input_source(message) is False
