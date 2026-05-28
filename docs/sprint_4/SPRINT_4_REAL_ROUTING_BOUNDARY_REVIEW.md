# Sprint 4 Real Routing Boundary Review

Status: Boundary review — before admitting minimal non-dispatch Agent Communication Protocol (ACP) routing result.

## Purpose

This document records the Sprint 4 boundary review for deciding whether a minimal real routing result may be admitted for MVP functional proof.

Sprint 4 has already established that it is the MVP completion phase and that workflow expansion is required for MVP proof.

The purpose of this document is to admit only a minimal, non-dispatch routing result if it can support MVP functional proof without introducing dispatch, agent instruction creation, Analysis generation, runtime pipeline execution, downstream pipeline logic, taxonomy behavior, risk scoring, governance behavior, or output rendering.

This document does not admit full routing.

This document does not admit ACPMessage dispatch.

This document does not admit agent routing or agent orchestration.

This document does not admit Analysis generation.

This document does not admit runtime pipeline execution or downstream pipeline logic.

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
- Sprint 4 Workflow Expansion Review
- Sprint 4 Test Structure Expansion Boundary Review
- Sprint 4 Test Structure Expansion Pass
- Sprint 4 Workflow Discovery Check
- Sprint 4 Workflow Update Boundary Review
- Sprint 4 Workflow Update Pass

Current validation status:

- Python Tests workflow: GREEN
- Workflow test discovery: EXPANDED
- Unit tests: INCLUDED
- Contract tests: INCLUDED
- Smoke tests: INCLUDED
- Sprint 4 strategic objective: MVP completion with functional proof
- Routing preparation: DEFINED
- Real ACP routing: NOT YET ADMITTED
- ACPMessage dispatch: HOLD
- Analysis generation: HOLD
- runtime pipeline execution: NOT ADMITTED
- downstream pipeline logic: NOT ADMITTED
- merge to `main`: NOT PERFORMED

## Boundary Question

Can Sprint 4 admit a minimal non-dispatch routing result for MVP functional proof?

## Verdict

Verdict:

`ADMIT MINIMAL NON-DISPATCH ROUTING RESULT WITH HARD SAFEGUARDS`

Sprint 4 may admit a minimal routing result only if it remains:

- Protocol Router readiness-derived;
- non-dispatching;
- non-orchestrating;
- non-analytical;
- non-runtime;
- bounded to route-preparation status only;
- not ACPMessage dispatch;
- not agent selection;
- not agent instruction creation;
- not Analysis generation;
- not downstream pipeline logic.

This boundary review does not yet implement routing.

It only defines the admissible shape and safeguards for a future minimal routing result pass.

## Critical Boundary Distinction

Protocol Router readiness is not routing.

Minimal routing result is not dispatch.

Minimal routing result is not agent selection.

Minimal routing result is not agent instruction creation.

Minimal routing result is not ACPMessage dispatch.

Minimal routing result is not Analysis generation.

Minimal routing result is not runtime pipeline execution.

Minimal routing result is not downstream pipeline logic.

For Sprint 4 MVP proof, routing may only mean a bounded internal status result showing that the admitted ACP chain can produce a controlled route-preparation marker.

It must not move work to an agent.

It must not create a real route table.

It must not execute the pipeline.

It must not call downstream analysis modules.

## Admitted Future Scope

A future minimal routing implementation may include only:

- reading an existing Protocol Router readiness result;
- checking whether the readiness status is `protocol_router_ready`;
- preserving the original bounded MDS DecompositionResult;
- preserving the existing CMO field envelope;
- preserving ACP Scope Guard status;
- preserving ACP Schema Validator status;
- preserving ACPMessage status;
- preserving ACPBundle status;
- returning a minimal routing result status;
- returning source and target stage identity;
- exposing a bounded non-dispatch routing result;
- testing that no dispatch, agent instruction, selected agent, Analysis, taxonomy, risk, governance, output, runtime, or downstream fields are exposed.

Allowed minimal routing statuses:

- `route_ready_no_dispatch`
- `hold_for_additional_validation`
- `not_ready_for_routing`
- `requires_future_boundary_review`
- `mvp_proof_route_marker`

## Recommended Source Area

Preferred source file for a future implementation pass:

- `src/cognitive_shield/core/agent_communication_protocol_acp/routing_result.py`

Do not edit:

- `src/cognitive_shield/core/agent_communication_protocol_acp/router.py`

Reason:

`router.py` should remain untouched until a fuller Protocol Router behavior boundary is admitted.

A separate `routing_result.py` keeps the Sprint 4 MVP routing proof bounded, reversible, and non-dispatching.

## Recommended Function Name

Preferred function name:

- `build_minimal_routing_result`

Acceptable alternatives:

- `build_non_dispatch_routing_result`
- `create_mvp_routing_marker`

Function names should avoid:

- `route_to_agent`
- `select_agent`
- `dispatch_to_agent`
- `create_dispatch_target`
- `create_agent_instruction`
- `run_router`
- `run_pipeline`
- `generate_analysis`
- `analyze`
- `score`
- `evaluate`

## Admitted Output Shape

A future minimal routing result helper may return only fields such as:

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

Forbidden fields:

- `routing_decision`
- `agent_route`
- `dispatch_target`
- `agent_id`
- `selected_agent`
- `agent_instruction`
- `route_table`
- `analysis_bundle`
- `evidence_analysis_output`
- `narrative_analysis_output`
- `cognitive_analysis_output`
- `taxonomy_labels`
- `risk_profile`
- `governance_signal`
- `output_payload`
- `runtime_pipeline`
- `runtime_event`
- `downstream_pipeline`
- `pipeline_dispatch`

## Required Test Boundary

A future test file should verify:

- a ready Protocol Router readiness result creates a minimal routing result;
- a non-ready Protocol Router readiness result does not create a ready routing result;
- empty input returns a non-ready routing status;
- original `decomposition_result` is preserved unchanged;
- original `field_envelope` is preserved unchanged;
- source stage is preserved or defaults safely;
- target stage is preserved or defaults safely;
- no dispatch target is exposed;
- no agent instruction is exposed;
- no selected agent is exposed;
- no route table is exposed;
- no Analysis bundle is exposed;
- no taxonomy, risk, governance, output, runtime, or downstream fields are exposed.

Future tests must not verify:

- real ACPMessage dispatch;
- agent dispatch;
- agent orchestration;
- route table behavior;
- Analysis generation;
- truth assessment;
- evidence assessment;
- taxonomy labeling;
- risk scoring;
- governance behavior;
- output rendering;
- downstream pipeline behavior.

## MVP Functional Proof Relationship

The minimal routing result is admitted only because Sprint 4 must produce MVP functional proof.

The MVP proof may use the minimal routing result as the final admitted routing-side marker:

Input  
→ MDS bounded structure  
→ CMO bounded structure  
→ ACP structural chain  
→ Protocol Router readiness  
→ minimal non-dispatch routing result  
→ MVP proof object

This routing result must remain internal and non-dispatching.

It must not become a product runtime router.

## Workflow Relationship

The Python Tests workflow has been expanded to discover:

- `tests/unit`
- `tests/contract`
- `tests/smoke`

Therefore, a future minimal routing result pass must include unit tests, and the later MVP functional proof must include smoke-level verification.

Python Tests workflow must be GREEN before accepting the pass as closed.

## Not Admitted

The following remain not admitted by this document:

- full ACP routing;
- routing decision creation beyond bounded non-dispatch status;
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

Any future minimal routing implementation must preserve the following safeguards:

1. Do not edit `router.py`.
2. Do not create dispatch targets.
3. Do not create agent instructions.
4. Do not select agents.
5. Do not expose route tables.
6. Do not dispatch ACPMessages.
7. Do not call Analysis modules.
8. Do not call taxonomy, risk, governance, or output modules.
9. Do not trigger runtime pipeline execution.
10. Do not introduce downstream pipeline logic.
11. Preserve original `decomposition_result`.
12. Preserve original `field_envelope`.
13. Preserve Protocol Router readiness status.
14. Return status-only routing result.
15. Include explicit forbidden-field tests.
16. Require Python Tests workflow GREEN.

## Recommended Next Pass

If this review is accepted, create the minimal routing result pass in compressed mode:

1. source file;
2. unit test file;
3. closure note.

Recommended files:

- `src/cognitive_shield/core/agent_communication_protocol_acp/routing_result.py`
- `tests/unit/test_acp_routing_result.py`
- `docs/sprint_4/SPRINT_4_MINIMAL_ROUTING_RESULT_PASS_CLOSURE_NOTE.md`

## Future Follow-Up

After a minimal routing result pass, the next required document should be:

- `docs/sprint_4/SPRINT_4_MVP_FUNCTIONAL_PROOF_PLAN.md`

That plan should define the MVP proof chain and the smoke test that verifies it.

## No-Drift Confirmation

Confirmed:

- Sprint 4 remains controlled.
- Workflow test discovery has been expanded.
- Minimal routing result is admitted only as a future non-dispatch result.
- Real dispatch remains on HOLD.
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

Sprint 4 Real Routing Boundary Review: COMPLETE.

Minimal non-dispatch routing result: ADMITTED FOR CONTROLLED IMPLEMENTATION WITH HARD SAFEGUARDS.

Full ACP routing: NOT ADMITTED.

ACPMessage dispatch: HOLD.

Agent instruction creation: HOLD.

Analysis generation: HOLD.

Runtime pipeline execution: NOT ADMITTED.

Downstream pipeline logic: NOT ADMITTED.

Recommended next pass:

- minimal routing result compressed pass.
