"""
Message Decomposition Specification (MDS) contract boundary for Cognitive Shield.

This module is a Sprint 1 bounded scaffold. It does not implement message
decomposition behavior.
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
