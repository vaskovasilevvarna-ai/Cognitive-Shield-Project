# Sprint 3 ACPMessage Boundary Review

Status: Boundary review — before admitting Agent Communication Protocol (ACP) message behavior.

## Purpose

This document records the Sprint 3 boundary review after the controlled Agent Communication Protocol (ACP) bundle pass.

The purpose is to decide whether the project may admit a minimal ACPMessage boundary while preventing drift into ACP routing, ACPMessage dispatch, agent routing, agent orchestration, Protocol Router behavior, Analysis generation, runtime pipeline execution, downstream pipeline logic, taxonomy behavior, risk scoring, governance behavior, or output rendering.

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

Current validation status:

- Python Tests workflow: GREEN
- Current Python Tests workflow: sufficient for first ACP structural boundaries
- Workflow expansion: not required yet
- Workflow expansion checkpoint: required before routing-adjacent or Analysis-adjacent behavior

Current restricted areas:

- ACP routing: HOLD
- ACPMessage creation: HOLD until this boundary is accepted
- ACPMessage dispatch: HOLD
- agent routing: HOLD
- agent orchestration: HOLD
- Protocol Router behavior: HOLD
- Schema Validator behavior: HOLD
- Scope Guard behavior: HOLD
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

Can the project admit a minimal ACPMessage as the next Sprint 3 ACP-layer micro-slice?

## Verdict

Verdict:

`ADMIT REVIEW WITH HARD SAFEGUARDS`

The project may admit a future minimal ACPMessage implementation only if it remains:

- message-only;
- ACPBundle-derived;
- structural only;
- non-routing;
- non-dispatching;
- non-orchestrating;
- non-analytical;
- non-runtime;
- not Protocol Router behavior;
- not Analysis generation;
- not downstream pipeline logic.

This boundary review does not yet implement ACPMessage behavior.

## Critical Boundary Distinction

An ACPBundle is not an ACPMessage.

An ACPMessage is not ACP routing.

An ACPMessage is not ACPMessage dispatch.

An ACPMessage is not a routing decision.

An ACPMessage is not a dispatch target.

An ACPMessage is not agent orchestration.

An ACPMessage is not Protocol Router behavior.

An ACPMessage is not an Analysis input bundle.

An ACPMessage is only a bounded structural message container derived from an already admitted ACPBundle.

It must not route, dispatch, orchestrate, analyze, classify, score, govern, render, or execute anything.

## Admitted Future Scope

The future implementation may include only:

- reading an existing ACPBundle;
- checking whether the ACPBundle status is `acp_bundle_created`;
- preserving the original bounded MDS DecompositionResult;
- preserving the existing CMO field envelope;
- preserving the ACP envelope status;
- preserving the ACPBundle status;
- returning a minimal ACPMessage status;
- returning source and target stage identity;
- exposing a minimal ACPMessage-like structural object;
- testing that no routing, dispatch, Analysis, taxonomy, risk, governance, output, or runtime fields are exposed.

Allowed ACPMessage statuses may include:

- `acp_message_created`
- `not_ready_for_acp_message`

## Not Admitted

The following remain not admitted:

- ACP routing;
- ACPMessage dispatch;
- agent routing;
- agent orchestration;
- Protocol Router behavior;
- Scope Guard behavior beyond later boundary review;
- Schema Validator behavior beyond later boundary review;
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

1. The behavior must remain a minimal ACPMessage boundary only.
2. The behavior must require an existing ACPBundle.
3. The behavior must require `acp_bundle_created` status.
4. The behavior must preserve the original bounded MDS DecompositionResult.
5. The behavior must preserve the existing CMO field envelope.
6. The behavior must preserve the ACP envelope status.
7. The behavior must preserve the ACPBundle status.
8. The behavior must not create a routing decision.
9. The behavior must not create a dispatch target.
10. The behavior must not route anything.
11. The behavior must not dispatch anything to agents.
12. The behavior must not orchestrate agent communication.
13. The behavior must not call Protocol Router behavior.
14. The behavior must not call Schema Validator behavior.
15. The behavior must not call Scope Guard behavior.
16. The behavior must not call Analysis modules.
17. The behavior must not call taxonomy, risk, governance, or output modules.
18. The behavior must not infer hidden or implicit meaning.
19. The behavior must not assess truth.
20. The behavior must not assess evidence.
21. The behavior must not create relation objects.
22. The behavior must not create risk signals.
23. The behavior must not trigger runtime pipeline execution.
24. The original ACPBundle object must be preserved unchanged or wrapped without semantic mutation.
25. Tests must prove that forbidden routing, dispatch, Analysis, taxonomy, risk, governance, output, and runtime fields are absent.
26. Closure documentation must state that ACP routing, ACPMessage dispatch, Analysis generation, runtime execution, and downstream logic remain on HOLD.

## Candidate Function Name

Preferred function name:

- `build_acp_message`

Acceptable alternatives:

- `build_minimal_acp_message`
- `create_acp_message_minimal`

Function names should avoid:

- `route_to_agent`
- `dispatch_to_agents`
- `orchestrate_agents`
- `run_pipeline`
- `generate_analysis`
- `analyze`
- `score`
- `evaluate`

## Recommended Source Area

Preferred source file:

- `src/cognitive_shield/core/agent_communication_protocol_acp/message.py`

Reason:

The existing ACP scaffold files should remain stable.

The `cmo_boundary.py` file should remain focused on CMO-to-ACP boundary eligibility.

The `minimal_envelope.py` file should remain focused on ACP minimal envelope behavior.

The `bundle.py` file should remain focused on ACPBundle behavior.

The `router.py`, `contracts.py`, `schemas.py`, `schema_validator.py`, `scope_guard.py`, `contradiction_registrar.py`, `uncertainty_propagator.py`, and `synthesis_exporter.py` files should remain untouched until their own boundary reviews.

A separate `message.py` file keeps the ACPMessage boundary explicit and reversible.

## Admitted Output Shape

A future minimal ACPMessage helper may return a minimal dictionary containing only fields such as:

- `acp_message_status`
- `source_stage`
- `target_stage`
- `acp_bundle_status`
- `decomposition_result`
- `field_envelope`

Allowed ACPMessage statuses:

- `acp_message_created`
- `not_ready_for_acp_message`

The minimal ACPMessage must not expose:

- `agent_route`
- `routing_decision`
- `dispatch_target`
- `agent_id`
- `agent_instruction`
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

- a valid ACPBundle creates a minimal ACPMessage;
- a non-ready ACPBundle does not create an ACPMessage;
- the original bounded MDS DecompositionResult is preserved unchanged;
- the existing CMO field envelope is preserved unchanged;
- source stage is CMO;
- target stage is ACP;
- no routing fields are exposed;
- no dispatch fields are exposed;
- no agent instruction fields are exposed;
- no Analysis fields are exposed;
- no taxonomy, risk, governance, output, truth, evidence, relation, or runtime fields are exposed.

Future tests must not verify:

- ACP routing;
- ACPMessage dispatch;
- agent dispatch;
- agent orchestration;
- Protocol Router behavior;
- Schema Validator behavior;
- Scope Guard behavior;
- Analysis generation;
- truth assessment;
- evidence assessment;
- taxonomy labeling;
- risk scoring;
- governance behavior;
- output rendering;
- downstream pipeline behavior.

## Workflow Coverage Note

The current Python Tests workflow is sufficient for minimal ACPMessage structural behavior only if the implementation remains bounded and non-routing.

Workflow expansion is not required before minimal ACPMessage behavior.

However, workflow expansion review is required before routing-adjacent or Analysis-adjacent behavior, including:

- ACP routing;
- ACPMessage dispatch;
- Protocol Router behavior;
- Schema Validator behavior;
- Scope Guard behavior;
- Analysis generation;
- runtime pipeline execution;
- downstream pipeline logic.

## Documentation Discipline

This boundary review is justified because ACPMessage is the first stronger ACP-side message container after ACPBundle.

A closure note is required only if ACPMessage behavior is implemented.

Small repository checks may remain in chat unless they reveal a blocker.

## No-Drift Confirmation

Confirmed:

- Sprint 2 closure state remains preserved.
- Sprint 3 is open for controlled entry only.
- Workflow coverage review is complete.
- ACP boundary eligibility remains eligibility-only.
- ACP minimal envelope remains envelope-only.
- ACPBundle remains bundle-only.
- ACPMessage behavior is admitted only as a future review-approved structural message boundary.
- ACP routing remains on HOLD.
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

If this review is accepted, create the ACPMessage pass in compressed mode:

1. source file;
2. test file;
3. closure note.

Recommended files:

- `src/cognitive_shield/core/agent_communication_protocol_acp/message.py`
- `tests/unit/test_acp_message.py`
- `docs/sprint_3/SPRINT_3_ACP_MESSAGE_PASS_CLOSURE_NOTE.md`

## Verdict Summary

ACPMessage boundary: ADMITTED FOR CONTROLLED IMPLEMENTATION WITH HARD SAFEGUARDS.

ACP routing: HOLD.

ACPMessage dispatch: HOLD.

Agent orchestration: HOLD.

Analysis generation: HOLD.

Runtime pipeline execution: NOT ADMITTED.

Downstream pipeline logic: NOT ADMITTED.
