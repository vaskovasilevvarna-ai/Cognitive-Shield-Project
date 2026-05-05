"""Unit tests for shared analysis contracts."""

from cognitive_shield.shared.contracts.analysis_contracts import EvidenceAnalysisOutput


def test_evidence_analysis_output_can_be_created_with_defaults() -> None:
    """EvidenceAnalysisOutput can be constructed with default signal lists."""
    output = EvidenceAnalysisOutput(message_id="msg-001")

    assert output.message_id == "msg-001"
    assert output.claim_assessments == []
    assert output.evidence_signals == []
    assert output.uncertainty_signals == []
