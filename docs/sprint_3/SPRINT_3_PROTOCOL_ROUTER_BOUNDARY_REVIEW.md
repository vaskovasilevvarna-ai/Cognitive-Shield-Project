# Sprint 3 Protocol Router Boundary Review

Status: Boundary review — before admitting Agent Communication Protocol (ACP) Protocol Router behavior.

## Purpose

This document records the Sprint 3 boundary review after the Routing-Adjacent Workflow Review.

The purpose is to decide whether the project may admit a minimal Protocol Router boundary while preventing drift into real ACP routing, ACPMessage dispatch, agent routing, agent orchestration, dispatch target creation, agent instruction creation, Analysis generation, runtime pipeline execution, downstream pipeline logic, taxonomy behavior, risk scoring, governance behavior, or output rendering.

This review does not admit implementation by itself.

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

Current validation status:

- Python Tests workflow: GREEN
- Current Python Tests workflow: sufficient for Protocol Router boundary review
- Current Python Tests workflow: sufficient for future minimal router readiness only if non-routing
- Workflow expansion: required before real routing, dispatch, agent orchestration, Analysis, runtime, or downstream behavior

Current ACP state:

ACP boundary eligibility  
→ ACP minimal envelope  
→ ACPBundle  
→ ACPMessage  
→ ACP Schema Validator  
→ ACP Scope Guard

Current restricted areas:

- Protocol Router behavior: HOLD until this boundary is accepted
- ACP routing: HOLD
- ACPMessage dispatch: HOLD
- agent routing: HOLD
- agent orchestration: HOLD
- routing decision creation: HOLD
- dispatch target creation: HOLD
- agent instruction creation: HOLD
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

## Boundary Question

Can the project admit a minimal Protocol Router boundary as the next Sprint 3 ACP-layer micro-slice?

## Verdict

Verdict:

`ADMIT REVIEW WITH HARD SAFEGUARDS`

The project may admit a future minimal Protocol Router implementation only if it remains:

- router-readiness-only;
- Scope Guard-derived;
- structural only;
- non-routing;
- non-dispatching;
- non-orchestrating;
- non-analytical;
- non-runtime;
- not real ACP routing;
- not dispatch target creation;
- not agent instruction creation;
- not Analysis generation;
- not downstream pipeline logic.

This boundary review does not yet implement Protocol Router behavior.

## Critical Boundary Distinction

ACP Scope Guard behavior is not Protocol Router behavior.

Protocol Router readiness is not real ACP routing.

Protocol Router readiness is not a routing decision.

Protocol Router readiness is not a dispatch target.

Protocol Router readiness is not ACPMessage dispatch.

Protocol Router readiness is not agent orchestration.

Protocol Router readiness is not Analysis generation.

Protocol Router readiness is only a bounded readiness check over an already scope-allowed ACP structural message.

It may determine whether a schema-valid and scope-allowed ACPMessage is structurally ready for a future router layer.

It must not decide where the message goes.

It must not select an agent.

It must not create dispatch targets.

It must not create agent instructions.

It must not call Analysis modules.

It must not execute runtime pipeline behavior.

## Admitted Future Scope

The future implementation may include only:

- reading an existing ACP Scope Guard result;
- checking whether the scope status is `acp_scope_allowed`;
- preserving the original bounded MDS DecompositionResult;
- preserving the existing CMO field envelope;
- preserving the ACPBundle status;
- preserving the ACPMessage status;
- preserving the ACP schema validation status;
- preserving the ACP scope status;
- returning a minimal Protocol Router readiness status;
- returning source and target stage identity;
- exposing a minimal router readiness result;
- testing that no actual routing, dispatch, agent instruction, Analysis, taxonomy, risk, governance, output, or runtime fields are exposed.

Allowed Protocol Router readiness statuses may include:

- `protocol_router_ready`
- `protocol_router_not_ready`

## Not Admitted

The following remain not admitted:

- real ACP routing;
- ACPMessage dispatch;
- agent routing;
- agent orchestration;
- routing decision creation;
- dispatch target creation;
- agent instruction creation;
- route selection;
- agent selection;
- route table behavior;
- dynamic protocol routing;
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

## Hard Safeguards

Any future implementation after this review must preserve the following safeguards:

1. The behavior must remain a minimal Protocol Router readiness boundary only.
2. The behavior must require an existing ACP Scope Guard result.
3. The behavior must require or check `acp_scope_allowed` status.
4. The behavior must preserve the original bounded MDS DecompositionResult.
5. The behavior must preserve the existing CMO field envelope.
6. The behavior must preserve the ACPBundle status.
7. The behavior must preserve the ACPMessage status.
8. The behavior must preserve the ACP schema validation status.
9. The behavior must preserve the ACP scope status.
10. The behavior must not create a routing decision.
11. The behavior must not create a dispatch target.
12. The behavior must not create agent instructions.
13. The behavior must not select an agent.
14. The behavior must not route anything.
15. The behavior must not dispatch anything to agents.
16. The behavior must not orchestrate agent communication.
17. The behavior must not call Analysis modules.
18. The behavior must not call taxonomy, risk, governance, or output modules.
19. The behavior must not infer hidden or implicit meaning.
20. The behavior must not assess truth.
21. The behavior must not assess evidence.
22. The behavior must not create relation objects.
23. The behavior must not create risk signals.
24. The behavior must not trigger runtime pipeline execution.
25. The original Scope Guard result must be preserved unchanged or wrapped without semantic mutation.
26. Tests must prove that forbidden routing, dispatch, agent instruction, Analysis, taxonomy, risk, governance, output, and runtime fields are absent.
27. Closure documentation must state that real ACP routing, ACPMessage dispatch, Analysis generation, runtime execution, and downstream logic remain on HOLD.

## Candidate Function Name

Preferred function name:

- `check_protocol_router_readiness`

Acceptable alternatives:

- `check_acp_router_readiness`
- `build_protocol_router_readiness_status`

Function names should avoid:

- `route_to_agent`
- `select_agent`
- `dispatch_to_agents`
- `create_routing_decision`
- `create_dispatch_target`
- `orchestrate_agents`
- `run_protocol_router`
- `run_pipeline`
- `generate_analysis`
- `analyze`
- `score`
- `evaluate`

## Recommended Source Area

Preferred source file:

- `src/cognitive_shield/core/agent_communication_protocol_acp/router_readiness.py`

Alternative:

- `src/cognitive_shield/core/agent_communication_protocol_acp/router.py`

Preferred choice:

Use a separate `router_readiness.py` file for the first bounded implementation.

Reason:

The existing `router.py` scaffold should remain untouched until a broader Protocol Router design pass is admitted.

A separate readiness file keeps the current behavior explicitly bounded, reversible, non-routing, and non-dispatching.

The `contracts.py`, `schemas.py`, `schema_validator.py`, `scope_guard.py`, `contradiction_registrar.py`, `uncertainty_propagator.py`, and `synthesis_exporter.py` files should remain untouched until their own boundary reviews.

## Admitted Output Shape

A future minimal Protocol Router readiness helper may return a minimal dictionary containing only fields such as:

- `protocol_router_readiness_status`
- `source_stage`
- `target_stage`
- `acp_scope_status`
- `acp_schema_validation_status`
- `acp_message_status`
- `acp_bundle_status`
- `decomposition_result`
- `field_envelope`

Allowed Protocol Router readiness statuses:

- `protocol_router_ready`
- `protocol_router_not_ready`

The minimal router readiness result must not expose:

- `agent_route`
- `routing_decision`
- `dispatch_target`
- `agent_id`
- `agent_instruction`
- `selected_agent`
- `route_table`
- `analysis_bundle`
- `evidence_analysis_output`
- `narrative_analysis_output`
- `cognitive_analysis_output`
- `taxonomy_labels`
- `risk_profile`
- `governance_signal`
- `output_payload`
- `truth_value`
- `evidence_assessment`

## Required Test Boundary

Future tests may verify:

- a valid ACP Scope Guard result returns `protocol_router_ready`;
- a rejected ACP Scope Guard result returns `protocol_router_not_ready`;
- empty input returns `protocol_router_not_ready`;
- the original bounded MDS DecompositionResult is preserved unchanged;
- the existing CMO field envelope is preserved unchanged;
- source stage is CMO;
- target stage is ACP;
- no routing decision fields are exposed;
- no dispatch target fields are exposed;
- no agent instruction fields are exposed;
- no selected agent fields are exposed;
- no Analysis fields are exposed;
- no taxonomy, risk, governance, output, truth, evidence, relation, or runtime fields are exposed.

Future tests must not verify:

- real ACP routing;
- ACPMessage dispatch;
- agent dispatch;
- agent orchestration;
- route selection;
- agent selection;
- route table behavior;
- Analysis generation;
- truth assessment;
- evidence assessment;
- taxonomy labeling;
- risk scoring;
- governance behavior;
- output rendering;
- downstream pipeline behavior.

## Workflow Coverage Note

The current Python Tests workflow is sufficient for Protocol Router boundary review.

The current Python Tests workflow is also sufficient for a future minimal router readiness implementation only if that implementation remains non-routing and structural.

Workflow expansion is required before real routing, dispatch, agent orchestration, Analysis-adjacent behavior, runtime behavior, or downstream behavior.

## Documentation Discipline

This boundary review is justified because Protocol Router is the first routing-adjacent ACP layer after ACP Scope Guard.

A closure note is required only if Protocol Router readiness behavior is implemented.

Small repository checks may remain in chat unless they reveal a blocker.

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
- Protocol Router behavior is admitted only as a future review-approved readiness boundary.
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

## Recommended Next Step

Recommended next step:

If this review is accepted, create the Protocol Router readiness pass in compressed mode:

1. source file;
2. test file;
3. closure note.

Recommended files:

- `src/cognitive_shield/core/agent_communication_protocol_acp/router_readiness.py`
- `tests/unit/test_acp_router_readiness.py`
- `docs/sprint_3/SPRINT_3_PROTOCOL_ROUTER_READINESS_PASS_CLOSURE_NOTE.md`

## Verdict Summary

Protocol Router boundary: ADMITTED FOR CONTROLLED READINESS IMPLEMENTATION WITH HARD SAFEGUARDS.

Real ACP routing: HOLD.

ACPMessage dispatch: HOLD.

Agent orchestration: HOLD.

Analysis generation: HOLD.

Runtime pipeline execution: NOT ADMITTED.

Downstream pipeline logic: NOT ADMITTED.
