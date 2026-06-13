from cognitive_shield.app.functional_local_engine import (
    ENGINE_STAGE,
    RUNTIME_MODE,
    run_functional_local_engine,
)


def test_functional_local_engine_returns_bounded_structured_output() -> None:
    result = run_functional_local_engine("This is a controlled prototype input.")

    assert isinstance(result, dict)

    assert result["engine_stage"] == ENGINE_STAGE
    assert result["runtime_mode"] == RUNTIME_MODE
    assert result["engine_status"] == "functional_local_engine_entry_created"

    assert result["analysis_status"] == "not_implemented"
    assert result["risk_status"] == "not_evaluated"
    assert result["confidence_status"] == "not_computed"
    assert result["verdict_status"] == "not_produced"

    assert "risk_score" not in result
    assert "confidence" not in result
    assert "verdict" not in result

    assert isinstance(result["proof_result"], dict)
