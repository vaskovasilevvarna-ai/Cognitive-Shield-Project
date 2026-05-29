# Smoke Tests

Status: Sprint 4 smoke-test scaffold.

## Purpose

This directory is reserved for smoke tests that verify bounded MVP-level functional proof behavior for Cognitive Shield.

Smoke tests are not a replacement for unit tests or contract tests.

Smoke tests are intended to verify that admitted components can connect in a controlled, local, reproducible way without bypassing architectural boundaries.

## Sprint 4 Role

Sprint 4 is the MVP completion phase.

The smoke-test area supports the Sprint 4 goal of producing a testable MVP-level functional proof.

Future smoke tests may verify a bounded chain such as:

Input  
→ Message Decomposition Specification (MDS) bounded structure  
→ Canonical Message Object (CMO) bounded structure  
→ Agent Communication Protocol (ACP) structural chain  
→ Protocol Router readiness or admitted minimal routing result  
→ MVP proof object

## Allowed Smoke Test Behavior

Future smoke tests may verify:

- admitted chain connectivity;
- expected status transitions;
- preservation of `decomposition_result`;
- preservation of `field_envelope`;
- absence of forbidden routing, dispatch, Analysis, runtime, and downstream fields;
- local reproducibility of MVP proof behavior.

## Not Allowed In Smoke Tests

Smoke tests must not introduce or depend on:

- real ACP routing;
- ACPMessage dispatch;
- agent routing;
- agent orchestration;
- dispatch target creation;
- agent instruction creation;
- Analysis generation;
- taxonomy behavior;
- risk scoring;
- governance behavior;
- output rendering;
- runtime pipeline execution;
- downstream pipeline logic;
- cloud services;
- telemetry;
- external APIs.

## Forbidden Field Families

Future smoke tests should explicitly check that MVP proof objects do not expose forbidden fields such as:

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

## Current Status

This directory is scaffold-only.

No MVP smoke test is admitted by this README.

No MVP functional proof implementation is admitted by this README.

No workflow YAML change is admitted by this README.
