"""
MDS explicit claim unit boundary for Cognitive Shield.

This module provides a minimal explicit claim unit behavior.

It converts existing explicit claim candidates into structural claim units
without performing implicit inference, hidden claim reconstruction, truth
assessment, evidence assessment, framing extraction, relation inference,
DecompositionResult construction, CMO construction, ACP routing, Analysis
generation, runtime pipeline execution, or downstream pipeline logic.
"""

from cognitive_shield.core.message_decomposition_specification_mds.claim_candidates import (
    CLAIM_CANDIDATE_TYPE,
)
from cognitive_shield.core.message_decomposition_specification_mds.surface_preparation import (
    MDS_STAGE,
)

EXPLICIT_CLAIM_UNIT_TYPE = "explicit_claim_unit"


def build_explicit_claim_units(
    claim_candidates: list[dict[str, str]],
) -> dict[str, object]:
    """
    Build explicit claim units from explicit claim candidates.

    This function preserves source claim candidate identity, source surface unit
    identity, and source text. It creates structural claim unit records only.
    It does not assess truth, evaluate evidence, infer hidden claims, extract
    relations, or construct a DecompositionResult.
    """
    claim_units = []

    for index, claim_candidate in enumerate(claim_candidates, start=1):
        if claim_candidate.get("candidate_type") != CLAIM_CANDIDATE_TYPE:
            continue

        if claim_candidate.get("candidate_status") != "claim_candidate_created":
            continue

        source_text = claim_candidate.get("source_text", "").strip()

        if not source_text:
            continue

        claim_units.append(
            {
                "claim_unit_id": f"claim-unit-{index:03d}",
                "source_claim_candidate_id": claim_candidate.get(
                    "claim_candidate_id",
                    "",
                ),
                "source_surface_unit_id": claim_candidate.get(
                    "source_surface_unit_id",
                    "",
                ),
                "source_text": claim_candidate.get("source_text", ""),
                "unit_type": EXPLICIT_CLAIM_UNIT_TYPE,
                "claim_unit_status": "claim_unit_created",
                "order_index": claim_candidate.get("order_index", str(index)),
            }
        )

    claim_unit_status = "claim_unit_created" if claim_units else "not_claim_unit"

    return {
        "mds_stage": MDS_STAGE,
        "claim_unit_status": claim_unit_status,
        "claim_units": claim_units,
    }


__all__ = [
    "EXPLICIT_CLAIM_UNIT_TYPE",
    "build_explicit_claim_units",
]
