"""Unit tests for explicit MDS claim unit bundle boundary."""

from cognitive_shield.core.message_decomposition_specification_mds.claim_units import (
    EXPLICIT_CLAIM_UNIT_TYPE,
)
from cognitive_shield.core.message_decomposition_specification_mds.claim_unit_bundle import (
    build_explicit_claim_unit_bundle,
)
from cognitive_shield.core.message_decomposition_specification_mds.surface_preparation import (
    MDS_STAGE,
)


def test_build_explicit_claim_unit_bundle_bundles_claim_units() -> None:
    """Explicit claim unit bundle preserves existing structural claim units."""
    claim_units = [
        {
            "claim_unit_id": "claim-unit-001",
            "source_claim_candidate_id": "claim-candidate-001",
            "source_surface_unit_id": "surface-unit-001",
            "source_text": "This is an explicit surface statement.",
            "unit_type": EXPLICIT_CLAIM_UNIT_TYPE,
            "claim_unit_status": "claim_unit_created",
            "order_index": "1",
        }
    ]

    bundle = build_explicit_claim_unit_bundle(claim_units)

    assert bundle == {
        "mds_stage": MDS_STAGE,
        "bundle_status": "claim_unit_bundle_created",
        "claim_units": claim_units,
    }


def test_build_explicit_claim_unit_bundle_preserves_claim_unit_order() -> None:
    """Explicit claim unit bundle preserves claim unit order."""
    claim_units = [
        {
            "claim_unit_id": "claim-unit-001",
            "source_claim_candidate_id": "claim-candidate-001",
            "source_surface_unit_id": "surface-unit-001",
            "source_text": "First explicit surface statement.",
            "unit_type": EXPLICIT_CLAIM_UNIT_TYPE,
            "claim_unit_status": "claim_unit_created",
            "order_index": "1",
        },
        {
            "claim_unit_id": "claim-unit-002",
            "source_claim_candidate_id": "claim-candidate-002",
            "source_surface_unit_id": "surface-unit-002",
            "source_text": "Second explicit surface statement.",
            "unit_type": EXPLICIT_CLAIM_UNIT_TYPE,
            "claim_unit_status": "claim_unit_created",
            "order_index": "2",
        },
    ]

    bundle = build_explicit_claim_unit_bundle(claim_units)

    assert bundle["claim_units"][0]["claim_unit_id"] == "claim-unit-001"
    assert bundle["claim_units"][1]["claim_unit_id"] == "claim-unit-002"
    assert bundle["claim_units"][0]["order_index"] == "1"
    assert bundle["claim_units"][1]["order_index"] == "2"


def test_build_explicit_claim_unit_bundle_returns_no_claim_units_for_empty_input() -> None:
    """Explicit claim unit bundle returns no claim units for empty input."""
    bundle = build_explicit_claim_unit_bundle([])

    assert bundle == {
        "mds_stage": MDS_STAGE,
        "bundle_status": "no_claim_units",
        "claim_units": [],
    }


def test_build_explicit_claim_unit_bundle_ignores_non_claim_unit_records() -> None:
    """Explicit claim unit bundle ignores records that are not claim units."""
    claim_units = [
        {
            "claim_unit_id": "claim-unit-001",
            "source_claim_candidate_id": "claim-candidate-001",
            "source_surface_unit_id": "surface-unit-001",
            "source_text": "This should not be bundled.",
            "unit_type": "not_a_claim_unit",
            "claim_unit_status": "claim_unit_created",
            "order_index": "1",
        }
    ]

    bundle = build_explicit_claim_unit_bundle(claim_units)

    assert bundle == {
        "mds_stage": MDS_STAGE,
        "bundle_status": "no_claim_units",
        "claim_units": [],
    }


def test_build_explicit_claim_unit_bundle_ignores_inactive_claim_units() -> None:
    """Explicit claim unit bundle ignores inactive claim unit records."""
    claim_units = [
        {
            "claim_unit_id": "claim-unit-001",
            "source_claim_candidate_id": "claim-candidate-001",
            "source_surface_unit_id": "surface-unit-001",
            "source_text": "This should not be bundled.",
            "unit_type": EXPLICIT_CLAIM_UNIT_TYPE,
            "claim_unit_status": "not_claim_unit",
            "order_index": "1",
        }
    ]

    bundle = build_explicit_claim_unit_bundle(claim_units)

    assert bundle == {
        "mds_stage": MDS_STAGE,
        "bundle_status": "no_claim_units",
        "claim_units": [],
    }


def test_build_explicit_claim_unit_bundle_exposes_no_downstream_fields() -> None:
    """Explicit claim unit bundle does not expose analytical or downstream fields."""
    claim_units = [
        {
            "claim_unit_id": "claim-unit-001",
            "source_claim_candidate_id": "claim-candidate-001",
            "source_surface_unit_id": "surface-unit-001",
            "source_text": "This is an explicit surface statement.",
            "unit_type": EXPLICIT_CLAIM_UNIT_TYPE,
            "claim_unit_status": "claim_unit_created",
            "order_index": "1",
        }
    ]

    bundle = build_explicit_claim_unit_bundle(claim_units)

    forbidden_fields = {
        "truth_value",
        "evidence_assessment",
        "framing_units",
        "relation_objects",
        "context_carriers",
        "global_narrative_structure",
        "decomposition_uncertainty",
        "traceability_map",
        "decomposition_result",
        "canonical_message_object",
        "acp_bundle",
        "analysis_bundle",
        "taxonomy_labels",
        "risk_profile",
    }

    assert forbidden_fields.isdisjoint(bundle.keys())

    for claim_unit in bundle["claim_units"]:
        assert forbidden_fields.isdisjoint(claim_unit.keys())
