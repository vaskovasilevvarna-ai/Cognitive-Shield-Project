"""Unit tests for bounded MDS DecompositionResult shell."""

from cognitive_shield.core.message_decomposition_specification_mds.decomposition_result import (
    build_bounded_decomposition_result,
)
from cognitive_shield.core.message_decomposition_specification_mds.surface_preparation import (
    MDS_STAGE,
)


def test_build_bounded_decomposition_result_wraps_minimal_assembly() -> None:
    """Bounded DecompositionResult preserves existing minimal assembly."""
    minimal_assembly = {
        "mds_stage": MDS_STAGE,
        "assembly_status": "mds_minimal_assembly_created",
        "surface_bundle": {
            "mds_stage": MDS_STAGE,
            "bundle_status": "surface_bundle_created",
        },
        "claim_unit_bundle": {
            "mds_stage": MDS_STAGE,
            "bundle_status": "claim_unit_bundle_created",
            "claim_units": [],
        },
    }

    result = build_bounded_decomposition_result(minimal_assembly)

    assert result == {
        "mds_stage": MDS_STAGE,
        "decomposition_result_status": "decomposition_result_created",
        "minimal_assembly": minimal_assembly,
    }


def test_build_bounded_decomposition_result_preserves_minimal_assembly() -> None:
    """Bounded DecompositionResult does not rewrite minimal assembly."""
    minimal_assembly = {
        "mds_stage": MDS_STAGE,
        "assembly_status": "mds_minimal_assembly_created",
        "surface_bundle": {
            "surface_unit": {
                "surface_unit_id": "surface-unit-001",
                "source_text": "Surface text.",
            },
        },
        "claim_unit_bundle": {
            "claim_units": [
                {
                    "claim_unit_id": "claim-unit-001",
                    "source_text": "Explicit claim unit text.",
                }
            ],
        },
    }

    result = build_bounded_decomposition_result(minimal_assembly)

    assert result["minimal_assembly"] == minimal_assembly


def test_build_bounded_decomposition_result_returns_no_structures_status_for_empty_input() -> None:
    """Bounded DecompositionResult returns bounded status for empty input."""
    result = build_bounded_decomposition_result({})

    assert result == {
        "mds_stage": MDS_STAGE,
        "decomposition_result_status": "no_mds_structures",
        "minimal_assembly": {},
    }


def test_build_bounded_decomposition_result_exposes_no_downstream_fields() -> None:
    """Bounded DecompositionResult does not expose downstream or analytical fields."""
    result = build_bounded_decomposition_result(
        {
            "mds_stage": MDS_STAGE,
            "assembly_status": "mds_minimal_assembly_created",
            "surface_bundle": {},
            "claim_unit_bundle": {},
        }
    )

    forbidden_fields = {
        "canonical_message_object",
        "cmo",
        "acp_bundle",
        "acp_message",
        "analysis_bundle",
        "taxonomy_labels",
        "risk_profile",
        "governance_signal",
        "output_payload",
        "truth_value",
        "evidence_assessment",
        "relation_objects",
        "framing_units",
    }

    assert forbidden_fields.isdisjoint(result.keys())
    assert forbidden_fields.isdisjoint(result["minimal_assembly"].keys())
