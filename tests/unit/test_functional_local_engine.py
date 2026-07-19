from cognitive_shield.app.functional_local_engine import (
    ENGINE_STAGE,
    RUNTIME_MODE,
    run_functional_local_engine,
)


def test_run_functional_local_engine_returns_bounded_engine_envelope() -> None:
    result = run_functional_local_engine("Bounded local prototype test input.")

    assert result["engine_stage"] == ENGINE_STAGE
    assert result["runtime_mode"] == RUNTIME_MODE
    assert result["engine_status"] == "functional_local_engine_entry_created"

    assert result["input_status"] == "input_received"
    assert result["mvp_proof_status"] == "mvp_functional_proof_created"

    assert result["analysis_status"] == "not_implemented"
    assert result["risk_status"] == "not_evaluated"
    assert result["confidence_status"] == "not_computed"
    assert result["verdict_status"] == "not_produced"

    proof_result = result["proof_result"]

    assert proof_result["mvp_proof_status"] == "mvp_functional_proof_created"
    assert proof_result["input_status"] == "input_received"
    assert proof_result["decomposition_result_status"] == "decomposition_result_created"
    assert proof_result["cmo_status"] == "bounded_cmo_construction_created"
    assert proof_result["acp_boundary_status"] == "eligible_for_acp_boundary"
    assert proof_result["routing_result_status"] == "route_ready_no_dispatch"


def test_run_functional_local_engine_does_not_claim_downstream_decisions() -> None:
    result = run_functional_local_engine("Bounded local prototype test input.")

    assert "risk_score" not in result
    assert "confidence" not in result
    assert "verdict" not in result

    proof_result = result["proof_result"]

    assert "risk_score" not in proof_result
    assert "confidence" not in proof_result
    assert "verdict" not in proof_result
