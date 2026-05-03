# Sprint 1 Action Pack

Status: Draft v0.1 — pre-implementation action document.

## Purpose

Sprint 1 is not free-form coding.

Sprint 1 is a bounded implementation admission phase after Sprint 0 repository preparation and structural closure.

The purpose of Sprint 1 is to begin controlled implementation while preserving the architecture-first discipline established in Sprint 0.

Sprint 1 must not redesign the system, bypass the architecture, or introduce hidden product behavior through code.

## Basis

Sprint 1 begins after:

- Sprint 0 repository preparation closure;
- B1 Level B symmetry pass closure;
- B2 minimal unit / contract tests opening closure;
- B3 scripts / examples opening closure;
- B4 final Sprint 0 closure judgment;
- Sprint 1 admission readiness note.

## Working Posture

Official posture:

Constrained Core Build.

This means:

- architecture-first implementation;
- small bounded steps;
- explicit contracts;
- typed interfaces where possible;
- no mixed-responsibility files;
- no hidden policy logic;
- no ad hoc data passing;
- no implementation shortcuts across governance layers.

## Sprint 1 Scope

Sprint 1 is allowed to work on:

- reviewing and stabilizing shared contracts;
- implementing the first minimal contract slice;
- adding minimal tests only after a contract is stable enough to test;
- preparing the first bounded module connection;
- preserving traceability from implementation files back to architecture contracts.

## Sprint 1 Non-Scope

Sprint 1 must not start with:

- broad Shield Core implementation;
- full Message Decomposition Specification (MDS) behavior;
- complete pipeline execution;
- broad test coverage;
- benchmark datasets;
- scenario libraries;
- rich Output layer behavior;
- full Education Core training logic;
- UI / UX product refinement;
- merge to main without separate review.

## Recommended First Slice

Recommended first implementation slice:

Shared contracts stabilization plus first minimal InputMessage contract pass.

Initial order:

1. Review `src/cognitive_shield/shared/contracts/input_contracts.py`.
2. Confirm or minimally refine `InputMessage`.
3. Confirm traceability expectations.
4. Add one minimal unit test only after the contract shape is stable.
5. Do not implement Message Decomposition Specification (MDS) logic yet.

## Hard Safeguards

Sprint 1 must preserve the following safeguards:

- no free-form coding;
- no label-to-verdict shortcut;
- no bypass of Confidence / Uncertainty Model;
- no bypass of Internal Arbiter (IA);
- no bypass of Decision Policy Layer (DPL);
- no hidden UI adjudication;
- no premature Education Core autonomy;
- no broad implementation without explicit admission;
- no merge-to-main decision inside Sprint 1 entry work.

## Method

Continue the working method used during Sprint 0:

1. one small step;
2. verification;
3. commit;
4. short confirmation;
5. next small step.

## Definition of Done for Sprint 1 Entry Preparation

Sprint 1 entry preparation is done when:

- Sprint 1 action documents are present in `docs/sprint_1/`;
- Sprint 1 boundaries are explicit;
- the first implementation slice is selected;
- testing entry rules are explicit;
- commit discipline is preserved;
- no code implementation has started before the entry control pass.

## Entry Verdict

Sprint 1 may begin only after a separate Sprint 1 Entry Control Pass.

This document prepares Sprint 1. It does not start implementation by itself.
