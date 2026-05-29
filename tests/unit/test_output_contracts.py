"""Unit tests for shared output contracts."""

from cognitive_shield.shared.contracts.output_contracts import CanonicalOutputSchema


def test_canonical_output_schema_can_be_created_with_defaults() -> None:
    """CanonicalOutputSchema can be constructed with default output blocks."""
    output = CanonicalOutputSchema(message_id="msg-001")

    assert output.message_id == "msg-001"
    assert output.executive_signal == {}
    assert output.claim_level_findings == []
    assert output.uncertainty_block == {}
    assert output.conflict_block == {}
    assert output.decision_block == {}
    assert output.traceability_block == {}
