# Sprint 4 Routing Preparation Review

Status: Sprint 4 routing preparation review — before workflow expansion and real routing boundary review.

## Purpose

This document reviews and refines the routing preparation requirements carried forward from Sprint 3.

The purpose is to define what real Agent Communication Protocol (ACP) routing would mean in the Cognitive Shield MVP, what must remain forbidden, and what must be prepared before any routing implementation can be admitted.

This document supports the Sprint 4 MVP completion objective.

This document does not admit implementation by itself.

This document does not admit edits to `router.py`.

This document does not admit real routing, dispatch, agent instruction creation, Analysis generation, runtime pipeline execution, downstream pipeline logic, taxonomy behavior, risk scoring, governance behavior, or output rendering.

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

Current validation status:

- Python Tests workflow: GREEN
- Sprint 4 strategic objective: MVP completion with functional proof
- Real ACP routing: NOT ADMITTED
- Routing implementation: HOLD
- ACPMessage dispatch: HOLD
- Analysis generation: HOLD
- runtime pipeline execution: NOT ADMITTED
- downstream pipeline logic: NOT ADMITTED
- merge to `main`: NOT PERFORMED

## Preparation Question

What must be defined before real ACP routing can be reviewed for admission?

## Verdict

Verdict:

`ROUTING PREPARATION COMPLETE FOR BOUNDARY REVIEW — IMPLEMENTATION STILL ON HOLD`

Sprint 4 may proceed toward workflow expansion review and real routing boundary review.

This document does not admit routing implementation.

The routing preparation required before a boundary review is now defined at a planning level.

## Routing Objective

For Sprint 4 MVP purposes, routing must be understood as a bounded internal preparation step.

A future minimal routing result may answer only:

- whether the ACPMessage is prepared for a next internal processing lane;
- whether it should remain held;
- whether additional review is required;
- whether it is not ready for routing.

Routing must not mean:

- dispatching to an agent;
- selecting a real agent;
- creating agent instructions;
- generating Analysis;
- invoking taxonomy behavior;
- invoking risk scoring;
- invoking governance behavior;
- rendering output;
- triggering runtime pipeline execution.

## MVP-Level Routing Goal

The Sprint 4 MVP-level routing goal is not full routing.

The MVP-level routing goal is to produce a bounded proof that the system can move from:

Input  
→ MDS bounded structure  
→ CMO bounded structure  
→ ACP structural chain  
→ Protocol Router readiness  
→ controlled routing preparation or minimal non-dispatch routing result  
→ MVP functional proof output

This routing goal must remain non-dispatching.

## Route Target Taxonomy — Preparation

Before real routing can be admitted, route target categories must be bounded.

The first route target taxonomy must be minimal and non-dispatching.

Candidate route target categories for future review:

- `hold_for_review`
- `ready_for_future_analysis_boundary`
- `requires_additional_validation`
- `not_ready_for_routing`
- `routing_deferred`

These are preparation candidates only.

They are not yet implemented.

## Allowed Route Types — Preparation

Future minimal routing may only consider non-dispatch route types.

Candidate allowed route types:

- `route_ready_no_dispatch`
- `hold_for_additional_validation`
- `not_ready_for_routing`
- `requires_future_boundary_review`
- `mvp_proof_route_marker`

These route types must not create dispatch behavior.

These route types must not call agents.

These route types must not generate Analysis.

## Forbidden Route Types

The following route types remain forbidden:

- direct agent dispatch;
- direct agent assignment;
- direct Analysis generation route;
- direct taxonomy route;
- direct risk scoring route;
- direct governance route;
- direct output rendering route;
- runtime execution route;
- downstream pipeline route;
- external system route;
- cloud/API route;
- telemetry route.

## No-Dispatch Rule

The no-dispatch rule is mandatory.

A future routing result must not:

- dispatch an ACPMessage;
- call an agent;
- select a concrete agent;
- produce a dispatch target;
- create an agent instruction;
- trigger runtime pipeline behavior.

Any dispatch behavior requires a separate future boundary review and is not part of Sprint 4 MVP proof unless explicitly admitted later.

## No-Agent-Instruction Rule

Routing must not create agent instructions.

Forbidden:

- agent task generation;
- agent prompt generation;
- agent assignment;
- agent priority assignment;
- agent-specific instruction payload;
- hidden orchestration instructions.

A future router may produce only bounded status and route-preparation markers unless a separate boundary admits more.

## No-Analysis-Generation Rule

Routing must not generate Analysis.

Routing must not call:

- Evidence Analysis;
- Narrative Analysis;
- Cognitive Analysis;
- taxonomy modules;
- risk scoring modules;
- governance modules;
- output modules.

Any Analysis boundary must be separately reviewed and admitted after MVP routing proof work.

## Route Result Output Shape — Preparation

A future minimal route result may only expose a bounded output shape.

Candidate allowed fields:

- `routing_result_status`
- `source_stage`
- `target_stage`
- `protocol_router_readiness_status`
- `acp_scope_status`
- `acp_schema_validation_status`
- `acp_message_status`
- `acp_bundle_status`
- `decomposition_result`
- `field_envelope`

Candidate routing result statuses:

- `route_ready_no_dispatch`
- `hold_for_additional_validation`
- `not_ready_for_routing`
- `requires_future_boundary_review`
- `mvp_proof_route_marker`

Forbidden fields:

- `routing_decision`
- `agent_route`
- `dispatch_target`
- `agent_id`
- `agent_instruction`
- `selected_agent`
- `route_table`
- `analysis_bundle`
- `taxonomy_labels`
- `risk_profile`
- `governance_signal`
- `output_payload`

## MVP Functional Proof Implication

Sprint 4 MVP functional proof does not require full real routing.

The MVP proof may be acceptable if it demonstrates either:

1. Protocol Router readiness plus routing preparation status; or
2. a minimal non-dispatch routing result admitted by a future boundary review.

The preferred target is a minimal non-dispatch routing result, but only if the workflow expansion review and real routing boundary review admit it safely.

## Failure Modes To Control

Future routing work must control the following failure modes:

1. Routing-as-dispatch drift.
2. Agent instruction leakage.
3. Hidden Analysis activation.
4. Route target ambiguity.
5. Scope Guard bypass.
6. Schema Validator bypass.
7. Route table overreach.
8. Premature downstream coupling.
9. Analysis-family shortcut.
10. Runtime pipeline activation by implication.
11. User-visible output leakage.
12. Governance bypass.
13. Taxonomy/risk premature activation.
14. Merge-to-main before MVP proof safeguards.

## Required Workflow Review Before Implementation

Before any routing implementation, Sprint 4 must complete:

- `docs/sprint_4/SPRINT_4_WORKFLOW_EXPANSION_REVIEW.md`

That review must decide whether the current Python Tests workflow is sufficient or whether it must be expanded.

It must specifically consider:

- no-dispatch regression tests;
- no-agent-instruction regression tests;
- no-analysis-generation regression tests;
- no-runtime-execution regression tests;
- no-forbidden-field tests;
- ACP end-to-end smoke test;
- package-level import test;
- contract test grouping.

## Required Boundary Review Before Implementation

Before any routing implementation, Sprint 4 must complete:

- `docs/sprint_4/SPRINT_4_REAL_ROUTING_BOUNDARY_REVIEW.md`

That document must decide whether minimal non-dispatch routing can be admitted.

It must not automatically admit routing merely because preparation is complete.

## Required MVP Proof Plan

Before Sprint 4 closure, the project must complete:

- `docs/sprint_4/SPRINT_4_MVP_FUNCTIONAL_PROOF_PLAN.md`

That document must define:

- the proof input;
- the admitted chain;
- expected status transitions;
- expected preserved structures;
- forbidden fields;
- proof tests;
- closure criteria.

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

## Required Safeguards For Future Routing Boundary

A future routing boundary must preserve the following safeguards:

1. Routing must remain non-dispatching unless dispatch is separately admitted.
2. Routing must not create agent instructions.
3. Routing must not call Analysis modules.
4. Routing must not call taxonomy, risk, governance, or output modules.
5. Routing must not trigger runtime pipeline execution.
6. Routing must not expose downstream-ready payloads.
7. Routing must preserve the original bounded MDS DecompositionResult.
8. Routing must preserve the existing CMO field envelope.
9. Routing must preserve Protocol Router readiness status.
10. Tests must prove forbidden fields are absent.
11. Workflow coverage must be reviewed before implementation.
12. MVP functional proof must remain local and reproducible.

## Sprint 4 MVP Alignment

This routing preparation review supports the Sprint 4 MVP completion target.

Sprint 4 must not close as a documentation-only routing sprint unless MVP functional proof is explicitly blocked.

The preferred Sprint 4 outcome remains:

- bounded routing or routing-readiness proof;
- workflow/test expansion where required;
- MVP functional proof plan;
- MVP functional proof implementation;
- MVP proof closure note;
- Sprint 4 closure readiness review;
- Sprint 4 exit audit snapshot.

## No-Drift Confirmation

Confirmed:

- Sprint 3 closure state remains preserved.
- Sprint 4 is open for controlled MVP completion work.
- Routing preparation is refined.
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

## Recommended Next Step

Recommended next document:

- `docs/sprint_4/SPRINT_4_WORKFLOW_EXPANSION_REVIEW.md`

After workflow expansion review, the next document should be:

- `docs/sprint_4/SPRINT_4_REAL_ROUTING_BOUNDARY_REVIEW.md`

Then:

- `docs/sprint_4/SPRINT_4_MVP_FUNCTIONAL_PROOF_PLAN.md`

## Verdict Summary

Sprint 4 Routing Preparation Review: COMPLETE.

Routing preparation: DEFINED.

Real ACP routing: NOT ADMITTED BY THIS DOCUMENT.

Routing implementation: HOLD.

Dispatch target creation: HOLD.

Agent instruction creation: HOLD.

ACPMessage dispatch: HOLD.

Analysis generation: HOLD.

Runtime pipeline execution: NOT ADMITTED.

Downstream pipeline logic: NOT ADMITTED.

Recommended next document:

- `SPRINT_4_WORKFLOW_EXPANSION_REVIEW.md`
