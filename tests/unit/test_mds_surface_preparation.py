"""Unit tests for minimal MDS surface preparation."""

from cognitive_shield.core.message_decomposition_specification_mds.contracts import (
    InputMessage,
)
from cognitive_shield.core.message_decomposition_specification_mds.surface_preparation import (
    MDS_STAGE,
    prepare_mds_surface_minimal,
)


def test_prepare_mds_surface_minimal_prepares_valid_surface_text() -> None:
    """MDS surface preparation preserves valid surface text."""
    message = InputMessage(
        message_id="msg-001",
        raw_text="Minimal surface text for MDS preparation.",
        language="en",
    )

    prepared = prepare_mds_surface_minimal(message)

    assert prepared == {
        "message_id": "msg-001",
        "source_text": "Minimal surface text for MDS preparation.",
        "mds_stage": MDS_STAGE,
        "preparation_status": "prepared",
        "surface_status": "surface_text_preserved",
    }


def test_prepare_mds_surface_minimal_blocks_empty_surface_text() -> None:
    """MDS surface preparation blocks empty surface text."""
    message = InputMessage(
        message_id="msg-001",
        raw_text="",
        language="en",
    )

    prepared = prepare_mds_surface_minimal(message)

    assert prepared == {
        "message_id": "msg-001",
        "source_text": "",
        "mds_stage": MDS_STAGE,
        "preparation_status": "blocked",
        "surface_status": "invalid_surface_text",
    }


def test_prepare_mds_surface_minimal_blocks_whitespace_only_surface_text() -> None:
    """MDS surface preparation blocks whitespace-only surface text."""
    message = InputMessage(
        message_id="msg-001",
        raw_text="   ",
        language="en",
    )

    prepared = prepare_mds_surface_minimal(message)

    assert prepared == {
        "message_id": "msg-001",
        "source_text": "   ",
        "mds_stage": MDS_STAGE,
        "preparation_status": "blocked",
        "surface_status": "invalid_surface_text",
    }


def test_prepare_mds_surface_minimal_exposes_no_decomposition_fields() -> None:
    """MDS surface preparation does not expose decomposition or downstream fields."""
    message = InputMessage(
        message_id="msg-001",
        raw_text="Minimal surface text for no-drift check.",
        language="en",
    )

    prepared = prepare_mds_surface_minimal(message)

    forbidden_fields = {
        "surface_segments",
        "claim_units",
        "framing_units",
        "relation_objects",
        "context_carriers",
        "global_narrative_structure",
        "decomposition_uncertainty",
        "traceability_map",
        "canonical_message_object",
        "acp_bundle",
        "analysis_bundle",
        "taxonomy_labels",
        "risk_profile",
    }

    assert forbidden_fields.isdisjoint(prepared.keys())
