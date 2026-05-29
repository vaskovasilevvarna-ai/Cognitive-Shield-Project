"""Unit tests for ACP bundle boundary."""

from cognitive_shield.core.agent_communication_protocol_acp.bundle import (
    build_acp_bundle,
)
from cognitive_shield.core.agent_communication_protocol_acp.cmo_boundary import (
    SOURCE_STAGE,
    TARGET_STAGE,
)


def test_build_acp_bundle_creates_bundle_from_ready_envelope() -> None:
    """ACPBundle is created from a ready ACP minimal envelope."""
    decomposition_result = {
        "mds_stage": "message_decomposition_specification_mds",
        "decomposition_result_status": "decomposition_result_created",
        "minimal_assembly": {},
    }
    field_envelope = {
        "source_reference": "bounded_decomposition_result",
        "structural_status": "field_envelope_placeholder",
    }
    acp_minimal_envelope = {
        "acp_envelope_status": "acp_minimal_envelope_created",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "acp_boundary_status": "eligible_for_acp_boundary",
        "decomposition_result": decomposition_result,
        "field_envelope": field_envelope,
    }

    bundle = build_acp_bundle(acp_minimal_envelope)

    assert bundle == {
        "acp_bundle_status": "acp_bundle_created",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "acp_envelope_status": "acp_minimal_envelope_created",
        "decomposition_result": decomposition_result,
        "field_envelope": field_envelope,
    }


def test_build_acp_bundle_rejects_non_ready_envelope() -> None:
    """ACPBundle is not created from a non-ready ACP minimal envelope."""
    acp_minimal_envelope = {
        "acp_envelope_status": "not_ready_for_acp_minimal_envelope",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "acp_boundary_status": "not_eligible_for_acp_boundary",
        "decomposition_result": {},
        "field_envelope": {},
    }

    bundle = build_acp_bundle(acp_minimal_envelope)

    assert bundle == {
        "acp_bundle_status": "not_ready_for_acp_bundle",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "acp_envelope_status": "not_ready_for_acp_minimal_envelope",
        "decomposition_result": {},
        "field_envelope": {},
    }


def test_build_acp_bundle_rejects_empty_input() -> None:
    """ACPBundle rejects empty input."""
    bundle = build_acp_bundle({})

    assert bundle == {
        "acp_bundle_status": "not_ready_for_acp_bundle",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "acp_envelope_status": "",
        "decomposition_result": {},
        "field_envelope": {},
    }


def test_build_acp_bundle_preserves_decomposition_result() -> None:
    """ACPBundle preserves the original DecompositionResult."""
    decomposition_result = {
        "mds_stage": "message_decomposition_specification_mds",
        "decomposition_result_status": "decomposition_result_created",
        "minimal_assembly": {
            "surface_bundle": {},
            "claim_unit_bundle": {},
        },
    }
    acp_minimal_envelope = {
        "acp_envelope_status": "acp_minimal_envelope_created",
        "decomposition_result": decomposition_result,
        "field_envelope": {},
    }

    bundle = build_acp_bundle(acp_minimal_envelope)

    assert bundle["decomposition_result"] == decomposition_result


def test_build_acp_bundle_preserves_field_envelope() -> None:
    """ACPBundle preserves the existing field envelope."""
    field_envelope = {
        "source_reference": "bounded_decomposition_result",
        "structural_status": "field_envelope_placeholder",
    }
    acp_minimal_envelope = {
        "acp_envelope_status": "acp_minimal_envelope_created",
        "decomposition_result": {},
        "field_envelope": field_envelope,
    }

    bundle = build_acp_bundle(acp_minimal_envelope)

    assert bundle["field_envelope"] == field_envelope


def test_build_acp_bundle_uses_default_stages_when_missing() -> None:
    """ACPBundle uses bounded default stage identifiers."""
    acp_minimal_envelope = {
        "acp_envelope_status": "acp_minimal_envelope_created",
        "decomposition_result": {},
        "field_envelope": {},
    }

    bundle = build_acp_bundle(acp_minimal_envelope)

    assert bundle["source_stage"] == SOURCE_STAGE
    assert bundle["target_stage"] == TARGET_STAGE


def test_build_acp_bundle_exposes_no_acp_message_routing_or_downstream_fields() -> None:
    """ACPBundle does not expose ACPMessage, routing, or downstream fields."""
    acp_minimal_envelope = {
        "acp_envelope_status": "acp_minimal_envelope_created",
        "decomposition_result": {
            "decomposition_result_status": "decomposition_result_created",
        },
        "field_envelope": {
            "source_reference": "bounded_decomposition_result",
            "structural_status": "field_envelope_placeholder",
        },
    }

    bundle = build_acp_bundle(acp_minimal_envelope)

    forbidden_fields = {
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

    assert forbidden_fields.isdisjoint(bundle.keys())
    assert forbidden_fields.isdisjoint(bundle["decomposition_result"].keys())
    assert forbidden_fields.isdisjoint(bundle["field_envelope"].keys())
