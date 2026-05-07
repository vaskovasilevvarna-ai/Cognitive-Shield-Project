"""Unit tests for the MDS mapper scaffold."""

from cognitive_shield.core.message_decomposition_specification_mds.contracts import (
    InputMessage,
)
from cognitive_shield.core.message_decomposition_specification_mds.mapper import (
    build_input_trace_map,
)


def test_build_input_trace_map_returns_minimal_message_trace() -> None:
    """MDS mapper scaffold returns minimal InputMessage trace data."""
    message = InputMessage(
        message_id="msg-001",
        raw_text="Minimal message for MDS mapper scaffold.",
        language="en",
    )

    trace_map = build_input_trace_map(message)

    assert trace_map == {
        "message_id": "msg-001",
        "language": "en",
    }
