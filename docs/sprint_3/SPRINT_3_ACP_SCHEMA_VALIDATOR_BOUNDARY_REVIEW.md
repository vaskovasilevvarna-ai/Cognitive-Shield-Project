# Sprint 3 ACP Schema Validator Boundary Review

Status: Boundary review — before admitting Agent Communication Protocol (ACP) schema validation behavior.

## Purpose

This document records the Sprint 3 boundary review after the controlled Agent Communication Protocol (ACP) message pass.

The purpose is to decide whether the project may admit a minimal ACP Schema Validator boundary while preventing drift into ACP routing, ACPMessage dispatch, agent routing, agent orchestration, Protocol Router behavior, Scope Guard enforcement, Analysis generation, runtime pipeline execution, downstream pipeline logic, taxonomy behavior, risk scoring, governance behavior, or output rendering.

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

Current validation status:

- Python Tests workflow: GREEN
- Current Python Tests workflow: sufficient for bounded structural ACP behavior
- Workflow expansion: not required before minimal schema validation behavior
- Workflow expansion checkpoint: required before routing-adjacent or Analysis-adjacent behavior

Current restricted areas:

- ACP routing: HOLD
- ACPMessage dispatch: HOLD
- agent routing: HOLD
- agent orchestration: HOLD
- Protocol Router behavior: HOLD
- Scope Guard enforcement: HOLD
- Schema Validator behavior: HOLD until this boundary is accepted
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

Can the project admit a minimal ACP Schema Validator as the next Sprint 3 ACP-layer micro-slice?

## Verdict

Verdict:

`ADMIT REVIEW WITH HARD SAFEGUARDS`

The project may admit a future minimal ACP Schema Validator implementation only if it remains:

- schema-validation-only;
- ACPMessage-derived;
- structural only;
- non-routing;
- non-dispatching;
- non-orchestrating;
- non-policy-enforcing;
- non-analytical;
- non-runtime;
- not Protocol Router behavior;
- not Scope Guard behavior;
- not Analysis generation;
- not downstream pipeline logic.

This boundary review does not yet implement ACP Schema Validator behavior.

## Critical Boundary Distinction

An ACPMessage is not schema validation.

ACP Schema Validator behavior is not ACP routing.

ACP Schema Validator behavior is not ACPMessage dispatch.

ACP Schema Validator behavior is not a routing decision.

ACP Schema Validator behavior is not a dispatch target.

ACP Schema Validator behavior is not Scope Guard enforcement.

ACP Schema Validator behavior is not Protocol Router behavior.

ACP Schema Validator behavior is not agent orchestration.

ACP Schema Validator behavior is not an Analysis input bundle.

ACP Schema Validator behavior is only a bounded structural validation check over an already admitted ACPMessage.

It must not route, dispatch, orchestrate, classify, score, govern, render, or execute anything.

## Admitted Future Scope

The future implementation may include only:

- reading an existing ACPMessage;
- checking whether the ACPMessage status is `acp_message_created`;
- checking whether minimal required ACPMessage fields are present;
- preserving the original bounded MDS DecompositionResult;
- preserving the existing CMO field envelope;
- preserving the ACPBundle status;
- preserving the ACPMessage status;
- returning a minimal schema validation status;
- returning source and target stage identity;
- exposing a minimal schema validation result;
- testing that no routing, dispatch, Scope Guard, Protocol Router, Analysis, taxonomy, risk, governance, output, or runtime fields are exposed.

Allowed schema validation statuses may include:

- `acp_schema_valid`
- `acp_schema_invalid`

## Not Admitted

The following remain not admitted:

- ACP routing;
- ACPMessage dispatch;
- agent routing;
- agent orchestration;
- Protocol Router behavior;
- Scope Guard enforcement;
- routing decision creation;
- dispatch target creation;
- agent instruction creation;
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

1. The behavior must remain a minimal ACP Schema Validator boundary only.
2. The behavior must require an existing ACPMessage.
3. The behavior must require or check `acp_message_created` status.
4. The behavior must preserve the original bounded MDS DecompositionResult.
5. The behavior must preserve the existing CMO field envelope.
6. The behavior must preserve the ACPBundle status.
7. The behavior must preserve the ACPMessage status.
8. The behavior must not create a routing decision.
9. The behavior must not create a dispatch target.
10. The behavior must not create agent instructions.
11. The behavior must not route anything.
12. The behavior must not dispatch anything to agents.
13. The behavior must not orchestrate agent communication.
14. The behavior must not call Protocol Router behavior.
15. The behavior must not call Scope Guard behavior.
16. The behavior must not call Analysis modules.
17. The behavior must not call taxonomy, risk, governance, or output modules.
18. The behavior must not infer hidden or implicit meaning.
19. The behavior must not assess truth.
20. The behavior must not assess evidence.
21. The behavior must not create relation objects.
22. The behavior must not create risk signals.
23. The behavior must not trigger runtime pipeline execution.
24. The original ACPMessage object must be preserved unchanged or wrapped without semantic mutation.
25. Tests must prove that forbidden routing, dispatch, Scope Guard, Protocol Router, Analysis, taxonomy, risk, governance, output, and runtime fields are absent.
26. Closure documentation must state that ACP routing, ACPMessage dispatch, Analysis generation, runtime execution, and downstream logic remain on HOLD.

## Candidate Function Name

Preferred function name:

- `validate_acp_message_schema`

Acceptable alternatives:

- `check_acp_message_schema`
- `validate_minimal_acp_message_schema`

Function names should avoid:

- `route_to_agent`
- `dispatch_to_agents`
- `orchestrate_agents`
- `enforce_scope`
- `run_pipeline`
- `generate_analysis`
- `analyze`
- `score`
- `evaluate`

## Recommended Source Area

Preferred source file:

- `src/cognitive_shield/core/agent_communication_protocol_acp/schema_validator_minimal.py`

Alternative:

- `src/cognitive_shield/core/agent_communication_protocol_acp/schema_validator.py`

Preferred choice:

Use a separate `schema_validator_minimal.py` file for the first bounded implementation.

Reason:

The existing `schema_validator.py` scaffold should remain untouched until a broader Schema Validator design pass is admitted.

A separate minimal file keeps the current behavior explicitly bounded, reversible, and non-routing.

The `router.py`, `contracts.py`, `schemas.py`, `scope_guard.py`, `contradiction_registrar.py`, `uncertainty_propagator.py`, and `synthesis_exporter.py` files should remain untouched until their own boundary reviews.

## Admitted Output Shape

A future minimal ACP Schema Validator helper may return a minimal dictionary containing only fields such as:

- `acp_schema_validation_status`
- `source_stage`
- `target_stage`
- `acp_message_status`
- `acp_bundle_status`
- `decomposition_result`
- `field_envelope`

Allowed schema validation statuses:

- `acp_schema_valid`
- `acp_schema_invalid`

The minimal schema validation result must not expose:

- `agent_route`
- `routing_decision`
- `dispatch_target`
- `agent_id`
- `agent_instruction`
- `scope_decision`
- `scope_violation`
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

- a valid ACPMessage returns `acp_schema_valid`;
- a non-ready ACPMessage returns `acp_schema_invalid`;
- empty input returns `acp_schema_invalid`;
- the original bounded MDS DecompositionResult is preserved unchanged;
- the existing CMO field envelope is preserved unchanged;
- source stage is CMO;
- target stage is ACP;
- no routing fields are exposed;
- no dispatch fields are exposed;
- no agent instruction fields are exposed;
- no Scope Guard fields are exposed;
- no Protocol Router fields are exposed;
- no Analysis fields are exposed;
- no taxonomy, risk, governance, output, truth, evidence, relation, or runtime fields are exposed.

Future tests must not verify:

- ACP routing;
- ACPMessage dispatch;
- agent dispatch;
- agent orchestration;
- Protocol Router behavior;
- Scope Guard enforcement;
- Analysis generation;
- truth assessment;
- evidence assessment;
- taxonomy labeling;
- risk scoring;
- governance behavior;
- output rendering;
- downstream pipeline behavior.

## Workflow Coverage Note

The current Python Tests workflow is sufficient for minimal ACP Schema Validator behavior only if the implementation remains bounded and structural.

Workflow expansion is not required before minimal schema validation behavior.

However, workflow expansion review is required before routing-adjacent or Analysis-adjacent behavior, including:

- ACP routing;
- ACPMessage dispatch;
- Protocol Router behavior;
- Scope Guard enforcement;
- Analysis generation;
- runtime pipeline execution;
- downstream pipeline logic.

## Documentation Discipline

This boundary review is justified because ACP Schema Validator is the first validation layer after ACPMessage.

A closure note is required only if ACP Schema Validator behavior is implemented.

Small repository checks may remain in chat unless they reveal a blocker.

## No-Drift Confirmation

Confirmed:

- Sprint 2 closure state remains preserved.
- Sprint 3 is open for controlled entry only.
- Workflow coverage review is complete.
- ACP boundary eligibility remains eligibility-only.
- ACP minimal envelope remains envelope-only.
- ACPBundle remains bundle-only.
- ACPMessage remains message-only.
- ACP Schema Validator behavior is admitted only as a future review-approved structural validation boundary.
- ACP routing remains on HOLD.
- ACPMessage dispatch remains on HOLD.
- Protocol Router behavior remains on HOLD.
- Scope Guard behavior remains on HOLD.
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

If this review is accepted, create the ACP Schema Validator pass in compressed mode:

1. source file;
2. test file;
3. closure note.

Recommended files:

- `src/cognitive_shield/core/agent_communication_protocol_acp/schema_validator_minimal.py`
- `tests/unit/test_acp_schema_validator_minimal.py`
- `docs/sprint_3/SPRINT_3_ACP_SCHEMA_VALIDATOR_PASS_CLOSURE_NOTE.md`

## Verdict Summary

ACP Schema Validator boundary: ADMITTED FOR CONTROLLED IMPLEMENTATION WITH HARD SAFEGUARDS.

ACP routing: HOLD.

ACPMessage dispatch: HOLD.

Protocol Router behavior: HOLD.

Scope Guard behavior: HOLD.

Agent orchestration: HOLD.

Analysis generation: HOLD.

Runtime pipeline execution: NOT ADMITTED.

Downstream pipeline logic: NOT ADMITTED.
