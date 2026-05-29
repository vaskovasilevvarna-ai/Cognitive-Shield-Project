"""Unit tests for MDS-to-CMO boundary eligibility."""

from cognitive_shield.core.canonical_message_object_cmo.mds_boundary import (
    SOURCE_STAGE,
    TARGET_STAGE,
    check_mds_to_cmo_boundary_eligibility,
)
from cognitive_shield.core.message_decomposition_specification_mds.surface_preparation import (
    MDS_STAGE,
)


def test_check_mds_to_cmo_boundary_eligibility_accepts_bounded_result() -> None:
    """MDS-to-CMO boundary accepts a bounded DecompositionResult shell."""
    decomposition_result = {
        "mds_stage": MDS_STAGE,
        "decomposition_result_status": "decomposition_result_created",
        "minimal_assembly": {
            "mds_stage": MDS_STAGE,
            "assembly_status": "mds_minimal_assembly_created",
            "surface_bundle": {},
            "claim_unit_bundle": {},
        },
    }

    boundary = check_mds_to_cmo_boundary_eligibility(decomposition_result)

    assert boundary == {
        "boundary_status": "eligible_for_cmo_boundary",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "decomposition_result_status": "decomposition_result_created",
        "decomposition_result": decomposition_result,
    }


def test_check_mds_to_cmo_boundary_eligibility_rejects_empty_result() -> None:
    """MDS-to-CMO boundary rejects an empty DecompositionResult shell."""
    boundary = check_mds_to_cmo_boundary_eligibility({})

    assert boundary == {
        "boundary_status": "not_eligible_for_cmo_boundary",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "decomposition_result_status": "",
        "decomposition_result": {},
    }


def test_check_mds_to_cmo_boundary_eligibility_rejects_no_structures_status() -> None:
    """MDS-to-CMO boundary rejects a no-structures DecompositionResult shell."""
    decomposition_result = {
        "mds_stage": MDS_STAGE,
        "decomposition_result_status": "no_mds_structures",
        "minimal_assembly": {},
    }

    boundary = check_mds_to_cmo_boundary_eligibility(decomposition_result)

    assert boundary == {
        "boundary_status": "not_eligible_for_cmo_boundary",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "decomposition_result_status": "no_mds_structures",
        "decomposition_result": decomposition_result,
    }


def test_check_mds_to_cmo_boundary_eligibility_preserves_decomposition_result() -> None:
    """MDS-to-CMO boundary preserves the original DecompositionResult unchanged."""
    decomposition_result = {
        "mds_stage": MDS_STAGE,
        "decomposition_result_status": "decomposition_result_created",
        "minimal_assembly": {
            "surface_bundle": {
                "bundle_status": "surface_bundle_created",
            },
            "claim_unit_bundle": {
                "bundle_status": "claim_unit_bundle_created",
                "claim_units": [],
            },
        },
    }

    boundary = check_mds_to_cmo_boundary_eligibility(decomposition_result)

    assert boundary["decomposition_result"] == decomposition_result


def test_check_mds_to_cmo_boundary_eligibility_exposes_no_downstream_fields() -> None:
    """MDS-to-CMO boundary does not expose CMO, ACP, Analysis, or downstream fields."""
    decomposition_result = {
        "mds_stage": MDS_STAGE,
        "decomposition_result_status": "decomposition_result_created",
        "minimal_assembly": {},
    }

    boundary = check_mds_to_cmo_boundary_eligibility(decomposition_result)

    forbidden_fields = {
        "canonical_message_object",
        "cmo",
        "cmo_fields",
        "cmo_schema",
        "acp_bundle",
        "acp_message",
        "analysis_bundle",
        "taxonomy_labels",
        "risk_profile",
        "governance_signal",
        "output_payload",
        "truth_value",
        "evidence_assessment",
    }

    assert forbidden_fields.isdisjoint(boundary.keys())
    assert forbidden_fields.isdisjoint(boundary["decomposition_result"].keys())
