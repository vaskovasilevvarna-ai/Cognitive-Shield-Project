"""
Shared package import shell test for Sprint 0.
"""

from cognitive_shield import shared


def test_shared_package_import() -> None:
    """
    Verify that the shared package can be imported.
    """
    assert shared is not None
