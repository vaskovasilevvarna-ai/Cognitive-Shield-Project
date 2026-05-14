"""
Phase A integration shell scaffold for Cognitive Shield.

This module is a Sprint 1 bounded scaffold. It does not implement runtime
pipeline execution, Input to MDS execution, CMO construction, ACP routing,
Analysis generation, downstream pipeline logic, or end-to-end message
processing.
"""

PHASE_A_SEQUENCE = (
    "input",
    "message_decomposition_specification_mds",
    "canonical_message_object_cmo",
    "agent_communication_protocol_acp",
    "analysis",
)


def get_phase_a_sequence_preview() -> tuple[str, ...]:
    """
    Return the declared Phase A scaffold sequence.

    This is a non-executing sequence identity helper only. It does not call,
    execute, connect, or transform data across Phase A modules.
    """
    return PHASE_A_SEQUENCE


__all__ = [
    "PHASE_A_SEQUENCE",
    "get_phase_a_sequence_preview",
]
