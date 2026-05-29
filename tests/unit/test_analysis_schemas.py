"""Unit tests for the Analysis schema boundary scaffold."""

from cognitive_shield.core.analysis.schemas import (
    ANALYSIS_SCHEMA_NAME,
    ANALYSIS_SCHEMA_VERSION,
)


def test_analysis_schema_identity_constants_are_defined() -> None:
    """Analysis schema boundary exposes stable schema identity constants."""
    assert ANALYSIS_SCHEMA_NAME == "analysis"
    assert ANALYSIS_SCHEMA_VERSION == "0.1"
