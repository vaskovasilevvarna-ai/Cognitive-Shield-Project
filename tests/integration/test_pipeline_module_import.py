"""
Pipeline module import shell test for Sprint 0.
"""

from cognitive_shield.app.single_message_pass import pipeline


def test_pipeline_module_import() -> None:
    """
    Verify that the pipeline module can be imported.
    """
    assert pipeline is not None
