"""
Shared output contracts for Sprint 0.
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class CanonicalOutputSchema:
    message_id: str
    executive_signal: dict[str, Any] = field(default_factory=dict)
    claim_level_findings: list[dict[str, Any]] = field(default_factory=list)
    uncertainty_block: dict[str, Any] = field(default_factory=dict)
    conflict_block: dict[str, Any] = field(default_factory=dict)
    decision_block: dict[str, Any] = field(default_factory=dict)
    traceability_block: dict[str, Any] = field(default_factory=dict)
