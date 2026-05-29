"""
Minimal Analysis contract boundary for Cognitive Shield.

This module is a Sprint 1 bounded scaffold. It re-exports stable shared
analysis contracts and does not implement evidence analysis, narrative analysis,
cognitive analysis, taxonomy behavior, risk scoring, governance behavior, or
downstream pipeline logic.
"""

from cognitive_shield.shared.contracts.analysis_contracts import (
    CognitiveAnalysisOutput,
    EvidenceAnalysisOutput,
    NarrativeAnalysisOutput,
)

__all__ = [
    "EvidenceAnalysisOutput",
    "NarrativeAnalysisOutput",
    "CognitiveAnalysisOutput",
]
