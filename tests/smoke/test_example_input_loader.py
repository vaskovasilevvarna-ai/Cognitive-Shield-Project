from pathlib import Path

from cognitive_shield.app.example_input_loader import (
    EXPECTED_INPUT_TYPE,
    load_single_message_example,
    run_engine_from_example,
)


REPO_ROOT = Path(__file__).resolve().parents[2]
EXAMPLE_PATH = REPO_ROOT / "examples" / "single_message_inputs" / "minimal_message.json"


def test_load_single_message_example_reads_controlled_fixture() -> None:
    payload = load_single_message_example(EXAMPLE_PATH)

    assert payload["id"] == "minimal-message-001"
    assert payload["language"] == "en"
    assert payload["input_type"] == EXPECTED_INPUT_TYPE
    assert isinstance(payload["content"], str)
    assert payload["content"].strip()


def test_run_engine_from_example_returns_bounded_structured_output() -> None:
    result = run_engine_from_example(EXAMPLE_PATH)

    assert result["example_input_id"] == "minimal-message-001"
    assert result["example_language"] == "en"
    assert result["example_input_type"] == EXPECTED_INPUT_TYPE
    assert result["example_loader_status"] == "loaded_single_message_example"

    engine_result = result["engine_result"]

    assert engine_result["engine_stage"] == "functional_local_prototype_engine_entry"
    assert engine_result["runtime_mode"] == "local_bounded_prototype"
    assert engine_result["analysis_status"] == "not_implemented"
    assert engine_result["risk_status"] == "not_evaluated"
    assert engine_result["confidence_status"] == "not_computed"
    assert engine_result["verdict_status"] == "not_produced"

    assert "risk_score" not in engine_result
    assert "confidence" not in engine_result
    assert "verdict" not in engine_result
