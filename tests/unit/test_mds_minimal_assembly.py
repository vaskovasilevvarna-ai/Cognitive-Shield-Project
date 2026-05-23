"""Unit tests for minimal MDS assembly boundary."""

from cognitive_shield.core.message_decomposition_specification_mds.minimal_assembly import (
    build_mds_minimal_assembly,
)
from cognitive_shield.core.message_decomposition_specification_mds.surface_preparation import (
    MDS_STAGE,
)


def test_build_mds_minimal_assembly_groups_existing_structures() -> None:
    """Minimal MDS assembly groups existing bounded MDS structures."""
    surface_bundle = {
        "mds_stage": MDS_STAGE,
        "bundle_status": "surface_bundle_created",
        "surface_preparation": {
            "message_id": "msg-001",
            "source_text": "This is an explicit surface statement.",
            "mds_stage": MDS_STAGE,
            "preparation_status": "prepared",
            "surface_status": "surface_text_preserved",
        },
        "surface_unit": {
            "surface_unit_id": "surface-unit-001",
            "source_text": "This is an explicit surface statement.",
            "unit_type": "surface_text",
            "mds_stage": MDS_STAGE,
            "surface_status": "surface_unit_created",
        },
    }

    claim_unit_bundle = {
        "mds_stage": MDS_STAGE,
        "bundle_status": "claim_unit_bundle_created",
        "claim_units": [
            {
                "claim_unit_id": "claim-unit-001",
                "source_claim_candidate_id": "claim-candidate-001",
                "source_surface_unit_id": "surface-unit-001",
                "source_text": "This is an explicit surface statement.",
                "unit_type": "explicit_claim_unit",
                "claim_unit_status": "claim_unit_created",
                "order_index": "1",
            }
        ],
    }

    assembly = build_mds_minimal_assembly(
        surface_bundle=surface_bundle,
        claim_unit_bundle=claim_unit_bundle,
    )

    assert assembly == {
        "mds_stage": MDS_STAGE,
        "assembly_status": "mds_minimal_assembly_created",
        "surface_bundle": surface_bundle,
        "claim_unit_bundle": claim_unit_bundle,
    }


def test_build_mds_minimal_assembly_preserves_surface_bundle() -> None:
    """Minimal MDS assembly preserves the existing surface bundle unchanged."""
    surface_bundle = {
        "mds_stage": MDS_STAGE,
        "bundle_status": "surface_bundle_created",
        "surface_unit": {
            "surface_unit_id": "surface-unit-001",
            "source_text": "Surface text.",
        },
    }

    assembly = build_mds_minimal_assembly(
        surface_bundle=surface_bundle,
        claim_unit_bundle={},
    )

    assert assembly["surface_bundle"] == surface_bundle


def test_build_mds_minimal_assembly_preserves_claim_unit_bundle() -> None:
    """Minimal MDS assembly preserves the existing claim unit bundle unchanged."""
    claim_unit_bundle = {
        "mds_stage": MDS_STAGE,
        "bundle_status": "claim_unit_bundle_created",
        "claim_units": [
            {
                "claim_unit_id": "claim-unit-001",
                "source_text": "Claim unit text.",
            }
        ],
    }

    assembly = build_mds_minimal_assembly(
        surface_bundle={},
        claim_unit_bundle=claim_unit_bundle,
    )

    assert assembly["claim_unit_bundle"] == claim_unit_bundle


def test_build_mds_minimal_assembly_returns_no_structures_status_for_empty_inputs() -> None:
    """Minimal MDS assembly returns bounded status for empty structures."""
    assembly = build_mds_minimal_assembly(
        surface_bundle={},
        claim_unit_bundle={},
    )

    assert assembly == {
        "mds_stage": MDS_STAGE,
        "assembly_status": "no_mds_structures",
        "surface_bundle": {},
        "claim_unit_bundle": {},
    }


def test_build_mds_minimal_assembly_exposes_no_downstream_fields() -> None:
    """Minimal MDS assembly does not expose downstream or analytical fields."""
    assembly = build_mds_minimal_assembly(
        surface_bundle={
            "mds_stage": MDS_STAGE,
            "bundle_status": "surface_bundle_created",
        },
        claim_unit_bundle={
            "mds_stage": MDS_STAGE,
            "bundle_status": "claim_unit_bundle_created",
            "claim_units": [],
        },
    )

    forbidden_fields = {
        "decomposition_result",
        "canonical_message_object",
        "acp_bundle",
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

    assert forbidden_fields.isdisjoint(assembly.keys())
    assert forbidden_fields.isdisjoint(assembly["surface_bundle"].keys())
    assert forbidden_fields.isdisjoint(assembly["claim_unit_bundle"].keys())
