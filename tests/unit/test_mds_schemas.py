"""Unit tests for the MDS schema boundary scaffold."""

from cognitive_shield.core.message_decomposition_specification_mds.schemas import (
    MDS_SCHEMA_NAME,
    MDS_SCHEMA_VERSION,
)


def test_mds_schema_identity_constants_are_defined() -> None:
    """MDS schema boundary exposes stable schema identity constants."""
    assert MDS_SCHEMA_NAME == "message_decomposition_specification_mds"
    assert MDS_SCHEMA_VERSION == "0.1"
