"""
Core Input schema boundary for Cognitive Shield.

This module is a Sprint 1 bounded scaffold. It does not implement real input
normalization, transcript parsing, language routing, ingestion behavior, or
downstream pipeline logic.
"""

INPUT_SCHEMA_NAME = "core_input"
INPUT_SCHEMA_VERSION = "0.1"

__all__ = [
    "INPUT_SCHEMA_NAME",
    "INPUT_SCHEMA_VERSION",
]
