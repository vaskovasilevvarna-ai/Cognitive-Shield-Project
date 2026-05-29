"""
Core Input contract boundary for Cognitive Shield.

This module is a Sprint 1 bounded scaffold. It re-exports the stable shared
InputMessage contract and does not implement input normalization, transcript
parsing, language routing, ingestion behavior, or downstream pipeline logic.
"""

from cognitive_shield.shared.contracts.input_contracts import InputMessage

__all__ = [
    "InputMessage",
]
