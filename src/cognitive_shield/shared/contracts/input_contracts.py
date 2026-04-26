"""
Shared input contracts for Sprint 0.
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class InputMessage:
    message_id: str
    raw_text: str
    language: str
    source_type: str | None = None
    timestamp: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class SurfaceSegment:
    segment_id: str
    text: str
    start_offset: int
    end_offset: int


@dataclass
class ClaimUnit:
    claim_id: str
    text: str
    source_segment_ids: list[str]
    claim_type: str
    explicitness: str
    uncertainty_flags: list[str] = field(default_factory=list)


@dataclass
class FramingUnit:
    framing_id: str
    text: str
    framing_mode: str
    source_segment_ids: list[str]


@dataclass
class RelationObject:
    relation_id: str
    relation_type: str
    from_unit_id: str
    to_unit_id: str


@dataclass
class ContextCarrier:
    context_id: str
    context_type: str
    value: str
    linked_unit_ids: list[str] = field(default_factory=list)
