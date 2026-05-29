"""Unit tests for minimal ACP schema validator boundary."""

from cognitive_shield.core.agent_communication_protocol_acp.cmo_boundary import (
    SOURCE_STAGE,
    TARGET_STAGE,
)
from cognitive_shield.core.agent_communication_protocol_acp.schema_validator_minimal import (
    REQUIRED_ACP_MESSAGE_FIELDS,
    validate_acp_message_schema,
)


def test_validate_acp_message_schema_accepts_valid_message() -> None:
    """Minimal ACP schema validator accepts a structurally valid ACPMessage."""
    decomposition_result = {
        "mds_stage": "message_decomposition_specification_mds",
        "decomposition_result_status": "decomposition_result_created",
        "minimal_assembly": {},
    }
    field_envelope = {
        "source_reference": "bounded_decomposition_result",
        "structural_status": "field_envelope_placeholder",
    }
    acp_message = {
        "acp_message_status": "acp_message_created",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "acp_bundle_status": "acp_bundle_created",
        "decomposition_result": decomposition_result,
        "field_envelope": field_envelope,
    }

    validation = validate_acp_message_schema(acp_message)

    assert validation == {
        "acp_schema_validation_status": "acp_schema_valid",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "acp_message_status": "acp_message_created",
        "acp_bundle_status": "acp_bundle_created",
        "decomposition_result": decomposition_result,
        "field_envelope": field_envelope,
    }


def test_validate_acp_message_schema_rejects_non_ready_message() -> None:
    """Minimal ACP schema validator rejects a non-ready ACPMessage."""
    acp_message = {
        "acp_message_status": "not_ready_for_acp_message",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "acp_bundle_status": "not_ready_for_acp_bundle",
        "decomposition_result": {},
        "field_envelope": {},
    }

    validation = validate_acp_message_schema(acp_message)

    assert validation == {
        "acp_schema_validation_status": "acp_schema_invalid",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "acp_message_status": "not_ready_for_acp_message",
        "acp_bundle_status": "not_ready_for_acp_bundle",
        "decomposition_result": {},
        "field_envelope": {},
    }


def test_validate_acp_message_schema_rejects_missing_required_fields() -> None:
    """Minimal ACP schema validator rejects missing required fields."""
    acp_message = {
        "acp_message_status": "acp_message_created",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "acp_bundle_status": "acp_bundle_created",
    }

    validation = validate_acp_message_schema(acp_message)

    assert validation["acp_schema_validation_status"] == "acp_schema_invalid"
    assert REQUIRED_ACP_MESSAGE_FIELDS.difference(acp_message.keys()) == {
        "decomposition_result",
        "field_envelope",
    }


def test_validate_acp_message_schema_rejects_empty_input() -> None:
    """Minimal ACP schema validator rejects empty input."""
    validation = validate_acp_message_schema({})

    assert validation == {
        "acp_schema_validation_status": "acp_schema_invalid",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "acp_message_status": "",
        "acp_bundle_status": "",
        "decomposition_result": {},
        "field_envelope": {},
    }


def test_validate_acp_message_schema_preserves_decomposition_result() -> None:
    """Minimal ACP schema validator preserves the original DecompositionResult."""
    decomposition_result = {
        "mds_stage": "message_decomposition_specification_mds",
        "decomposition_result_status": "decomposition_result_created",
        "minimal_assembly": {
            "surface_bundle": {},
            "claim_unit_bundle": {},
        },
    }
    acp_message = {
        "acp_message_status": "acp_message_created",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "acp_bundle_status": "acp_bundle_created",
        "decomposition_result": decomposition_result,
        "field_envelope": {},
    }

    validation = validate_acp_message_schema(acp_message)

    assert validation["decomposition_result"] == decomposition_result


def test_validate_acp_message_schema_preserves_field_envelope() -> None:
    """Minimal ACP schema validator preserves the existing field envelope."""
    field_envelope = {
        "source_reference": "bounded_decomposition_result",
        "structural_status": "field_envelope_placeholder",
    }
    acp_message = {
        "acp_message_status": "acp_message_created",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "acp_bundle_status": "acp_bundle_created",
        "decomposition_result": {},
        "field_envelope": field_envelope,
    }

    validation = validate_acp_message_schema(acp_message)

    assert validation["field_envelope"] == field_envelope


def test_validate_acp_message_schema_uses_default_stages_when_missing() -> None:
    """Minimal ACP schema validator uses bounded default stage identifiers."""
    acp_message = {
        "acp_message_status": "acp_message_created",
        "acp_bundle_status": "acp_bundle_created",
        "decomposition_result": {},
        "field_envelope": {},
    }

    validation = validate_acp_message_schema(acp_message)

    assert validation["source_stage"] == SOURCE_STAGE
    assert validation["target_stage"] == TARGET_STAGE


def test_validate_acp_message_schema_exposes_no_routing_scope_or_downstream_fields() -> None:
    """Minimal ACP schema validator does not expose routing, scope, or downstream fields."""
    acp_message = {
        "acp_message_status": "acp_message_created",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "acp_bundle_status": "acp_bundle_created",
        "decomposition_result": {
            "decomposition_result_status": "decomposition_result_created",
        },
        "field_envelope": {
            "source_reference": "bounded_decomposition_result",
            "structural_status": "field_envelope_placeholder",
        },
    }

    validation = validate_acp_message_schema(acp_message)

    forbidden_fields = {
        "agent_route",
        "routing_decision",
        "dispatch_target",
        "agent_id",
        "agent_instruction",
        "scope_decision",
        "scope_violation",
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

    assert forbidden_fields.isdisjoint(validation.keys())
    assert forbidden_fields.isdisjoint(validation["decomposition_result"].keys())
    assert forbidden_fields.isdisjoint(validation["field_envelope"].keys())
