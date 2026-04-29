"""
Shared contracts package import shell test for Sprint 0.
"""

from cognitive_shield.shared import contracts


def test_shared_contracts_package_import() -> None:
    """
    Verify that the shared contracts package can be imported.
    """
    assert contracts is not None
