"""
Shared risk and governance contracts for Cognitive Shield.
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class RiskDimensionScore:
    dimension: str
    score_value: float
    drivers: list[dict[str, Any]] = field(default_factory=list)
    dampeners: list[dict[str, Any]] = field(default_factory=list)
    uncertainty_modifiers: list[dict[str, Any]] = field(default_factory=list)


@dataclass
class RiskProfile:
    message_id: str
    dimension_scores: list[RiskDimensionScore] = field(default_factory=list)
    global_aggregation: dict[str, Any] = field(default_factory=dict)
    explainability_traces: list[dict[str, Any]] = field(default_factory=list)


@dataclass
class ConfidenceUncertaintyProfile:
    message_id: str
    confidence_band: str
    uncertainty_mode: str
    uncertainty_sources: list[dict[str, Any]] = field(default_factory=list)
    propagation_notes: list[dict[str, Any]] = field(default_factory=list)


@dataclass
class ArbiterDecisionRecord:
    message_id: str
    conflict_map: list[dict[str, Any]] = field(default_factory=list)
    validated_risk_profile: dict[str, Any] = field(default_factory=dict)
    adjusted_confidence_profile: dict[str, Any] = field(default_factory=dict)
    decision_readiness: str = "not_ready"
    escalation_flags: list[str] = field(default_factory=list)


@dataclass
class DecisionPolicyRecord:
    message_id: str
    policy_mode: str
    admissible_actions: list[str] = field(default_factory=list)
    restrictions: list[str] = field(default_factory=list)
    policy_rationale: list[dict[str, Any]] = field(default_factory=list)


@dataclass
class ShieldDecisionRecord:
    message_id: str
    decision_posture: str
    decision_summary: str
    governance_notes: list[dict[str, Any]] = field(default_factory=list)
    uncertainty_visibility_requirements: list[str] = field(default_factory=list)
