# Sprint 4 Entry Control Pass

Status: Entry control pass — before admitting Sprint 4 routing preparation behavior.

## Purpose

This document opens Sprint 4 for the Cognitive Shield repository work on branch `active/mvp-foundation`.

The purpose is to verify Sprint 3 closure, preserve the boundaries established during Sprint 3, and define the controlled entry conditions before any real Agent Communication Protocol (ACP) routing behavior can be considered.

This document does not admit coding by itself.

This document does not admit real routing.

This document does not admit edits to `router.py`.

This document does not admit routing decision creation, route selection, dispatch target creation, agent instruction creation, ACPMessage dispatch, agent routing, agent orchestration, Analysis generation, runtime pipeline execution, downstream pipeline logic, taxonomy behavior, risk scoring, governance behavior, or output rendering.

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

Sprint 3 final status:

- Sprint 3 Closure Readiness Review: COMPLETE
- Sprint 3 Exit Audit Snapshot: COMPLETE
- Python Tests workflow: GREEN
- Protocol Router readiness: CLOSED
- Routing Preparation Gate: CLOSED
- Real ACP routing: NOT ADMITTED
- Routing implementation: HOLD
- ACPMessage dispatch: HOLD
- Analysis generation: HOLD
- runtime pipeline execution: NOT ADMITTED
- downstream pipeline logic: NOT ADMITTED
- merge to `main`: NOT PERFORMED

## Sprint 4 Entry Question

Can Sprint 4 open controlled real-routing preparation work?

## Entry Verdict

Verdict:

`SPRINT 4 MAY OPEN — ROUTING PREPARATION ONLY`

Sprint 4 may open only as a controlled routing-preparation phase.

Sprint 4 must not begin with direct routing implementation.

Sprint 4 must not begin by editing `router.py`.

Sprint 4 must not create routing decisions, dispatch targets, agent instructions, route tables, ACPMessage dispatch, Analysis generation, runtime pipeline execution, or downstream pipeline logic.

## Required First Control Tasks

Sprint 4 must begin with the following control tasks:

1. Verify Sprint 3 closure state.
2. Verify Python Tests workflow status.
3. Review Routing Preparation Gate requirements from Sprint 3.
4. Perform workflow expansion review before any real routing behavior.
5. Decide whether a Real Routing Boundary Review is admissible.
6. Keep routing implementation on HOLD until separately admitted.

## Sprint 4 Initial Scope

Sprint 4 initial scope is limited to:

- routing preparation review;
- workflow expansion review;
- real routing boundary review;
- routing objective definition;
- route target taxonomy preparation;
- allowed / forbidden route type definition;
- no-dispatch rule definition;
- no-agent-instruction rule definition;
- no-analysis-generation rule definition;
- route result output shape planning;
- routing failure mode planning.

No implementation is admitted by this entry control pass.

## Current Not-Admitted Areas

The following remain not admitted at Sprint 4 entry:

- real ACP routing
- routing decision creation
- route selection
- dispatch target creation
- agent instruction creation
- agent selection
- route table behavior
- dynamic protocol routing
- ACPMessage dispatch
- agent routing
- agent orchestration
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
- semantic interpretation beyond admitted MDS-local, CMO-local, and ACP structural containers

## Why Sprint 4 Must Start With Control

Sprint 4 begins at a qualitatively higher-risk threshold.

Previous sprints built bounded structural readiness:

- MDS bounded structure;
- CMO bounded pre-ACP chain;
- ACP structural containers;
- ACP validation and scope;
- Protocol Router readiness.

Real routing is different.

It can introduce:

- route selection;
- practical dispatch pressure;
- implicit agent assignment;
- hidden downstream flow;
- Analysis-adjacent coupling;
- runtime control-flow behavior.

Therefore, Sprint 4 must begin with control documentation before coding.

## Required Next Document

Recommended next repo document:

- `docs/sprint_4/SPRINT_4_ROUTING_PREPARATION_REVIEW.md`

This document should revisit and refine the Sprint 3 Routing Preparation Gate before any workflow expansion or real routing boundary is attempted.

## Recommended Sprint 4 Document Order

Recommended order:

1. `SPRINT_4_ENTRY_CONTROL_PASS.md`
2. `SPRINT_4_ROUTING_PREPARATION_REVIEW.md`
3. `SPRINT_4_WORKFLOW_EXPANSION_REVIEW.md`
4. `SPRINT_4_REAL_ROUTING_BOUNDARY_REVIEW.md`

Only after those documents should implementation even be considered.

## Entry Safeguards

Sprint 4 must preserve the following safeguards:

1. Do not admit coding before boundary review.
2. Do not edit `router.py` directly at Sprint 4 entry.
3. Do not create routing decisions by default.
4. Do not create route tables by default.
5. Do not create dispatch targets.
6. Do not create agent instructions.
7. Do not dispatch ACPMessages.
8. Do not generate Analysis.
9. Do not trigger runtime pipeline execution.
10. Do not introduce downstream pipeline logic.
11. Keep taxonomy, risk, governance, and output layers on HOLD.
12. Perform workflow expansion review before real routing behavior.
13. Preserve all Sprint 3 no-drift boundaries.

## No-Drift Confirmation

Confirmed at Sprint 4 entry:

- Sprint 3 closed with boundaries.
- ACP boundary eligibility remains eligibility-only.
- ACP minimal envelope remains envelope-only.
- ACPBundle remains bundle-only.
- ACPMessage remains message-only.
- ACP Schema Validator remains schema-validation-only.
- ACP Scope Guard remains scope-check-only.
- Protocol Router readiness remains readiness-only.
- Routing Preparation Gate remains non-coding.
- Real ACP routing remains on HOLD.
- Routing implementation remains on HOLD.
- Routing decision creation remains on HOLD.
- Dispatch target creation remains on HOLD.
- Agent instruction creation remains on HOLD.
- ACPMessage dispatch remains on HOLD.
- Analysis generation remains on HOLD.
- Runtime pipeline execution remains not admitted.
- Downstream pipeline logic remains not admitted.
- Taxonomy behavior has not started.
- Risk scoring has not started.
- Governance behavior has not started.
- Output rendering has not started.
- Merge to `main` has not been performed.

## Entry Verdict Summary

Sprint 4: OPEN FOR CONTROLLED ROUTING PREPARATION.

Coding: NOT ADMITTED.

Real ACP routing: NOT ADMITTED.

Routing implementation: HOLD.

Routing decision creation: HOLD.

Dispatch target creation: HOLD.

Agent instruction creation: HOLD.

ACPMessage dispatch: HOLD.

Analysis generation: HOLD.

Runtime pipeline execution: NOT ADMITTED.

Downstream pipeline logic: NOT ADMITTED.

Recommended next document:

- `SPRINT_4_ROUTING_PREPARATION_REVIEW.md`
