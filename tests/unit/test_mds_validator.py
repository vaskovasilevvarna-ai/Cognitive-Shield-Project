"""Unit tests for the MDS validator scaffold."""

from cognitive_shield.core.message_decomposition_specification_mds.contracts import (
    InputMessage,
)
from cognitive_shield.core.message_decomposition_specification_mds.validator import (
    is_valid_input_message,
)


def test_is_valid_input_message_accepts_minimal_surface_fields() -> None:
    """Validator accepts an InputMessage with required surface fields."""
    message = InputMessage(
        message_id="msg-001",
        raw_text="Minimal message for MDS validator scaffold.",
        language="en",
    )

    assert is_valid_input_message(message) is True


def test_is_valid_input_message_rejects_empty_required_surface_fields() -> None:
    """Validator rejects missing required surface fields."""
    message = InputMessage(
        message_id="",
        raw_text="",
        language="",
    )

    assert is_valid_input_message(message) is False
