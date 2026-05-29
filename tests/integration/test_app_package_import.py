"""
App package import shell test for Sprint 0.
"""

from cognitive_shield import app


def test_app_package_import() -> None:
    """
    Verify that the app package can be imported.
    """
    assert app is not None
