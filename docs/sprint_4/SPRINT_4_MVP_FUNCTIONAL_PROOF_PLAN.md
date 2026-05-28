# Sprint 4 MVP Functional Proof Plan

Status: MVP functional proof planning document — after Sprint 4 Real Routing Boundary Review.

## Purpose

This document defines the MVP functional proof plan for Sprint 4 of the Cognitive Shield repository work on branch `active/mvp-foundation`.

Sprint 4 is the MVP completion phase.

The purpose of this document is to define the minimal testable proof that Cognitive Shield works at MVP level by connecting the admitted bounded chain from input-derived structure through Message Decomposition Specification (MDS), Canonical Message Object (CMO), Agent Communication Protocol (ACP), Protocol Router readiness, and a minimal non-dispatch routing result.

This document does not admit implementation by itself.

This document does not admit full routing.

This document does not admit dispatch.

This document does not admit agent instruction creation.

This document does not admit Analysis generation, taxonomy behavior, risk scoring, governance behavior, output rendering, runtime pipeline execution, or downstream pipeline logic.

## Baseline

Sprint 3 closed with boundaries.

Sprint 3 delivered:

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
- Sprint 4 Real Routing Boundary Review

Current validation status:

- Python Tests workflow: GREEN
- Workflow test discovery: EXPANDED
- Unit tests: INCLUDED
- Contract tests: INCLUDED
- Smoke tests: INCLUDED
- Minimal non-dispatch routing result: ADMITTED FOR CONTROLLED IMPLEMENTATION
- MVP smoke tests: REQUIRED
- MVP functional proof: REQUIRED TARGET
- Full ACP routing: NOT ADMITTED
- ACPMessage dispatch: HOLD
- Analysis generation: HOLD
- runtime pipeline execution: NOT ADMITTED
- downstream pipeline logic: NOT ADMITTED
- merge to `main`: NOT PERFORMED

## Proof Question

What must Sprint 4 prove for Cognitive Shield to reach MVP-level functional proof?

## Verdict

Verdict:

`MVP FUNCTIONAL PROOF MAY BE PLANNED WITH MINIMAL NON-DISPATCH ROUTING RESULT`

Sprint 4 may proceed toward an MVP functional proof that includes a minimal non-dispatch routing result.

The proof must remain bounded, local, reproducible, and non-runtime.

The proof must demonstrate that the admitted system chain works without silently introducing forbidden downstream behavior.

## MVP Functional Proof Definition

For Sprint 4, MVP functional proof means:

- a single controlled input can move through the admitted bounded chain;
- the chain produces expected structural status outputs;
- key intermediate structures are preserved;
- the proof includes a minimal non-dispatch routing result;
- the proof is covered by smoke-level testing;
- Python Tests workflow returns GREEN;
- no forbidden downstream behavior is introduced.

MVP functional proof does not mean:

- full disinformation detection;
- full Evidence Analysis;
- full Narrative Analysis;
- full Cognitive Analysis;
- taxonomy labeling;
- risk scoring;
- governance decision;
- explainable interface rendering;
- education behavior;
- runtime product execution;
- agent dispatch;
- production readiness.

## Required MVP Proof Chain

The Sprint 4 MVP functional proof should follow this admitted chain:

Input behavior nucleus  
→ Message Decomposition Specification (MDS) bounded structure  
→ bounded MDS DecompositionResult  
→ MDS-to-Canonical Message Object (CMO) boundary eligibility  
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
→ minimal non-dispatch routing result  
→ MVP proof object

The chain must not skip validation layers.

The chain must not bypass ACP Schema Validator.

The chain must not bypass ACP Scope Guard.

The chain must not bypass Protocol Router readiness.

## Minimal Non-Dispatch Routing Result Role

The minimal routing result is the final routing-side marker in the MVP proof.

It may show only that the admitted chain can produce a bounded route-preparation result.

It must remain:

- non-dispatching;
- non-orchestrating;
- non-analytical;
- non-runtime;
- status-only;
- local;
- reproducible;
- testable.

It must not create:

- dispatch target;
- selected agent;
- agent instruction;
- route table;
- Analysis bundle;
- taxonomy labels;
- risk profile;
- governance signal;
- output payload;
- runtime pipeline event;
- downstream pipeline dispatch.

## Recommended Minimal Routing Result Pass

Before implementing the MVP proof smoke test, Sprint 4 should implement the minimal routing result pass.

Recommended files:

- `src/cognitive_shield/core/agent_communication_protocol_acp/routing_result.py`
- `tests/unit/test_acp_routing_result.py`
- `docs/sprint_4/SPRINT_4_MINIMAL_ROUTING_RESULT_PASS_CLOSURE_NOTE.md`

This pass should be completed and Python Tests workflow should return GREEN before MVP proof smoke test implementation begins.

## MVP Proof Source Area

After the minimal routing result pass, the MVP functional proof may use a dedicated proof helper.

Preferred source file:

- `src/cognitive_shield/app/mvp_functional_proof.py`

Alternative:

- `src/cognitive_shield/app/single_message_pass/mvp_functional_proof.py`

Preferred choice:

Use:

- `src/cognitive_shield/app/mvp_functional_proof.py`

Reason:

The MVP proof is application-level proof wiring.

It should not be placed inside MDS, CMO, or ACP packages.

It should not mutate core architecture modules.

It should connect admitted modules only.

## MVP Proof Function Name

Preferred function name:

- `run_mvp_functional_proof`

Acceptable alternatives:

- `build_mvp_functional_proof`
- `run_single_message_mvp_proof`

Function names should avoid:

- `run_pipeline`
- `dispatch_to_agent`
- `generate_analysis`
- `score_risk`
- `render_output`
- `execute_runtime`

Reason:

The MVP proof is not full runtime pipeline execution.

It is a bounded proof helper.

## MVP Proof Object Shape

A future MVP proof helper may return a minimal dictionary containing only fields such as:

- `mvp_proof_status`
- `input_status`
- `decomposition_result_status`
- `cmo_status`
- `acp_boundary_status`
- `acp_envelope_status`
- `acp_bundle_status`
- `acp_message_status`
- `acp_schema_validation_status`
- `acp_scope_status`
- `protocol_router_readiness_status`
- `routing_result_status`
- `decomposition_result`
- `field_envelope`

Allowed MVP proof statuses:

- `mvp_functional_proof_created`
- `mvp_functional_proof_not_ready`

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

## MVP Smoke Test Requirement

Sprint 4 must include at least one smoke test proving the MVP functional proof works.

Recommended file:

- `tests/smoke/test_mvp_functional_proof.py`

The smoke test should verify:

- the MVP proof helper returns `mvp_functional_proof_created`;
- admitted status fields are present;
- `decomposition_result` is preserved;
- `field_envelope` is preserved;
- minimal non-dispatch routing result is included;
- no forbidden routing / dispatch / Analysis / runtime / downstream fields are exposed.

## MVP Smoke Test Input

The MVP proof should use a small, deterministic input.

Suggested input:

```text
Public claim example for MVP proof.
