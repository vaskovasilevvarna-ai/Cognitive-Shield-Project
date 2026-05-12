"""
Minimal Evidence analysis scaffold for Cognitive Shield.

This module is a Sprint 1 bounded scaffold. It does not implement real evidence
analysis, source evaluation, taxonomy behavior, risk scoring, governance
behavior, or downstream pipeline logic.
"""

from cognitive_shield.core.analysis.contracts import EvidenceAnalysisOutput


def build_evidence_preview(output: EvidenceAnalysisOutput) -> dict[str, str]:
    """
    Build a minimal evidence analysis preview.

    This is a scaffold-level helper only. It does not evaluate evidence,
    score sources, classify claims, apply taxonomy labels, compute risk,
    or execute downstream analysis.
    """
    return {
        "message_id": output.message_id,
        "analysis_type": "evidence",
        "analysis_status": "preview_only",
    }


__all__ = [
    "build_evidence_preview",
]
