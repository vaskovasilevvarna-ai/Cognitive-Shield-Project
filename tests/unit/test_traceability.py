"""Unit tests for shared traceability helpers."""

from cognitive_shield.shared.utils.traceability import (
    build_trace_block,
    build_trace_ref,
)


def test_build_trace_ref_combines_message_and_unit_ids() -> None:
    """build_trace_ref creates a stable minimal trace reference."""
    trace_ref = build_trace_ref(message_id="msg-001", unit_id="claim-001")

    assert trace_ref == "msg-001:claim-001"


def test_build_trace_block_returns_keyword_payload() -> None:
    """build_trace_block returns a dictionary from keyword arguments."""
    trace_block = build_trace_block(
        message_id="msg-001",
        unit_id="claim-001",
        trace_ref="msg-001:claim-001",
    )

    assert trace_block == {
        "message_id": "msg-001",
        "unit_id": "claim-001",
        "trace_ref": "msg-001:claim-001",
    }
