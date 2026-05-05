"""Unit tests for shared analysis contracts."""

from cognitive_shield.shared.contracts.analysis_contracts import (
    CognitiveAnalysisOutput,
    EvidenceAnalysisOutput,
    NarrativeAnalysisOutput,
)


def test_evidence_analysis_output_can_be_created_with_defaults() -> None:
    """EvidenceAnalysisOutput can be constructed with default signal lists."""
    output = EvidenceAnalysisOutput(message_id="msg-001")

    assert output.message_id == "msg-001"
    assert output.claim_assessments == []
    assert output.evidence_signals == []
    assert output.uncertainty_signals == []


def test_narrative_analysis_output_can_be_created_with_defaults() -> None:
    """NarrativeAnalysisOutput can be constructed with default signal lists."""
    output = NarrativeAnalysisOutput(message_id="msg-001")

    assert output.message_id == "msg-001"
    assert output.framing_assessments == []
    assert output.narrative_signals == []
    assert output.uncertainty_signals == []


def test_cognitive_analysis_output_can_be_created_with_defaults() -> None:
    """CognitiveAnalysisOutput can be constructed with default signal lists."""
    output = CognitiveAnalysisOutput(message_id="msg-001")

    assert output.message_id == "msg-001"
    assert output.cognitive_pressure_signals == []
    assert output.attention_capture_signals == []
    assert output.uncertainty_signals == []
