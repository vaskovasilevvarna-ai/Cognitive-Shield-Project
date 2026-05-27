"""
ACP boundary eligibility for CMO output in Cognitive Shield.

This module provides a bounded Canonical Message Object (CMO) to Agent
Communication Protocol (ACP) boundary eligibility check.

It does not create an ACPBundle, create an ACPMessage, route to agents,
dispatch messages, orchestrate agent communication, generate Analysis, execute
runtime pipeline behavior, or introduce downstream pipeline logic.
"""

SOURCE_STAGE = "canonical_message_object_cmo"
TARGET_STAGE = "agent_communication_protocol_acp"


def check_cmo_to_acp_boundary_eligibility(
    bounded_cmo_construction: dict[str, object],
) -> dict[str, object]:
    """
    Check whether a bounded CMO construction candidate is eligible for ACP boundary review.

    This function preserves the original bounded MDS DecompositionResult and
    field envelope. It returns only a boundary eligibility status. It does not
    create ACP bundles, create ACP messages, route, dispatch, orchestrate,
    generate Analysis, or execute downstream pipeline behavior.
    """
    construction_status = bounded_cmo_construction.get(
        "bounded_cmo_construction_status",
        "",
    )

    acp_boundary_status = (
        "eligible_for_acp_boundary"
        if construction_status == "bounded_cmo_construction_created"
        else "not_eligible_for_acp_boundary"
    )

    return {
        "acp_boundary_status": acp_boundary_status,
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "bounded_cmo_construction_status": construction_status,
        "decomposition_result": bounded_cmo_construction.get(
            "decomposition_result",
            {},
        ),
        "field_envelope": bounded_cmo_construction.get("field_envelope", {}),
    }


__all__ = [
    "SOURCE_STAGE",
    "TARGET_STAGE",
    "check_cmo_to_acp_boundary_eligibility",
]
