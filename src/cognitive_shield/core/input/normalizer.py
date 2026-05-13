"""
Core Input normalizer scaffold for Cognitive Shield.

This module is a Sprint 1 bounded scaffold. It does not implement real input
normalization, transcript parsing, language routing, ingestion behavior, or
downstream pipeline logic.
"""

from cognitive_shield.core.input.contracts import InputMessage


def build_input_normalization_preview(message: InputMessage) -> dict[str, str]:
    """
    Build a minimal input normalization preview.

    This is a scaffold-level helper only. It does not normalize text, parse
    transcripts, route languages, infer source types, or execute downstream
    pipeline behavior.
    """
    return {
        "message_id": message.message_id,
        "language": message.language,
        "normalization_status": "preview_only",
    }


__all__ = [
    "build_input_normalization_preview",
]
