"""Unit tests for the MDS to CMO preview scaffold."""

from cognitive_shield.pipeline.mds_to_cmo_preview import (
    CMO_TARGET_STAGE,
    MDS_SOURCE_STAGE,
    build_mds_to_cmo_preview,
)


def test_build_mds_to_cmo_preview_returns_expected_boundary_preview() -> None:
    """MDS to CMO preview scaffold returns preview-only handoff fields."""
    preview = build_mds_to_cmo_preview()

    assert preview == {
        "source_stage": MDS_SOURCE_STAGE,
        "target_stage": CMO_TARGET_STAGE,
        "handoff_status": "preview_only",
        "conversion_status": "not_started",
    }


def test_mds_to_cmo_preview_contains_no_conversion_or_construction_fields() -> None:
    """MDS to CMO preview scaffold does not expose conversion or CMO fields."""
    preview = build_mds_to_cmo_preview()

    forbidden_fields = {
        "surface_segments",
        "claim_units",
        "framing_units",
        "relation_objects",
        "context_carriers",
        "decomposition_uncertainty",
        "traceability_map",
        "message_metadata",
        "surface_layer",
        "claim_layer",
        "framing_layer",
        "relation_layer",
        "context_layer",
        "global_structure_layer",
        "uncertainty_layer",
        "traceability_layer",
    }

    assert forbidden_fields.isdisjoint(preview.keys())
