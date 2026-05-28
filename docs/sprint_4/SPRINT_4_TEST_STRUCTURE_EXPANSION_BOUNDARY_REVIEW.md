# Sprint 4 Test Structure Expansion Boundary Review

Status: Boundary review — before admitting Sprint 4 test-structure expansion.

## Purpose

This document records the Sprint 4 boundary review for expanding the repository test structure in support of MVP functional proof.

Sprint 4 has already established that workflow expansion is required for MVP proof.

The purpose of this document is to decide whether the project may admit a bounded test-structure expansion pass, including a smoke-test area and supporting documentation, without yet implementing MVP proof logic, real routing, dispatch, Analysis generation, runtime pipeline execution, or downstream pipeline logic.

This document does not admit MVP proof implementation by itself.

This document does not admit real ACP routing.

This document does not admit ACPMessage dispatch, agent routing, agent orchestration, Analysis generation, taxonomy behavior, risk scoring, governance behavior, output rendering, runtime pipeline execution, or downstream pipeline logic.

## Baseline

Sprint 3 closed with boundaries.

Sprint 3 delivered the following controlled ACP chain:

ACP boundary eligibility  
→ ACP minimal envelope  
→ ACPBundle  
→ ACPMessage  
→ ACP Schema Validator  
→ ACP Scope Guard  
→ Protocol Router readiness  
→ Routing Preparation Gate

Sprint 4 has completed:

- Sprint 4 Entry Control Pass
- Sprint 4 MVP Completion Control Review
- Sprint 4 Routing Preparation Review
- Sprint 4 Workflow Expansion Review

Current validation status:

- Python Tests workflow: GREEN
- Sprint 4 strategic objective: MVP completion with functional proof
- Workflow expansion: REQUIRED FOR SPRINT 4 MVP PROOF
- Smoke tests: REQUIRED
- No-dispatch regression tests: REQUIRED
- No-agent-instruction regression tests: REQUIRED
- No-analysis-generation regression tests: REQUIRED
- No-runtime-execution regression tests: REQUIRED
- No-forbidden-field regression tests: REQUIRED
- Real ACP routing: NOT ADMITTED
- Routing implementation: HOLD
- ACPMessage dispatch: HOLD
- Analysis generation: HOLD
- runtime pipeline execution: NOT ADMITTED
- downstream pipeline logic: NOT ADMITTED
- merge to `main`: NOT PERFORMED

## Boundary Question

Can the project admit a bounded test-structure expansion pass for Sprint 4 MVP proof?

## Verdict

Verdict:

`ADMIT TEST STRUCTURE EXPANSION WITH HARD SAFEGUARDS`

Sprint 4 may admit a bounded test-structure expansion pass.

The pass may create a smoke-test area and supporting README documentation.

The pass may prepare the repository for future MVP proof tests.

The pass must not implement MVP proof logic yet.

The pass must not implement routing.

The pass must not change runtime behavior.

The pass must not edit production source modules.

## Admitted Future Scope

The future test-structure expansion implementation may include only:

- creating `tests/smoke/README.md`;
- creating `tests/smoke/__init__.py`;
- optionally updating or confirming `tests/contract/README.md`;
- documenting the role of smoke tests;
- documenting the role of no-forbidden-field regression tests;
- documenting that smoke tests must remain non-dispatching, non-analytical, and non-runtime;
- preserving the current Python Tests workflow behavior;
- verifying that Python Tests workflow remains GREEN after the test-structure expansion.

This boundary admits test scaffolding only.

It does not admit proof behavior.

## Preferred Files

Recommended files for the next compressed pass:

- `tests/smoke/README.md`
- `tests/smoke/__init__.py`
- `docs/sprint_4/SPRINT_4_TEST_STRUCTURE_EXPANSION_PASS_CLOSURE_NOTE.md`

Optional later file, not required in the first pass:

- `tests/contract/README.md` update

The first pass should stay small.

## Not Admitted

The following remain not admitted by this document:

- MVP functional proof implementation;
- MVP smoke test implementation;
- real ACP routing;
- routing decision creation;
- route selection;
- dispatch target creation;
- agent instruction creation;
- agent selection;
- route table behavior;
- dynamic protocol routing;
- ACPMessage dispatch;
- agent routing;
- agent orchestration;
- Contradiction Registrar behavior;
- Uncertainty Propagator behavior;
- Synthesis Exporter behavior;
- Analysis generation;
- EvidenceAnalysisOutput generation;
- NarrativeAnalysisOutput generation;
- CognitiveAnalysisOutput generation;
- Analysis bundle generation;
- taxonomy behavior;
- label-to-verdict logic;
- risk scoring;
- confidence or uncertainty evaluation;
- governance behavior;
- output rendering;
- runtime pipeline execution;
- downstream pipeline logic;
- merge to `main`.

Also still not admitted:

- implicit claim inference;
- hidden claim reconstruction;
- truth assessment;
- evidence assessment;
- framing extraction;
- relation inference;
- semantic interpretation beyond admitted MDS-local, CMO-local, and ACP structural containers.

## Smoke Test Area Definition

The `tests/smoke/` area should be reserved for proof-level tests that verify bounded end-to-end behavior across admitted modules.

Smoke tests may later verify:

- admitted chain connectivity;
- expected status transitions;
- preservation of `decomposition_result`;
- preservation of `field_envelope`;
- absence of forbidden routing / dispatch / Analysis / runtime fields;
- local reproducibility of MVP proof behavior.

Smoke tests must not:

- create real routing behavior;
- dispatch ACPMessages;
- create agent instructions;
- call Analysis modules;
- call taxonomy modules;
- call risk scoring modules;
- call governance modules;
- render output;
- trigger runtime pipeline execution;
- introduce downstream pipeline logic.

## No-Forbidden-Field Regression Role

Sprint 4 requires explicit no-forbidden-field discipline.

Future smoke or contract tests should check that MVP proof objects do not expose forbidden fields such as:

- `routing_decision`
- `agent_route`
- `dispatch_target`
- `agent_id`
- `selected_agent`
- `agent_instruction`
- `route_table`
- `analysis_bundle`
- `evidence_analysis_output`
- `narrative_analysis_output`
- `cognitive_analysis_output`
- `taxonomy_labels`
- `risk_profile`
- `governance_signal`
- `output_payload`
- `runtime_pipeline`
- `runtime_event`
- `downstream_pipeline`
- `pipeline_dispatch`

The first test-structure pass may document this requirement without implementing the regression tests yet.

## Workflow Relationship

The current `.github/workflows/python-tests.yml` remains active.

This boundary does not require workflow YAML changes by itself.

After `tests/smoke/` is created, the next workflow check must confirm whether the current workflow discovers smoke tests automatically.

If the workflow already runs all tests through a command such as `pytest` or `python -m pytest`, then no workflow YAML change may be needed.

If the workflow only runs `tests/unit/`, then a later workflow update pass will be required.

## Required Safeguards

The test-structure expansion pass must preserve the following safeguards:

1. Do not edit production source modules.
2. Do not implement MVP proof logic yet.
3. Do not implement routing.
4. Do not edit `router.py`.
5. Do not create dispatch targets.
6. Do not create agent instructions.
7. Do not generate Analysis.
8. Do not trigger runtime pipeline execution.
9. Do not introduce downstream pipeline logic.
10. Keep the pass documentation-only plus test-folder scaffold.
11. Keep Python Tests workflow GREEN.
12. Add a closure note after the pass.

## Candidate Commit Scope

The next implementation pass should be small and repository-structural.

Expected commit scope:

- add `tests/smoke/README.md`;
- add `tests/smoke/__init__.py`;
- add Sprint 4 closure note for the test-structure expansion pass.

No Python behavior should be added in this pass.

No MVP smoke test should be added in this pass unless separately admitted later.

## Recommended Next Step

Recommended next step:

If this review is accepted, create the test-structure expansion pass in compressed mode:

1. smoke README;
2. smoke package marker;
3. closure note.

Recommended files:

- `tests/smoke/README.md`
- `tests/smoke/__init__.py`
- `docs/sprint_4/SPRINT_4_TEST_STRUCTURE_EXPANSION_PASS_CLOSURE_NOTE.md`

## Future Follow-Up Documents

After this pass, recommended next documents include:

- `docs/sprint_4/SPRINT_4_WORKFLOW_DISCOVERY_CHECK.md`
- `docs/sprint_4/SPRINT_4_REAL_ROUTING_BOUNDARY_REVIEW.md`
- `docs/sprint_4/SPRINT_4_MVP_FUNCTIONAL_PROOF_PLAN.md`

The workflow discovery check should decide whether `.github/workflows/python-tests.yml` needs editing after `tests/smoke/` exists.

## No-Drift Confirmation

Confirmed:

- Sprint 3 closure state remains preserved.
- Sprint 4 remains controlled.
- Sprint 4 objective remains MVP completion with functional proof.
- Test-structure expansion is admitted only as scaffolding.
- MVP proof implementation is not admitted by this document.
- Real ACP routing remains on HOLD.
- Routing implementation remains on HOLD.
- Routing decision creation remains on HOLD.
- Dispatch target creation remains on HOLD.
- Agent instruction creation remains on HOLD.
- ACPMessage dispatch remains on HOLD.
- Analysis generation remains on HOLD.
- Taxonomy behavior has not started.
- Risk scoring has not started.
- Governance behavior has not started.
- Output rendering has not started.
- Runtime pipeline execution remains not admitted.
- Downstream pipeline logic remains not admitted.
- Merge to `main` has not been performed.

## Verdict Summary

Sprint 4 Test Structure Expansion Boundary Review: COMPLETE.

Test-structure expansion: ADMITTED WITH HARD SAFEGUARDS.

Smoke test area: ADMITTED AS SCAFFOLD.

MVP smoke test implementation: HOLD.

MVP functional proof implementation: HOLD.

Workflow YAML update: HOLD until workflow discovery check.

Real ACP routing: NOT ADMITTED BY THIS DOCUMENT.

Routing implementation: HOLD.

Analysis generation: HOLD.

Runtime pipeline execution: NOT ADMITTED.

Downstream pipeline logic: NOT ADMITTED.

Recommended next pass:

- test-structure expansion compressed pass.
