"""Unit tests for the Narrative analysis scaffold."""

from cognitive_shield.core.analysis.contracts import NarrativeAnalysisOutput
from cognitive_shield.core.analysis.narrative import build_narrative_preview


def test_build_narrative_preview_returns_minimal_narrative_fields() -> None:
    """Narrative analysis scaffold returns narrative preview fields only."""
    output = NarrativeAnalysisOutput(message_id="msg-001")

    narrative_preview = build_narrative_preview(output)

    assert narrative_preview == {
        "message_id": "msg-001",
        "analysis_type": "narrative",
        "analysis_status": "preview_only",
    }
