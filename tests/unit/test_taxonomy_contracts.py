"""Unit tests for shared taxonomy contracts."""

from cognitive_shield.shared.contracts.taxonomy_contracts import (
    BoundedTaxonomyOutput,
    TaxonomyLabelAssignment,
)


def test_taxonomy_label_assignment_can_be_created_with_required_fields() -> None:
    """TaxonomyLabelAssignment can be constructed with required label fields."""
    assignment = TaxonomyLabelAssignment(
        target_unit_id="claim-001",
        taxonomy_family="evidence",
        label="weak_evidence",
    )

    assert assignment.target_unit_id == "claim-001"
    assert assignment.taxonomy_family == "evidence"
    assert assignment.label == "weak_evidence"
    assert assignment.axis is None
    assert assignment.priority == "primary"
    assert assignment.confidence_hint is None
    assert assignment.uncertainty_flags == []
    assert assignment.trace_ref == ""


def test_bounded_taxonomy_output_can_be_created_with_defaults() -> None:
    """BoundedTaxonomyOutput can be constructed with default label lists."""
    output = BoundedTaxonomyOutput(message_id="msg-001")

    assert output.message_id == "msg-001"
    assert output.evidence_labels == []
    assert output.narrative_labels == []
    assert output.cognitive_labels == []
    assert output.multi_label_notes == []
