"""
Fixture loading shell test for Sprint 0.
"""

import json
from pathlib import Path


def test_clean_fixture_exists_and_is_valid_json() -> None:
    """
    Verify that the clean fixture exists and can be parsed as JSON.
    """
    fixture_path = Path("tests/fixtures/clean_message.json")
    assert fixture_path.exists()

    data = json.loads(fixture_path.read_text(encoding="utf-8"))
    assert data["message_id"] == "fixture-clean-001"
