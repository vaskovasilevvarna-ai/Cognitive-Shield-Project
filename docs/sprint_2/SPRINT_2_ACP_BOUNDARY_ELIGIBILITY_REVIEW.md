# Sprint 2 ACP Boundary Eligibility Review

Status: Boundary review — before admitting Agent Communication Protocol (ACP) boundary eligibility behavior.

## Purpose

This document records the Sprint 2 boundary review after the controlled Canonical Message Object (CMO) bounded construction pass.

The purpose is to decide whether the project may admit a bounded Agent Communication Protocol (ACP) boundary eligibility step while preventing drift into real ACP routing, ACPBundle creation, ACPMessage creation, agent dispatch, agent orchestration, Analysis generation, runtime pipeline execution, downstream pipeline logic, taxonomy behavior, risk scoring, governance behavior, or output rendering.

This review does not admit implementation by itself.

## Baseline

Sprint 2 has completed:

- Sprint 2 Entry Control Pass
- Pre-real Message Decomposition Specification (MDS) behavior scope refinement
- MDS surface preparation pass
- MDS surface unit pass
- MDS surface bundle pass
- MDS explicit surface segmentation pass
- MDS explicit claim candidate pass
- MDS explicit claim unit pass
- MDS explicit claim unit bundle pass
- MDS minimal assembly pass
- MDS bounded DecompositionResult pass
- MDS-to-CMO boundary eligibility pass
- CMO minimal shell pass
- CMO structural contract pass
- CMO field envelope pass
- CMO minimal object pass
- CMO construction readiness review
- CMO construction boundary review
- CMO bounded construction pass
- Python Tests workflow validation

Current state:

- MDS early structural stack: CLOSED
- bounded DecompositionResult shell: CLOSED
- MDS-to-CMO boundary eligibility: CLOSED
- CMO minimal shell: CLOSED
- CMO structural contract: CLOSED
- CMO field envelope: CLOSED
- CMO minimal object: CLOSED
- CMO bounded construction candidate: CLOSED
- Python Tests workflow: GREEN

Current restricted areas:

- ACP routing: HOLD
- ACPBundle creation: HOLD
- ACPMessage creation: HOLD
- ACPMessage dispatch: HOLD
- agent orchestration: HOLD
- Analysis generation: NOT STARTED
- EvidenceAnalysisOutput generation: NOT STARTED
- NarrativeAnalysisOutput generation: NOT STARTED
- CognitiveAnalysisOutput generation: NOT STARTED
- runtime pipeline execution: NOT ADMITTED
- downstream pipeline logic: NOT ADMITTED
- taxonomy behavior: NOT STARTED
- risk scoring: NOT STARTED
- governance behavior: NOT STARTED
- output rendering: NOT STARTED
- merge to `main`: NOT PERFORMED

## Boundary Question

Can the project admit an ACP boundary eligibility step as the next Sprint 2 micro-slice?

## Verdict

Verdict:

`ADMIT REVIEW WITH HARD SAFEGUARDS`

The project may admit a future ACP boundary eligibility implementation only if it remains:

- eligibility-only;
- CMO-construction-candidate-derived;
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

This boundary review does not yet implement ACP boundary eligibility behavior.

## Critical Boundary Distinction

A CMO bounded construction candidate is not an ACPBundle.

ACP boundary eligibility is not ACP routing.

ACP boundary eligibility is not ACPMessage creation.

ACP boundary eligibility is not ACPMessage dispatch.

ACP boundary eligibility is not agent orchestration.

ACP boundary eligibility is not Analysis generation.

ACP boundary eligibility is only a local boundary check confirming whether the bounded CMO construction candidate has the minimum structural readiness to be considered for a future Agent Communication Protocol (ACP) layer.

It must not route, dispatch, orchestrate, analyze, classify, score, govern, render, or execute anything.

## Admitted Future Scope

The future implementation may include only:

- reading an existing CMO bounded construction candidate;
- checking whether the bounded construction status is `bounded_cmo_construction_created`;
- preserving the original bounded MDS DecompositionResult;
- preserving the existing field envelope;
- returning ACP boundary eligibility status;
- returning source and target stage identity;
- exposing a minimal ACP eligibility object;
- testing that no ACPBundle, ACPMessage, routing, dispatch, Analysis, taxonomy, risk, governance, output, or runtime fields are exposed.

Allowed ACP boundary eligibility statuses may include:

- `eligible_for_acp_boundary`
- `not_eligible_for_acp_boundary`

## Not Admitted

The following remain not admitted:

- ACP routing;
- ACPBundle creation;
- ACPMessage creation;
- ACPMessage dispatch;
- agent routing;
- agent orchestration;
- Protocol Router behavior;
- Scope Guard behavior beyond existing scaffold;
- Schema Validator behavior beyond existing scaffold;
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
- semantic interpretation beyond already admitted MDS-local and CMO-local structures.

## Hard Safeguards

Any future implementation after this review must preserve the following safeguards:

1. The behavior must remain an ACP boundary eligibility check only.
2. The behavior must require an existing CMO bounded construction candidate.
3. The behavior must require `bounded_cmo_construction_created` status.
4. The behavior must preserve the original bounded MDS DecompositionResult.
5. The behavior must preserve the existing CMO field envelope.
6. The behavior must not create an ACPBundle.
7. The behavior must not create an ACPMessage.
8. The behavior must not route anything.
9. The behavior must not dispatch anything to agents.
10. The behavior must not orchestrate agent communication.
11. The behavior must not call ACP routing modules.
12. The behavior must not call Analysis modules.
13. The behavior must not call taxonomy, risk, governance, or output modules.
14. The behavior must not infer hidden or implicit meaning.
15. The behavior must not assess truth.
16. The behavior must not assess evidence.
17. The behavior must not create relation objects.
18. The behavior must not create risk signals.
19. The behavior must not trigger runtime pipeline execution.
20. The original CMO bounded construction candidate must be preserved unchanged or wrapped without semantic mutation.
21. Tests must prove that forbidden ACP, Analysis, taxonomy, risk, governance, output, and runtime fields are absent.
22. Closure documentation must state that ACP routing, ACPBundle creation, ACPMessage creation, Analysis generation, runtime execution, and downstream logic remain on HOLD.

## Candidate Function Name

Preferred function name:

- `check_cmo_to_acp_boundary_eligibility`

Acceptable alternatives:

- `is_cmo_candidate_acp_eligible`
- `build_acp_boundary_eligibility_status`

Function names should avoid:

- `route_to_acp`
- `create_acp_bundle`
- `create_acp_message`
- `dispatch_to_agents`
- `orchestrate_agents`
- `run_pipeline`
- `generate_analysis`
- `analyze`
- `score`
- `evaluate`

## Recommended Source Area

Preferred source file:

- `src/cognitive_shield/core/agent_communication_protocol_acp/cmo_boundary.py`

Alternative if the ACP package is not ready for behavior files:

- `src/cognitive_shield/core/canonical_message_object_cmo/acp_boundary.py`

Preferred choice should be made after source inspection of the current ACP package structure.

## Admitted Output Shape

A future ACP boundary eligibility helper may return a minimal dictionary containing only fields such as:

- `acp_boundary_status`
- `source_stage`
- `target_stage`
- `bounded_cmo_construction_status`
- `decomposition_result`
- `field_envelope`

Allowed source stage:

- `canonical_message_object_cmo`

Allowed target stage:

- `agent_communication_protocol_acp`

Allowed ACP boundary statuses:

- `eligible_for_acp_boundary`
- `not_eligible_for_acp_boundary`

The ACP boundary eligibility object must not expose:

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

- a valid CMO bounded construction candidate can be marked eligible for the ACP boundary;
- a non-ready CMO bounded construction candidate is marked not eligible;
- the original bounded MDS DecompositionResult is preserved unchanged;
- the existing field envelope is preserved unchanged;
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
- Analysis generation;
- truth assessment;
- evidence assessment;
- taxonomy labeling;
- risk scoring;
- governance behavior;
- output rendering;
- downstream pipeline behavior.

## Documentation Discipline

This boundary review is justified because ACP boundary eligibility is the first controlled step approaching the Agent Communication Protocol (ACP) layer after bounded CMO construction.

After this review, source inspection of the current ACP package structure is required before implementation.

A closure note is required only if ACP boundary eligibility behavior is implemented.

## No-Drift Confirmation

Confirmed:

- MDS bounded DecompositionResult remains preserved;
- MDS-to-CMO boundary eligibility remains bounded;
- CMO minimal shell remains shell-only;
- CMO structural contract remains contract-only;
- CMO field envelope remains envelope-only;
- CMO minimal object remains minimal-object-only;
- CMO bounded construction remains construction-candidate-only;
- ACP boundary eligibility is admitted only as a future review-approved eligibility check;
- ACP routing remains on HOLD;
- ACPBundle creation remains on HOLD;
- ACPMessage creation remains on HOLD;
- ACPMessage dispatch remains on HOLD;
- agent orchestration remains on HOLD;
- Analysis generation remains on HOLD;
- taxonomy behavior has not started;
- risk scoring has not started;
- governance behavior has not started;
- output rendering has not started;
- runtime pipeline execution has not started;
- downstream pipeline logic has not started;
- merge to `main` has not been performed.

## Recommended Next Step

Recommended next step:

Inspect the current ACP package structure before coding.

Inspect first:

- `src/cognitive_shield/core/agent_communication_protocol_acp/`

Then decide:

- use `src/cognitive_shield/core/agent_communication_protocol_acp/cmo_boundary.py`;
- or use `src/cognitive_shield/core/canonical_message_object_cmo/acp_boundary.py`;
- or hold implementation if the ACP package structure is not ready.

If accepted after inspection, create the ACP boundary eligibility pass in compressed mode:

1. source file;
2. test file;
3. closure note.

Recommended likely files:

- `src/cognitive_shield/core/agent_communication_protocol_acp/cmo_boundary.py`
- `tests/unit/test_acp_cmo_boundary.py`
- `docs/sprint_2/SPRINT_2_ACP_BOUNDARY_ELIGIBILITY_PASS_CLOSURE_NOTE.md`

## Verdict Summary

ACP boundary eligibility review: ADMITTED FOR CONTROLLED ELIGIBILITY IMPLEMENTATION WITH HARD SAFEGUARDS.

ACP routing: HOLD.

ACPBundle creation: HOLD.

ACPMessage creation: HOLD.

ACPMessage dispatch: HOLD.

Agent orchestration: HOLD.

Analysis generation: HOLD.

Runtime pipeline execution: NOT ADMITTED.

Downstream pipeline logic: NOT ADMITTED.
