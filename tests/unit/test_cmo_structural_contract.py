"""Unit tests for CMO structural contract boundary."""

from cognitive_shield.core.canonical_message_object_cmo.mds_boundary import (
    SOURCE_STAGE,
    TARGET_STAGE,
)
from cognitive_shield.core.canonical_message_object_cmo.structural_contract import (
    build_cmo_structural_contract,
)


def test_build_cmo_structural_contract_ready_from_valid_shell() -> None:
    """CMO structural contract becomes ready from a valid minimal shell."""
    decomposition_result = {
        "mds_stage": SOURCE_STAGE,
        "decomposition_result_status": "decomposition_result_created",
        "minimal_assembly": {},
    }
    cmo_shell = {
        "cmo_shell_status": "cmo_shell_created",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "boundary_status": "eligible_for_cmo_boundary",
        "decomposition_result": decomposition_result,
    }

    contract = build_cmo_structural_contract(cmo_shell)

    assert contract == {
        "cmo_contract_status": "cmo_structural_contract_ready",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "cmo_shell_status": "cmo_shell_created",
        "decomposition_result": decomposition_result,
    }


def test_build_cmo_structural_contract_not_ready_from_non_eligible_shell() -> None:
    """CMO structural contract is not ready from a non-created shell."""
    cmo_shell = {
        "cmo_shell_status": "not_eligible_for_cmo_shell",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "boundary_status": "not_eligible_for_cmo_boundary",
        "decomposition_result": {},
    }

    contract = build_cmo_structural_contract(cmo_shell)

    assert contract == {
        "cmo_contract_status": "not_ready_for_cmo_structural_contract",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "cmo_shell_status": "not_eligible_for_cmo_shell",
        "decomposition_result": {},
    }


def test_build_cmo_structural_contract_preserves_decomposition_result() -> None:
    """CMO structural contract preserves the original DecompositionResult."""
    decomposition_result = {
        "mds_stage": SOURCE_STAGE,
        "decomposition_result_status": "decomposition_result_created",
        "minimal_assembly": {
            "surface_bundle": {},
            "claim_unit_bundle": {},
        },
    }
    cmo_shell = {
        "cmo_shell_status": "cmo_shell_created",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "decomposition_result": decomposition_result,
    }

    contract = build_cmo_structural_contract(cmo_shell)

    assert contract["decomposition_result"] == decomposition_result


def test_build_cmo_structural_contract_uses_default_stages_when_missing() -> None:
    """CMO structural contract uses bounded default stage identifiers."""
    cmo_shell = {
        "cmo_shell_status": "cmo_shell_created",
        "decomposition_result": {},
    }

    contract = build_cmo_structural_contract(cmo_shell)

    assert contract["source_stage"] == SOURCE_STAGE
    assert contract["target_stage"] == TARGET_STAGE


def test_build_cmo_structural_contract_exposes_no_full_cmo_or_downstream_fields() -> None:
    """CMO structural contract does not expose full CMO or downstream fields."""
    cmo_shell = {
        "cmo_shell_status": "cmo_shell_created",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "decomposition_result": {
            "decomposition_result_status": "decomposition_result_created",
        },
    }

    contract = build_cmo_structural_contract(cmo_shell)

    forbidden_fields = {
        "canonical_message_object",
        "CanonicalMessageObject",
        "cmo_fields",
        "cmo_schema",
        "cmo_mapping",
        "normalized_content",
        "enriched_content",
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

    assert forbidden_fields.isdisjoint(contract.keys())
    assert forbidden_fields.isdisjoint(contract["decomposition_result"].keys())
