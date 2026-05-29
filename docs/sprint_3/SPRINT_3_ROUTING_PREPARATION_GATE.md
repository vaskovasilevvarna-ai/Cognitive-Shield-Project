# Sprint 3 Routing Preparation Gate

Status: Final Sprint 3 control document — non-coding routing preparation gate.

## Purpose

This document records the final Sprint 3 control gate after the Real Routing Admission Review.

The purpose is to define what must be prepared before real Agent Communication Protocol (ACP) routing can be considered in a later sprint.

This document does not admit implementation.

This document does not admit real routing.

This document does not admit edits to `router.py`.

This document does not admit ACPMessage dispatch, agent routing, agent orchestration, Analysis generation, runtime pipeline execution, downstream pipeline logic, taxonomy behavior, risk scoring, governance behavior, or output rendering.

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
- Real Routing Admission Review

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

## Gate Question

What must be prepared before real ACP routing can be considered?

## Gate Verdict

Verdict:

`ROUTING PREPARATION ONLY — REAL ROUTING REMAINS DEFERRED`

Sprint 3 may record routing preparation requirements, but must not implement routing.

Real ACP routing remains deferred beyond the current Sprint 3 implementation scope.

This gate closes the routing-adjacent preparation logic for Sprint 3.

## Why This Gate Exists

Protocol Router readiness confirmed that a schema-valid and scope-allowed ACPMessage can be marked structurally ready for future router consideration.

However, readiness is not routing.

Real routing would introduce a new behavioral class:

- routing decision creation;
- route selection;
- dispatch target creation;
- agent instruction creation;
- agent selection;
- route table behavior;
- downstream flow expectations.

These behaviors require stronger safeguards, additional workflow review, and separate boundary documentation before implementation.

## Routing Objective Definition

Before real routing can be admitted, the project must define the routing objective.

A future routing objective must answer:

- what the router is allowed to decide;
- what it is forbidden to decide;
- whether it selects a route family, a module family, or a processing lane;
- whether it remains purely structural or becomes operational;
- whether routing produces an internal readiness marker or a downstream action object.

At this stage, routing objective is not yet defined.

Therefore, real routing remains on HOLD.

## Route Target Taxonomy Requirement

Before real routing can be implemented, the project must define a route target taxonomy.

This taxonomy must distinguish at minimum:

- non-dispatch route categories;
- analysis-preparation categories;
- validation-only categories;
- hold / reject categories;
- escalation-needed categories;
- future agent-family categories.

No route target taxonomy is admitted yet.

No route target is implemented.

No route table is implemented.

## Allowed Route Types — Future Requirement

A future real routing boundary must define allowed route types.

Possible allowed route types may include only bounded non-dispatch types at first, such as:

- `route_ready_no_dispatch`
- `hold_for_additional_validation`
- `not_ready_for_routing`
- `requires_future_boundary_review`

These are not admitted now.

They are only preparation candidates for future review.

## Forbidden Route Types

The following route types remain forbidden unless separately admitted later:

- direct agent dispatch;
- direct Analysis generation route;
- direct taxonomy route;
- direct risk scoring route;
- direct governance route;
- direct output rendering route;
- runtime execution route;
- external system route;
- cloud/API route;
- telemetry route.

## No-Dispatch Rule

Any future routing implementation must preserve a strict no-dispatch rule unless dispatch is separately admitted.

Routing must not automatically dispatch ACPMessages.

Routing must not call agents.

Routing must not create dispatch targets.

Routing must not create agent instructions.

Routing must not execute runtime pipeline behavior.

## No-Agent-Instruction Rule

A future router must not create agent instructions unless a separate Agent Instruction Boundary Review is completed.

Forbidden at this stage:

- agent task generation;
- agent prompt generation;
- agent assignment;
- agent priority assignment;
- agent-specific instruction payloads;
- hidden orchestration instructions.

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

Any future Analysis boundary must be separately reviewed and admitted.

## Route Result Output Shape — Future Requirement

Before routing can be implemented, the project must define a bounded route result output shape.

A future route result may only be considered if it avoids dispatch and downstream execution.

Potential future fields may include:

- `routing_readiness_status`
- `route_preparation_status`
- `source_stage`
- `target_stage`
- `acp_scope_status`
- `protocol_router_readiness_status`
- `decomposition_result`
- `field_envelope`

Forbidden fields remain:

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

## Failure Modes To Address Before Real Routing

A future routing boundary must address at least the following failure modes:

1. Routing-as-dispatch drift.
2. Agent instruction leakage.
3. Hidden analysis activation.
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
14. Merge-to-main before routing safeguards.

## Workflow Coverage Expansion Requirement

Before any real routing implementation, a new workflow coverage review is required.

The review must decide whether to add or expand checks for:

- routing no-dispatch tests;
- no-agent-instruction tests;
- no-analysis-generation tests;
- no-runtime-execution tests;
- forbidden-field regression tests;
- ACP package integration smoke tests;
- contract tests;
- package import tests;
- static checks or linting.

Current Python Tests workflow remains sufficient for bounded readiness behavior only.

It is not sufficient by itself for real routing implementation.

## Required Tests Before Future Routing

A future routing implementation cannot be admitted without tests proving:

- no dispatch target is created;
- no agent instruction is created;
- no selected agent is created;
- no route table is exposed unless separately admitted;
- no Analysis bundle is created;
- no taxonomy labels are created;
- no risk profile is created;
- no governance signal is created;
- no output payload is created;
- no runtime pipeline execution is triggered;
- original DecompositionResult is preserved;
- field envelope is preserved;
- ACP Scope Guard result is preserved;
- Protocol Router readiness result is preserved.

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

## Sprint 3 Closure Implication

This document is intended as the final Sprint 3 control document before Sprint 3 closure review.

After this gate, the recommended next document is:

- `docs/sprint_3/SPRINT_3_CLOSURE_READINESS_REVIEW.md`

Sprint 3 should close at:

ACP boundary eligibility  
→ ACP minimal envelope  
→ ACPBundle  
→ ACPMessage  
→ ACP Schema Validator  
→ ACP Scope Guard  
→ Protocol Router readiness  
→ Routing Preparation Gate

Real routing should be deferred.

## Recommended Sprint 4 Entry

Sprint 4 should begin with:

- Sprint 4 Entry Control Pass;
- Routing Preparation Review;
- Workflow Expansion Review;
- Real Routing Boundary Review.

Sprint 4 should not begin with direct routing code.

## No-Drift Confirmation

Confirmed:

- Sprint 2 closure state remains preserved.
- Sprint 3 remains controlled.
- ACP boundary eligibility remains eligibility-only.
- ACP minimal envelope remains envelope-only.
- ACPBundle remains bundle-only.
- ACPMessage remains message-only.
- ACP Schema Validator remains schema-validation-only.
- ACP Scope Guard remains scope-check-only.
- Protocol Router readiness remains readiness-only.
- Routing Preparation Gate remains non-coding.
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

Routing Preparation Gate: COMPLETE.

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

- `SPRINT_3_CLOSURE_READINESS_REVIEW.md`

Recommended next sprint:

- Sprint 4 Routing Preparation / Real Routing Boundary work.
