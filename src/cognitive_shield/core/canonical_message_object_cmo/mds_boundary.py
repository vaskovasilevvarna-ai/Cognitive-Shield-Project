"""
CMO boundary eligibility for MDS output in Cognitive Shield.

This module provides a bounded MDS-to-CMO boundary eligibility check.

It does not construct a Canonical Message Object (CMO), map MDS fields into
a CMO schema, route to ACP, generate Analysis, execute runtime pipeline
behavior, or introduce downstream pipeline logic.
"""

SOURCE_STAGE = "message_decomposition_specification_mds"
TARGET_STAGE = "canonical_message_object_cmo"


def check_mds_to_cmo_boundary_eligibility(
    decomposition_result: dict[str, object],
) -> dict[str, object]:
    """
    Check whether a bounded MDS DecompositionResult is eligible for CMO boundary review.

    This function preserves the original decomposition result and returns only
    a boundary eligibility status. It does not create a Canonical Message Object,
    map fields, enrich content, route to ACP, generate Analysis, or execute
    downstream pipeline behavior.
    """
    result_status = decomposition_result.get(
        "decomposition_result_status",
        "",
    )

    boundary_status = (
        "eligible_for_cmo_boundary"
        if result_status == "decomposition_result_created"
        else "not_eligible_for_cmo_boundary"
    )

    return {
        "boundary_status": boundary_status,
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "decomposition_result_status": result_status,
        "decomposition_result": decomposition_result,
    }


__all__ = [
    "SOURCE_STAGE",
    "TARGET_STAGE",
    "check_mds_to_cmo_boundary_eligibility",
]
