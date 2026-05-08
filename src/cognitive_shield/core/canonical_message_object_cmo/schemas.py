"""
Canonical Message Object (CMO) schema boundary for Cognitive Shield.

This module is a Sprint 1 bounded scaffold. It does not implement real CMO
schema validation, CMO construction, Message Decomposition Specification (MDS)
output conversion, or downstream pipeline logic.
"""

CMO_SCHEMA_NAME = "canonical_message_object_cmo"
CMO_SCHEMA_VERSION = "0.1"

__all__ = [
    "CMO_SCHEMA_NAME",
    "CMO_SCHEMA_VERSION",
]
