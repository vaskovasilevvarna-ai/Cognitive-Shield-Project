"""Unit tests for the CMO builder scaffold."""

from cognitive_shield.core.canonical_message_object_cmo.builder import (
    can_build_from_input_message,
)
from cognitive_shield.core.canonical_message_object_cmo.contracts import (
    InputMessage,
)


def test_can_build_from_input_message_returns_true_for_valid_input() -> None:
    """CMO builder scaffold accepts valid InputMessage objects."""
    message = InputMessage(
        message_id="msg-001",
        raw_text="Minimal message for CMO builder scaffold.",
        language="en",
    )

    assert can_build_from_input_message(message) is True


def test_can_build_from_input_message_returns_false_for_invalid_input() -> None:
    """CMO builder scaffold rejects InputMessage objects with empty required fields."""
    message = InputMessage(
        message_id="",
        raw_text="",
        language="",
    )

    assert can_build_from_input_message(message) is False
