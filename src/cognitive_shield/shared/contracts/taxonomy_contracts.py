"""
Shared taxonomy contracts for Cognitive Shield.
"""

from dataclasses import dataclass, field


@dataclass
class TaxonomyLabelAssignment:
    target_unit_id: str
    taxonomy_family: str
    label: str
    axis: str | None = None
    priority: str = "primary"
    confidence_hint: str | None = None
    uncertainty_flags: list[str] = field(default_factory=list)
    trace_ref: str = ""


@dataclass
class BoundedTaxonomyOutput:
    message_id: str
    evidence_labels: list[TaxonomyLabelAssignment] = field(default_factory=list)
    narrative_labels: list[TaxonomyLabelAssignment] = field(default_factory=list)
    cognitive_labels: list[TaxonomyLabelAssignment] = field(default_factory=list)
    multi_label_notes: list[dict[str, str]] = field(default_factory=list)
