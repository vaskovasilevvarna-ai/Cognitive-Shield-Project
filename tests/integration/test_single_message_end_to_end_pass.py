"""
Integration shell test for the single-message end-to-end analytical pass.
"""

from cognitive_shield.app.single_message_pass.pipeline import run_pipeline


def test_single_message_end_to_end_pass_shell() -> None:
    """
    Sprint 0 shell test.

    This test only verifies that the minimal pipeline entry point is callable.
    """
    result = run_pipeline()
    assert result is None
