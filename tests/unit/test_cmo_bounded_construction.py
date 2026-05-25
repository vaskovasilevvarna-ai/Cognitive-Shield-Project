"""Unit tests for bounded CMO construction candidate boundary."""

from cognitive_shield.core.canonical_message_object_cmo.bounded_construction import (
    build_bounded_cmo_construction,
)
from cognitive_shield.core.canonical_message_object_cmo.mds_boundary import (
    SOURCE_STAGE,
    TARGET_STAGE,
)


def test_build_bounded_cmo_construction_creates_candidate_from_minimal_object() -> None:
    """Bounded CMO construction candidate is created from a ready minimal object."""
    decomposition_result = {
        "mds_stage": SOURCE_STAGE,
        "decomposition_result_status": "decomposition_result_created",
        "minimal_assembly": {},
    }
    field_envelope = {
        "source_reference": "bounded_decomposition_result",
        "structural_status": "field_envelope_placeholder",
    }
    minimal_cmo_object = {
        "minimal_cmo_object_status": "minimal_cmo_object_created",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "cmo_field_envelope_status": "cmo_field_envelope_created",
        "decomposition_result": decomposition_result,
        "field_envelope": field_envelope,
    }

    construction = build_bounded_cmo_construction(minimal_cmo_object)

    assert construction == {
        "bounded_cmo_construction_status": "bounded_cmo_construction_created",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "minimal_cmo_object_status": "minimal_cmo_object_created",
        "decomposition_result": decomposition_result,
        "field_envelope": field_envelope,
    }


def test_build_bounded_cmo_construction_rejects_non_ready_minimal_object() -> None:
    """Bounded CMO construction is not created from a non-ready minimal object."""
    minimal_cmo_object = {
        "minimal_cmo_object_status": "not_ready_for_minimal_cmo_object",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "cmo_field_envelope_status": "not_ready_for_cmo_field_envelope",
        "decomposition_result": {},
        "field_envelope": {},
    }

    construction = build_bounded_cmo_construction(minimal_cmo_object)

    assert construction == {
        "bounded_cmo_construction_status": "not_ready_for_bounded_cmo_construction",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "minimal_cmo_object_status": "not_ready_for_minimal_cmo_object",
        "decomposition_result": {},
        "field_envelope": {},
    }


def test_build_bounded_cmo_construction_preserves_decomposition_result() -> None:
    """Bounded CMO construction preserves the original DecompositionResult."""
    decomposition_result = {
        "mds_stage": SOURCE_STAGE,
        "decomposition_result_status": "decomposition_result_created",
        "minimal_assembly": {
            "surface_bundle": {},
            "claim_unit_bundle": {},
        },
    }
    minimal_cmo_object = {
        "minimal_cmo_object_status": "minimal_cmo_object_created",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "decomposition_result": decomposition_result,
        "field_envelope": {},
    }

    construction = build_bounded_cmo_construction(minimal_cmo_object)

    assert construction["decomposition_result"] == decomposition_result


def test_build_bounded_cmo_construction_preserves_field_envelope() -> None:
    """Bounded CMO construction preserves the existing field envelope."""
    field_envelope = {
        "source_reference": "bounded_decomposition_result",
        "structural_status": "field_envelope_placeholder",
    }
    minimal_cmo_object = {
        "minimal_cmo_object_status": "minimal_cmo_object_created",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "decomposition_result": {},
        "field_envelope": field_envelope,
    }

    construction = build_bounded_cmo_construction(minimal_cmo_object)

    assert construction["field_envelope"] == field_envelope


def test_build_bounded_cmo_construction_uses_default_stages_when_missing() -> None:
    """Bounded CMO construction uses bounded default stage identifiers."""
    minimal_cmo_object = {
        "minimal_cmo_object_status": "minimal_cmo_object_created",
        "decomposition_result": {},
        "field_envelope": {},
    }

    construction = build_bounded_cmo_construction(minimal_cmo_object)

    assert construction["source_stage"] == SOURCE_STAGE
    assert construction["target_stage"] == TARGET_STAGE


def test_build_bounded_cmo_construction_exposes_no_full_cmo_or_downstream_fields() -> None:
    """Bounded CMO construction does not expose full CMO or downstream fields."""
    minimal_cmo_object = {
        "minimal_cmo_object_status": "minimal_cmo_object_created",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "decomposition_result": {
            "decomposition_result_status": "decomposition_result_created",
        },
        "field_envelope": {
            "source_reference": "bounded_decomposition_result",
            "structural_status": "field_envelope_placeholder",
        },
    }

    construction = build_bounded_cmo_construction(minimal_cmo_object)

    forbidden_fields = {
        "canonical_message_object",
        "CanonicalMessageObject",
        "full_cmo",
        "cmo_schema",
        "cmo_mapping",
        "mapped_fields",
        "normalized_content",
        "enriched_content",
        "acp_bundle",
        "acp_message",
        "analysis_bundle",
        "taxonomy_labels",
        "risk_profile",
        "governance_signal",
        "output_payload",
        "truth_value",
        "evidence_assessment",
    }

    assert forbidden_fields.isdisjoint(construction.keys())
    assert forbidden_fields.isdisjoint(construction["decomposition_result"].keys())
    assert forbidden_fields.isdisjoint(construction["field_envelope"].keys())
