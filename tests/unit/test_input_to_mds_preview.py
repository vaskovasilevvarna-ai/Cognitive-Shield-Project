"""Unit tests for the Input to MDS preview scaffold."""

from cognitive_shield.core.input.contracts import InputMessage
from cognitive_shield.pipeline.input_to_mds_preview import (
    MDS_TARGET_STAGE,
    build_input_to_mds_preview,
)


def test_build_input_to_mds_preview_returns_valid_handoff_preview() -> None:
    """Input to MDS preview scaffold returns preview-only handoff for valid input."""
    message = InputMessage(
        message_id="msg-001",
        raw_text="Minimal message for Input to MDS preview.",
        language="en",
    )

    preview = build_input_to_mds_preview(message)

    assert preview == {
        "message_id": "msg-001",
        "language": "en",
        "source_status": "valid_input_source",
        "target_stage": MDS_TARGET_STAGE,
        "handoff_status": "preview_only",
    }


def test_build_input_to_mds_preview_blocks_invalid_input_source() -> None:
    """Input to MDS preview scaffold blocks invalid input at preview level."""
    message = InputMessage(
        message_id="",
        raw_text="",
        language="",
    )

    preview = build_input_to_mds_preview(message)

    assert preview == {
        "message_id": "",
        "language": "",
        "source_status": "invalid_input_source",
        "target_stage": MDS_TARGET_STAGE,
        "handoff_status": "blocked_preview",
    }


def test_input_to_mds_preview_contains_no_decomposition_fields() -> None:
    """Input to MDS preview scaffold does not expose decomposition fields."""
    message = InputMessage(
        message_id="msg-001",
        raw_text="Minimal message for no-decomposition-field check.",
        language="en",
    )

    preview = build_input_to_mds_preview(message)

    forbidden_fields = {
        "surface_segments",
        "claim_units",
        "framing_units",
        "relation_objects",
        "context_carriers",
        "decomposition_uncertainty",
        "traceability_map",
    }

    assert forbidden_fields.isdisjoint(preview.keys())
