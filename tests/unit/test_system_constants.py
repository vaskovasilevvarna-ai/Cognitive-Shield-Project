"""Unit tests for shared system constants."""

from cognitive_shield.shared.constants.system_constants import (
    DEFAULT_CONFIDENCE_BAND,
    DEFAULT_DECISION_READINESS,
    DEFAULT_POLICY_MODE,
    DEFAULT_UNCERTAINTY_MODE,
    SUPPORTED_LANGUAGES,
)


def test_supported_languages_include_bg_and_en() -> None:
    """SUPPORTED_LANGUAGES preserves Bulgarian and English readiness."""
    assert SUPPORTED_LANGUAGES == ("bg", "en")


def test_default_governance_constants_are_bounded_and_visible() -> None:
    """Default governance constants preserve conservative Sprint 1 posture."""
    assert DEFAULT_POLICY_MODE == "bounded"
    assert DEFAULT_DECISION_READINESS == "not_ready"
    assert DEFAULT_CONFIDENCE_BAND == "low"
    assert DEFAULT_UNCERTAINTY_MODE == "visible"
