# Sprint 3 Workflow Coverage Review

Status: Workflow coverage review — before admitting Sprint 3 ACP-layer behavior.

## Purpose

This document reviews whether the current GitHub Actions workflow coverage is sufficient for Sprint 3.

Sprint 3 may introduce Agent Communication Protocol (ACP) layer behavior after Sprint 2 closed with ACP boundary eligibility. Because Sprint 3 may move closer to ACP envelope, ACPBundle, ACPMessage, Schema Validator, Scope Guard, Protocol Router, and eventually Analysis boundary behavior, workflow coverage must be explicitly reviewed before new implementation begins.

This document does not admit coding by itself.

## Baseline

Sprint 2 closed with boundaries.

Sprint 2 delivered the following controlled chain:

Input behavior nucleus  
→ Message Decomposition Specification (MDS) early structural stack  
→ bounded MDS DecompositionResult shell  
→ MDS-to-Canonical Message Object (CMO) boundary eligibility  
→ CMO minimal shell  
→ CMO structural contract  
→ CMO field envelope  
→ CMO minimal object  
→ CMO bounded construction candidate  
→ Agent Communication Protocol (ACP) boundary eligibility

Sprint 3 Entry Control Pass is complete.

Current status:

- Sprint 3: OPEN FOR CONTROLLED ENTRY
- Python Tests workflow: GREEN
- ACP boundary eligibility: CLOSED
- ACP routing: HOLD
- ACPBundle creation: HOLD
- ACPMessage creation: HOLD
- Analysis generation: HOLD
- runtime pipeline execution: NOT ADMITTED
- downstream pipeline logic: NOT ADMITTED

## Existing Workflow

Current workflow:

- `.github/workflows/python-tests.yml`

Known purpose:

- run Python tests;
- validate admitted Python unit behavior;
- provide GREEN / RED repository feedback before accepting new bounded behavior.

Current coverage is considered sufficient for:

- current unit tests;
- MDS structural tests;
- CMO boundary and pre-construction tests;
- ACP boundary eligibility tests;
- basic regression detection for admitted Python modules.

## Workflow Coverage Question

Is the existing Python Tests workflow sufficient for the first Sprint 3 ACP structural boundary?

## Verdict

Verdict:

`CURRENT PYTHON TESTS WORKFLOW IS SUFFICIENT FOR FIRST ACP STRUCTURAL BOUNDARY — EXPANSION CHECKPOINT REQUIRED BEFORE ROUTING-ADJACENT BEHAVIOR`

The existing Python Tests workflow is sufficient to open the first Sprint 3 boundary review and, if admitted later, a minimal ACP structural behavior such as ACP minimal envelope.

However, the workflow should be reviewed again before any routing-adjacent or dispatch-adjacent behavior is admitted.

## Why Existing Workflow Is Sufficient for First ACP Structural Boundary

The first recommended Sprint 3 behavior is not ACP routing.

The first recommended Sprint 3 behavior is:

- ACP minimal envelope boundary review;
- then potentially ACP minimal envelope implementation.

This can remain:

- structural only;
- eligibility-derived;
- non-routing;
- non-dispatching;
- non-orchestrating;
- non-analytical;
- non-runtime.

Such behavior can be covered by the existing Python unit test workflow.

## What Existing Workflow Must Continue To Catch

The Python Tests workflow must continue to catch:

- Python syntax errors;
- import errors;
- broken unit tests;
- broken MDS behavior;
- broken CMO behavior;
- broken ACP boundary eligibility behavior;
- regression in bounded structural objects;
- accidental exposure of forbidden fields where tests cover those boundaries.

## Current Coverage Limitations

The existing Python Tests workflow is not yet sufficient by itself for later Sprint 3 behavior such as:

- ACP routing;
- ACPBundle creation;
- ACPMessage creation;
- ACPMessage dispatch;
- agent routing;
- agent orchestration;
- Protocol Router behavior;
- Schema Validator behavior;
- Scope Guard behavior;
- Contradiction Registrar behavior;
- Uncertainty Propagator behavior;
- Synthesis Exporter behavior;
- Analysis generation;
- runtime pipeline execution.

These later behaviors may require expanded workflow coverage.

## Expansion Triggers

A workflow expansion review is required before admitting any of the following:

- ACP routing;
- ACPBundle creation;
- ACPMessage creation;
- ACPMessage dispatch;
- Protocol Router behavior;
- Schema Validator behavior;
- Scope Guard behavior;
- Analysis generation;
- runtime pipeline execution;
- downstream pipeline logic.

Possible future workflow additions may include:

- contract tests;
- ACP-specific test grouping;
- stricter import checks;
- static formatting or linting;
- schema validation tests;
- boundary regression tests;
- no-forbidden-field regression tests;
- package-level integration smoke tests.

This review does not require those additions now.

## Sprint 3 First Boundary Recommendation

Recommended first Sprint 3 boundary:

- `docs/sprint_3/SPRINT_3_ACP_MINIMAL_ENVELOPE_BOUNDARY_REVIEW.md`

Reason:

ACP minimal envelope is the safest next ACP-layer step after ACP boundary eligibility.

It can remain structural and non-runtime.

It does not require ACP routing, ACPBundle creation, ACPMessage creation, agent dispatch, or Analysis generation.

## Not Admitted

The following remain not admitted after this workflow review:

- ACP routing
- ACPBundle creation
- ACPMessage creation
- ACPMessage dispatch
- agent routing
- agent orchestration
- Protocol Router behavior
- Scope Guard behavior beyond boundary review
- Schema Validator behavior beyond boundary review
- Contradiction Registrar behavior
- Uncertainty Propagator behavior
- Synthesis Exporter behavior
- Analysis generation
- EvidenceAnalysisOutput generation
- NarrativeAnalysisOutput generation
- CognitiveAnalysisOutput generation
- taxonomy behavior
- label-to-verdict logic
- risk scoring
- confidence or uncertainty evaluation
- governance behavior
- output rendering
- runtime pipeline execution
- downstream pipeline logic
- merge to `main`

Also still not admitted:

- implicit claim inference
- hidden claim reconstruction
- truth assessment
- evidence assessment
- framing extraction
- relation inference
- semantic interpretation beyond admitted MDS-local and CMO-local structures

## Required Safeguards

Sprint 3 workflow discipline must preserve the following safeguards:

1. New Python behavior must have matching unit tests.
2. Python Tests workflow must be GREEN before accepting any pass as closed.
3. ACP routing must not be admitted through minimal envelope behavior.
4. ACPBundle creation must not be admitted through minimal envelope behavior.
5. ACPMessage creation must not be admitted through minimal envelope behavior.
6. Analysis generation must remain on HOLD.
7. Runtime pipeline execution must remain not admitted.
8. Downstream pipeline logic must remain not admitted.
9. Any future routing-adjacent behavior requires a new workflow coverage review.
10. Any future Analysis-adjacent behavior requires a new workflow coverage review.

## No-Drift Confirmation

Confirmed:

- Sprint 2 closure state remains preserved.
- Sprint 3 is open for controlled entry only.
- Current Python Tests workflow remains the active validation mechanism.
- Existing workflow is sufficient for the first structural ACP boundary.
- ACP routing remains on HOLD.
- ACPBundle creation remains on HOLD.
- ACPMessage creation remains on HOLD.
- Analysis generation remains on HOLD.
- runtime pipeline execution remains not admitted.
- downstream pipeline logic remains not admitted.
- taxonomy behavior has not started.
- risk scoring has not started.
- governance behavior has not started.
- output rendering has not started.
- merge to `main` has not been performed.

## Recommended Next Step

Recommended next repo document:

- `docs/sprint_3/SPRINT_3_ACP_MINIMAL_ENVELOPE_BOUNDARY_REVIEW.md`

This next document should decide whether to admit ACP minimal envelope behavior.

It must not admit:

- ACP routing;
- ACPBundle creation;
- ACPMessage creation;
- ACPMessage dispatch;
- Analysis generation;
- runtime pipeline execution;
- downstream pipeline logic.

## Verdict Summary

Workflow coverage review: COMPLETE.

Current Python Tests workflow: SUFFICIENT FOR FIRST ACP STRUCTURAL BOUNDARY.

Workflow expansion: NOT REQUIRED YET.

Workflow expansion checkpoint: REQUIRED BEFORE ROUTING-ADJACENT OR ANALYSIS-ADJACENT BEHAVIOR.

Recommended next document:

- `SPRINT_3_ACP_MINIMAL_ENVELOPE_BOUNDARY_REVIEW.md`

ACP routing: HOLD.

ACPBundle creation: HOLD.

ACPMessage creation: HOLD.

Analysis generation: HOLD.

Runtime pipeline execution: NOT ADMITTED.

Downstream pipeline logic: NOT ADMITTED.
