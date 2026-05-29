"""Unit tests for the Input readiness status helper."""

from cognitive_shield.core.input.contracts import InputMessage
from cognitive_shield.core.input.readiness import build_input_readiness_status


def test_build_input_readiness_status_returns_ready_for_valid_input() -> None:
    """Input readiness returns ready for a minimally valid InputMessage."""
    message = InputMessage(
        message_id="msg-001",
        raw_text="Minimal valid input message.",
        language="en",
    )

    readiness = build_input_readiness_status(message)

    assert readiness == {
        "message_id": "msg-001",
        "language": "en",
        "input_status": "ready",
        "reason": "minimal_input_source_valid",
    }


def test_build_input_readiness_status_blocks_invalid_input() -> None:
    """Input readiness blocks an invalid InputMessage."""
    message = InputMessage(
        message_id="",
        raw_text="",
        language="",
    )

    readiness = build_input_readiness_status(message)

    assert readiness == {
        "message_id": "",
        "language": "",
        "input_status": "blocked",
        "reason": "minimal_input_source_invalid",
    }


def test_build_input_readiness_status_blocks_whitespace_only_raw_text() -> None:
    """Input readiness blocks whitespace-only raw_text."""
    message = InputMessage(
        message_id="msg-001",
        raw_text="   ",
        language="en",
    )

    readiness = build_input_readiness_status(message)

    assert readiness == {
        "message_id": "msg-001",
        "language": "en",
        "input_status": "blocked",
        "reason": "minimal_input_source_invalid",
    }


def test_build_input_readiness_status_exposes_no_downstream_fields() -> None:
    """Input readiness does not expose MDS or downstream fields."""
    message = InputMessage(
        message_id="msg-001",
        raw_text="Minimal valid input message.",
        language="en",
    )

    readiness = build_input_readiness_status(message)

    forbidden_fields = {
        "surface_segments",
        "claim_units",
        "framing_units",
        "relation_objects",
        "context_carriers",
        "decomposition_uncertainty",
        "traceability_map",
        "canonical_message_object",
        "acp_bundle",
        "analysis_bundle",
        "taxonomy_labels",
        "risk_profile",
    }

    assert forbidden_fields.isdisjoint(readiness.keys())
