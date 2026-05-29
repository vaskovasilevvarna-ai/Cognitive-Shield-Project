"""Unit tests for the Input schema boundary scaffold."""

from cognitive_shield.core.input.schemas import (
    INPUT_SCHEMA_NAME,
    INPUT_SCHEMA_VERSION,
)


def test_input_schema_identity_constants_are_defined() -> None:
    """Input schema boundary exposes stable schema identity constants."""
    assert INPUT_SCHEMA_NAME == "core_input"
    assert INPUT_SCHEMA_VERSION == "0.1"
