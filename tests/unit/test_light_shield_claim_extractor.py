from cognitive_shield.app.light_shield_claim_extractor import (
    CLAIM_LIKE_UNITS_STATUS,
    EXTRACTION_STATUS,
    NO_CLAIM_LIKE_UNITS_STATUS,
    UNIT_TYPE,
    UNIT_UNCERTAINTY_NOTE,
    extract_claim_like_units,
)


FORBIDDEN_KEYS = {
    "risk_score",
    "confidence_score",
    "verdict",
    "shield_decision",
    "truth_value",
    "is_true",
    "is_false",
    "taxonomy_labels",
    "warning_signals",
}


def test_extract_claim_like_units_from_single_sentence() -> None:
    result = extract_claim_like_units("Public institutions should explain this claim.")

    assert result["claim_like_units_status"] == CLAIM_LIKE_UNITS_STATUS
    assert len(result["claim_like_units"]) == 1

    unit = result["claim_like_units"][0]

    assert unit["unit_id"] == "clu-001"
    assert unit["text"] == "Public institutions should explain this claim."
    assert unit["sequence_index"] == 0
    assert unit["unit_type"] == UNIT_TYPE
    assert unit["extraction_status"] == EXTRACTION_STATUS
    assert unit["uncertainty_note"] == UNIT_UNCERTAINTY_NOTE


def test_extract_claim_like_units_preserves_multiple_sentence_order() -> None:
    result = extract_claim_like_units(
        "First candidate claim. Second candidate claim! Third candidate claim?"
    )

    units = result["claim_like_units"]

    assert [unit["unit_id"] for unit in units] == [
        "clu-001",
        "clu-002",
        "clu-003",
    ]
    assert [unit["sequence_index"] for unit in units] == [0, 1, 2]
    assert [unit["text"] for unit in units] == [
        "First candidate claim.",
        "Second candidate claim!",
        "Third candidate claim?",
    ]


def test_extract_claim_like_units_handles_newline_boundaries() -> None:
    result = extract_claim_like_units(
        "First line without terminal punctuation\n"
        "Second line with a claim.\n"
        "\n"
        "Third line."
    )

    units = result["claim_like_units"]

    assert [unit["text"] for unit in units] == [
        "First line without terminal punctuation",
        "Second line with a claim.",
        "Third line.",
    ]


def test_extract_claim_like_units_returns_controlled_empty_result() -> None:
    result = extract_claim_like_units("   \n\t   ")

    assert result["claim_like_units_status"] == NO_CLAIM_LIKE_UNITS_STATUS
    assert result["claim_like_units"] == []
    assert result["limitations"]


def test_extract_claim_like_units_exposes_explicit_limitations() -> None:
    result = extract_claim_like_units("Candidate claim.")

    assert len(result["limitations"]) >= 2
    assert any(
        "not semantic claim verification" in limitation
        for limitation in result["limitations"]
    )
    assert any(
        "truth, falsity" in limitation
        for limitation in result["limitations"]
    )


def test_extract_claim_like_units_does_not_claim_forbidden_judgments() -> None:
    result = extract_claim_like_units(
        "One candidate claim. Another candidate claim."
    )

    for key in FORBIDDEN_KEYS:
        assert key not in result

    for unit in result["claim_like_units"]:
        for key in FORBIDDEN_KEYS:
            assert key not in unit
