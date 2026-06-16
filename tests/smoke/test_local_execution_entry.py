import json

from cognitive_shield.app.local_execution_entry import (
    EXECUTION_MODE,
    EXECUTION_STATUS,
    PROTOTYPE_PHASE,
    run_local_execution_entry,
)


def test_run_local_execution_entry_returns_bounded_execution_result() -> None:
    result = run_local_execution_entry()

    assert result["execution_status"] == EXECUTION_STATUS
    assert result["execution_mode"] == EXECUTION_MODE
    assert result["prototype_phase"] == PROTOTYPE_PHASE

    assert "json_output" in result
    assert isinstance(result["json_output"], str)

    parsed_json_output = json.loads(result["json_output"])

    assert parsed_json_output["json_output_status"] == "rendered"
    assert parsed_json_output["json_output_format"] == "json"
    assert parsed_json_output["json_output_format_version"] == "0.1"

    assert "structured_output" in parsed_json_output

    structured_output = parsed_json_output["structured_output"]
    assert structured_output["output_status"] == "created"
    assert structured_output["output_format_version"] == "0.1"
    assert structured_output["prototype_phase"] == "functional_local_prototype_engine"

    assert "runner_output" in structured_output


def test_local_execution_entry_preserves_no_verdict_invariants() -> None:
    result = run_local_execution_entry()

    assert "risk_score" not in result
    assert "confidence" not in result
    assert "verdict" not in result

    parsed_json_output = json.loads(result["json_output"])

    assert "risk_score" not in parsed_json_output
    assert "confidence" not in parsed_json_output
    assert "verdict" not in parsed_json_output

    structured_output = parsed_json_output["structured_output"]

    assert "risk_score" not in structured_output
    assert "confidence" not in structured_output
    assert "verdict" not in structured_output

    runner_output = structured_output["runner_output"]
    engine_output = runner_output["engine_output"]
    engine_result = engine_output["engine_result"]

    assert engine_result["analysis_status"] == "not_implemented"
    assert engine_result["risk_status"] == "not_evaluated"
    assert engine_result["confidence_status"] == "not_computed"
    assert engine_result["verdict_status"] == "not_produced"

    assert "risk_score" not in engine_result
    assert "confidence" not in engine_result
    assert "verdict" not in engine_result
