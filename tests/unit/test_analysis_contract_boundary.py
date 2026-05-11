"""Unit tests for the Analysis contract boundary scaffold."""

from cognitive_shield.core.analysis.contracts import (
    CognitiveAnalysisOutput,
    EvidenceAnalysisOutput,
    NarrativeAnalysisOutput,
)


def test_analysis_contract_boundary_exports_evidence_output() -> None:
    """Analysis contract boundary exposes the shared EvidenceAnalysisOutput contract."""
    output = EvidenceAnalysisOutput(message_id="msg-001")

    assert output.message_id == "msg-001"
    assert output.claim_assessments == []
    assert output.evidence_signals == []
    assert output.uncertainty_signals == []


def test_analysis_contract_boundary_exports_narrative_output() -> None:
    """Analysis contract boundary exposes the shared NarrativeAnalysisOutput contract."""
    output = NarrativeAnalysisOutput(message_id="msg-001")

    assert output.message_id == "msg-001"
    assert output.framing_assessments == []
    assert output.narrative_signals == []
    assert output.uncertainty_signals == []


def test_analysis_contract_boundary_exports_cognitive_output() -> None:
    """Analysis contract boundary exposes the shared CognitiveAnalysisOutput contract."""
    output = CognitiveAnalysisOutput(message_id="msg-001")

    assert output.message_id == "msg-001"
    assert output.cognitive_pressure_signals == []
    assert output.attention_capture_signals == []
    assert output.uncertainty_signals == []
