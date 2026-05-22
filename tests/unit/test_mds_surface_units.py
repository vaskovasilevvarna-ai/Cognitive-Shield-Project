"""Unit tests for minimal MDS surface unit boundary."""

from cognitive_shield.core.message_decomposition_specification_mds.surface_units import (
    MDS_STAGE,
    SURFACE_UNIT_TYPE,
    build_minimal_surface_unit,
)


def test_build_minimal_surface_unit_creates_single_surface_unit() -> None:
    """MDS surface unit preserves source text as one surface-level unit."""
    surface_unit = build_minimal_surface_unit(
        "Minimal surface text for unit boundary."
    )

    assert surface_unit == {
        "surface_unit_id": "surface-unit-001",
        "source_text": "Minimal surface text for unit boundary.",
        "unit_type": SURFACE_UNIT_TYPE,
        "mds_stage": MDS_STAGE,
        "surface_status": "surface_unit_created",
    }


def test_build_minimal_surface_unit_blocks_empty_source_text() -> None:
    """MDS surface unit blocks empty source text."""
    surface_unit = build_minimal_surface_unit("")

    assert surface_unit == {
        "surface_unit_id": "surface-unit-001",
        "source_text": "",
        "unit_type": SURFACE_UNIT_TYPE,
        "mds_stage": MDS_STAGE,
        "surface_status": "invalid_surface_text",
    }


def test_build_minimal_surface_unit_blocks_whitespace_only_source_text() -> None:
    """MDS surface unit blocks whitespace-only source text."""
    surface_unit = build_minimal_surface_unit("   ")

    assert surface_unit == {
        "surface_unit_id": "surface-unit-001",
        "source_text": "   ",
        "unit_type": SURFACE_UNIT_TYPE,
        "mds_stage": MDS_STAGE,
        "surface_status": "invalid_surface_text",
    }


def test_build_minimal_surface_unit_exposes_no_decomposition_fields() -> None:
    """MDS surface unit does not expose claim, relation, or downstream fields."""
    surface_unit = build_minimal_surface_unit(
        "Minimal surface text for no-drift check."
    )

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

    assert forbidden_fields.isdisjoint(surface_unit.keys())
