"""
Agent Communication Protocol (ACP) contract boundary for Cognitive Shield.

This module is a Sprint 1 bounded scaffold. It defines minimal protocol
contract shapes only. It does not implement routing, orchestration,
contradiction registration, uncertainty propagation, synthesis export, analysis
execution, governance behavior, or downstream pipeline logic.
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class ACPMessage:
    """
    Minimal typed message envelope for future ACP exchange.

    This is a scaffold contract only. It does not route, execute, validate, or
    synthesize agent outputs.
    """

    message_id: str
    sender: str
    recipient: str
    message_type: str
    payload: dict[str, Any] = field(default_factory=dict)
    uncertainty_flags: list[str] = field(default_factory=list)
    trace_ref: str = ""


@dataclass
class ACPBundle:
    """
    Minimal container for future ACP message exchange.

    This is a scaffold contract only. It does not perform orchestration or
    synthesis.
    """

    bundle_id: str
    source_message_id: str
    messages: list[ACPMessage] = field(default_factory=list)
    contradiction_notes: list[dict[str, Any]] = field(default_factory=list)
    uncertainty_notes: list[dict[str, Any]] = field(default_factory=list)


__all__ = [
    "ACPMessage",
    "ACPBundle",
]
