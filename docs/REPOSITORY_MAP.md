# Repository Map

## Purpose
This document defines the repository structure for the bounded MVP implementation.

The repository must reflect the architecture, not future product polish.

## Top-level tree

```text
cognitive-shield/
├── README.md
├── LICENSE
├── pyproject.toml
├── requirements.txt
├── .gitignore
├── .editorconfig
├── pytest.ini
├── Makefile
├── docs/
│   ├── architecture/
│   ├── sprint-0/
│   ├── contracts/
│   ├── testing/
│   └── repo-governance/
├── src/
│   └── cognitive_shield/
│       ├── shared/
│       │   ├── types/
│       │   ├── contracts/
│       │   ├── schemas/
│       │   ├── errors/
│       │   ├── constants/
│       │   └── utils/
│       ├── core/
│       │   ├── message_decomposition_specification_mds/
│       │   ├── canonical_message_object_cmo/
│       │   ├── agent_communication_protocol_acp/
│       │   ├── taxonomy/
│       │   ├── taxonomy_to_risk_mapping/
│       │   ├── risk_scoring_model/
│       │   ├── confidence_uncertainty_model/
│       │   ├── internal_arbiter_ia/
│       │   ├── decision_policy_layer_dpl/
│       │   └── shield_decision_sd/
│       ├── output/
│       │   ├── canonical_output_schema_cos/
│       │   ├── uncertainty_conflict_visualization_grammar_ucvg/
│       │   ├── output_orchestrator/
│       │   └── explainable_interface/
│       ├── education/
│       │   ├── education_safety_envelope_layer/
│       │   ├── cognitive_defense_training_model_cdtm/
│       │   └── training_shell/
│       └── app/
│           └── single_message_pass/
├── tests/
│   ├── unit/
│   ├── contract/
│   ├── integration/
│   ├── fixtures/
│   └── golden/
├── scripts/
└── examples/
