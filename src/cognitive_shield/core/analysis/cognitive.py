"""
Minimal Cognitive analysis scaffold for Cognitive Shield.

This module is a Sprint 1 bounded scaffold. It does not implement real cognitive
analysis, cognitive pressure detection, taxonomy behavior, risk scoring,
governance behavior, or downstream pipeline logic.
"""

from cognitive_shield.core.analysis.contracts import CognitiveAnalysisOutput


def build_cognitive_preview(output: CognitiveAnalysisOutput) -> dict[str, str]:
    """
    Build a minimal cognitive analysis preview.

    This is a scaffold-level helper only. It does not detect cognitive pressure,
    identify attention capture patterns, apply taxonomy labels, compute risk,
    or execute downstream analysis.
    """
    return {
        "message_id": output.message_id,
        "analysis_type": "cognitive",
        "analysis_status": "preview_only",
    }


__all__ = [
    "build_cognitive_preview",
]
