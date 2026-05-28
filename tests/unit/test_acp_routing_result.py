"""Unit tests for minimal non-dispatch ACP routing result boundary."""

from cognitive_shield.core.agent_communication_protocol_acp.cmo_boundary import (
    SOURCE_STAGE,
    TARGET_STAGE,
)
from cognitive_shield.core.agent_communication_protocol_acp.routing_result import (
    build_minimal_routing_result,
)


def test_build_minimal_routing_result_accepts_ready_router_readiness() -> None:
    """Minimal routing result accepts a ready Protocol Router readiness result."""
    decomposition_result = {
        "mds_stage": "message_decomposition_specification_mds",
        "decomposition_result_status": "decomposition_result_created",
        "minimal_assembly": {},
    }
    field_envelope = {
        "source_reference": "bounded_decomposition_result",
        "structural_status": "field_envelope_placeholder",
    }
    protocol_router_readiness = {
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

    routing_result = build_minimal_routing_result(protocol_router_readiness)

    assert routing_result == {
        "routing_result_status": "route_ready_no_dispatch",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "protocol_router_readiness_status": "protocol_router_ready",
        "acp_scope_status": "acp_scope_allowed",
        "acp_schema_validation_status": "acp_schema_valid",
        "acp_message_status": "acp_message_created",
        "acp_bundle_status": "acp_bundle_created",
        "decomposition_result": decomposition_result,
        "field_envelope": field_envelope,
    }


def test_build_minimal_routing_result_rejects_not_ready_router_readiness() -> None:
    """Minimal routing result rejects a not-ready Protocol Router readiness result."""
    protocol_router_readiness = {
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

    routing_result = build_minimal_routing_result(protocol_router_readiness)

    assert routing_result == {
        "routing_result_status": "not_ready_for_routing",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "protocol_router_readiness_status": "protocol_router_not_ready",
        "acp_scope_status": "acp_scope_rejected",
        "acp_schema_validation_status": "acp_schema_invalid",
        "acp_message_status": "not_ready_for_acp_message",
        "acp_bundle_status": "not_ready_for_acp_bundle",
        "decomposition_result": {},
        "field_envelope": {},
    }


def test_build_minimal_routing_result_rejects_empty_input() -> None:
    """Minimal routing result rejects empty input."""
    routing_result = build_minimal_routing_result({})

    assert routing_result == {
        "routing_result_status": "not_ready_for_routing",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "protocol_router_readiness_status": "",
        "acp_scope_status": "",
        "acp_schema_validation_status": "",
        "acp_message_status": "",
        "acp_bundle_status": "",
        "decomposition_result": {},
        "field_envelope": {},
    }


def test_build_minimal_routing_result_preserves_decomposition_result() -> None:
    """Minimal routing result preserves the original DecompositionResult."""
    decomposition_result = {
        "mds_stage": "message_decomposition_specification_mds",
        "decomposition_result_status": "decomposition_result_created",
        "minimal_assembly": {
            "surface_bundle": {},
            "claim_unit_bundle": {},
        },
    }
    protocol_router_readiness = {
        "protocol_router_readiness_status": "protocol_router_ready",
        "acp_scope_status": "acp_scope_allowed",
        "acp_schema_validation_status": "acp_schema_valid",
        "acp_message_status": "acp_message_created",
        "acp_bundle_status": "acp_bundle_created",
        "decomposition_result": decomposition_result,
        "field_envelope": {},
    }

    routing_result = build_minimal_routing_result(protocol_router_readiness)

    assert routing_result["decomposition_result"] == decomposition_result


def test_build_minimal_routing_result_preserves_field_envelope() -> None:
    """Minimal routing result preserves the existing field envelope."""
    field_envelope = {
        "source_reference": "bounded_decomposition_result",
        "structural_status": "field_envelope_placeholder",
    }
    protocol_router_readiness = {
        "protocol_router_readiness_status": "protocol_router_ready",
        "acp_scope_status": "acp_scope_allowed",
        "acp_schema_validation_status": "acp_schema_valid",
        "acp_message_status": "acp_message_created",
        "acp_bundle_status": "acp_bundle_created",
        "decomposition_result": {},
        "field_envelope": field_envelope,
    }

    routing_result = build_minimal_routing_result(protocol_router_readiness)

    assert routing_result["field_envelope"] == field_envelope


def test_build_minimal_routing_result_uses_default_stages_when_missing() -> None:
    """Minimal routing result uses bounded default stage identifiers."""
    protocol_router_readiness = {
        "protocol_router_readiness_status": "protocol_router_ready",
        "acp_scope_status": "acp_scope_allowed",
        "acp_schema_validation_status": "acp_schema_valid",
        "acp_message_status": "acp_message_created",
        "acp_bundle_status": "acp_bundle_created",
        "decomposition_result": {},
        "field_envelope": {},
    }

    routing_result = build_minimal_routing_result(protocol_router_readiness)

    assert routing_result["source_stage"] == SOURCE_STAGE
    assert routing_result["target_stage"] == TARGET_STAGE


def test_build_minimal_routing_result_exposes_no_dispatch_agent_analysis_or_runtime_fields() -> None:
    """Minimal routing result exposes no dispatch, agent, Analysis, or runtime fields."""
    protocol_router_readiness = {
        "protocol_router_readiness_status": "protocol_router_ready",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "acp_scope_status": "acp_scope_allowed",
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

    routing_result = build_minimal_routing_result(protocol_router_readiness)

    forbidden_fields = {
        "routing_decision",
        "agent_route",
        "dispatch_target",
        "agent_id",
        "selected_agent",
        "agent_instruction",
        "route_table",
        "analysis_bundle",
        "evidence_analysis_output",
        "narrative_analysis_output",
        "cognitive_analysis_output",
        "taxonomy_labels",
        "risk_profile",
        "governance_signal",
        "output_payload",
        "runtime_pipeline",
        "runtime_event",
        "downstream_pipeline",
        "pipeline_dispatch",
    }

    assert forbidden_fields.isdisjoint(routing_result.keys())
    assert forbidden_fields.isdisjoint(routing_result["decomposition_result"].keys())
    assert forbidden_fields.isdisjoint(routing_result["field_envelope"].keys())
