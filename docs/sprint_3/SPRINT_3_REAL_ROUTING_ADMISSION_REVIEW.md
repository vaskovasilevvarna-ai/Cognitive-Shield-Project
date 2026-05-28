# Sprint 3 Real Routing Admission Review

Status: Admission review — before deciding whether real Agent Communication Protocol (ACP) routing may enter Sprint 3.

## Purpose

This document records the Sprint 3 admission review after the controlled Protocol Router readiness pass.

The purpose is to decide whether real Agent Communication Protocol (ACP) routing should be admitted into Sprint 3, deferred to Sprint 4, or held pending additional safeguards.

This document does not admit implementation by itself.

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

Sprint 3 has completed:

- Sprint 3 Entry Control Pass
- Sprint 3 Workflow Coverage Review
- ACP minimal envelope boundary review
- ACP minimal envelope pass
- ACPBundle boundary review
- ACPBundle pass
- ACPMessage boundary review
- ACPMessage pass
- ACP Schema Validator boundary review
- ACP Schema Validator pass
- ACP Scope Guard boundary review
- ACP Scope Guard pass
- Routing-Adjacent Workflow Review
- Protocol Router boundary review
- Protocol Router readiness pass

Current validation status:

- Python Tests workflow: GREEN
- Current Python Tests workflow: sufficient for bounded structural ACP behavior
- Current Python Tests workflow: sufficient for Protocol Router readiness behavior
- Workflow expansion: required before real routing, dispatch, agent orchestration, Analysis, runtime, or downstream behavior

Current ACP state:

ACP boundary eligibility  
→ ACP minimal envelope  
→ ACPBundle  
→ ACPMessage  
→ ACP Schema Validator  
→ ACP Scope Guard  
→ Protocol Router readiness

Current restricted areas:

- real ACP routing: HOLD
- routing decision creation: HOLD
- route selection: HOLD
- dispatch target creation: HOLD
- agent instruction creation: HOLD
- ACPMessage dispatch: HOLD
- agent routing: HOLD
- agent orchestration: HOLD
- Contradiction Registrar behavior: HOLD
- Uncertainty Propagator behavior: HOLD
- Synthesis Exporter behavior: HOLD
- Analysis generation: NOT STARTED
- runtime pipeline execution: NOT ADMITTED
- downstream pipeline logic: NOT ADMITTED
- taxonomy behavior: NOT STARTED
- risk scoring: NOT STARTED
- governance behavior: NOT STARTED
- output rendering: NOT STARTED
- merge to `main`: NOT PERFORMED

## Admission Question

Should real ACP routing be admitted into Sprint 3?

## Verdict

Verdict:

`DO NOT ADMIT REAL ROUTING YET — DEFER TO A SEPARATE ROUTING PREPARATION GATE`

Real ACP routing should not be admitted immediately after Protocol Router readiness.

Sprint 3 has reached a stable pre-routing checkpoint, but real routing introduces a qualitatively different behavioral class.

The correct next step is not routing implementation.

The correct next step is to decide whether Sprint 3 should close at router readiness, or whether a separate routing preparation gate should be opened before any routing behavior is implemented.

## Why Real Routing Is Not Automatically Admitted

Real routing is not equivalent to Protocol Router readiness.

Protocol Router readiness only confirms that a schema-valid and scope-allowed ACPMessage is structurally ready for future router-layer consideration.

Real routing would introduce at least one of the following:

- routing decision creation;
- route selection;
- dispatch target creation;
- agent instruction creation;
- agent selection;
- route table behavior;
- potential dispatch-adjacent behavior;
- downstream flow expectations.

These are not merely structural wrappers.

They begin to shape system behavior.

## Risk Assessment

Real routing introduces the following risks:

### 1. Dispatch Drift Risk

Even if routing does not dispatch directly, a routing decision can create practical pressure toward dispatch.

### 2. Agent Instruction Drift Risk

Route selection may implicitly create agent-task semantics before agent instruction boundaries are defined.

### 3. Analysis-Adjacent Drift Risk

Routing may begin to imply which analysis family should receive the message, creating pressure toward Analysis generation.

### 4. Runtime Pipeline Drift Risk

Routing can become the first real runtime control-flow behavior if not tightly bounded.

### 5. Scope Guard Weakening Risk

If routing is admitted too soon, Scope Guard may become a formal checkpoint but lose practical control over downstream flow.

### 6. Workflow Coverage Risk

The current Python Tests workflow is sufficient for structural and readiness behavior, but real routing may require additional test coverage, including no-dispatch, no-analysis, and no-runtime regression checks.

## Admission Decision

Real ACP routing is not admitted in this review.

The project may only admit a future routing preparation review if it remains:

- admission-only;
- non-implementation;
- no routing decision creation;
- no route selection;
- no dispatch target creation;
- no agent instruction creation;
- no ACPMessage dispatch;
- no Analysis generation;
- no runtime pipeline execution;
- no downstream pipeline logic.

## Not Admitted

The following remain not admitted:

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

## Required Before Real Routing Can Be Implemented

Before real routing can be implemented, the project must complete a separate preparation gate covering:

1. routing objective definition;
2. route target taxonomy;
3. allowed route types;
4. forbidden route types;
5. no-dispatch rule;
6. no-agent-instruction rule;
7. no-analysis-generation rule;
8. route result output shape;
9. failure modes;
10. workflow coverage expansion decision;
11. tests for absence of dispatch, agent instruction, Analysis, runtime, and downstream behavior.

## Recommended Next Options

The project has two disciplined options.

### Option A — Close Sprint 3 Here

Close Sprint 3 at Protocol Router readiness.

This is the safer option if the goal is to prevent routing spillover.

Sprint 4 would begin with:

- Routing Preparation Gate;
- Workflow Expansion Review;
- Real Routing Boundary Review.

### Option B — Open Routing Preparation Gate Inside Sprint 3

Continue Sprint 3 only with a non-coding routing preparation document.

Recommended document:

- `docs/sprint_3/SPRINT_3_ROUTING_PREPARATION_GATE.md`

This gate must not implement routing.

It must define what real routing would mean and what tests / safeguards are required before implementation.

## Recommendation

Recommended decision:

`OPEN ROUTING PREPARATION GATE ONLY IF MORE WORK IS DONE IN SPRINT 3`

Do not open implementation.

Do not edit `router.py`.

Do not create routing decisions.

Do not create dispatch targets.

Do not create agent instructions.

The safest implementation boundary remains deferred until after routing preparation and workflow coverage expansion are reviewed.

## No-Drift Confirmation

Confirmed:

- Sprint 2 closure state remains preserved.
- Sprint 3 is open and controlled.
- Routing-adjacent workflow review is complete.
- ACP boundary eligibility remains eligibility-only.
- ACP minimal envelope remains envelope-only.
- ACPBundle remains bundle-only.
- ACPMessage remains message-only.
- ACP Schema Validator remains schema-validation-only.
- ACP Scope Guard remains scope-check-only.
- Protocol Router readiness remains readiness-only.
- Real ACP routing remains on HOLD.
- ACPMessage dispatch remains on HOLD.
- agent orchestration remains on HOLD.
- Analysis generation remains on HOLD.
- taxonomy behavior has not started.
- risk scoring has not started.
- governance behavior has not started.
- output rendering has not started.
- runtime pipeline execution has not started.
- downstream pipeline logic has not started.
- merge to `main` has not been performed.

## Verdict Summary

Real Routing Admission Review: COMPLETE.

Real ACP routing: NOT ADMITTED.

Routing implementation: HOLD.

Routing decision creation: HOLD.

Dispatch target creation: HOLD.

Agent instruction creation: HOLD.

ACPMessage dispatch: HOLD.

Analysis generation: HOLD.

Runtime pipeline execution: NOT ADMITTED.

Downstream pipeline logic: NOT ADMITTED.

Recommended next document if Sprint 3 continues:

- `SPRINT_3_ROUTING_PREPARATION_GATE.md`

Recommended alternative:

- close Sprint 3 at Protocol Router readiness and defer real routing preparation to Sprint 4.
