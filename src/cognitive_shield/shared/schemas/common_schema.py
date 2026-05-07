"""
Common schema helpers for Cognitive Shield.
"""

from typing import Any


def build_schema_metadata(name: str, version: str) -> dict[str, Any]:
    """
    Build a minimal schema metadata block.
    """
    return {
        "name": name,
        "version": version,
    }


def build_empty_traceability() -> dict[str, Any]:
    """
    Build an empty traceability placeholder.
    """
    return {}
