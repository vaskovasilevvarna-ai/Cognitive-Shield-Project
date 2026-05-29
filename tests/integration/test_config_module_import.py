"""
Config module import shell test for Sprint 0.
"""

from cognitive_shield.app.single_message_pass import config


def test_config_module_import() -> None:
    """
    Verify that the config module can be imported.
    """
    assert config is not None
