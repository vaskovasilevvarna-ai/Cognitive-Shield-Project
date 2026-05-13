"""
Core Input validator scaffold for Cognitive Shield.

This module is a Sprint 1 bounded scaffold. It does not implement real input
normalization, transcript parsing, language routing, ingestion behavior, or
downstream pipeline logic.
"""

from cognitive_shield.core.input.contracts import InputMessage


def is_valid_input_source(message: InputMessage) -> bool:
    """
    Check whether an InputMessage has minimal source fields.

    This is a scaffold-level check only. It does not normalize input, parse
    transcripts, route languages, infer source types, or execute downstream
    pipeline behavior.
    """
    return bool(
        message.message_id
        and message.raw_text
        and message.language
    )


__all__ = [
    "is_valid_input_source",
]
