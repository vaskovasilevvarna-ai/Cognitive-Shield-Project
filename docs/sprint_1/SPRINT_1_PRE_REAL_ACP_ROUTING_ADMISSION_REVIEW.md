# Sprint 1 Pre-Real ACP Routing Admission Review

Status: Control review — before any real Agent Communication Protocol (ACP) routing.

## Purpose

This document records a stricter admission review before any real Agent Communication Protocol (ACP) routing behavior is allowed.

The purpose is to prevent preview-level Phase A handoff work from drifting into real ACP routing, agent orchestration, runtime pipeline execution, downstream pipeline logic, or hidden governance behavior.

## Baseline

The following checkpoints are closed:

- Phase A bounded scaffold checkpoint
- Phase A Repository Verification Pass
- Phase A Exit Audit / Snapshot
- Test Sanity Refresh after Phase A Verification
- Pipeline package scaffold
- Phase A shell scaffold
- Test Sanity Refresh after Phase A Shell
- Input to MDS Preview Pass
- Test Sanity Refresh after Input to MDS Preview
- Pre-Real MDS Behavior Admission Review
- MDS to CMO Preview Entry Control
- MDS to CMO Preview Pass
- Test Sanity Refresh after MDS to CMO Preview
- Pre-Real CMO Construction Admission Review
- CMO to ACP Preview Entry Control
- CMO to ACP Preview Pass

## Current State

Current state:

- Input bounded scaffold: Closed
- Message Decomposition Specification (MDS) bounded scaffold: Closed
- Canonical Message Object (CMO) bounded scaffold: Closed
- Agent Communication Protocol (ACP) bounded scaffold: Closed
- Analysis bounded scaffold: Closed
- Real MDS behavior: On HOLD
- Real MDS output conversion: Not started
- Real CMO construction: On HOLD
- Real ACP routing: Not started
- Runtime pipeline execution: Not started
- Downstream pipeline logic: Not started
- Merge to `main`: Not performed

## Admission Question

Can the project admit real Agent Communication Protocol (ACP) routing now?

## Verdict

Verdict:

`HOLD`

Real Agent Communication Protocol (ACP) routing is not admitted yet.

The project may continue with preview-level boundary work only.

## Reason for HOLD

Real ACP routing is high-impact because it would introduce the first actual coordination behavior between analytical modules.

It would affect:

- ACP message routing;
- sender and recipient interpretation;
- scope guarding;
- schema validation behavior;
- contradiction registration;
- uncertainty propagation;
- synthesis export;
- future Analysis handoff;
- future Internal Arbiter (IA) and governance layers;
- downstream taxonomy and risk layers.

This is too important to admit immediately after a preview-level CMO to ACP handoff.

## Still Admitted

The following remain admitted:

- bounded preview helpers;
- readiness / handoff preview dictionaries;
- non-executing sequence identity helpers;
- tests that verify preview shape only;
- tests that verify forbidden routing fields are absent.

## Not Admitted

The following remain not admitted:

- real ACP routing;
- ACPBundle creation;
- ACPMessage dispatch;
- agent orchestration;
- protocol state machine;
- real scope enforcement;
- real schema validation engine;
- contradiction registration behavior;
- uncertainty propagation behavior;
- synthesis export behavior;
- Analysis generation;
- taxonomy behavior;
- risk scoring;
- confidence or uncertainty evaluation;
- Internal Arbiter (IA) behavior;
- Decision Policy Layer (DPL) behavior;
- Shield Decision (SD) behavior;
- governance behavior;
- output rendering;
- runtime pipeline execution;
- downstream pipeline logic;
- merge to `main`.

## Hard Safeguards

Before real ACP routing can be admitted, the project must define:

1. exact minimal ACP routing scope;
2. accepted CMO-side input contract;
3. accepted ACP output contract;
4. sender / recipient constraints;
5. routing table constraints;
6. scope guard requirements;
7. schema validation requirements;
8. contradiction preservation requirements;
9. uncertainty propagation requirements;
10. synthesis export boundary;
11. failure modes;
12. rollback / reversibility plan;
13. unit tests;
14. contract tests.

## Preview Boundary Rule

Preview helpers may describe readiness or handoff state.

Preview helpers must not route ACP messages.

Preview helpers must not create `ACPBundle`.

Preview helpers must not dispatch messages or agents.

Preview helpers must not call real ACP router, scope guard, schema validator, contradiction registrar, uncertainty propagator, or synthesis exporter behavior.

Preview helpers must not generate Analysis outputs.

## Required Test Boundary For Future Preview Work

Future preview tests may verify:

- expected source stage;
- expected target stage;
- preview-only handoff status;
- routing status remains not started;
- forbidden ACP routing fields are absent;
- forbidden Analysis output fields are absent.

Future preview tests must not verify:

- ACP message routing;
- ACPBundle construction;
- agent orchestration;
- message dispatch;
- contradiction registration;
- uncertainty propagation;
- synthesis export;
- Analysis output generation;
- downstream pipeline behavior.

## No-Drift Confirmation

Confirmed:

- real MDS behavior remains on HOLD;
- real MDS output conversion has not started;
- real CMO construction remains on HOLD;
- real ACP routing has not started;
- Analysis generation has not started;
- runtime pipeline execution has not started;
- downstream pipeline logic has not started;
- taxonomy behavior has not started;
- risk scoring has not started;
- governance behavior has not started;
- output rendering has not started;
- merge to `main` has not been performed.

## Recommended Next Gate

Recommended next gate:

`ACP to Analysis preview entry control`

Reason:

The project may continue building the preview chain, but only if the next slice remains non-executing and does not perform real ACP routing, generate real Analysis outputs, or execute runtime pipeline behavior.

## Verdict Summary

Real ACP routing: HOLD.

Preview-level boundary work: ADMITTED WITH HARD SAFEGUARDS.

Runtime pipeline execution: NOT ADMITTED.

Next safe step: ACP to Analysis preview entry control.
