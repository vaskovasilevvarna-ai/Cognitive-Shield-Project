"""Unit tests for minimal CMO shell boundary."""

from cognitive_shield.core.canonical_message_object_cmo.mds_boundary import (
    SOURCE_STAGE,
    TARGET_STAGE,
)
from cognitive_shield.core.canonical_message_object_cmo.minimal_shell import (
    build_minimal_cmo_shell,
)


def test_build_minimal_cmo_shell_creates_shell_for_eligible_boundary() -> None:
    """Minimal CMO shell is created only from eligible boundary result."""
    decomposition_result = {
        "mds_stage": SOURCE_STAGE,
        "decomposition_result_status": "decomposition_result_created",
        "minimal_assembly": {},
    }
    mds_boundary_result = {
        "boundary_status": "eligible_for_cmo_boundary",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "decomposition_result_status": "decomposition_result_created",
        "decomposition_result": decomposition_result,
    }

    shell = build_minimal_cmo_shell(mds_boundary_result)

    assert shell == {
        "cmo_shell_status": "cmo_shell_created",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "boundary_status": "eligible_for_cmo_boundary",
        "decomposition_result": decomposition_result,
    }


def test_build_minimal_cmo_shell_rejects_non_eligible_boundary() -> None:
    """Minimal CMO shell is not created from non-eligible boundary result."""
    mds_boundary_result = {
        "boundary_status": "not_eligible_for_cmo_boundary",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "decomposition_result_status": "no_mds_structures",
        "decomposition_result": {},
    }

    shell = build_minimal_cmo_shell(mds_boundary_result)

    assert shell == {
        "cmo_shell_status": "not_eligible_for_cmo_shell",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "boundary_status": "not_eligible_for_cmo_boundary",
        "decomposition_result": {},
    }


def test_build_minimal_cmo_shell_preserves_decomposition_result() -> None:
    """Minimal CMO shell preserves the original DecompositionResult."""
    decomposition_result = {
        "mds_stage": SOURCE_STAGE,
        "decomposition_result_status": "decomposition_result_created",
        "minimal_assembly": {
            "surface_bundle": {},
            "claim_unit_bundle": {},
        },
    }
    mds_boundary_result = {
        "boundary_status": "eligible_for_cmo_boundary",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "decomposition_result": decomposition_result,
    }

    shell = build_minimal_cmo_shell(mds_boundary_result)

    assert shell["decomposition_result"] == decomposition_result


def test_build_minimal_cmo_shell_exposes_no_full_cmo_or_downstream_fields() -> None:
    """Minimal CMO shell does not expose full CMO or downstream fields."""
    mds_boundary_result = {
        "boundary_status": "eligible_for_cmo_boundary",
        "source_stage": SOURCE_STAGE,
        "target_stage": TARGET_STAGE,
        "decomposition_result": {
            "decomposition_result_status": "decomposition_result_created",
        },
    }

    shell = build_minimal_cmo_shell(mds_boundary_result)

    forbidden_fields = {
        "canonical_message_object",
        "CanonicalMessageObject",
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

    assert forbidden_fields.isdisjoint(shell.keys())
    assert forbidden_fields.isdisjoint(shell["decomposition_result"].keys())
