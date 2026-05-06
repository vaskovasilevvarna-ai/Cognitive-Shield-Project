"""Unit tests for shared risk and governance contracts."""

from cognitive_shield.shared.contracts.risk_contracts import (
    ArbiterDecisionRecord,
    ConfidenceUncertaintyProfile,
    DecisionPolicyRecord,
    RiskDimensionScore,
    RiskProfile,
    ShieldDecisionRecord,
)


def test_risk_dimension_score_can_be_created_with_defaults() -> None:
    """RiskDimensionScore can be constructed with default explanatory lists."""
    score = RiskDimensionScore(
        dimension="evidence_risk",
        score_value=0.25,
    )

    assert score.dimension == "evidence_risk"
    assert score.score_value == 0.25
    assert score.drivers == []
    assert score.dampeners == []
    assert score.uncertainty_modifiers == []


def test_risk_profile_can_be_created_with_defaults() -> None:
    """RiskProfile can be constructed with default aggregation structures."""
    profile = RiskProfile(message_id="msg-001")

    assert profile.message_id == "msg-001"
    assert profile.dimension_scores == []
    assert profile.global_aggregation == {}
    assert profile.explainability_traces == []


def test_confidence_uncertainty_profile_can_be_created_with_required_fields() -> None:
    """ConfidenceUncertaintyProfile can be constructed with required fields."""
    profile = ConfidenceUncertaintyProfile(
        message_id="msg-001",
        confidence_band="medium",
        uncertainty_mode="visible",
    )

    assert profile.message_id == "msg-001"
    assert profile.confidence_band == "medium"
    assert profile.uncertainty_mode == "visible"
    assert profile.uncertainty_sources == []
    assert profile.propagation_notes == []


def test_arbiter_decision_record_can_be_created_with_defaults() -> None:
    """ArbiterDecisionRecord can be constructed with default governance fields."""
    record = ArbiterDecisionRecord(message_id="msg-001")

    assert record.message_id == "msg-001"
    assert record.conflict_map == []
    assert record.validated_risk_profile == {}
    assert record.adjusted_confidence_profile == {}
    assert record.decision_readiness == "not_ready"
    assert record.escalation_flags == []


def test_decision_policy_record_can_be_created_with_required_fields() -> None:
    """DecisionPolicyRecord can be constructed with required policy fields."""
    record = DecisionPolicyRecord(
        message_id="msg-001",
        policy_mode="bounded",
    )

    assert record.message_id == "msg-001"
    assert record.policy_mode == "bounded"
    assert record.admissible_actions == []
    assert record.restrictions == []
    assert record.policy_rationale == []


def test_shield_decision_record_can_be_created_with_required_fields() -> None:
    """ShieldDecisionRecord can be constructed with required decision fields."""
    record = ShieldDecisionRecord(
        message_id="msg-001",
        decision_posture="explain",
        decision_summary="Minimal bounded decision summary.",
    )

    assert record.message_id == "msg-001"
    assert record.decision_posture == "explain"
    assert record.decision_summary == "Minimal bounded decision summary."
    assert record.governance_notes == []
    assert record.uncertainty_visibility_requirements == []
