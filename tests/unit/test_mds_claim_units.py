"""Unit tests for explicit MDS claim unit boundary."""

from cognitive_shield.core.message_decomposition_specification_mds.claim_candidates import (
    CLAIM_CANDIDATE_TYPE,
)
from cognitive_shield.core.message_decomposition_specification_mds.claim_units import (
    EXPLICIT_CLAIM_UNIT_TYPE,
    build_explicit_claim_units,
)
from cognitive_shield.core.message_decomposition_specification_mds.surface_preparation import (
    MDS_STAGE,
)


def test_build_explicit_claim_units_creates_unit_from_candidate() -> None:
    """Explicit claim unit boundary creates structural claim units only."""
    claim_candidates = [
        {
            "claim_candidate_id": "claim-candidate-001",
            "source_surface_unit_id": "surface-unit-001",
            "source_text": "This is an explicit surface statement.",
            "candidate_type": CLAIM_CANDIDATE_TYPE,
            "candidate_status": "claim_candidate_created",
            "order_index": "1",
        }
    ]

    claim_units = build_explicit_claim_units(claim_candidates)

    assert claim_units == {
        "mds_stage": MDS_STAGE,
        "claim_unit_status": "claim_unit_created",
        "claim_units": [
            {
                "claim_unit_id": "claim-unit-001",
                "source_claim_candidate_id": "claim-candidate-001",
                "source_surface_unit_id": "surface-unit-001",
                "source_text": "This is an explicit surface statement.",
                "unit_type": EXPLICIT_CLAIM_UNIT_TYPE,
                "claim_unit_status": "claim_unit_created",
                "order_index": "1",
            }
        ],
    }


def test_build_explicit_claim_units_preserves_candidate_and_surface_identity() -> None:
    """Explicit claim units preserve candidate and surface identities."""
    claim_candidates = [
        {
            "claim_candidate_id": "claim-candidate-007",
            "source_surface_unit_id": "surface-unit-009",
            "source_text": "Another explicit surface statement.",
            "candidate_type": CLAIM_CANDIDATE_TYPE,
            "candidate_status": "claim_candidate_created",
            "order_index": "3",
        }
    ]

    claim_units = build_explicit_claim_units(claim_candidates)

    claim_unit = claim_units["claim_units"][0]

    assert claim_unit["source_claim_candidate_id"] == "claim-candidate-007"
    assert claim_unit["source_surface_unit_id"] == "surface-unit-009"
    assert claim_unit["source_text"] == "Another explicit surface statement."
    assert claim_unit["order_index"] == "3"


def test_build_explicit_claim_units_returns_no_units_for_empty_candidates() -> None:
    """Explicit claim unit boundary returns no units for empty candidates."""
    claim_units = build_explicit_claim_units([])

    assert claim_units == {
        "mds_stage": MDS_STAGE,
        "claim_unit_status": "not_claim_unit",
        "claim_units": [],
    }


def test_build_explicit_claim_units_ignores_non_candidate_inputs() -> None:
    """Explicit claim unit boundary ignores non-candidate input records."""
    claim_candidates = [
        {
            "claim_candidate_id": "claim-candidate-001",
            "source_surface_unit_id": "surface-unit-001",
            "source_text": "This should not become a claim unit.",
            "candidate_type": "not_a_claim_candidate",
            "candidate_status": "claim_candidate_created",
            "order_index": "1",
        }
    ]

    claim_units = build_explicit_claim_units(claim_candidates)

    assert claim_units == {
        "mds_stage": MDS_STAGE,
        "claim_unit_status": "not_claim_unit",
        "claim_units": [],
    }


def test_build_explicit_claim_units_ignores_inactive_candidate_status() -> None:
    """Explicit claim unit boundary ignores inactive candidate records."""
    claim_candidates = [
        {
            "claim_candidate_id": "claim-candidate-001",
            "source_surface_unit_id": "surface-unit-001",
            "source_text": "This should not become a claim unit.",
            "candidate_type": CLAIM_CANDIDATE_TYPE,
            "candidate_status": "not_claim_candidate",
            "order_index": "1",
        }
    ]

    claim_units = build_explicit_claim_units(claim_candidates)

    assert claim_units == {
        "mds_stage": MDS_STAGE,
        "claim_unit_status": "not_claim_unit",
        "claim_units": [],
    }


def test_build_explicit_claim_units_exposes_no_downstream_fields() -> None:
    """Explicit claim units do not expose analytical or downstream fields."""
    claim_candidates = [
        {
            "claim_candidate_id": "claim-candidate-001",
            "source_surface_unit_id": "surface-unit-001",
            "source_text": "This is an explicit surface statement.",
            "candidate_type": CLAIM_CANDIDATE_TYPE,
            "candidate_status": "claim_candidate_created",
            "order_index": "1",
        }
    ]

    claim_units = build_explicit_claim_units(claim_candidates)

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

    assert forbidden_fields.isdisjoint(claim_units.keys())

    for claim_unit in claim_units["claim_units"]:
        assert forbidden_fields.isdisjoint(claim_unit.keys())
