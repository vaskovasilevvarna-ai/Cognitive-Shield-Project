"""Unit tests for the Input normalizer scaffold and minimal behavior."""

from cognitive_shield.core.input.contracts import InputMessage
from cognitive_shield.core.input.normalizer import (
    build_input_normalization_preview,
    prepare_input_message_minimal,
)


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


def test_prepare_input_message_minimal_trims_raw_text_only() -> None:
    """Minimal Input behavior trims raw_text while preserving core fields."""
    message = InputMessage(
        message_id="msg-001",
        raw_text="  Minimal message with surrounding whitespace.  ",
        language="en",
    )

    prepared = prepare_input_message_minimal(message)

    assert prepared.message_id == "msg-001"
    assert prepared.raw_text == "Minimal message with surrounding whitespace."
    assert prepared.language == "en"


def test_prepare_input_message_minimal_does_not_add_decomposition_fields() -> None:
    """Minimal Input behavior does not expose MDS or downstream fields."""
    message = InputMessage(
        message_id="msg-001",
        raw_text="  Minimal message for no-drift check.  ",
        language="en",
    )

    prepared = prepare_input_message_minimal(message)

    forbidden_fields = {
        "surface_segments",
        "claim_units",
        "framing_units",
        "relation_objects",
        "context_carriers",
        "decomposition_uncertainty",
        "traceability_map",
        "canonical_message_object",
        "acp_bundle",
        "analysis_bundle",
        "taxonomy_labels",
        "risk_profile",
    }

    assert forbidden_fields.isdisjoint(prepared.__dict__.keys())
