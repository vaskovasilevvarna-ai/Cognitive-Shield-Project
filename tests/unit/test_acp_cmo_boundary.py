"""Unit tests for CMO-to-ACP boundary eligibility."""

from cognitive_shield.core.agent_communication_protocol_acp.cmo_boundary import (
    SOURCE_STAGE,
    TARGET_STAGE,
    check_cmo_to_acp_boundary_eligibility,
)


def test_check_cmo_to_acp_boundary_eligibility_accepts_bounded_construction() -> None:
    """CMO-to-ACP boundary accepts a bounded CMO construction candidate."""
    decomposition_result = {
        "mds_stage": "message_decomposition_specification_mds",
        "decomposition_result_status": "decomposition_result_created",
        "minimal_assembly": {},
    }
    field_envelope = {
        "source_reference": "bounded_decomposition_result",
        "structural_status": "field_envelope_placeholder",
    }
    bounded_cmo_construction = {
        "bounded_cmo_construction_status": "bounded_cmo_construction_created",
        "source_stage": SOURCE_STAGE,
        "target_stage": "canonical_message_object_cmo",
        "minimal_cmo_object_status": "minimal_cmo_object_created",
        "decomposition_result": decomposition_result,
        "field_envelope": field_envelope,
    }

    boundary = check_cmo_to_acp_boundary_eligibility(bounded_cmo_construction)

    assert boundary == {
        "acp_boundary_status": "eligible_for_acp_boundary",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "bounded_cmo_construction_status": "bounded_cmo_construction_created",
        "decomposition_result": decomposition_result,
        "field_envelope": field_envelope,
    }


def test_check_cmo_to_acp_boundary_eligibility_rejects_non_ready_construction() -> None:
    """CMO-to-ACP boundary rejects a non-ready CMO construction candidate."""
    bounded_cmo_construction = {
        "bounded_cmo_construction_status": "not_ready_for_bounded_cmo_construction",
        "decomposition_result": {},
        "field_envelope": {},
    }

    boundary = check_cmo_to_acp_boundary_eligibility(bounded_cmo_construction)

    assert boundary == {
        "acp_boundary_status": "not_eligible_for_acp_boundary",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "bounded_cmo_construction_status": "not_ready_for_bounded_cmo_construction",
        "decomposition_result": {},
        "field_envelope": {},
    }


def test_check_cmo_to_acp_boundary_eligibility_rejects_empty_input() -> None:
    """CMO-to-ACP boundary rejects empty input."""
    boundary = check_cmo_to_acp_boundary_eligibility({})

    assert boundary == {
        "acp_boundary_status": "not_eligible_for_acp_boundary",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "bounded_cmo_construction_status": "",
        "decomposition_result": {},
        "field_envelope": {},
    }


def test_check_cmo_to_acp_boundary_eligibility_preserves_decomposition_result() -> None:
    """CMO-to-ACP boundary preserves the original DecompositionResult."""
    decomposition_result = {
        "mds_stage": "message_decomposition_specification_mds",
        "decomposition_result_status": "decomposition_result_created",
        "minimal_assembly": {
            "surface_bundle": {},
            "claim_unit_bundle": {},
        },
    }
    bounded_cmo_construction = {
        "bounded_cmo_construction_status": "bounded_cmo_construction_created",
        "decomposition_result": decomposition_result,
        "field_envelope": {},
    }

    boundary = check_cmo_to_acp_boundary_eligibility(bounded_cmo_construction)

    assert boundary["decomposition_result"] == decomposition_result


def test_check_cmo_to_acp_boundary_eligibility_preserves_field_envelope() -> None:
    """CMO-to-ACP boundary preserves the existing field envelope."""
    field_envelope = {
        "source_reference": "bounded_decomposition_result",
        "structural_status": "field_envelope_placeholder",
    }
    bounded_cmo_construction = {
        "bounded_cmo_construction_status": "bounded_cmo_construction_created",
        "decomposition_result": {},
        "field_envelope": field_envelope,
    }

    boundary = check_cmo_to_acp_boundary_eligibility(bounded_cmo_construction)

    assert boundary["field_envelope"] == field_envelope


def test_check_cmo_to_acp_boundary_eligibility_exposes_no_acp_or_downstream_fields() -> None:
    """CMO-to-ACP boundary does not expose ACP routing or downstream fields."""
    bounded_cmo_construction = {
        "bounded_cmo_construction_status": "bounded_cmo_construction_created",
        "decomposition_result": {
            "decomposition_result_status": "decomposition_result_created",
        },
        "field_envelope": {
            "source_reference": "bounded_decomposition_result",
            "structural_status": "field_envelope_placeholder",
        },
    }

    boundary = check_cmo_to_acp_boundary_eligibility(bounded_cmo_construction)

    forbidden_fields = {
        "acp_bundle",
        "ACPBundle",
        "acp_message",
        "ACPMessage",
        "agent_route",
        "routing_decision",
        "dispatch_target",
        "analysis_bundle",
        "evidence_analysis_output",
        "narrative_analysis_output",
        "cognitive_analysis_output",
        "taxonomy_labels",
        "risk_profile",
        "governance_signal",
        "output_payload",
        "truth_value",
        "evidence_assessment",
    }

    assert forbidden_fields.isdisjoint(boundary.keys())
    assert forbidden_fields.isdisjoint(boundary["decomposition_result"].keys())
    assert forbidden_fields.isdisjoint(boundary["field_envelope"].keys())
