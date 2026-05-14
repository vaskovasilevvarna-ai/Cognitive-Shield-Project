"""Unit tests for the Phase A integration shell scaffold."""

from cognitive_shield.pipeline.phase_a_shell import (
    PHASE_A_SEQUENCE,
    get_phase_a_sequence_preview,
)


def test_phase_a_sequence_declares_expected_scaffold_order() -> None:
    """Phase A shell scaffold exposes the expected non-executing sequence."""
    assert PHASE_A_SEQUENCE == (
        "input",
        "message_decomposition_specification_mds",
        "canonical_message_object_cmo",
        "agent_communication_protocol_acp",
        "analysis",
    )


def test_get_phase_a_sequence_preview_returns_declared_sequence() -> None:
    """Phase A sequence preview returns the declared scaffold sequence only."""
    assert get_phase_a_sequence_preview() == PHASE_A_SEQUENCE
