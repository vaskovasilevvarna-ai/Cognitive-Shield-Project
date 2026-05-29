"""Unit tests for shared common schema helpers."""

from cognitive_shield.shared.schemas.common_schema import (
    build_empty_traceability,
    build_schema_metadata,
)


def test_build_schema_metadata_returns_name_and_version() -> None:
    """build_schema_metadata returns a minimal schema metadata block."""
    metadata = build_schema_metadata(name="InputMessage", version="0.1")

    assert metadata == {
        "name": "InputMessage",
        "version": "0.1",
    }


def test_build_empty_traceability_returns_empty_dict() -> None:
    """build_empty_traceability returns an empty traceability placeholder."""
    traceability = build_empty_traceability()

    assert traceability == {}
