"""Unit tests for minimal CMO object boundary."""

from cognitive_shield.core.canonical_message_object_cmo.mds_boundary import (
    SOURCE_STAGE,
    TARGET_STAGE,
)
from cognitive_shield.core.canonical_message_object_cmo.minimal_object import (
    build_minimal_cmo_object,
)


def test_build_minimal_cmo_object_creates_object_from_ready_envelope() -> None:
    """Minimal CMO object is created only from a ready field envelope."""
    decomposition_result = {
        "mds_stage": SOURCE_STAGE,
        "decomposition_result_status": "decomposition_result_created",
        "minimal_assembly": {},
    }
    field_envelope = {
        "source_reference": "bounded_decomposition_result",
        "structural_status": "field_envelope_placeholder",
    }
    cmo_field_envelope = {
        "cmo_field_envelope_status": "cmo_field_envelope_created",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "cmo_contract_status": "cmo_structural_contract_ready",
        "decomposition_result": decomposition_result,
        "field_envelope": field_envelope,
    }

    minimal_object = build_minimal_cmo_object(cmo_field_envelope)

    assert minimal_object == {
        "minimal_cmo_object_status": "minimal_cmo_object_created",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "cmo_field_envelope_status": "cmo_field_envelope_created",
        "decomposition_result": decomposition_result,
        "field_envelope": field_envelope,
    }


def test_build_minimal_cmo_object_rejects_non_ready_envelope() -> None:
    """Minimal CMO object is not created from a non-ready field envelope."""
    cmo_field_envelope = {
        "cmo_field_envelope_status": "not_ready_for_cmo_field_envelope",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "cmo_contract_status": "not_ready_for_cmo_structural_contract",
        "decomposition_result": {},
        "field_envelope": {},
    }

    minimal_object = build_minimal_cmo_object(cmo_field_envelope)

    assert minimal_object == {
        "minimal_cmo_object_status": "not_ready_for_minimal_cmo_object",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "cmo_field_envelope_status": "not_ready_for_cmo_field_envelope",
        "decomposition_result": {},
        "field_envelope": {},
    }


def test_build_minimal_cmo_object_preserves_decomposition_result() -> None:
    """Minimal CMO object preserves the original DecompositionResult."""
    decomposition_result = {
        "mds_stage": SOURCE_STAGE,
        "decomposition_result_status": "decomposition_result_created",
        "minimal_assembly": {
            "surface_bundle": {},
            "claim_unit_bundle": {},
        },
    }
    cmo_field_envelope = {
        "cmo_field_envelope_status": "cmo_field_envelope_created",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "decomposition_result": decomposition_result,
        "field_envelope": {
            "source_reference": "bounded_decomposition_result",
            "structural_status": "field_envelope_placeholder",
        },
    }

    minimal_object = build_minimal_cmo_object(cmo_field_envelope)

    assert minimal_object["decomposition_result"] == decomposition_result


def test_build_minimal_cmo_object_preserves_field_envelope() -> None:
    """Minimal CMO object preserves the existing field envelope."""
    field_envelope = {
        "source_reference": "bounded_decomposition_result",
        "structural_status": "field_envelope_placeholder",
    }
    cmo_field_envelope = {
        "cmo_field_envelope_status": "cmo_field_envelope_created",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "decomposition_result": {},
        "field_envelope": field_envelope,
    }

    minimal_object = build_minimal_cmo_object(cmo_field_envelope)

    assert minimal_object["field_envelope"] == field_envelope


def test_build_minimal_cmo_object_uses_default_stages_when_missing() -> None:
    """Minimal CMO object uses bounded default stage identifiers."""
    cmo_field_envelope = {
        "cmo_field_envelope_status": "cmo_field_envelope_created",
        "decomposition_result": {},
        "field_envelope": {},
    }

    minimal_object = build_minimal_cmo_object(cmo_field_envelope)

    assert minimal_object["source_stage"] == SOURCE_STAGE
    assert minimal_object["target_stage"] == TARGET_STAGE


def test_build_minimal_cmo_object_exposes_no_full_cmo_or_downstream_fields() -> None:
    """Minimal CMO object does not expose full CMO or downstream fields."""
    cmo_field_envelope = {
        "cmo_field_envelope_status": "cmo_field_envelope_created",
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

    minimal_object = build_minimal_cmo_object(cmo_field_envelope)

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

    assert forbidden_fields.isdisjoint(minimal_object.keys())
    assert forbidden_fields.isdisjoint(minimal_object["decomposition_result"].keys())
    assert forbidden_fields.isdisjoint(minimal_object["field_envelope"].keys())
