# Sprint 3 ACP Minimal Envelope Boundary Review

Status: Boundary review — before admitting minimal Agent Communication Protocol (ACP) envelope behavior.

## Purpose

This document records the Sprint 3 boundary review after the Sprint 3 Workflow Coverage Review.

The purpose is to decide whether the project may admit a minimal Agent Communication Protocol (ACP) envelope while preventing drift into ACPBundle creation, ACPMessage creation, ACP routing, ACPMessage dispatch, agent orchestration, Analysis generation, runtime pipeline execution, downstream pipeline logic, taxonomy behavior, risk scoring, governance behavior, or output rendering.

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

Current validation status:

- Python Tests workflow: GREEN
- Current Python Tests workflow: sufficient for first ACP structural boundary
- Workflow expansion: not required yet
- Workflow expansion checkpoint: required before routing-adjacent or Analysis-adjacent behavior

Current restricted areas:

- ACP routing: HOLD
- ACPBundle creation: HOLD
- ACPMessage creation: HOLD
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

Can the project admit a minimal ACP envelope as the first Sprint 3 ACP-layer micro-slice?

## Verdict

Verdict:

`ADMIT REVIEW WITH HARD SAFEGUARDS`

The project may admit a future minimal ACP envelope implementation only if it remains:

- envelope-only;
- eligibility-derived;
- structural only;
- non-routing;
- non-dispatching;
- non-orchestrating;
- non-analytical;
- non-runtime;
- not ACPBundle creation;
- not ACPMessage creation;
- not Analysis generation;
- not downstream pipeline logic.

This boundary review does not yet implement ACP minimal envelope behavior.

## Critical Boundary Distinction

ACP boundary eligibility is not ACP routing.

A minimal ACP envelope is not an ACPBundle.

A minimal ACP envelope is not an ACPMessage.

A minimal ACP envelope is not a routing decision.

A minimal ACP envelope is not a dispatch target.

A minimal ACP envelope is not agent orchestration.

A minimal ACP envelope is not an Analysis input bundle.

A minimal ACP envelope is only a bounded structural wrapper around the existing ACP boundary eligibility signal.

It must not route, dispatch, orchestrate, analyze, classify, score, govern, render, or execute anything.

## Admitted Future Scope

The future implementation may include only:

- reading an existing ACP boundary eligibility result;
- checking whether the ACP boundary status is `eligible_for_acp_boundary`;
- preserving the original bounded MDS DecompositionResult;
- preserving the existing CMO field envelope;
- returning a minimal ACP envelope status;
- returning source and target stage identity;
- exposing a minimal ACP envelope object;
- testing that no ACPBundle, ACPMessage, routing, dispatch, Analysis, taxonomy, risk, governance, output, or runtime fields are exposed.

Allowed ACP envelope statuses may include:

- `acp_minimal_envelope_created`
- `not_ready_for_acp_minimal_envelope`

## Not Admitted

The following remain not admitted:

- ACP routing;
- ACPBundle creation;
- ACPMessage creation;
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
- semantic interpretation beyond admitted MDS-local and CMO-local structures.

## Hard Safeguards

Any future implementation after this review must preserve the following safeguards:

1. The behavior must remain a minimal ACP envelope only.
2. The behavior must require an existing ACP boundary eligibility result.
3. The behavior must require `eligible_for_acp_boundary` status.
4. The behavior must preserve the original bounded MDS DecompositionResult.
5. The behavior must preserve the existing CMO field envelope.
6. The behavior must not create an ACPBundle.
7. The behavior must not create an ACPMessage.
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
24. The original ACP boundary eligibility object must be preserved unchanged or wrapped without semantic mutation.
25. Tests must prove that forbidden ACPBundle, ACPMessage, routing, dispatch, Analysis, taxonomy, risk, governance, output, and runtime fields are absent.
26. Closure documentation must state that ACPBundle creation, ACPMessage creation, ACP routing, Analysis generation, runtime execution, and downstream logic remain on HOLD.

## Candidate Function Name

Preferred function name:

- `build_acp_minimal_envelope`

Acceptable alternatives:

- `create_minimal_acp_envelope`
- `build_acp_envelope_minimal`

Function names should avoid:

- `create_acp_bundle`
- `create_acp_message`
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

- `src/cognitive_shield/core/agent_communication_protocol_acp/minimal_envelope.py`

Reason:

The existing ACP scaffold files should remain stable.

The `cmo_boundary.py` file should remain focused on CMO-to-ACP boundary eligibility.

The `router.py`, `contracts.py`, `schemas.py`, `schema_validator.py`, `scope_guard.py`, `contradiction_registrar.py`, `uncertainty_propagator.py`, and `synthesis_exporter.py` files should remain untouched until their own boundary reviews.

A separate `minimal_envelope.py` file keeps the ACP envelope boundary explicit and reversible.

## Admitted Output Shape

A future minimal ACP envelope helper may return a minimal dictionary containing only fields such as:

- `acp_envelope_status`
- `source_stage`
- `target_stage`
- `acp_boundary_status`
- `decomposition_result`
- `field_envelope`

Allowed ACP envelope statuses:

- `acp_minimal_envelope_created`
- `not_ready_for_acp_minimal_envelope`

The minimal ACP envelope must not expose:

- `acp_bundle`
- `ACPBundle`
- `acp_message`
- `ACPMessage`
- `agent_route`
- `routing_decision`
- `dispatch_target`
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

- a valid ACP boundary eligibility result creates a minimal ACP envelope;
- a non-eligible ACP boundary result does not create a minimal ACP envelope;
- the original bounded MDS DecompositionResult is preserved unchanged;
- the existing CMO field envelope is preserved unchanged;
- source stage is CMO;
- target stage is ACP;
- no ACPBundle is created;
- no ACPMessage is created;
- no routing fields are exposed;
- no dispatch fields are exposed;
- no Analysis fields are exposed;
- no taxonomy, risk, governance, output, truth, evidence, relation, or runtime fields are exposed.

Future tests must not verify:

- ACPBundle construction;
- ACPMessage construction;
- ACP routing;
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

The current Python Tests workflow is sufficient for this first ACP structural boundary.

Workflow expansion is not required before ACP minimal envelope behavior.

However, workflow expansion review is required before routing-adjacent or Analysis-adjacent behavior, including:

- ACP routing;
- ACPBundle creation;
- ACPMessage creation;
- ACPMessage dispatch;
- Protocol Router behavior;
- Schema Validator behavior;
- Scope Guard behavior;
- Analysis generation;
- runtime pipeline execution;
- downstream pipeline logic.

## Documentation Discipline

This boundary review is justified because ACP minimal envelope is the first controlled ACP-layer object after ACP boundary eligibility.

A closure note is required only if ACP minimal envelope behavior is implemented.

Small repository checks may remain in chat unless they reveal a blocker.

## No-Drift Confirmation

Confirmed:

- Sprint 2 closure state remains preserved.
- Sprint 3 is open for controlled entry only.
- Workflow coverage review is complete.
- ACP boundary eligibility remains eligibility-only.
- ACP minimal envelope behavior is admitted only as a future review-approved structural envelope boundary.
- ACP routing remains on HOLD.
- ACPBundle creation remains on HOLD.
- ACPMessage creation remains on HOLD.
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

If this review is accepted, create the ACP minimal envelope pass in compressed mode:

1. source file;
2. test file;
3. closure note.

Recommended files:

- `src/cognitive_shield/core/agent_communication_protocol_acp/minimal_envelope.py`
- `tests/unit/test_acp_minimal_envelope.py`
- `docs/sprint_3/SPRINT_3_ACP_MINIMAL_ENVELOPE_PASS_CLOSURE_NOTE.md`

## Verdict Summary

ACP minimal envelope boundary: ADMITTED FOR CONTROLLED IMPLEMENTATION WITH HARD SAFEGUARDS.

ACP routing: HOLD.

ACPBundle creation: HOLD.

ACPMessage creation: HOLD.

ACPMessage dispatch: HOLD.

Agent orchestration: HOLD.

Analysis generation: HOLD.

Runtime pipeline execution: NOT ADMITTED.

Downstream pipeline logic: NOT ADMITTED.
