"""Unit tests for the Analysis bundle scaffold."""

from cognitive_shield.core.analysis.bundle import build_analysis_bundle_preview
from cognitive_shield.core.analysis.contracts import (
    CognitiveAnalysisOutput,
    EvidenceAnalysisOutput,
    NarrativeAnalysisOutput,
)


def test_build_analysis_bundle_preview_returns_minimal_bundle_fields() -> None:
    """Analysis bundle scaffold returns bundle preview fields only."""
    evidence_output = EvidenceAnalysisOutput(message_id="msg-001")
    narrative_output = NarrativeAnalysisOutput(message_id="msg-001")
    cognitive_output = CognitiveAnalysisOutput(message_id="msg-001")

    bundle_preview = build_analysis_bundle_preview(
        evidence_output=evidence_output,
        narrative_output=narrative_output,
        cognitive_output=cognitive_output,
    )

    assert bundle_preview == {
        "message_id": "msg-001",
        "bundle_type": "analysis",
        "bundle_status": "preview_only",
    }
