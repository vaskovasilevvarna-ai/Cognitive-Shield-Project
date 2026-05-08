"""Unit tests for the CMO contract boundary scaffold."""

from cognitive_shield.core.canonical_message_object_cmo.contracts import (
    ClaimUnit,
    ContextCarrier,
    FramingUnit,
    InputMessage,
    RelationObject,
    SurfaceSegment,
)


def test_cmo_contract_boundary_exports_input_message() -> None:
    """CMO contract boundary exposes the shared InputMessage contract."""
    message = InputMessage(
        message_id="msg-001",
        raw_text="Minimal CMO boundary test message.",
        language="en",
    )

    assert message.message_id == "msg-001"
    assert message.raw_text == "Minimal CMO boundary test message."
    assert message.language == "en"


def test_cmo_contract_boundary_exports_structuring_units() -> None:
    """CMO contract boundary exposes shared structuring contracts."""
    segment = SurfaceSegment(
        segment_id="seg-001",
        text="Minimal segment.",
        start_offset=0,
        end_offset=16,
    )
    claim = ClaimUnit(
        claim_id="claim-001",
        text="Minimal claim.",
        source_segment_ids=["seg-001"],
        claim_type="assertion",
        explicitness="explicit",
    )
    framing = FramingUnit(
        framing_id="frame-001",
        text="Minimal framing.",
        framing_mode="neutral",
        source_segment_ids=["seg-001"],
    )
    relation = RelationObject(
        relation_id="rel-001",
        relation_type="references",
        from_unit_id="claim-001",
        to_unit_id="frame-001",
    )
    context = ContextCarrier(
        context_id="ctx-001",
        context_type="source_context",
        value="Minimal context.",
    )

    assert segment.segment_id == "seg-001"
    assert claim.claim_id == "claim-001"
    assert framing.framing_id == "frame-001"
    assert relation.relation_id == "rel-001"
    assert context.context_id == "ctx-001"
