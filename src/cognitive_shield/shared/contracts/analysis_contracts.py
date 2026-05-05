"""
Shared analysis contracts for Cognitive Shield.
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class EvidenceAnalysisOutput:
    message_id: str
    claim_assessments: list[dict[str, Any]] = field(default_factory=list)
    evidence_signals: list[dict[str, Any]] = field(default_factory=list)
    uncertainty_signals: list[dict[str, Any]] = field(default_factory=list)


@dataclass
class NarrativeAnalysisOutput:
    message_id: str
    framing_assessments: list[dict[str, Any]] = field(default_factory=list)
    narrative_signals: list[dict[str, Any]] = field(default_factory=list)
    uncertainty_signals: list[dict[str, Any]] = field(default_factory=list)


@dataclass
class CognitiveAnalysisOutput:
    message_id: str
    cognitive_pressure_signals: list[dict[str, Any]] = field(default_factory=list)
    attention_capture_signals: list[dict[str, Any]] = field(default_factory=list)
    uncertainty_signals: list[dict[str, Any]] = field(default_factory=list)
