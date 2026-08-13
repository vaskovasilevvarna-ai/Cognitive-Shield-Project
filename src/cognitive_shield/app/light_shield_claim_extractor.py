"""Bounded claim-like unit extractor for Light Shield v0.

This module provides a small deterministic text splitter for the first
behavioral slice of Light Shield v0.

It produces candidate claim-like units from a single input text using bounded
punctuation and newline splitting.

It does not verify claims, assess truth or falsity, detect manipulation,
classify taxonomy labels, score risk or confidence, produce verdicts, or call
external models or services.
"""

from __future__ import annotations

import re
from typing import Any


CLAIM_LIKE_UNITS_STATUS = "bounded_claim_like_units_extracted"
NO_CLAIM_LIKE_UNITS_STATUS = "no_claim_like_units_extracted"
UNIT_TYPE = "claim_like_unit"
EXTRACTION_STATUS = "extracted_by_bounded_splitter"

UNIT_UNCERTAINTY_NOTE = (
    "This is a candidate claim-like unit, not a verified claim."
)

LIMITATIONS = [
    (
        "Units are produced by deterministic punctuation and newline splitting, "
        "not semantic claim verification."
    ),
    (
        "Extracted units do not indicate truth, falsity, manipulation, risk, "
        "confidence, or verdict."
    ),
]


def _normalize_preserving_lines(input_text: str) -> str:
    """Normalize whitespace while preserving non-empty line boundaries."""

    normalized_lines = [
        " ".join(line.split())
        for line in input_text.splitlines()
        if line.strip()
    ]
    return "\n".join(normalized_lines)


def _split_candidate_fragments(input_text: str) -> list[str]:
    """Split normalized text on bounded sentence punctuation and newlines."""

    normalized_text = _normalize_preserving_lines(input_text)

    if not normalized_text:
        return []

    fragments = re.split(
        r"(?<=[.!?…])\s+|\n+",
        normalized_text,
    )

    return [fragment.strip() for fragment in fragments if fragment.strip()]


def extract_claim_like_units(input_text: str) -> dict[str, Any]:
    """Extract deterministic bounded claim-like units from one input text."""

    fragments = _split_candidate_fragments(input_text)

    claim_like_units = [
        {
            "unit_id": f"clu-{index:03d}",
            "text": fragment,
            "sequence_index": index - 1,
            "unit_type": UNIT_TYPE,
            "extraction_status": EXTRACTION_STATUS,
            "uncertainty_note": UNIT_UNCERTAINTY_NOTE,
        }
        for index, fragment in enumerate(fragments, start=1)
    ]

    status = (
        CLAIM_LIKE_UNITS_STATUS
        if claim_like_units
        else NO_CLAIM_LIKE_UNITS_STATUS
    )

    return {
        "claim_like_units_status": status,
        "claim_like_units": claim_like_units,
        "limitations": list(LIMITATIONS),
    }


__all__ = [
    "CLAIM_LIKE_UNITS_STATUS",
    "EXTRACTION_STATUS",
    "LIMITATIONS",
    "NO_CLAIM_LIKE_UNITS_STATUS",
    "UNIT_TYPE",
    "UNIT_UNCERTAINTY_NOTE",
    "extract_claim_like_units",
]
