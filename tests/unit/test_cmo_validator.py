"""Unit tests for the CMO validator scaffold."""

from cognitive_shield.core.canonical_message_object_cmo.contracts import (
    InputMessage,
)
from cognitive_shield.core.canonical_message_object_cmo.validator import (
    is_valid_cmo_source_message,
)


def test_is_valid_cmo_source_message_accepts_minimal_source_message() -> None:
    """CMO validator scaffold accepts InputMessage objects with required fields."""
    message = InputMessage(
        message_id="msg-001",
        raw_text="Minimal message for CMO validator scaffold.",
        language="en",
    )

    assert is_valid_cmo_source_message(message) is True


def test_is_valid_cmo_source_message_rejects_empty_required_fields() -> None:
    """CMO validator scaffold rejects empty required source fields."""
    message = InputMessage(
        message_id="",
        raw_text="",
        language="",
    )

    assert is_valid_cmo_source_message(message) is False
