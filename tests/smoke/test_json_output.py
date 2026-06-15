import json

from cognitive_shield.app.json_output import (
    JSON_OUTPUT_FORMAT,
    JSON_OUTPUT_FORMAT_VERSION,
    JSON_OUTPUT_STATUS,
    build_json_output,
)


def test_build_json_output_returns_parseable_json_string() -> None:
    result = build_json_output()

    assert isinstance(result, str)

    parsed = json.loads(result)

    assert parsed["json_output_status"] == JSON_OUTPUT_STATUS
    assert parsed["json_output_format"] == JSON_OUTPUT_FORMAT
    assert parsed["json_output_format_version"] == JSON_OUTPUT_FORMAT_VERSION

    assert "structured_output" in parsed

    structured_output = parsed["structured_output"]
    assert structured_output["output_status"] == "created"
    assert structured_output["output_format_version"] == "0.1"
    assert structured_output["prototype_phase"] == "functional_local_prototype_engine"

    assert "runner_output" in structured_output


def test_json_output_preserves_bounded_no_verdict_invariants() -> None:
    result = build_json_output()
    parsed = json.loads(result)

    assert "risk_score" not in parsed
    assert "confidence" not in parsed
    assert "verdict" not in parsed

    structured_output = parsed["structured_output"]

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
