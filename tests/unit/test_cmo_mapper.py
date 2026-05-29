"""Unit tests for the CMO mapper scaffold."""

from cognitive_shield.core.canonical_message_object_cmo.contracts import (
    InputMessage,
)
from cognitive_shield.core.canonical_message_object_cmo.mapper import (
    build_cmo_source_trace_map,
)


def test_build_cmo_source_trace_map_returns_minimal_source_trace() -> None:
    """CMO mapper scaffold returns minimal InputMessage source trace data."""
    message = InputMessage(
        message_id="msg-001",
        raw_text="Minimal message for CMO mapper scaffold.",
        language="en",
    )

    trace_map = build_cmo_source_trace_map(message)

    assert trace_map == {
        "message_id": "msg-001",
        "language": "en",
    }
