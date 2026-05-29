"""
MVP functional proof helper for Cognitive Shield.

This module provides a local, bounded MVP-level functional proof.

It wires the already admitted structural chain into a testable proof object:

input-derived bounded structure
→ bounded MDS DecompositionResult placeholder
→ CMO field envelope placeholder
→ ACP boundary eligibility-shaped result
→ ACP minimal envelope
→ ACPBundle
→ ACPMessage
→ ACP Schema Validator
→ ACP Scope Guard
→ Protocol Router readiness
→ minimal non-dispatch routing result
→ MVP proof object

This helper does not implement full runtime pipeline behavior. It does not
dispatch ACPMessages, select agents, create agent instructions, generate
Analysis, call taxonomy/risk/governance/output modules, or introduce downstream
pipeline logic.
"""

from cognitive_shield.core.agent_communication_protocol_acp.bundle import (
    build_acp_bundle,
)
from cognitive_shield.core.agent_communication_protocol_acp.cmo_boundary import (
    SOURCE_STAGE,
    TARGET_STAGE,
)
from cognitive_shield.core.agent_communication_protocol_acp.message import (
    build_acp_message,
)
from cognitive_shield.core.agent_communication_protocol_acp.minimal_envelope import (
    build_acp_minimal_envelope,
)
from cognitive_shield.core.agent_communication_protocol_acp.router_readiness import (
    check_protocol_router_readiness,
)
from cognitive_shield.core.agent_communication_protocol_acp.routing_result import (
    build_minimal_routing_result,
)
from cognitive_shield.core.agent_communication_protocol_acp.schema_validator_minimal import (
    validate_acp_message_schema,
)
from cognitive_shield.core.agent_communication_protocol_acp.scope_guard_minimal import (
    check_acp_scope_guard,
)


DEFAULT_MVP_PROOF_INPUT = "Public claim example for MVP proof."


def _build_bounded_decomposition_result(input_text: str) -> dict[str, object]:
    """
    Build a minimal bounded DecompositionResult-shaped object for MVP proof.

    This is proof-local scaffolding. It does not perform semantic analysis,
    implicit claim inference, evidence assessment, taxonomy behavior, risk
    scoring, or governance behavior.
    """
    input_status = "input_received" if input_text else "input_not_ready"

    return {
        "mds_stage": "message_decomposition_specification_mds",
        "input_status": input_status,
        "decomposition_result_status": (
            "decomposition_result_created"
            if input_status == "input_received"
            else "decomposition_result_not_ready"
        ),
        "minimal_assembly": {
            "surface_bundle": {
                "surface_text": input_text,
                "surface_status": "surface_preserved",
            },
            "claim_unit_bundle": {
                "claim_unit_status": "bounded_claim_unit_placeholder",
            },
        },
    }


def _build_cmo_field_envelope() -> dict[str, object]:
    """
    Build a minimal CMO field envelope-shaped object for MVP proof.

    This is proof-local scaffolding and does not perform CMO semantic
    construction beyond the bounded field envelope needed by admitted ACP
    helpers.
    """
    return {
        "source_reference": "bounded_decomposition_result",
        "structural_status": "field_envelope_placeholder",
    }


def _build_acp_boundary_result(
    decomposition_result: dict[str, object],
    field_envelope: dict[str, object],
) -> dict[str, object]:
    """
    Build an ACP boundary eligibility-shaped result for admitted ACP helpers.

    This does not route, dispatch, generate Analysis, or execute a runtime
    pipeline.
    """
    is_ready = (
        decomposition_result.get("decomposition_result_status")
        == "decomposition_result_created"
    )

    return {
        "acp_boundary_status": (
            "eligible_for_acp_boundary"
            if is_ready
            else "not_eligible_for_acp_boundary"
        ),
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "bounded_cmo_construction_status": (
            "bounded_cmo_construction_created"
            if is_ready
            else "not_ready_for_bounded_cmo_construction"
        ),
        "decomposition_result": decomposition_result,
        "field_envelope": field_envelope,
    }


def run_mvp_functional_proof(
    input_text: str = DEFAULT_MVP_PROOF_INPUT,
) -> dict[str, object]:
    """
    Run the bounded Sprint 4 MVP functional proof.

    The proof connects admitted modules and returns a bounded proof object. It
    does not execute the full product pipeline and does not introduce dispatch,
    Analysis generation, taxonomy behavior, risk scoring, governance behavior,
    output rendering, runtime execution, or downstream logic.
    """
    decomposition_result = _build_bounded_decomposition_result(input_text)
    field_envelope = _build_cmo_field_envelope()

    acp_boundary_result = _build_acp_boundary_result(
        decomposition_result=decomposition_result,
        field_envelope=field_envelope,
    )
    acp_envelope = build_acp_minimal_envelope(acp_boundary_result)
    acp_bundle = build_acp_bundle(acp_envelope)
    acp_message = build_acp_message(acp_bundle)
    schema_validation = validate_acp_message_schema(acp_message)
    scope_guard = check_acp_scope_guard(schema_validation)
    router_readiness = check_protocol_router_readiness(scope_guard)
    routing_result = build_minimal_routing_result(router_readiness)

    proof_ready = (
        routing_result.get("routing_result_status") == "route_ready_no_dispatch"
    )

    return {
        "mvp_proof_status": (
            "mvp_functional_proof_created"
            if proof_ready
            else "mvp_functional_proof_not_ready"
        ),
        "input_status": decomposition_result.get("input_status", ""),
        "decomposition_result_status": decomposition_result.get(
            "decomposition_result_status",
            "",
        ),
        "cmo_status": acp_boundary_result.get(
            "bounded_cmo_construction_status",
            "",
        ),
        "acp_boundary_status": acp_boundary_result.get("acp_boundary_status", ""),
        "acp_envelope_status": acp_envelope.get("acp_envelope_status", ""),
        "acp_bundle_status": acp_bundle.get("acp_bundle_status", ""),
        "acp_message_status": acp_message.get("acp_message_status", ""),
        "acp_schema_validation_status": schema_validation.get(
            "acp_schema_validation_status",
            "",
        ),
        "acp_scope_status": scope_guard.get("acp_scope_status", ""),
        "protocol_router_readiness_status": router_readiness.get(
            "protocol_router_readiness_status",
            "",
        ),
        "routing_result_status": routing_result.get("routing_result_status", ""),
        "decomposition_result": routing_result.get("decomposition_result", {}),
        "field_envelope": routing_result.get("field_envelope", {}),
    }


__all__ = [
    "DEFAULT_MVP_PROOF_INPUT",
    "run_mvp_functional_proof",
]
