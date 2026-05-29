"""Unit tests for the Evidence analysis scaffold."""

from cognitive_shield.core.analysis.contracts import EvidenceAnalysisOutput
from cognitive_shield.core.analysis.evidence import build_evidence_preview


def test_build_evidence_preview_returns_minimal_evidence_fields() -> None:
    """Evidence analysis scaffold returns evidence preview fields only."""
    output = EvidenceAnalysisOutput(message_id="msg-001")

    evidence_preview = build_evidence_preview(output)

    assert evidence_preview == {
        "message_id": "msg-001",
        "analysis_type": "evidence",
        "analysis_status": "preview_only",
    }
