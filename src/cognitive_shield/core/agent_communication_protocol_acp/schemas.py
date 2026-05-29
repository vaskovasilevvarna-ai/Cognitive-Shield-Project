"""
Agent Communication Protocol (ACP) schema boundary for Cognitive Shield.

This module is a Sprint 1 bounded scaffold. It does not implement real ACP
schema validation, routing, orchestration, contradiction registration,
uncertainty propagation, synthesis export, or downstream pipeline logic.
"""

ACP_SCHEMA_NAME = "agent_communication_protocol_acp"
ACP_SCHEMA_VERSION = "0.1"

__all__ = [
    "ACP_SCHEMA_NAME",
    "ACP_SCHEMA_VERSION",
]
