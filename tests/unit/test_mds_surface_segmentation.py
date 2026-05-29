"""Unit tests for explicit MDS surface segmentation."""

from cognitive_shield.core.message_decomposition_specification_mds.surface_preparation import (
    MDS_STAGE,
)
from cognitive_shield.core.message_decomposition_specification_mds.surface_segmentation import (
    SURFACE_UNIT_TYPE,
    segment_surface_text_explicit,
)


def test_segment_surface_text_explicit_creates_one_surface_unit_for_single_line() -> None:
    """Explicit surface segmentation creates one unit for single-line text."""
    segmentation = segment_surface_text_explicit(
        "Minimal surface text for segmentation."
    )

    assert segmentation == {
        "mds_stage": MDS_STAGE,
        "segmentation_status": "surface_segments_created",
        "surface_units": [
            {
                "surface_unit_id": "surface-unit-001",
                "source_text": "Minimal surface text for segmentation.",
                "unit_type": SURFACE_UNIT_TYPE,
                "mds_stage": MDS_STAGE,
                "surface_status": "surface_unit_created",
                "order_index": "1",
            }
        ],
    }


def test_segment_surface_text_explicit_creates_units_from_visible_line_boundaries() -> None:
    """Explicit surface segmentation preserves line order and text."""
    segmentation = segment_surface_text_explicit(
        "First visible surface line.\nSecond visible surface line."
    )

    assert segmentation == {
        "mds_stage": MDS_STAGE,
        "segmentation_status": "surface_segments_created",
        "surface_units": [
            {
                "surface_unit_id": "surface-unit-001",
                "source_text": "First visible surface line.",
                "unit_type": SURFACE_UNIT_TYPE,
                "mds_stage": MDS_STAGE,
                "surface_status": "surface_unit_created",
                "order_index": "1",
            },
            {
                "surface_unit_id": "surface-unit-002",
                "source_text": "Second visible surface line.",
                "unit_type": SURFACE_UNIT_TYPE,
                "mds_stage": MDS_STAGE,
                "surface_status": "surface_unit_created",
                "order_index": "2",
            },
        ],
    }


def test_segment_surface_text_explicit_ignores_blank_lines() -> None:
    """Explicit surface segmentation ignores blank lines without inference."""
    segmentation = segment_surface_text_explicit(
        "First visible surface line.\n\n   \nSecond visible surface line."
    )

    assert len(segmentation["surface_units"]) == 2
    assert segmentation["surface_units"][0]["source_text"] == "First visible surface line."
    assert segmentation["surface_units"][1]["source_text"] == "Second visible surface line."


def test_segment_surface_text_explicit_blocks_empty_source_text() -> None:
    """Explicit surface segmentation blocks empty source text."""
    segmentation = segment_surface_text_explicit("")

    assert segmentation == {
        "mds_stage": MDS_STAGE,
        "segmentation_status": "blocked_invalid_surface_text",
        "surface_units": [],
    }


def test_segment_surface_text_explicit_blocks_whitespace_only_source_text() -> None:
    """Explicit surface segmentation blocks whitespace-only source text."""
    segmentation = segment_surface_text_explicit("   ")

    assert segmentation == {
        "mds_stage": MDS_STAGE,
        "segmentation_status": "blocked_invalid_surface_text",
        "surface_units": [],
    }


def test_segment_surface_text_explicit_exposes_no_decomposition_fields() -> None:
    """Explicit surface segmentation does not expose analytical fields."""
    segmentation = segment_surface_text_explicit(
        "First visible surface line.\nSecond visible surface line."
    )

    forbidden_fields = {
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

    assert forbidden_fields.isdisjoint(segmentation.keys())

    for surface_unit in segmentation["surface_units"]:
        assert forbidden_fields.isdisjoint(surface_unit.keys())
