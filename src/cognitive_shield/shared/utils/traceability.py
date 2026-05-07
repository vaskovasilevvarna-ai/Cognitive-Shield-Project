"""
Shared traceability helpers for Cognitive Shield.
"""

from typing import Any


def build_trace_ref(message_id: str, unit_id: str) -> str:
    """
    Build a minimal trace reference string.
    """
    return f"{message_id}:{unit_id}"


def build_trace_block(**kwargs: Any) -> dict[str, Any]:
    """
    Build a minimal traceability block placeholder.
    """
    return dict(kwargs)
