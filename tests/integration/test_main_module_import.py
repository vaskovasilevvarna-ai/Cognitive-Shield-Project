"""
Main module import shell test for Sprint 0.
"""

from cognitive_shield.app.single_message_pass import __main__


def test_main_module_import() -> None:
    """
    Verify that the __main__ module can be imported.
    """
    assert __main__ is not None
