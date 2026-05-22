"""Unit tests for minimal MDS surface bundle boundary."""

from cognitive_shield.core.message_decomposition_specification_mds.contracts import (
    InputMessage,
)
from cognitive_shield.core.message_decomposition_specification_mds.surface_bundle import (
    build_mds_surface_bundle,
)
from cognitive_shield.core.message_decomposition_specification_mds.surface_preparation import (
    MDS_STAGE,
)


def test_build_mds_surface_bundle_creates_minimal_bundle_for_valid_text() -> None:
    """MDS surface bundle combines preparation and one surface unit."""
    message = InputMessage(
        message_id="msg-001",
        raw_text="Minimal surface text for bundle boundary.",
        language="en",
    )

    bundle = build_mds_surface_bundle(message)

    assert bundle["mds_stage"] == MDS_STAGE
    assert bundle["bundle_status"] == "surface_bundle_created"
    assert bundle["surface_preparation"] == {
        "message_id": "msg-001",
        "source_text": "Minimal surface text for bundle boundary.",
        "mds_stage": MDS_STAGE,
        "preparation_status": "prepared",
        "surface_status": "surface_text_preserved",
    }
    assert bundle["surface_unit"] == {
        "surface_unit_id": "surface-unit-001",
        "source_text": "Minimal surface text for bundle boundary.",
        "unit_type": "surface_text",
        "mds_stage": MDS_STAGE,
        "surface_status": "surface_unit_created",
    }


def test_build_mds_surface_bundle_blocks_empty_text() -> None:
    """MDS surface bundle blocks empty source text."""
    message = InputMessage(
        message_id="msg-001",
        raw_text="",
        language="en",
    )

    bundle = build_mds_surface_bundle(message)

    assert bundle == {
        "mds_stage": MDS_STAGE,
        "bundle_status": "blocked_invalid_surface_text",
        "surface_preparation": {
            "message_id": "msg-001",
            "source_text": "",
            "mds_stage": MDS_STAGE,
            "preparation_status": "blocked",
            "surface_status": "invalid_surface_text",
        },
        "surface_unit": {},
    }


def test_build_mds_surface_bundle_blocks_whitespace_only_text() -> None:
    """MDS surface bundle blocks whitespace-only source text."""
    message = InputMessage(
        message_id="msg-001",
        raw_text="   ",
        language="en",
    )

    bundle = build_mds_surface_bundle(message)

    assert bundle == {
        "mds_stage": MDS_STAGE,
        "bundle_status": "blocked_invalid_surface_text",
        "surface_preparation": {
            "message_id": "msg-001",
            "source_text": "   ",
            "mds_stage": MDS_STAGE,
            "preparation_status": "blocked",
            "surface_status": "invalid_surface_text",
        },
        "surface_unit": {},
    }


def test_build_mds_surface_bundle_exposes_no_decomposition_fields() -> None:
    """MDS surface bundle does not expose claim, relation, or downstream fields."""
    message = InputMessage(
        message_id="msg-001",
        raw_text="Minimal surface text for no-drift check.",
        language="en",
    )

    bundle = build_mds_surface_bundle(message)

    forbidden_fields = {
        "surface_segments",
        "claim_units",
        "framing_units",
        "relation_objects",
        "context_carriers",
        "global_narrative_structure",
        "decomposition_uncertainty",
        "traceability_map",
        "decomposition_result",
        "canonical_message_object",
        "acp_bundle",
        "analysis_bundle",
        "taxonomy_labels",
        "risk_profile",
    }

    assert forbidden_fields.isdisjoint(bundle.keys())
    assert forbidden_fields.isdisjoint(bundle["surface_preparation"].keys())
    assert forbidden_fields.isdisjoint(bundle["surface_unit"].keys())
