"""Smoke tests for Sprint 4 MVP functional proof."""

from cognitive_shield.app.mvp_functional_proof import (
    DEFAULT_MVP_PROOF_INPUT,
    run_mvp_functional_proof,
)


FORBIDDEN_FIELDS = {
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


def test_run_mvp_functional_proof_creates_bounded_proof_object() -> None:
    """MVP functional proof creates the expected bounded proof object."""
    proof = run_mvp_functional_proof(DEFAULT_MVP_PROOF_INPUT)

    assert proof["mvp_proof_status"] == "mvp_functional_proof_created"
    assert proof["input_status"] == "input_received"
    assert proof["decomposition_result_status"] == "decomposition_result_created"
    assert proof["cmo_status"] == "bounded_cmo_construction_created"
    assert proof["acp_boundary_status"] == "eligible_for_acp_boundary"
    assert proof["acp_envelope_status"] == "acp_minimal_envelope_created"
    assert proof["acp_bundle_status"] == "acp_bundle_created"
    assert proof["acp_message_status"] == "acp_message_created"
    assert proof["acp_schema_validation_status"] == "acp_schema_valid"
    assert proof["acp_scope_status"] == "acp_scope_allowed"
    assert proof["protocol_router_readiness_status"] == "protocol_router_ready"
    assert proof["routing_result_status"] == "route_ready_no_dispatch"


def test_run_mvp_functional_proof_preserves_decomposition_result() -> None:
    """MVP functional proof preserves bounded DecompositionResult structure."""
    proof = run_mvp_functional_proof(DEFAULT_MVP_PROOF_INPUT)

    decomposition_result = proof["decomposition_result"]

    assert decomposition_result["mds_stage"] == "message_decomposition_specification_mds"
    assert decomposition_result["input_status"] == "input_received"
    assert decomposition_result["decomposition_result_status"] == (
        "decomposition_result_created"
    )
    assert decomposition_result["minimal_assembly"]["surface_bundle"][
        "surface_text"
    ] == DEFAULT_MVP_PROOF_INPUT


def test_run_mvp_functional_proof_preserves_field_envelope() -> None:
    """MVP functional proof preserves the CMO field envelope."""
    proof = run_mvp_functional_proof(DEFAULT_MVP_PROOF_INPUT)

    field_envelope = proof["field_envelope"]

    assert field_envelope == {
        "source_reference": "bounded_decomposition_result",
        "structural_status": "field_envelope_placeholder",
    }


def test_run_mvp_functional_proof_exposes_no_forbidden_fields() -> None:
    """MVP functional proof exposes no forbidden downstream fields."""
    proof = run_mvp_functional_proof(DEFAULT_MVP_PROOF_INPUT)

    assert FORBIDDEN_FIELDS.isdisjoint(proof.keys())
    assert FORBIDDEN_FIELDS.isdisjoint(proof["decomposition_result"].keys())
    assert FORBIDDEN_FIELDS.isdisjoint(proof["field_envelope"].keys())


def test_run_mvp_functional_proof_rejects_empty_input_without_downstream_behavior() -> None:
    """MVP functional proof rejects empty input without downstream behavior."""
    proof = run_mvp_functional_proof("")

    assert proof["mvp_proof_status"] == "mvp_functional_proof_not_ready"
    assert proof["input_status"] == "input_not_ready"
    assert proof["decomposition_result_status"] == "decomposition_result_not_ready"
    assert proof["routing_result_status"] == "not_ready_for_routing"

    assert FORBIDDEN_FIELDS.isdisjoint(proof.keys())
    assert FORBIDDEN_FIELDS.isdisjoint(proof["decomposition_result"].keys())
    assert FORBIDDEN_FIELDS.isdisjoint(proof["field_envelope"].keys())
