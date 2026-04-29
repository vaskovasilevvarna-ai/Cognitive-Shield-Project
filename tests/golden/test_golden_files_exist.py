"""
Golden file presence shell test for Sprint 0.
"""

from pathlib import Path


def test_golden_files_exist() -> None:
    """
    Verify that the initial golden files are present.
    """
    golden_dir = Path("tests/golden")

    expected_files = [
        "clean_message_expected_output.json",
        "mixed_signal_expected_output.json",
        "ambiguity_heavy_expected_output.json",
    ]

    for filename in expected_files:
        assert (golden_dir / filename).exists()
