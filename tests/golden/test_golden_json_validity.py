"""
Golden JSON validity shell test for Sprint 0.
"""

import json
from pathlib import Path


def test_clean_golden_output_is_valid_json() -> None:
    """
    Verify that the clean golden output file exists and is valid JSON.
    """
    golden_path = Path("tests/golden/clean_message_expected_output.json")
    assert golden_path.exists()

    data = json.loads(golden_path.read_text(encoding="utf-8"))
    assert data["message_id"] == "fixture-clean-001"
