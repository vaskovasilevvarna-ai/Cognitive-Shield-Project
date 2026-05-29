"""Unit tests for minimal ACP Scope Guard boundary."""

from cognitive_shield.core.agent_communication_protocol_acp.cmo_boundary import (
    SOURCE_STAGE,
    TARGET_STAGE,
)
from cognitive_shield.core.agent_communication_protocol_acp.scope_guard_minimal import (
    check_acp_scope_guard,
)


def test_check_acp_scope_guard_allows_valid_schema_result() -> None:
    """Minimal ACP Scope Guard allows a valid schema validation result."""
    decomposition_result = {
        "mds_stage": "message_decomposition_specification_mds",
        "decomposition_result_status": "decomposition_result_created",
        "minimal_assembly": {},
    }
    field_envelope = {
        "source_reference": "bounded_decomposition_result",
        "structural_status": "field_envelope_placeholder",
    }
    acp_schema_validation = {
        "acp_schema_validation_status": "acp_schema_valid",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "acp_message_status": "acp_message_created",
        "acp_bundle_status": "acp_bundle_created",
        "decomposition_result": decomposition_result,
        "field_envelope": field_envelope,
    }

    scope = check_acp_scope_guard(acp_schema_validation)

    assert scope == {
        "acp_scope_status": "acp_scope_allowed",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "acp_schema_validation_status": "acp_schema_valid",
        "acp_message_status": "acp_message_created",
        "acp_bundle_status": "acp_bundle_created",
        "decomposition_result": decomposition_result,
        "field_envelope": field_envelope,
    }


def test_check_acp_scope_guard_rejects_invalid_schema_result() -> None:
    """Minimal ACP Scope Guard rejects an invalid schema validation result."""
    acp_schema_validation = {
        "acp_schema_validation_status": "acp_schema_invalid",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "acp_message_status": "not_ready_for_acp_message",
        "acp_bundle_status": "not_ready_for_acp_bundle",
        "decomposition_result": {},
        "field_envelope": {},
    }

    scope = check_acp_scope_guard(acp_schema_validation)

    assert scope == {
        "acp_scope_status": "acp_scope_rejected",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "acp_schema_validation_status": "acp_schema_invalid",
        "acp_message_status": "not_ready_for_acp_message",
        "acp_bundle_status": "not_ready_for_acp_bundle",
        "decomposition_result": {},
        "field_envelope": {},
    }


def test_check_acp_scope_guard_rejects_empty_input() -> None:
    """Minimal ACP Scope Guard rejects empty input."""
    scope = check_acp_scope_guard({})

    assert scope == {
        "acp_scope_status": "acp_scope_rejected",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "acp_schema_validation_status": "",
        "acp_message_status": "",
        "acp_bundle_status": "",
        "decomposition_result": {},
        "field_envelope": {},
    }


def test_check_acp_scope_guard_preserves_decomposition_result() -> None:
    """Minimal ACP Scope Guard preserves the original DecompositionResult."""
    decomposition_result = {
        "mds_stage": "message_decomposition_specification_mds",
        "decomposition_result_status": "decomposition_result_created",
        "minimal_assembly": {
            "surface_bundle": {},
            "claim_unit_bundle": {},
        },
    }
    acp_schema_validation = {
        "acp_schema_validation_status": "acp_schema_valid",
        "acp_message_status": "acp_message_created",
        "acp_bundle_status": "acp_bundle_created",
        "decomposition_result": decomposition_result,
        "field_envelope": {},
    }

    scope = check_acp_scope_guard(acp_schema_validation)

    assert scope["decomposition_result"] == decomposition_result


def test_check_acp_scope_guard_preserves_field_envelope() -> None:
    """Minimal ACP Scope Guard preserves the existing field envelope."""
    field_envelope = {
        "source_reference": "bounded_decomposition_result",
        "structural_status": "field_envelope_placeholder",
    }
    acp_schema_validation = {
        "acp_schema_validation_status": "acp_schema_valid",
        "acp_message_status": "acp_message_created",
        "acp_bundle_status": "acp_bundle_created",
        "decomposition_result": {},
        "field_envelope": field_envelope,
    }

    scope = check_acp_scope_guard(acp_schema_validation)

    assert scope["field_envelope"] == field_envelope


def test_check_acp_scope_guard_uses_default_stages_when_missing() -> None:
    """Minimal ACP Scope Guard uses bounded default stage identifiers."""
    acp_schema_validation = {
        "acp_schema_validation_status": "acp_schema_valid",
        "acp_message_status": "acp_message_created",
        "acp_bundle_status": "acp_bundle_created",
        "decomposition_result": {},
        "field_envelope": {},
    }

    scope = check_acp_scope_guard(acp_schema_validation)

    assert scope["source_stage"] == SOURCE_STAGE
    assert scope["target_stage"] == TARGET_STAGE


def test_check_acp_scope_guard_exposes_no_routing_dispatch_or_downstream_fields() -> None:
    """Minimal ACP Scope Guard does not expose routing, dispatch, or downstream fields."""
    acp_schema_validation = {
        "acp_schema_validation_status": "acp_schema_valid",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
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

    scope = check_acp_scope_guard(acp_schema_validation)

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

    assert forbidden_fields.isdisjoint(scope.keys())
    assert forbidden_fields.isdisjoint(scope["decomposition_result"].keys())
    assert forbidden_fields.isdisjoint(scope["field_envelope"].keys())
