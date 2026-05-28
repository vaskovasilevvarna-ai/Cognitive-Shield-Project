# Sprint 4 Workflow Expansion Review

Status: Workflow expansion review — required for Sprint 4 MVP functional proof.

## Purpose

This document reviews and defines the workflow and testing expansion required for Sprint 4.

Sprint 4 is the MVP completion phase for the Cognitive Shield repository work on branch `active/mvp-foundation`.

The purpose is to decide what verification coverage is required before any routing implementation, MVP proof implementation, or end-to-end proof can be accepted as closed.

This document does not admit implementation by itself.

This document does not admit real ACP routing.

This document does not admit ACPMessage dispatch, agent routing, agent orchestration, Analysis generation, runtime pipeline execution, downstream pipeline logic, taxonomy behavior, risk scoring, governance behavior, or output rendering.

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

Current validation status:

- Python Tests workflow: GREEN
- Sprint 4 strategic objective: MVP completion with functional proof
- Routing preparation: DEFINED
- Real ACP routing: NOT ADMITTED
- Routing implementation: HOLD
- ACPMessage dispatch: HOLD
- Analysis generation: HOLD
- runtime pipeline execution: NOT ADMITTED
- downstream pipeline logic: NOT ADMITTED
- merge to `main`: NOT PERFORMED

## Workflow Expansion Question

Is workflow expansion required for Sprint 4 MVP functional proof?

## Verdict

Verdict:

`WORKFLOW EXPANSION REQUIRED FOR SPRINT 4 MVP PROOF`

The current Python Tests workflow remains useful and must stay active.

However, Sprint 4 now requires expanded verification because the sprint objective is no longer only isolated unit-level boundary behavior.

Sprint 4 must demonstrate a testable MVP-level functional proof.

Therefore, the repository needs expanded test discipline around:

- MVP smoke tests;
- no-dispatch regression tests;
- no-agent-instruction regression tests;
- no-analysis-generation regression tests;
- no-runtime-execution regression tests;
- no-forbidden-field regression tests;
- test grouping;
- possible contract test marker;
- proof-level verification.

## Why Expansion Is Required

Previous sprints validated isolated bounded layers:

- Message Decomposition Specification (MDS) bounded structural behavior;
- Canonical Message Object (CMO) bounded pre-ACP behavior;
- Agent Communication Protocol (ACP) structural containers;
- ACP Schema Validator;
- ACP Scope Guard;
- Protocol Router readiness.

Sprint 4 must go further.

Sprint 4 must prove that a minimal admitted chain can function as a coherent MVP-level flow.

That requires more than isolated unit tests.

It requires at least one proof-level test path showing that the bounded chain can move from input-derived structure through the admitted pipeline without forbidden downstream behavior.

## Existing Workflow

Current workflow:

- `.github/workflows/python-tests.yml`

Current purpose:

- run Python tests;
- catch syntax errors;
- catch import errors;
- run unit tests;
- provide GREEN / RED repository feedback.

The existing workflow remains required.

It should not be removed.

## Required Workflow Expansion Areas

Sprint 4 MVP proof requires the following verification areas.

### 1. MVP Smoke Tests

Required.

Purpose:

- verify that the MVP proof chain can run in a controlled way;
- verify that admitted modules can connect without bypassing boundaries;
- verify that expected status fields appear;
- verify that preserved structures remain present.

Possible location:

- `tests/smoke/`
- or `tests/contract/` if smoke tests are not yet admitted as a separate folder.

Preferred location for Sprint 4:

- `tests/smoke/`

### 2. No-Dispatch Regression Tests

Required.

Purpose:

- prove that no dispatch target is created;
- prove that no ACPMessage dispatch occurs;
- prove that no agent routing occurs;
- prove that no selected agent appears;
- prove that no agent instruction appears.

Forbidden fields to check:

- `dispatch_target`
- `agent_route`
- `agent_id`
- `selected_agent`
- `agent_instruction`
- `ACPMessageDispatch`

### 3. No-Analysis-Generation Regression Tests

Required.

Purpose:

- prove that MVP proof does not generate Analysis outputs;
- prove that routing or proof logic does not create Analysis bundles.

Forbidden fields to check:

- `analysis_bundle`
- `evidence_analysis_output`
- `narrative_analysis_output`
- `cognitive_analysis_output`
- `EvidenceAnalysisOutput`
- `NarrativeAnalysisOutput`
- `CognitiveAnalysisOutput`

### 4. No-Runtime-Execution Regression Tests

Required.

Purpose:

- prove that the MVP proof remains a controlled proof chain;
- prove that it does not trigger product-like runtime behavior;
- prove that no downstream pipeline execution is introduced silently.

Forbidden fields to check:

- `runtime_pipeline`
- `runtime_event`
- `execution_event`
- `downstream_pipeline`
- `pipeline_dispatch`

### 5. No-Forbidden-Field Regression Tests

Required.

Purpose:

- centralize checks for forbidden fields across MVP proof objects.

Forbidden field families include:

- routing / dispatch fields;
- agent instruction fields;
- Analysis fields;
- taxonomy fields;
- risk fields;
- governance fields;
- output fields;
- runtime fields.

### 6. Test Grouping

Required.

Purpose:

- keep unit tests separate from proof-level smoke tests;
- make workflow output easier to understand;
- prevent accidental mixing of implementation boundary tests and MVP proof tests.

Recommended grouping:

- `tests/unit/`
- `tests/contract/`
- `tests/smoke/`

If `tests/smoke/` does not yet exist, Sprint 4 should create it before MVP proof implementation.

### 7. Contract Test Marker

Recommended.

Purpose:

- mark boundary and contract-oriented tests explicitly;
- allow future workflow separation if needed.

Possible approach:

- keep using `tests/contract/`;
- optionally add pytest markers later, such as `contract` and `smoke`.

No marker implementation is required by this document.

A separate test-structure pass may admit it.

### 8. Package-Level Import / Smoke Check

Recommended.

Purpose:

- ensure the MVP proof chain imports cleanly;
- catch package-level wiring errors before proof closure.

Possible test:

- import all admitted MVP proof modules;
- verify no accidental import of Analysis, taxonomy, risk, governance, or output modules.

## Required Workflow Decision

Sprint 4 should expand verification in two steps.

### Step 1 — Test Structure Expansion

Recommended files / folders:

- `tests/smoke/README.md`
- `tests/smoke/__init__.py`
- possibly `tests/contract/README.md` update if needed

### Step 2 — Workflow Use

The existing `.github/workflows/python-tests.yml` may remain the main workflow if it already runs all tests under `tests/`.

If the workflow already runs the full test suite, then no immediate workflow YAML change may be necessary.

However, Sprint 4 must still add smoke tests and ensure they are picked up by the workflow.

If the workflow only runs unit tests, then it must be expanded to include smoke tests and contract tests.

## Workflow Update Rule

Workflow update is required if `.github/workflows/python-tests.yml` does not run:

- `tests/unit/`
- `tests/contract/`
- `tests/smoke/`

Workflow update is not required if the existing workflow already runs the whole test suite with a command such as:

- `pytest`
- `python -m pytest`

A source inspection or screenshot of the workflow may be needed before deciding whether YAML editing is required.

## Required Before MVP Proof Closure

Before Sprint 4 MVP proof can close, the repository must have:

1. Python Tests workflow GREEN.
2. MVP smoke test added and passing.
3. No-dispatch regression coverage.
4. No-agent-instruction regression coverage.
5. No-analysis-generation regression coverage.
6. No-runtime-execution regression coverage.
7. No-forbidden-field regression coverage.
8. Proof closure note confirming testable MVP functionality.
9. No merge to `main` unless separately admitted.

## Current Admission Decision

This document admits the need for workflow and test expansion planning.

It does not yet admit:

- editing workflow YAML;
- adding smoke tests;
- adding contract markers;
- implementing MVP proof;
- implementing routing.

Those require separate bounded passes.

## Recommended Next Implementation-Related Review

Recommended next document:

- `docs/sprint_4/SPRINT_4_TEST_STRUCTURE_EXPANSION_BOUNDARY_REVIEW.md`

Purpose:

- decide whether to create `tests/smoke/`;
- decide whether to add smoke README / package marker;
- decide whether to add no-forbidden-field helper tests;
- decide whether to inspect workflow YAML before editing it.

## Recommended Later Documents

After test structure review:

- `docs/sprint_4/SPRINT_4_REAL_ROUTING_BOUNDARY_REVIEW.md`
- `docs/sprint_4/SPRINT_4_MVP_FUNCTIONAL_PROOF_PLAN.md`
- possible `docs/sprint_4/SPRINT_4_WORKFLOW_UPDATE_PASS_CLOSURE_NOTE.md`
- possible `docs/sprint_4/SPRINT_4_MVP_SMOKE_TEST_PASS_CLOSURE_NOTE.md`

## Not Admitted

The following remain not admitted by this document:

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

## Required Safeguards

Sprint 4 workflow and test expansion must preserve the following safeguards:

1. Existing Python Tests workflow must remain GREEN.
2. New smoke tests must not bypass boundary layers.
3. Smoke tests must not generate Analysis.
4. Smoke tests must not create dispatch targets.
5. Smoke tests must not create agent instructions.
6. Smoke tests must not trigger runtime pipeline execution.
7. Smoke tests must verify preservation of bounded structures.
8. Forbidden-field checks must be explicit.
9. Workflow changes must be minimal and reversible.
10. Any workflow YAML edit requires a separate pass and closure note.

## MVP Alignment

This workflow expansion review supports the Sprint 4 MVP completion target.

Sprint 4 must produce a testable MVP-level functional proof.

That proof requires verification beyond isolated unit tests.

Therefore:

- smoke-level proof is required;
- no-forbidden-field regression coverage is required;
- proof closure documentation is required.

## No-Drift Confirmation

Confirmed:

- Sprint 3 closure state remains preserved.
- Sprint 4 is open for controlled MVP completion work.
- Routing preparation is complete at planning level.
- Workflow expansion is required for MVP proof.
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

Sprint 4 Workflow Expansion Review: COMPLETE.

Workflow expansion: REQUIRED FOR SPRINT 4 MVP PROOF.

Existing Python Tests workflow: remains active.

Smoke tests: REQUIRED.

No-dispatch regression tests: REQUIRED.

No-agent-instruction regression tests: REQUIRED.

No-analysis-generation regression tests: REQUIRED.

No-runtime-execution regression tests: REQUIRED.

No-forbidden-field regression tests: REQUIRED.

Workflow YAML update: REQUIRED ONLY IF current workflow does not run smoke / contract tests.

Real ACP routing: NOT ADMITTED BY THIS DOCUMENT.

Routing implementation: HOLD.

Analysis generation: HOLD.

Runtime pipeline execution: NOT ADMITTED.

Downstream pipeline logic: NOT ADMITTED.

Recommended next document:

- `SPRINT_4_TEST_STRUCTURE_EXPANSION_BOUNDARY_REVIEW.md`
