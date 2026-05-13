"""Unit tests for the Input normalizer scaffold."""

from cognitive_shield.core.input.contracts import InputMessage
from cognitive_shield.core.input.normalizer import build_input_normalization_preview


def test_build_input_normalization_preview_returns_minimal_fields() -> None:
    """Input normalizer scaffold returns normalization preview fields only."""
    message = InputMessage(
        message_id="msg-001",
        raw_text="Minimal message for Input normalizer scaffold.",
        language="en",
    )

    normalization_preview = build_input_normalization_preview(message)

    assert normalization_preview == {
        "message_id": "msg-001",
        "language": "en",
        "normalization_status": "preview_only",
    }
