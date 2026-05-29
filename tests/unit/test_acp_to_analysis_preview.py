"""Unit tests for the ACP to Analysis preview scaffold."""

from cognitive_shield.pipeline.acp_to_analysis_preview import (
    ACP_SOURCE_STAGE,
    ANALYSIS_TARGET_STAGE,
    build_acp_to_analysis_preview,
)


def test_build_acp_to_analysis_preview_returns_expected_boundary_preview() -> None:
    """ACP to Analysis preview scaffold returns preview-only handoff fields."""
    preview = build_acp_to_analysis_preview()

    assert preview == {
        "source_stage": ACP_SOURCE_STAGE,
        "target_stage": ANALYSIS_TARGET_STAGE,
        "handoff_status": "preview_only",
        "analysis_status": "not_started",
    }


def test_acp_to_analysis_preview_contains_no_routing_or_analysis_fields() -> None:
    """ACP to Analysis preview scaffold does not expose routing or analysis fields."""
    preview = build_acp_to_analysis_preview()

    forbidden_fields = {
        "acp_bundle",
        "acp_messages",
        "route_map",
        "routing_result",
        "agent_dispatch",
        "contradiction_map",
        "uncertainty_propagation",
        "synthesis_export",
        "evidence_analysis_output",
        "narrative_analysis_output",
        "cognitive_analysis_output",
        "analysis_bundle",
        "evidence_signals",
        "narrative_signals",
        "cognitive_pressure_signals",
        "taxonomy_labels",
        "risk_profile",
    }

    assert forbidden_fields.isdisjoint(preview.keys())
