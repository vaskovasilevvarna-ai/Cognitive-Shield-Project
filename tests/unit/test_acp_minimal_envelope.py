"""Unit tests for ACP minimal envelope boundary."""

from cognitive_shield.core.agent_communication_protocol_acp.cmo_boundary import (
    SOURCE_STAGE,
    TARGET_STAGE,
)
from cognitive_shield.core.agent_communication_protocol_acp.minimal_envelope import (
    build_acp_minimal_envelope,
)


def test_build_acp_minimal_envelope_creates_envelope_from_eligible_boundary() -> None:
    """ACP minimal envelope is created from an eligible boundary result."""
    decomposition_result = {
        "mds_stage": "message_decomposition_specification_mds",
        "decomposition_result_status": "decomposition_result_created",
        "minimal_assembly": {},
    }
    field_envelope = {
        "source_reference": "bounded_decomposition_result",
        "structural_status": "field_envelope_placeholder",
    }
    acp_boundary_result = {
        "acp_boundary_status": "eligible_for_acp_boundary",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "bounded_cmo_construction_status": "bounded_cmo_construction_created",
        "decomposition_result": decomposition_result,
        "field_envelope": field_envelope,
    }

    envelope = build_acp_minimal_envelope(acp_boundary_result)

    assert envelope == {
        "acp_envelope_status": "acp_minimal_envelope_created",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "acp_boundary_status": "eligible_for_acp_boundary",
        "decomposition_result": decomposition_result,
        "field_envelope": field_envelope,
    }


def test_build_acp_minimal_envelope_rejects_non_eligible_boundary() -> None:
    """ACP minimal envelope is not created from a non-eligible boundary result."""
    acp_boundary_result = {
        "acp_boundary_status": "not_eligible_for_acp_boundary",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "bounded_cmo_construction_status": "not_ready_for_bounded_cmo_construction",
        "decomposition_result": {},
        "field_envelope": {},
    }

    envelope = build_acp_minimal_envelope(acp_boundary_result)

    assert envelope == {
        "acp_envelope_status": "not_ready_for_acp_minimal_envelope",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "acp_boundary_status": "not_eligible_for_acp_boundary",
        "decomposition_result": {},
        "field_envelope": {},
    }


def test_build_acp_minimal_envelope_rejects_empty_input() -> None:
    """ACP minimal envelope rejects empty input."""
    envelope = build_acp_minimal_envelope({})

    assert envelope == {
        "acp_envelope_status": "not_ready_for_acp_minimal_envelope",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "acp_boundary_status": "",
        "decomposition_result": {},
        "field_envelope": {},
    }


def test_build_acp_minimal_envelope_preserves_decomposition_result() -> None:
    """ACP minimal envelope preserves the original DecompositionResult."""
    decomposition_result = {
        "mds_stage": "message_decomposition_specification_mds",
        "decomposition_result_status": "decomposition_result_created",
        "minimal_assembly": {
            "surface_bundle": {},
            "claim_unit_bundle": {},
        },
    }
    acp_boundary_result = {
        "acp_boundary_status": "eligible_for_acp_boundary",
        "decomposition_result": decomposition_result,
        "field_envelope": {},
    }

    envelope = build_acp_minimal_envelope(acp_boundary_result)

    assert envelope["decomposition_result"] == decomposition_result


def test_build_acp_minimal_envelope_preserves_field_envelope() -> None:
    """ACP minimal envelope preserves the existing field envelope."""
    field_envelope = {
        "source_reference": "bounded_decomposition_result",
        "structural_status": "field_envelope_placeholder",
    }
    acp_boundary_result = {
        "acp_boundary_status": "eligible_for_acp_boundary",
        "decomposition_result": {},
        "field_envelope": field_envelope,
    }

    envelope = build_acp_minimal_envelope(acp_boundary_result)

    assert envelope["field_envelope"] == field_envelope


def test_build_acp_minimal_envelope_uses_default_stages_when_missing() -> None:
    """ACP minimal envelope uses bounded default stage identifiers."""
    acp_boundary_result = {
        "acp_boundary_status": "eligible_for_acp_boundary",
        "decomposition_result": {},
        "field_envelope": {},
    }

    envelope = build_acp_minimal_envelope(acp_boundary_result)

    assert envelope["source_stage"] == SOURCE_STAGE
    assert envelope["target_stage"] == TARGET_STAGE


def test_build_acp_minimal_envelope_exposes_no_acp_bundle_message_or_downstream_fields() -> None:
    """ACP minimal envelope does not expose ACPBundle, ACPMessage, or downstream fields."""
    acp_boundary_result = {
        "acp_boundary_status": "eligible_for_acp_boundary",
        "decomposition_result": {
            "decomposition_result_status": "decomposition_result_created",
        },
        "field_envelope": {
            "source_reference": "bounded_decomposition_result",
            "structural_status": "field_envelope_placeholder",
        },
    }

    envelope = build_acp_minimal_envelope(acp_boundary_result)

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

    assert forbidden_fields.isdisjoint(envelope.keys())
    assert forbidden_fields.isdisjoint(envelope["decomposition_result"].keys())
    assert forbidden_fields.isdisjoint(envelope["field_envelope"].keys())
