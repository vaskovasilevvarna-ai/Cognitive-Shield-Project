"""
Dependencies module import shell test for Sprint 0.
"""

from cognitive_shield.app.single_message_pass import dependencies


def test_dependencies_module_import() -> None:
    """
    Verify that the dependencies module can be imported.
    """
    assert dependencies is not None
