"""Unit tests for ACP message boundary."""

from cognitive_shield.core.agent_communication_protocol_acp.cmo_boundary import (
    SOURCE_STAGE,
    TARGET_STAGE,
)
from cognitive_shield.core.agent_communication_protocol_acp.message import (
    build_acp_message,
)


def test_build_acp_message_creates_message_from_ready_bundle() -> None:
    """ACPMessage is created from a ready ACPBundle."""
    decomposition_result = {
        "mds_stage": "message_decomposition_specification_mds",
        "decomposition_result_status": "decomposition_result_created",
        "minimal_assembly": {},
    }
    field_envelope = {
        "source_reference": "bounded_decomposition_result",
        "structural_status": "field_envelope_placeholder",
    }
    acp_bundle = {
        "acp_bundle_status": "acp_bundle_created",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "acp_envelope_status": "acp_minimal_envelope_created",
        "decomposition_result": decomposition_result,
        "field_envelope": field_envelope,
    }

    message = build_acp_message(acp_bundle)

    assert message == {
        "acp_message_status": "acp_message_created",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "acp_bundle_status": "acp_bundle_created",
        "decomposition_result": decomposition_result,
        "field_envelope": field_envelope,
    }


def test_build_acp_message_rejects_non_ready_bundle() -> None:
    """ACPMessage is not created from a non-ready ACPBundle."""
    acp_bundle = {
        "acp_bundle_status": "not_ready_for_acp_bundle",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "acp_envelope_status": "not_ready_for_acp_minimal_envelope",
        "decomposition_result": {},
        "field_envelope": {},
    }

    message = build_acp_message(acp_bundle)

    assert message == {
        "acp_message_status": "not_ready_for_acp_message",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "acp_bundle_status": "not_ready_for_acp_bundle",
        "decomposition_result": {},
        "field_envelope": {},
    }


def test_build_acp_message_rejects_empty_input() -> None:
    """ACPMessage rejects empty input."""
    message = build_acp_message({})

    assert message == {
        "acp_message_status": "not_ready_for_acp_message",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "acp_bundle_status": "",
        "decomposition_result": {},
        "field_envelope": {},
    }


def test_build_acp_message_preserves_decomposition_result() -> None:
    """ACPMessage preserves the original DecompositionResult."""
    decomposition_result = {
        "mds_stage": "message_decomposition_specification_mds",
        "decomposition_result_status": "decomposition_result_created",
        "minimal_assembly": {
            "surface_bundle": {},
            "claim_unit_bundle": {},
        },
    }
    acp_bundle = {
        "acp_bundle_status": "acp_bundle_created",
        "decomposition_result": decomposition_result,
        "field_envelope": {},
    }

    message = build_acp_message(acp_bundle)

    assert message["decomposition_result"] == decomposition_result


def test_build_acp_message_preserves_field_envelope() -> None:
    """ACPMessage preserves the existing field envelope."""
    field_envelope = {
        "source_reference": "bounded_decomposition_result",
        "structural_status": "field_envelope_placeholder",
    }
    acp_bundle = {
        "acp_bundle_status": "acp_bundle_created",
        "decomposition_result": {},
        "field_envelope": field_envelope,
    }

    message = build_acp_message(acp_bundle)

    assert message["field_envelope"] == field_envelope


def test_build_acp_message_uses_default_stages_when_missing() -> None:
    """ACPMessage uses bounded default stage identifiers."""
    acp_bundle = {
        "acp_bundle_status": "acp_bundle_created",
        "decomposition_result": {},
        "field_envelope": {},
    }

    message = build_acp_message(acp_bundle)

    assert message["source_stage"] == SOURCE_STAGE
    assert message["target_stage"] == TARGET_STAGE


def test_build_acp_message_exposes_no_routing_dispatch_or_downstream_fields() -> None:
    """ACPMessage does not expose routing, dispatch, or downstream fields."""
    acp_bundle = {
        "acp_bundle_status": "acp_bundle_created",
        "decomposition_result": {
            "decomposition_result_status": "decomposition_result_created",
        },
        "field_envelope": {
            "source_reference": "bounded_decomposition_result",
            "structural_status": "field_envelope_placeholder",
        },
    }

    message = build_acp_message(acp_bundle)

    forbidden_fields = {
        "agent_route",
        "routing_decision",
        "dispatch_target",
        "agent_id",
        "agent_instruction",
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

    assert forbidden_fields.isdisjoint(message.keys())
    assert forbidden_fields.isdisjoint(message["decomposition_result"].keys())
    assert forbidden_fields.isdisjoint(message["field_envelope"].keys())
