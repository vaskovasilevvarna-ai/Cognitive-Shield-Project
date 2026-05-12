"""Unit tests for the Cognitive analysis scaffold."""

from cognitive_shield.core.analysis.cognitive import build_cognitive_preview
from cognitive_shield.core.analysis.contracts import CognitiveAnalysisOutput


def test_build_cognitive_preview_returns_minimal_cognitive_fields() -> None:
    """Cognitive analysis scaffold returns cognitive preview fields only."""
    output = CognitiveAnalysisOutput(message_id="msg-001")

    cognitive_preview = build_cognitive_preview(output)

    assert cognitive_preview == {
        "message_id": "msg-001",
        "analysis_type": "cognitive",
        "analysis_status": "preview_only",
    }
