"""Unit tests for the MDS service scaffold."""

from cognitive_shield.core.message_decomposition_specification_mds.contracts import (
    InputMessage,
)
from cognitive_shield.core.message_decomposition_specification_mds.service import (
    can_accept_input_message,
)


def test_can_accept_input_message_returns_true_for_valid_input() -> None:
    """MDS service scaffold accepts valid InputMessage objects."""
    message = InputMessage(
        message_id="msg-001",
        raw_text="Minimal message for MDS service scaffold.",
        language="en",
    )

    assert can_accept_input_message(message) is True


def test_can_accept_input_message_returns_false_for_invalid_input() -> None:
    """MDS service scaffold rejects InputMessage objects with empty required fields."""
    message = InputMessage(
        message_id="",
        raw_text="",
        language="",
    )

    assert can_accept_input_message(message) is False
