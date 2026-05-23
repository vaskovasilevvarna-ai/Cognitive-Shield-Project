"""
MDS explicit claim candidate boundary for Cognitive Shield.

This module provides a minimal explicit claim candidate behavior.

It identifies explicit claim candidates from existing surface units without
performing full claim extraction, implicit inference, truth assessment, evidence
assessment, framing extraction, relation inference, DecompositionResult
construction, CMO construction, ACP routing, Analysis generation, runtime
pipeline execution, or downstream pipeline logic.
"""

from cognitive_shield.core.message_decomposition_specification_mds.surface_preparation import (
    MDS_STAGE,
)

CLAIM_CANDIDATE_TYPE = "explicit_claim_candidate"


def _is_explicit_claim_candidate_text(source_text: str) -> bool:
    """
    Check whether surface text is a shallow explicit claim candidate.

    This is a minimal textual boundary check only. It does not assess truth,
    infer hidden meaning, evaluate evidence, classify framing, or extract
    relations.
    """
    stripped_text = source_text.strip()

    if not stripped_text:
        return False

    return stripped_text.endswith(".")


def build_explicit_claim_candidates(
    surface_units: list[dict[str, str]],
) -> dict[str, object]:
    """
    Build explicit claim candidates from surface units.

    This function preserves source surface unit identity and source text. It
    creates candidate-only records and does not produce confirmed claim units.
    """
    claim_candidates = []

    for index, surface_unit in enumerate(surface_units, start=1):
        source_text = surface_unit.get("source_text", "")
        source_surface_unit_id = surface_unit.get("surface_unit_id", "")

        if not _is_explicit_claim_candidate_text(source_text):
            continue

        claim_candidates.append(
            {
                "claim_candidate_id": f"claim-candidate-{index:03d}",
                "source_surface_unit_id": source_surface_unit_id,
                "source_text": source_text,
                "candidate_type": CLAIM_CANDIDATE_TYPE,
                "candidate_status": "claim_candidate_created",
                "order_index": str(index),
            }
        )

    candidate_status = (
        "claim_candidate_created"
        if claim_candidates
        else "not_claim_candidate"
    )

    return {
        "mds_stage": MDS_STAGE,
        "candidate_status": candidate_status,
        "claim_candidates": claim_candidates,
    }


__all__ = [
    "CLAIM_CANDIDATE_TYPE",
    "build_explicit_claim_candidates",
]
