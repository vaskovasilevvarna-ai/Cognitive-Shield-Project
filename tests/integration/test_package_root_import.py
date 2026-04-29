"""
Package root import shell test for Sprint 0.
"""

import cognitive_shield


def test_package_root_import() -> None:
    """
    Verify that the package root can be imported.
    """
    assert cognitive_shield is not None
