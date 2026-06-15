from cognitive_shield.app.local_runner import (
    RUNNER_MODE,
    RUNNER_STATUS,
    default_example_input_path,
    run_default_local_prototype,
)


def test_default_example_input_path_exists() -> None:
    assert default_example_input_path().exists()


def test_run_default_local_prototype_returns_structured_output() -> None:
    result = run_default_local_prototype()

    assert result["runner_status"] == RUNNER_STATUS
    assert result["runner_mode"] == RUNNER_MODE
    assert result["input_source"] == "examples/single_message_inputs/minimal_message.json"

    engine_output = result["engine_output"]

    assert engine_output["example_input_id"] == "minimal-message-001"
    assert engine_output["example_input_type"] == "single_message"
    assert engine_output["example_loader_status"] == "loaded_single_message_example"

    engine_result = engine_output["engine_result"]

    assert engine_result["engine_stage"] == "functional_local_prototype_engine_entry"
    assert engine_result["runtime_mode"] == "local_bounded_prototype"
    assert engine_result["analysis_status"] == "not_implemented"
    assert engine_result["risk_status"] == "not_evaluated"
    assert engine_result["confidence_status"] == "not_computed"
    assert engine_result["verdict_status"] == "not_produced"

    assert "risk_score" not in engine_result
    assert "confidence" not in engine_result
    assert "verdict" not in engine_result
