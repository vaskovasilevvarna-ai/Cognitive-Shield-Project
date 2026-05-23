"""Unit tests for explicit MDS claim candidate boundary."""

from cognitive_shield.core.message_decomposition_specification_mds.claim_candidates import (
    CLAIM_CANDIDATE_TYPE,
    build_explicit_claim_candidates,
)
from cognitive_shield.core.message_decomposition_specification_mds.surface_preparation import (
    MDS_STAGE,
)


def test_build_explicit_claim_candidates_creates_candidate_from_assertion_like_text() -> None:
    """Explicit claim candidate boundary creates candidate-only records."""
    surface_units = [
        {
            "surface_unit_id": "surface-unit-001",
            "source_text": "This is an explicit surface statement.",
            "unit_type": "surface_text",
            "mds_stage": MDS_STAGE,
            "surface_status": "surface_unit_created",
            "order_index": "1",
        }
    ]

    candidates = build_explicit_claim_candidates(surface_units)

    assert candidates == {
        "mds_stage": MDS_STAGE,
        "candidate_status": "claim_candidate_created",
        "claim_candidates": [
            {
                "claim_candidate_id": "claim-candidate-001",
                "source_surface_unit_id": "surface-unit-001",
                "source_text": "This is an explicit surface statement.",
                "candidate_type": CLAIM_CANDIDATE_TYPE,
                "candidate_status": "claim_candidate_created",
                "order_index": "1",
            }
        ],
    }


def test_build_explicit_claim_candidates_preserves_surface_unit_identity() -> None:
    """Explicit claim candidates preserve source surface unit identity."""
    surface_units = [
        {
            "surface_unit_id": "surface-unit-007",
            "source_text": "Another explicit surface statement.",
            "unit_type": "surface_text",
            "mds_stage": MDS_STAGE,
            "surface_status": "surface_unit_created",
            "order_index": "1",
        }
    ]

    candidates = build_explicit_claim_candidates(surface_units)

    assert candidates["claim_candidates"][0]["source_surface_unit_id"] == "surface-unit-007"
    assert candidates["claim_candidates"][0]["source_text"] == "Another explicit surface statement."


def test_build_explicit_claim_candidates_returns_no_candidate_for_non_assertion_like_text() -> None:
    """Explicit claim candidate boundary blocks non-assertion-like text."""
    surface_units = [
        {
            "surface_unit_id": "surface-unit-001",
            "source_text": "Is this a question?",
            "unit_type": "surface_text",
            "mds_stage": MDS_STAGE,
            "surface_status": "surface_unit_created",
            "order_index": "1",
        }
    ]

    candidates = build_explicit_claim_candidates(surface_units)

    assert candidates == {
        "mds_stage": MDS_STAGE,
        "candidate_status": "not_claim_candidate",
        "claim_candidates": [],
    }


def test_build_explicit_claim_candidates_returns_no_candidate_for_empty_surface_text() -> None:
    """Explicit claim candidate boundary blocks empty surface text."""
    surface_units = [
        {
            "surface_unit_id": "surface-unit-001",
            "source_text": "",
            "unit_type": "surface_text",
            "mds_stage": MDS_STAGE,
            "surface_status": "surface_unit_created",
            "order_index": "1",
        }
    ]

    candidates = build_explicit_claim_candidates(surface_units)

    assert candidates == {
        "mds_stage": MDS_STAGE,
        "candidate_status": "not_claim_candidate",
        "claim_candidates": [],
    }


def test_build_explicit_claim_candidates_exposes_no_downstream_fields() -> None:
    """Explicit claim candidates do not expose analytical or downstream fields."""
    surface_units = [
        {
            "surface_unit_id": "surface-unit-001",
            "source_text": "This is an explicit surface statement.",
            "unit_type": "surface_text",
            "mds_stage": MDS_STAGE,
            "surface_status": "surface_unit_created",
            "order_index": "1",
        }
    ]

    candidates = build_explicit_claim_candidates(surface_units)

    forbidden_fields = {
        "claim_units",
        "verified_claim",
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

    assert forbidden_fields.isdisjoint(candidates.keys())

    for claim_candidate in candidates["claim_candidates"]:
        assert forbidden_fields.isdisjoint(claim_candidate.keys())
