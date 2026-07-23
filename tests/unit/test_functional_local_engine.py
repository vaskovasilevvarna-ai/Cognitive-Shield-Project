from cognitive_shield.app.functional_local_engine import (
    ENGINE_STAGE,
    PROCESSING_STATUS,
    RUNTIME_MODE,
    run_functional_local_engine,
)


EXPECTED_ENGINE_RESULT_KEYS = {
    "engine_stage",
    "runtime_mode",
    "engine_status",
    "processing_status",
    "input_status",
    "mvp_proof_status",
    "decomposition_result_status",
    "cmo_status",
    "acp_boundary_status",
    "routing_result_status",
    "analysis_status",
    "risk_status",
    "confidence_status",
    "verdict_status",
    "proof_result",
}

FORBIDDEN_DOWNSTREAM_KEYS = {
    "risk_score",
    "confidence",
    "verdict",
    "shield_decision",
    "taxonomy_labels",
    "evidence_analysis",
    "narrative_analysis",
    "cognitive_analysis",
}


def test_run_functional_local_engine_returns_expected_top_level_contract() -> None:
    result = run_functional_local_engine("Bounded local prototype test input.")

    assert set(result) == EXPECTED_ENGINE_RESULT_KEYS


def test_run_functional_local_engine_returns_bounded_engine_envelope() -> None:
    result = run_functional_local_engine("Bounded local prototype test input.")

    assert result["engine_stage"] == ENGINE_STAGE
    assert result["runtime_mode"] == RUNTIME_MODE
    assert result["engine_status"] == "functional_local_engine_entry_created"
    assert result["processing_status"] == PROCESSING_STATUS

    assert result["input_status"] == "input_received"
    assert result["mvp_proof_status"] == "mvp_functional_proof_created"
    assert result["decomposition_result_status"] == "decomposition_result_created"
    assert result["cmo_status"] == "bounded_cmo_construction_created"
    assert result["acp_boundary_status"] == "eligible_for_acp_boundary"
    assert result["routing_result_status"] == "route_ready_no_dispatch"

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

    for key in FORBIDDEN_DOWNSTREAM_KEYS:
        assert key not in result

    proof_result = result["proof_result"]

    for key in FORBIDDEN_DOWNSTREAM_KEYS:
        assert key not in proof_result

  
