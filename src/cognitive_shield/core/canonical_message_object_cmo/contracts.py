"""
Canonical Message Object (CMO) contract boundary for Cognitive Shield.

This module is a Sprint 1 bounded scaffold. It does not implement real CMO
construction, Message Decomposition Specification (MDS) output conversion,
claim graph construction, taxonomy logic, risk scoring, or downstream pipeline
logic.
"""

from cognitive_shield.shared.contracts.input_contracts import (
    ClaimUnit,
    ContextCarrier,
    FramingUnit,
    InputMessage,
    RelationObject,
    SurfaceSegment,
)

__all__ = [
    "InputMessage",
    "SurfaceSegment",
    "ClaimUnit",
    "FramingUnit",
    "RelationObject",
    "ContextCarrier",
]
