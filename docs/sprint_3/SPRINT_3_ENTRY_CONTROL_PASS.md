# Sprint 3 Entry Control Pass

Status: Entry control pass — before admitting Sprint 3 behavior.

## Purpose

This document opens Sprint 3 for the Cognitive Shield repository work on branch `active/mvp-foundation`.

The purpose is to verify Sprint 2 closure, preserve the boundaries established during Sprint 2, perform a workflow coverage review, and decide whether the first Sprint 3 boundary may be opened.

This document does not admit coding by itself.

## Baseline

Sprint 2 closed with boundaries after delivering the following controlled chain:

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

Sprint 2 final status:

- Sprint 2 Closure Readiness Review: COMPLETE
- Sprint 2 Exit Audit Snapshot: COMPLETE
- Python Tests workflow: GREEN
- ACP boundary eligibility: CLOSED
- ACP routing: HOLD
- Analysis generation: HOLD
- runtime pipeline execution: NOT ADMITTED
- downstream pipeline logic: NOT ADMITTED
- merge to `main`: NOT PERFORMED

## Sprint 3 Entry Question

Can Sprint 3 open controlled ACP-layer behavior?

## Entry Verdict

Verdict:

`SPRINT 3 MAY OPEN — CONTROLLED ENTRY ONLY`

Sprint 3 may open only as a controlled boundary phase.

Sprint 3 must not begin with direct ACP routing, ACPBundle creation, ACPMessage dispatch, Analysis generation, runtime pipeline execution, or downstream pipeline logic.

## Required First Control Tasks

Sprint 3 must begin with the following control tasks:

1. Verify Sprint 2 closure state.
2. Verify Python Tests workflow status.
3. Perform GitHub Actions workflow coverage review.
4. Decide whether the first admissible Sprint 3 boundary is ACP minimal envelope, ACPBundle boundary, or another ACP-layer scaffold.
5. Keep ACP routing on HOLD until separately reviewed.

## Workflow Coverage Review

A workflow coverage review is required at Sprint 3 entry.

Reason:

Sprint 2 introduced MDS, CMO, and ACP boundary eligibility behavior, all still covered by the current Python Tests workflow.

Sprint 3 may introduce new ACP-layer risks, including ACP envelope structures, ACPBundle-like containers, schema validation behavior, scope guarding, routing-adjacent logic, and eventually Analysis boundary preparation.

Before adding new Sprint 3 behavior, the repository must decide whether the existing workflow is sufficient or whether a new or expanded GitHub Actions workflow is needed.

Workflow review must check:

- whether `.github/workflows/python-tests.yml` still runs all relevant unit tests;
- whether ACP-layer tests are included;
- whether future ACP structural tests need separate markers or folders;
- whether contract tests should be expanded;
- whether additional static checks are needed before routing-adjacent behavior is admitted.

This review does not require a new workflow automatically.

It only requires an explicit decision before Sprint 3 behavior begins.

## Current Not-Admitted Areas

The following remain not admitted at Sprint 3 entry:

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
- Analysis bundle generation
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

## Candidate First Sprint 3 Boundary

Recommended first Sprint 3 boundary:

`ACP minimal envelope boundary review`

Reason:

Sprint 2 ended with ACP boundary eligibility only.

The next safest step is not ACP routing and not ACPBundle creation.

The next safest step is a minimal ACP envelope that can wrap the ACP eligibility signal without creating ACPBundle, ACPMessage, routing, dispatch, orchestration, or Analysis generation.

## Why Not Start With Routing

Sprint 3 must not start with routing because routing would introduce:

- active agent direction;
- dispatch semantics;
- protocol behavior;
- possible Analysis-adjacent flow;
- higher risk of downstream logic;
- stronger need for schema validation and scope guarding.

Therefore routing requires later boundary reviews and should remain on HOLD.

## Why ACP Minimal Envelope Is Safer

ACP minimal envelope can remain:

- eligibility-derived;
- structural only;
- non-routing;
- non-dispatching;
- non-orchestrating;
- non-analytical;
- non-runtime.

It can preserve:

- ACP boundary status;
- source stage;
- target stage;
- bounded MDS DecompositionResult;
- CMO field envelope.

It must not create:

- ACPBundle;
- ACPMessage;
- routing decision;
- dispatch target;
- Analysis bundle;
- taxonomy labels;
- risk profile;
- governance signal;
- output payload.

## Required Next Document

Recommended next repo document:

- `docs/sprint_3/SPRINT_3_WORKFLOW_COVERAGE_REVIEW.md`

After that, if workflow coverage is acceptable, the next boundary document may be:

- `docs/sprint_3/SPRINT_3_ACP_MINIMAL_ENVELOPE_BOUNDARY_REVIEW.md`

## Entry Safeguards

Sprint 3 must preserve the following safeguards:

1. Do not admit coding before boundary review.
2. Do not admit ACP routing by default.
3. Do not create ACPBundle without a separate boundary review.
4. Do not create ACPMessage without a separate boundary review.
5. Do not dispatch anything to agents.
6. Do not generate Analysis.
7. Do not trigger runtime pipeline execution.
8. Do not introduce downstream pipeline logic.
9. Keep taxonomy, risk, governance, and output layers on HOLD.
10. Preserve Python Tests workflow discipline.
11. Perform workflow coverage review before new Sprint 3 behavior.
12. Preserve Sprint 2 no-drift boundaries.

## No-Drift Confirmation

Confirmed at Sprint 3 entry:

- Sprint 2 closed with boundaries.
- MDS remains structural and non-analytical.
- CMO remains bounded and pre-ACP.
- ACP boundary eligibility is closed.
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

## Entry Verdict Summary

Sprint 3: OPEN FOR CONTROLLED ENTRY.

First required step:

- Workflow coverage review.

Recommended next document:

- `SPRINT_3_WORKFLOW_COVERAGE_REVIEW.md`

Recommended first behavior boundary after workflow review:

- ACP minimal envelope boundary review.

ACP routing: HOLD.

ACPBundle creation: HOLD.

ACPMessage creation: HOLD.

Analysis generation: HOLD.

Runtime pipeline execution: NOT ADMITTED.

Downstream pipeline logic: NOT ADMITTED.
