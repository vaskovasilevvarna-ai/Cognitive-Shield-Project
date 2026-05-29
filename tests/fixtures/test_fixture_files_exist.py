"""
Fixture file presence shell test for Sprint 0.
"""

from pathlib import Path


def test_fixture_files_exist() -> None:
    """
    Verify that the initial fixture files are present.
    """
    fixture_dir = Path("tests/fixtures")

    expected_files = [
        "clean_message.json",
        "mixed_signal_message.json",
        "ambiguity_heavy_message.json",
    ]

    for filename in expected_files:
        assert (fixture_dir / filename).exists()
