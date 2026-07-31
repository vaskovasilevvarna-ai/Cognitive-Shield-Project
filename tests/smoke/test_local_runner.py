from pathlib import Path

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

    expected_input_source = (
        Path("examples") / "single_message_inputs" / "minimal_message.json"
    )
    assert Path(result["input_source"]) == expected_input_source

    engine_output = result["engine_output"]

    assert engine_output["example_input_id"] == "minimal-message-001"
    assert engine_output["example_input_type"] == "single_message"
    assert engine_output["example_loader_status"] == "loaded_single_message_example"

    engine_result = engine_output["engine_result"]

    assert engine_result["engine_stage"] == "functional_local_prototype_engine_entry"
    assert engine_result["runtime_mode"] == "local_bounded_prototype"

    assert (
        engine_result["processing_status"]
        == "bounded_mvp_functional_proof_completed"
    )

    assert engine_result["decomposition_result_status"] == "decomposition_result_created"
    assert engine_result["cmo_status"] == "bounded_cmo_construction_created"
    assert engine_result["acp_boundary_status"] == "eligible_for_acp_boundary"
    assert engine_result["routing_result_status"] == "route_ready_no_dispatch"

    assert (
        engine_result["analysis_envelope_status"]
        == "bounded_analysis_envelope_ready"
    )
    assert engine_result["risk_envelope_status"] == "bounded_risk_envelope_ready"
    assert (
        engine_result["confidence_envelope_status"]
        == "bounded_confidence_envelope_ready"
    )
    assert (
        engine_result["decision_envelope_status"]
        == "bounded_decision_envelope_ready"
    )

    assert engine_result["analysis_status"] == "not_implemented"
    assert engine_result["risk_status"] == "not_evaluated"
    assert engine_result["confidence_status"] == "not_computed"
    assert engine_result["verdict_status"] == "not_produced"

    assert "risk_score" not in engine_result
    assert "risk_level" not in engine_result
    assert "confidence" not in engine_result
    assert "confidence_score" not in engine_result
    assert "verdict" not in engine_result
    assert "shield_decision" not in engine_result
    assert "taxonomy_labels" not in engine_result



