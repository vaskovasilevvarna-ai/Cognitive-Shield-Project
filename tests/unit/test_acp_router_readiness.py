"""Unit tests for Protocol Router readiness boundary."""

from cognitive_shield.core.agent_communication_protocol_acp.cmo_boundary import (
    SOURCE_STAGE,
    TARGET_STAGE,
)
from cognitive_shield.core.agent_communication_protocol_acp.router_readiness import (
    check_protocol_router_readiness,
)


def test_check_protocol_router_readiness_accepts_allowed_scope_result() -> None:
    """Protocol Router readiness accepts an allowed ACP Scope Guard result."""
    decomposition_result = {
        "mds_stage": "message_decomposition_specification_mds",
        "decomposition_result_status": "decomposition_result_created",
        "minimal_assembly": {},
    }
    field_envelope = {
        "source_reference": "bounded_decomposition_result",
        "structural_status": "field_envelope_placeholder",
    }
    acp_scope_guard_result = {
        "acp_scope_status": "acp_scope_allowed",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "acp_schema_validation_status": "acp_schema_valid",
        "acp_message_status": "acp_message_created",
        "acp_bundle_status": "acp_bundle_created",
        "decomposition_result": decomposition_result,
        "field_envelope": field_envelope,
    }

    readiness = check_protocol_router_readiness(acp_scope_guard_result)

    assert readiness == {
        "protocol_router_readiness_status": "protocol_router_ready",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "acp_scope_status": "acp_scope_allowed",
        "acp_schema_validation_status": "acp_schema_valid",
        "acp_message_status": "acp_message_created",
        "acp_bundle_status": "acp_bundle_created",
        "decomposition_result": decomposition_result,
        "field_envelope": field_envelope,
    }


def test_check_protocol_router_readiness_rejects_rejected_scope_result() -> None:
    """Protocol Router readiness rejects a rejected ACP Scope Guard result."""
    acp_scope_guard_result = {
        "acp_scope_status": "acp_scope_rejected",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "acp_schema_validation_status": "acp_schema_invalid",
        "acp_message_status": "not_ready_for_acp_message",
        "acp_bundle_status": "not_ready_for_acp_bundle",
        "decomposition_result": {},
        "field_envelope": {},
    }

    readiness = check_protocol_router_readiness(acp_scope_guard_result)

    assert readiness == {
        "protocol_router_readiness_status": "protocol_router_not_ready",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "acp_scope_status": "acp_scope_rejected",
        "acp_schema_validation_status": "acp_schema_invalid",
        "acp_message_status": "not_ready_for_acp_message",
        "acp_bundle_status": "not_ready_for_acp_bundle",
        "decomposition_result": {},
        "field_envelope": {},
    }


def test_check_protocol_router_readiness_rejects_empty_input() -> None:
    """Protocol Router readiness rejects empty input."""
    readiness = check_protocol_router_readiness({})

    assert readiness == {
        "protocol_router_readiness_status": "protocol_router_not_ready",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "acp_scope_status": "",
        "acp_schema_validation_status": "",
        "acp_message_status": "",
        "acp_bundle_status": "",
        "decomposition_result": {},
        "field_envelope": {},
    }


def test_check_protocol_router_readiness_preserves_decomposition_result() -> None:
    """Protocol Router readiness preserves the original DecompositionResult."""
    decomposition_result = {
        "mds_stage": "message_decomposition_specification_mds",
        "decomposition_result_status": "decomposition_result_created",
        "minimal_assembly": {
            "surface_bundle": {},
            "claim_unit_bundle": {},
        },
    }
    acp_scope_guard_result = {
        "acp_scope_status": "acp_scope_allowed",
        "acp_schema_validation_status": "acp_schema_valid",
        "acp_message_status": "acp_message_created",
        "acp_bundle_status": "acp_bundle_created",
        "decomposition_result": decomposition_result,
        "field_envelope": {},
    }

    readiness = check_protocol_router_readiness(acp_scope_guard_result)

    assert readiness["decomposition_result"] == decomposition_result


def test_check_protocol_router_readiness_preserves_field_envelope() -> None:
    """Protocol Router readiness preserves the existing field envelope."""
    field_envelope = {
        "source_reference": "bounded_decomposition_result",
        "structural_status": "field_envelope_placeholder",
    }
    acp_scope_guard_result = {
        "acp_scope_status": "acp_scope_allowed",
        "acp_schema_validation_status": "acp_schema_valid",
        "acp_message_status": "acp_message_created",
        "acp_bundle_status": "acp_bundle_created",
        "decomposition_result": {},
        "field_envelope": field_envelope,
    }

    readiness = check_protocol_router_readiness(acp_scope_guard_result)

    assert readiness["field_envelope"] == field_envelope


def test_check_protocol_router_readiness_uses_default_stages_when_missing() -> None:
    """Protocol Router readiness uses bounded default stage identifiers."""
    acp_scope_guard_result = {
        "acp_scope_status": "acp_scope_allowed",
        "acp_schema_validation_status": "acp_schema_valid",
        "acp_message_status": "acp_message_created",
        "acp_bundle_status": "acp_bundle_created",
        "decomposition_result": {},
        "field_envelope": {},
    }

    readiness = check_protocol_router_readiness(acp_scope_guard_result)

    assert readiness["source_stage"] == SOURCE_STAGE
    assert readiness["target_stage"] == TARGET_STAGE


def test_check_protocol_router_readiness_exposes_no_routing_dispatch_or_downstream_fields() -> None:
    """Protocol Router readiness exposes no routing, dispatch, or downstream fields."""
    acp_scope_guard_result = {
        "acp_scope_status": "acp_scope_allowed",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "acp_schema_validation_status": "acp_schema_valid",
        "acp_message_status": "acp_message_created",
        "acp_bundle_status": "acp_bundle_created",
        "decomposition_result": {
            "decomposition_result_status": "decomposition_result_created",
        },
        "field_envelope": {
            "source_reference": "bounded_decomposition_result",
            "structural_status": "field_envelope_placeholder",
        },
    }

    readiness = check_protocol_router_readiness(acp_scope_guard_result)

    forbidden_fields = {
        "agent_route",
        "routing_decision",
        "dispatch_target",
        "agent_id",
        "agent_instruction",
        "selected_agent",
        "route_table",
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

    assert forbidden_fields.isdisjoint(readiness.keys())
    assert forbidden_fields.isdisjoint(readiness["decomposition_result"].keys())
    assert forbidden_fields.isdisjoint(readiness["field_envelope"].keys())
