from cognitive_shield.app.structured_output import (
    OUTPUT_FORMAT_VERSION,
    OUTPUT_STATUS,
    PROTOTYPE_PHASE,
    build_structured_output,
)


def test_build_structured_output_returns_bounded_output_envelope() -> None:
    result = build_structured_output()

    assert result["output_status"] == OUTPUT_STATUS
    assert result["output_format_version"] == OUTPUT_FORMAT_VERSION
    assert result["prototype_phase"] == PROTOTYPE_PHASE

    assert "runner_output" in result

    runner_output = result["runner_output"]
    assert runner_output["runner_status"] == "completed"
    assert runner_output["runner_mode"] == "local_prototype"

    engine_output = runner_output["engine_output"]
    assert engine_output["example_input_id"] == "minimal-message-001"
    assert engine_output["example_input_type"] == "single_message"

    engine_result = engine_output["engine_result"]
    assert engine_result["analysis_status"] == "not_implemented"
    assert engine_result["risk_status"] == "not_evaluated"
    assert engine_result["confidence_status"] == "not_computed"
    assert engine_result["verdict_status"] == "not_produced"

    assert "risk_score" not in result
    assert "confidence" not in result
    assert "verdict" not in result
