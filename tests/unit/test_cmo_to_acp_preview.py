"""Unit tests for the CMO to ACP preview scaffold."""

from cognitive_shield.pipeline.cmo_to_acp_preview import (
    ACP_TARGET_STAGE,
    CMO_SOURCE_STAGE,
    build_cmo_to_acp_preview,
)


def test_build_cmo_to_acp_preview_returns_expected_boundary_preview() -> None:
    """CMO to ACP preview scaffold returns preview-only handoff fields."""
    preview = build_cmo_to_acp_preview()

    assert preview == {
        "source_stage": CMO_SOURCE_STAGE,
        "target_stage": ACP_TARGET_STAGE,
        "handoff_status": "preview_only",
        "routing_status": "not_started",
    }


def test_cmo_to_acp_preview_contains_no_construction_or_routing_fields() -> None:
    """CMO to ACP preview scaffold does not expose construction or routing fields."""
    preview = build_cmo_to_acp_preview()

    forbidden_fields = {
        "canonical_message_object",
        "message_metadata",
        "surface_layer",
        "claim_layer",
        "framing_layer",
        "relation_layer",
        "context_layer",
        "global_structure_layer",
        "uncertainty_layer",
        "traceability_layer",
        "acp_bundle",
        "acp_messages",
        "route_map",
        "routing_result",
        "agent_dispatch",
        "contradiction_map",
        "uncertainty_propagation",
        "synthesis_export",
    }

    assert forbidden_fields.isdisjoint(preview.keys())
