import json

from cognitive_shield.app.command_wrapper import run_command_wrapper


def test_end_to_end_functional_local_prototype_path_completes() -> None:
    result = run_command_wrapper()

    assert result["command_status"] == "completed"
    assert result["command_mode"] == "minimal_local_command_wrapper"
    assert result["prototype_phase"] == "functional_local_prototype_engine"

    assert "execution_result" in result

    execution_result = result["execution_result"]
    assert execution_result["execution_status"] == "completed"
    assert execution_result["execution_mode"] == "local_python_entry"
    assert execution_result["prototype_phase"] == "functional_local_prototype_engine"

    assert "json_output" in execution_result
    assert isinstance(execution_result["json_output"], str)

    parsed_json_output = json.loads(execution_result["json_output"])

    assert parsed_json_output["json_output_status"] == "rendered"
    assert parsed_json_output["json_output_format"] == "json"
    assert parsed_json_output["json_output_format_version"] == "0.1"

    assert "structured_output" in parsed_json_output

    structured_output = parsed_json_output["structured_output"]
    assert structured_output["output_status"] == "created"
    assert structured_output["output_format_version"] == "0.1"
    assert structured_output["prototype_phase"] == "functional_local_prototype_engine"

    assert "runner_output" in structured_output

    runner_output = structured_output["runner_output"]
    assert runner_output["runner_status"] == "completed"
    assert runner_output["runner_mode"] == "local_prototype"

    assert "engine_output" in runner_output

    engine_output = runner_output["engine_output"]
    assert engine_output["example_input_id"] == "minimal-message-001"
    assert engine_output["example_input_type"] == "single_message"

    assert "engine_result" in engine_output

    engine_result = engine_output["engine_result"]
    assert engine_result["analysis_status"] == "not_implemented"
    assert engine_result["risk_status"] == "not_evaluated"
    assert engine_result["confidence_status"] == "not_computed"
    assert engine_result["verdict_status"] == "not_produced"


def test_end_to_end_functional_local_prototype_preserves_no_verdict_invariants() -> None:
    result = run_command_wrapper()

    assert "risk_score" not in result
    assert "confidence" not in result
    assert "verdict" not in result

    execution_result = result["execution_result"]

    assert "risk_score" not in execution_result
    assert "confidence" not in execution_result
    assert "verdict" not in execution_result

    parsed_json_output = json.loads(execution_result["json_output"])

    assert "risk_score" not in parsed_json_output
    assert "confidence" not in parsed_json_output
    assert "verdict" not in parsed_json_output

    structured_output = parsed_json_output["structured_output"]

    assert "risk_score" not in structured_output
    assert "confidence" not in structured_output
    assert "verdict" not in structured_output

    runner_output = structured_output["runner_output"]

    assert "risk_score" not in runner_output
    assert "confidence" not in runner_output
    assert "verdict" not in runner_output

    engine_output = runner_output["engine_output"]

    assert "risk_score" not in engine_output
    assert "confidence" not in engine_output
    assert "verdict" not in engine_output

    engine_result = engine_output["engine_result"]

    assert "risk_score" not in engine_result
    assert "confidence" not in engine_result
    assert "verdict" not in engine_result

    assert engine_result["analysis_status"] == "not_implemented"
    assert engine_result["risk_status"] == "not_evaluated"
    assert engine_result["confidence_status"] == "not_computed"
    assert engine_result["verdict_status"] == "not_produced"
