# Sprint 2 Entry Control Pass

Status: OPEN — Sprint 2 entry control.

## Purpose

This document opens Sprint 2 after Sprint 1 was closed with boundaries.

Sprint 2 must begin with a controlled entry pass before any new behavior implementation is admitted.

The purpose is to define the opening boundary for Sprint 2 and prevent uncontrolled transition from Sprint 1 scaffold / preview / Input behavior work into broad analytical behavior.

## Baseline

Sprint 1 closed as:

- MVP foundation sprint;
- Phase A scaffold sprint;
- Phase A preview-chain sprint;
- minimal Input behavior nucleus sprint.

Sprint 1 did not close as:

- real Message Decomposition Specification (MDS) behavior sprint;
- runtime pipeline sprint;
- analytical engine sprint;
- end-to-end MVP sprint;
- merge-to-main sprint.

## Current State

Current state after Sprint 1:

- Phase A scaffold layer: Closed
- Phase A preview chain: Closed
- Input behavior nucleus: Closed
- Real MDS behavior: HOLD
- Real CMO construction: HOLD
- Real ACP routing: HOLD
- Runtime pipeline execution: Not started
- Downstream pipeline logic: Not started
- Merge to `main`: Not performed

## Sprint 2 Opening Question

The opening question for Sprint 2 is:

What is the smallest admissible real Message Decomposition Specification (MDS)-side behavior slice?

## Not Admitted At Sprint 2 Entry

The following are not admitted by this entry pass:

- broad MDS implementation;
- claim extraction;
- implicit claim inference;
- framing extraction;
- relation inference;
- context assembly;
- `DecompositionResult` construction;
- real MDS output conversion;
- real Canonical Message Object (CMO) construction;
- real Agent Communication Protocol (ACP) routing;
- real Analysis generation;
- taxonomy behavior;
- risk scoring;
- governance behavior;
- output rendering;
- runtime pipeline execution;
- downstream pipeline logic;
- merge to `main`.

## Candidate First Sprint 2 Gate

Recommended first Sprint 2 gate:

`Pre-real MDS behavior scope refinement`

This gate should decide whether Sprint 2 may admit a minimal MDS-side behavior slice and define the exact boundary of that slice.

## Required Safeguards

Sprint 2 must preserve:

- no broad analytical behavior before explicit admission;
- no downstream module activation by implication;
- no hidden pipeline execution;
- no taxonomy or risk behavior;
- no output rendering;
- explicit tests for every admitted behavior;
- closure notes only for real behavior changes or major gates.

## Documentation Discipline

Sprint 2 documentation should be lighter than Sprint 1.

Repo documents should be created only for:

- new admission gates;
- real behavior changes;
- major checkpoint closure;
- recovery blockers;
- merge / release / public-readiness decisions.

Small sanity checks may remain in chat unless they uncover a problem.

## Entry Verdict

Sprint 2 is open for controlled entry.

Real MDS behavior remains on HOLD until a separate scope refinement / admission review is completed.

## Recommended Next Step

Next repo step:

`docs/sprint_2/SPRINT_2_PRE_REAL_MDS_BEHAVIOR_SCOPE_REFINEMENT.md`
