# Sprint 4 Workflow Discovery Check

Status: Workflow discovery check — after Sprint 4 test-structure expansion pass.

## Purpose

This document records the Sprint 4 workflow discovery check after creating the `tests/smoke/` scaffold.

The purpose is to determine whether the existing `.github/workflows/python-tests.yml` workflow already discovers and runs the new smoke-test area, or whether a later workflow YAML update pass is required.

This document does not admit workflow YAML changes by itself.

This document does not admit MVP smoke test implementation.

This document does not admit MVP functional proof implementation.

This document does not admit real ACP routing, ACPMessage dispatch, Analysis generation, runtime pipeline execution, downstream pipeline logic, taxonomy behavior, risk scoring, governance behavior, or output rendering.

## Baseline

Sprint 4 has completed:

- Sprint 4 Entry Control Pass
- Sprint 4 MVP Completion Control Review
- Sprint 4 Routing Preparation Review
- Sprint 4 Workflow Expansion Review
- Sprint 4 Test Structure Expansion Boundary Review
- Sprint 4 Test Structure Expansion Pass

Current validation status:

- Python Tests workflow: GREEN
- `tests/smoke/README.md`: ADDED
- `tests/smoke/__init__.py`: ADDED
- Smoke-test scaffold: CLOSED
- MVP smoke test implementation: HOLD
- MVP functional proof implementation: HOLD
- Workflow YAML update: HOLD pending discovery check

## Discovery Question

Does the current Python Tests workflow discover the future `tests/smoke/` test area automatically?

## Required Inspection

Before deciding whether workflow YAML changes are needed, inspect:

- `.github/workflows/python-tests.yml`

The key question is which command the workflow runs.

## Discovery Rules

If the workflow runs a broad command such as:

- `pytest`
- `python -m pytest`

then the workflow likely discovers:

- `tests/unit/`
- `tests/contract/`
- `tests/smoke/`

In that case, no workflow YAML update is required immediately.

If the workflow runs a narrow command such as:

- `pytest tests/unit`
- `python -m pytest tests/unit`

then the workflow does not automatically discover smoke tests.

In that case, a later workflow update pass is required.

## Verdict

Verdict:

`WORKFLOW DISCOVERY INSPECTION REQUIRED BEFORE WORKFLOW UPDATE`

No workflow YAML change is admitted yet.

The next action should be to inspect the current workflow command.

## Possible Outcomes

### Outcome A — Workflow Already Discovers All Tests

If `.github/workflows/python-tests.yml` runs the full test suite, then:

- workflow YAML update is not required now;
- MVP smoke tests can later be added under `tests/smoke/`;
- Python Tests workflow should automatically run them.

Expected status:

`WORKFLOW UPDATE NOT REQUIRED YET`

### Outcome B — Workflow Only Runs Unit Tests

If `.github/workflows/python-tests.yml` runs only `tests/unit/`, then:

- workflow YAML update is required before MVP proof closure;
- a separate workflow update boundary review is required;
- a separate workflow update pass is required.

Expected status:

`WORKFLOW UPDATE REQUIRED BEFORE MVP PROOF CLOSURE`

## Not Admitted

The following remain not admitted by this document:

- workflow YAML editing;
- MVP smoke test implementation;
- MVP functional proof implementation;
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

## Required Safeguards

The workflow discovery process must preserve the following safeguards:

1. Do not edit workflow YAML during discovery.
2. Do not add MVP smoke tests during discovery.
3. Do not add MVP proof implementation during discovery.
4. Do not introduce routing.
5. Do not introduce dispatch.
6. Do not introduce Analysis generation.
7. Do not introduce runtime pipeline execution.
8. Do not introduce downstream pipeline logic.
9. Keep Python Tests workflow GREEN.
10. Document whether workflow update is required.

## Recommended Next Step

Recommended next action:

Inspect `.github/workflows/python-tests.yml`.

If the workflow already runs all tests, the next document should be:

- `docs/sprint_4/SPRINT_4_MVP_FUNCTIONAL_PROOF_PLAN.md`

If the workflow only runs unit tests, the next document should be:

- `docs/sprint_4/SPRINT_4_WORKFLOW_UPDATE_BOUNDARY_REVIEW.md`

## No-Drift Confirmation

Confirmed:

- Sprint 4 remains controlled.
- Smoke-test scaffold is closed.
- Workflow discovery is review-only.
- Workflow YAML update remains on HOLD.
- MVP smoke test implementation remains on HOLD.
- MVP functional proof implementation remains on HOLD.
- Real ACP routing remains on HOLD.
- Routing implementation remains on HOLD.
- Dispatch target creation remains on HOLD.
- Agent instruction creation remains on HOLD.
- ACPMessage dispatch remains on HOLD.
- Analysis generation remains on HOLD.
- Runtime pipeline execution remains not admitted.
- Downstream pipeline logic remains not admitted.
- Merge to `main` has not been performed.

## Verdict Summary

Sprint 4 Workflow Discovery Check: REQUIRED.

Workflow YAML update: NOT ADMITTED YET.

Next action: inspect `.github/workflows/python-tests.yml`.

If workflow runs full `pytest`: workflow update may not be required.

If workflow runs only `tests/unit`: workflow update is required before MVP proof closure.

Recommended next step after inspection depends on workflow command.
