"""Unit tests for the CMO schema boundary scaffold."""

from cognitive_shield.core.canonical_message_object_cmo.schemas import (
    CMO_SCHEMA_NAME,
    CMO_SCHEMA_VERSION,
)


def test_cmo_schema_identity_constants_are_defined() -> None:
    """CMO schema boundary exposes stable schema identity constants."""
    assert CMO_SCHEMA_NAME == "canonical_message_object_cmo"
    assert CMO_SCHEMA_VERSION == "0.1"
