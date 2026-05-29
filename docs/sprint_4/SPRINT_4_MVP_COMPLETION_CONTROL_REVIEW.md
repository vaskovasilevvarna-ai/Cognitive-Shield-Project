# Sprint 4 MVP Completion Control Review

Status: Sprint 4 strategic control review — after Sprint 4 Entry Control Pass.

## Purpose

This document updates the Sprint 4 working objective.

Sprint 4 must not remain only a routing-preparation sprint.

Sprint 4 is now defined as the MVP completion sprint for the Cognitive Shield repository work on branch `active/mvp-foundation`.

The purpose is to align Sprint 4 with a testable MVP-level functional proof while preserving all existing safeguards around real routing, dispatch, Analysis generation, runtime pipeline execution, downstream pipeline logic, taxonomy behavior, risk scoring, governance behavior, and output rendering.

This document does not admit implementation by itself.

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

Sprint 4 Entry Control Pass is complete.

Current validation status:

- Python Tests workflow: GREEN
- Sprint 4 Entry Control Pass: COMPLETE
- Real ACP routing: NOT ADMITTED
- Routing implementation: HOLD
- ACPMessage dispatch: HOLD
- Analysis generation: HOLD
- runtime pipeline execution: NOT ADMITTED
- downstream pipeline logic: NOT ADMITTED
- merge to `main`: NOT PERFORMED

## Control Question

Should Sprint 4 remain a routing-preparation sprint, or should it be reframed as the MVP completion sprint?

## Verdict

Verdict:

`SPRINT 4 IS MVP COMPLETION PHASE — WITH CONTROLLED ROUTING PREPARATION`

Sprint 4 must be treated as the working phase that brings the project to MVP-level functional proof.

This does not mean full system completion.

This does not mean production readiness.

This does not mean full analytical intelligence.

This does mean that by the end of Sprint 4, the repository should contain a testable minimal end-to-end proof that the Cognitive Shield pipeline works at MVP level.

## MVP Completion Target

At the end of Sprint 4, the project should be able to demonstrate a minimal controlled flow:

Input  
→ Message Decomposition Specification (MDS) bounded structure  
→ Canonical Message Object (CMO) bounded structure  
→ Agent Communication Protocol (ACP) structural chain  
→ controlled routing readiness or minimal routing result  
→ MVP functional proof output

This proof must be testable.

It must not depend on cloud services.

It must not require telemetry.

It must not bypass the bounded architecture.

It must not secretly introduce downstream behavior before admission.

## MVP Functional Proof Definition

For Sprint 4, MVP functional proof means:

- a single input can move through the admitted bounded chain;
- the pipeline produces structured intermediate outputs;
- the system preserves key boundaries;
- tests can verify that the flow works;
- tests can verify that forbidden downstream behavior is absent;
- the result can be demonstrated locally;
- the proof is small, explicit, and reproducible.

MVP functional proof does not mean:

- full disinformation detection;
- full evidence evaluation;
- full narrative analysis;
- full cognitive risk analysis;
- full taxonomy labeling;
- full risk scoring;
- full governance decision;
- full output rendering;
- production UI;
- external integration;
- cloud deployment;
- community-ready final product.

## Sprint 4 Strategic Objective

Sprint 4 objective:

Controlled routing preparation  
→ workflow expansion decision  
→ real routing boundary decision  
→ minimal end-to-end MVP proof planning  
→ bounded implementation only if admitted  
→ testable MVP functional proof

Sprint 4 must close only when it has either:

1. delivered the MVP-level functional proof; or
2. explicitly documented why MVP proof is not yet admissible and what remains blocking.

The preferred target is option 1.

## Required Sprint 4 Workstreams

Sprint 4 should organize work into four controlled workstreams.

### Workstream 1 — Routing Preparation

Purpose:

- refine routing objective;
- define route target taxonomy;
- define allowed and forbidden route types;
- define no-dispatch rule;
- define no-agent-instruction rule;
- define no-analysis-generation rule;
- define route result output shape;
- define routing failure modes.

Required document:

- `docs/sprint_4/SPRINT_4_ROUTING_PREPARATION_REVIEW.md`

### Workstream 2 — Workflow Expansion

Purpose:

- determine whether the current Python Tests workflow is enough;
- decide whether new checks are required before routing behavior;
- define no-dispatch regression tests;
- define no-analysis-generation regression tests;
- define no-runtime-execution regression tests;
- define no-forbidden-field regression tests.

Required document:

- `docs/sprint_4/SPRINT_4_WORKFLOW_EXPANSION_REVIEW.md`

### Workstream 3 — Real Routing Boundary

Purpose:

- decide whether minimal real routing can be admitted;
- define whether routing remains non-dispatching;
- define allowed routing output shape;
- define forbidden routing output fields;
- prevent route selection from becoming dispatch;
- prevent routing from creating Analysis input bundles.

Required document:

- `docs/sprint_4/SPRINT_4_REAL_ROUTING_BOUNDARY_REVIEW.md`

### Workstream 4 — MVP Functional Proof

Purpose:

- define minimal end-to-end proof;
- define exact test input;
- define expected bounded outputs;
- define allowed chain components;
- define prohibited downstream behaviors;
- define test files;
- define proof closure criteria.

Required document:

- `docs/sprint_4/SPRINT_4_MVP_FUNCTIONAL_PROOF_PLAN.md`

## MVP Proof Required Chain

The MVP functional proof should use the already admitted chain as its basis:

Input behavior nucleus  
→ MDS surface / claim-unit / DecompositionResult chain  
→ MDS-to-CMO boundary eligibility  
→ CMO minimal shell  
→ CMO structural contract  
→ CMO field envelope  
→ CMO minimal object  
→ CMO bounded construction candidate  
→ ACP boundary eligibility  
→ ACP minimal envelope  
→ ACPBundle  
→ ACPMessage  
→ ACP Schema Validator  
→ ACP Scope Guard  
→ Protocol Router readiness  
→ future admitted routing result or routing readiness proof

The proof must remain bounded.

The proof must not skip layers.

The proof must not bypass validation.

The proof must not introduce downstream logic silently.

## MVP Proof Testing Requirements

Sprint 4 must end with tests that show:

- the admitted chain can run in a controlled way;
- each layer returns expected status fields;
- the original input-derived structure is preserved;
- `decomposition_result` is preserved through the chain where required;
- `field_envelope` is preserved through the chain where required;
- no forbidden fields are exposed;
- no dispatch target is created unless explicitly admitted;
- no agent instruction is created;
- no Analysis bundle is created;
- no taxonomy labels are created;
- no risk profile is created;
- no governance signal is created;
- no output payload is created;
- no runtime pipeline execution is triggered.

## MVP Proof Non-Goals

The Sprint 4 MVP proof must not attempt to complete:

- full ACP routing;
- real agent orchestration;
- Analysis generation;
- Evidence Analysis;
- Narrative Analysis;
- Cognitive Analysis;
- taxonomy labeling;
- risk scoring;
- governance decision;
- explainable interface rendering;
- education module behavior;
- runtime product UI.

These remain future layers unless separately admitted.

## Routing Constraints For MVP

If Sprint 4 admits minimal routing behavior, it must be constrained as follows:

- routing must be non-dispatching;
- routing must not select a real agent;
- routing must not create agent instructions;
- routing must not create Analysis input bundles;
- routing must not call Analysis modules;
- routing must not trigger runtime pipeline execution;
- routing must not expose downstream-ready payloads.

If minimal routing cannot satisfy these constraints, Sprint 4 should close with router readiness proof rather than real routing proof.

## Workflow Requirement

Before any routing implementation, Sprint 4 must complete workflow expansion review.

The review must decide whether the existing Python Tests workflow is sufficient or whether additional validation is needed.

Possible additions include:

- no-dispatch regression tests;
- no-agent-instruction regression tests;
- no-analysis-generation regression tests;
- no-runtime-execution regression tests;
- no-forbidden-field tests;
- ACP end-to-end smoke test;
- package-level import test;
- contract test grouping.

This control review does not require immediate workflow changes.

It requires a documented decision before routing implementation.

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

## Sprint 4 Closure Criteria

Sprint 4 can close only if the following are true:

1. Sprint 4 Entry Control Pass is complete.
2. Sprint 4 MVP Completion Control Review is complete.
3. Routing Preparation Review is complete.
4. Workflow Expansion Review is complete.
5. Real Routing Boundary Review is complete or routing is explicitly deferred.
6. MVP Functional Proof Plan is complete.
7. MVP functional proof implementation is either completed or explicitly deferred with blockers.
8. Python Tests workflow is GREEN.
9. No forbidden downstream behavior is introduced.
10. No merge to `main` is performed without a separate merge readiness review.

Preferred closure condition:

- MVP functional proof is implemented and testable.

Fallback closure condition:

- MVP functional proof is not yet admissible, and blockers are documented clearly.

## Recommended Sprint 4 Document Order

Recommended order:

1. `SPRINT_4_MVP_COMPLETION_CONTROL_REVIEW.md`
2. `SPRINT_4_ROUTING_PREPARATION_REVIEW.md`
3. `SPRINT_4_WORKFLOW_EXPANSION_REVIEW.md`
4. `SPRINT_4_REAL_ROUTING_BOUNDARY_REVIEW.md`
5. `SPRINT_4_MVP_FUNCTIONAL_PROOF_PLAN.md`
6. bounded implementation passes only if admitted
7. `SPRINT_4_MVP_FUNCTIONAL_PROOF_CLOSURE_NOTE.md`
8. `SPRINT_4_CLOSURE_READINESS_REVIEW.md`
9. `SPRINT_4_EXIT_AUDIT_SNAPSHOT.md`

## No-Drift Confirmation

Confirmed:

- Sprint 3 closure state remains preserved.
- Sprint 4 is open for controlled MVP completion work.
- Routing preparation remains controlled.
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

Sprint 4 MVP Completion Control Review: COMPLETE.

Sprint 4 strategic objective: MVP completion with functional proof.

Sprint 4 must not remain only routing preparation.

MVP functional proof: REQUIRED TARGET.

Real ACP routing: NOT ADMITTED BY THIS DOCUMENT.

Coding: NOT ADMITTED BY THIS DOCUMENT.

Routing implementation: HOLD.

Analysis generation: HOLD.

Runtime pipeline execution: NOT ADMITTED.

Downstream pipeline logic: NOT ADMITTED.

Recommended next document:

- `SPRINT_4_ROUTING_PREPARATION_REVIEW.md`
