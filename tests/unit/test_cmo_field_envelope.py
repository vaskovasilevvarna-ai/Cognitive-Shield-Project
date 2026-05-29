"""Unit tests for CMO field envelope boundary."""

from cognitive_shield.core.canonical_message_object_cmo.field_envelope import (
    build_cmo_field_envelope,
)
from cognitive_shield.core.canonical_message_object_cmo.mds_boundary import (
    SOURCE_STAGE,
    TARGET_STAGE,
)


def test_build_cmo_field_envelope_creates_envelope_from_ready_contract() -> None:
    """CMO field envelope is created only from a ready structural contract."""
    decomposition_result = {
        "mds_stage": SOURCE_STAGE,
        "decomposition_result_status": "decomposition_result_created",
        "minimal_assembly": {},
    }
    cmo_structural_contract = {
        "cmo_contract_status": "cmo_structural_contract_ready",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "cmo_shell_status": "cmo_shell_created",
        "decomposition_result": decomposition_result,
    }

    envelope = build_cmo_field_envelope(cmo_structural_contract)

    assert envelope == {
        "cmo_field_envelope_status": "cmo_field_envelope_created",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "cmo_contract_status": "cmo_structural_contract_ready",
        "decomposition_result": decomposition_result,
        "field_envelope": {
            "source_reference": "bounded_decomposition_result",
            "structural_status": "field_envelope_placeholder",
        },
    }


def test_build_cmo_field_envelope_rejects_non_ready_contract() -> None:
    """CMO field envelope is not created from a non-ready structural contract."""
    cmo_structural_contract = {
        "cmo_contract_status": "not_ready_for_cmo_structural_contract",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "cmo_shell_status": "not_eligible_for_cmo_shell",
        "decomposition_result": {},
    }

    envelope = build_cmo_field_envelope(cmo_structural_contract)

    assert envelope == {
        "cmo_field_envelope_status": "not_ready_for_cmo_field_envelope",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "cmo_contract_status": "not_ready_for_cmo_structural_contract",
        "decomposition_result": {},
        "field_envelope": {},
    }


def test_build_cmo_field_envelope_preserves_decomposition_result() -> None:
    """CMO field envelope preserves the original DecompositionResult."""
    decomposition_result = {
        "mds_stage": SOURCE_STAGE,
        "decomposition_result_status": "decomposition_result_created",
        "minimal_assembly": {
            "surface_bundle": {},
            "claim_unit_bundle": {},
        },
    }
    cmo_structural_contract = {
        "cmo_contract_status": "cmo_structural_contract_ready",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "decomposition_result": decomposition_result,
    }

    envelope = build_cmo_field_envelope(cmo_structural_contract)

    assert envelope["decomposition_result"] == decomposition_result


def test_build_cmo_field_envelope_uses_default_stages_when_missing() -> None:
    """CMO field envelope uses bounded default stage identifiers."""
    cmo_structural_contract = {
        "cmo_contract_status": "cmo_structural_contract_ready",
        "decomposition_result": {},
    }

    envelope = build_cmo_field_envelope(cmo_structural_contract)

    assert envelope["source_stage"] == SOURCE_STAGE
    assert envelope["target_stage"] == TARGET_STAGE


def test_build_cmo_field_envelope_exposes_no_full_cmo_or_downstream_fields() -> None:
    """CMO field envelope does not expose full CMO or downstream fields."""
    cmo_structural_contract = {
        "cmo_contract_status": "cmo_structural_contract_ready",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "decomposition_result": {
            "decomposition_result_status": "decomposition_result_created",
        },
    }

    envelope = build_cmo_field_envelope(cmo_structural_contract)

    forbidden_fields = {
        "canonical_message_object",
        "CanonicalMessageObject",
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

    assert forbidden_fields.isdisjoint(envelope.keys())
    assert forbidden_fields.isdisjoint(envelope["decomposition_result"].keys())
    assert forbidden_fields.isdisjoint(envelope["field_envelope"].keys())
