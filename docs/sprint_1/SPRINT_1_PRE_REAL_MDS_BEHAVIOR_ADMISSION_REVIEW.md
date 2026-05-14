# Sprint 1 Pre-Real MDS Behavior Admission Review

Status: Control review — before any real Message Decomposition Specification (MDS) behavior.

## Purpose

This document records a stricter admission review before any real Message Decomposition Specification (MDS) behavior is allowed.

The purpose is to prevent preview-level Phase A handoff work from drifting into real decomposition behavior, runtime pipeline execution, downstream pipeline logic, or hidden analytical implementation.

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

## Current State

Current state:

- Input bounded scaffold: Closed
- Message Decomposition Specification (MDS) bounded scaffold: Closed
- Canonical Message Object (CMO) bounded scaffold: Closed
- Agent Communication Protocol (ACP) bounded scaffold: Closed
- Analysis bounded scaffold: Closed
- Real MDS behavior: Not started
- Runtime pipeline execution: Not started
- Downstream pipeline logic: Not started
- Merge to `main`: Not performed

## Admission Question

Can the project admit real Message Decomposition Specification (MDS) behavior now?

## Verdict

Verdict:

`HOLD`

Real Message Decomposition Specification (MDS) behavior is not admitted yet.

The project may continue with preview-level boundary work only.

## Reason for HOLD

Real MDS behavior is high-impact because it would introduce the first actual analytical transformation in Phase A.

It would affect:

- surface segmentation;
- claim extraction;
- framing unit handling;
- relation objects;
- context carriers;
- decomposition uncertainty;
- traceability mapping;
- later Canonical Message Object (CMO) construction.

This is too important to admit immediately after the first preview slice.

## Still Admitted

The following remain admitted:

- bounded preview helpers;
- readiness / handoff preview dictionaries;
- non-executing sequence identity helpers;
- tests that verify preview shape only;
- tests that verify forbidden decomposition fields are absent.

## Not Admitted

The following remain not admitted:

- real surface segmentation;
- claim extraction;
- implicit claim inference;
- framing extraction;
- relation inference;
- context assembly;
- global narrative structure construction;
- decomposition uncertainty calculation;
- traceability map construction;
- `DecompositionResult` construction;
- Canonical Message Object (CMO) construction;
- Agent Communication Protocol (ACP) routing;
- Analysis generation;
- taxonomy behavior;
- risk scoring;
- governance behavior;
- output rendering;
- runtime pipeline execution;
- downstream pipeline logic;
- merge to `main`.

## Hard Safeguards

Before real MDS behavior can be admitted, the project must define:

1. exact minimal behavior scope;
2. accepted input contract;
3. exact output contract;
4. forbidden analytical expansions;
5. traceability requirements;
6. uncertainty handling requirements;
7. failure modes;
8. rollback / reversibility plan;
9. unit tests;
10. contract tests.

## Preview Boundary Rule

Preview helpers may describe readiness or handoff state.

Preview helpers must not create analytical units.

Preview helpers must not produce `DecompositionResult`.

Preview helpers must not call real MDS service, mapper, validator behavior beyond scaffold-level checks.

## Recommended Next Gate

Recommended next gate:

`MDS to CMO preview entry control`

Reason:

The project may continue building the preview chain, but only if the next slice remains non-executing and does not construct either a real DecompositionResult or a real Canonical Message Object.

## Verdict Summary

Real MDS behavior: HOLD.

Preview-level boundary work: ADMITTED WITH HARD SAFEGUARDS.

Next safe step: MDS to CMO preview entry control.
