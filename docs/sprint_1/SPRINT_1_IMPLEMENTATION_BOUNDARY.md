# Sprint 1 Implementation Boundary

Status: Draft v0.1 — implementation boundary document.

## Purpose

This document defines the implementation boundary for Sprint 1.

Sprint 1 is admitted only as a bounded implementation phase. It must not become free-form coding, product expansion, broad pipeline implementation, or redesign of the Cognitive Shield architecture.

The purpose of this boundary is to preserve the discipline established during Sprint 0 while allowing the first controlled implementation steps.

## Admitted Work

Sprint 1 may include:

- review of existing shared contracts;
- minimal refinement of one shared contract at a time;
- first bounded implementation slice;
- minimal tests only after a contract shape is stable;
- documentation updates that preserve implementation traceability;
- small commits tied to one role or one module;
- preparation for later Message Decomposition Specification (MDS) implementation without implementing full MDS behavior yet.

## First Admitted Focus

The recommended first admitted focus is:

Shared contracts stabilization plus first minimal InputMessage contract pass.

This includes:

1. review `src/cognitive_shield/shared/contracts/input_contracts.py`;
2. confirm the current `InputMessage` shape;
3. refine only if needed;
4. confirm traceability expectations;
5. add one minimal unit test after the contract is stable enough to test.

## Non-Admitted Work

Sprint 1 must not start with:

- full Shield Core implementation;
- full Message Decomposition Specification (MDS) behavior;
- full Canonical Message Object (CMO) builder behavior;
- full Agent Communication Protocol (ACP) routing behavior;
- broad taxonomy logic;
- Taxonomy-to-Risk Mapping logic;
- Risk Scoring Model implementation;
- Confidence / Uncertainty Model implementation;
- Internal Arbiter (IA) implementation;
- Decision Policy Layer (DPL) implementation;
- Shield Decision (SD) implementation;
- full Canonical Output Schema (COS) rendering;
- broad test suite;
- integration test expansion;
- benchmark datasets;
- scenario libraries;
- rich Output layer behavior;
- Education Core behavioral logic;
- UI / UX product refinement;
- merge to `main`.

## Hard Boundary Rules

Sprint 1 must preserve these rules:

- no free-form coding;
- no mixed-responsibility files;
- no ad hoc data passing;
- no label-to-verdict shortcut;
- no hidden UI adjudication;
- no premature Education Core autonomy;
- no bypass of Confidence / Uncertainty Model;
- no bypass of Internal Arbiter (IA);
- no bypass of Decision Policy Layer (DPL);
- no broad implementation without explicit admission;
- no merge-to-main decision without a separate review.

## Deferred by Design

The following are intentionally deferred from Sprint 1 entry work:

- full analytical pipeline;
- complete single-message end-to-end execution;
- broad unit and contract test coverage;
- real contract validation script logic;
- real fixture report generation;
- real scenario library;
- benchmark dataset creation;
- advanced calibration fronts;
- advanced Output layer representation;
- full Education Core training behavior.

These are not forgotten. They require later admission decisions.

## Entry Rule

Sprint 1 implementation may begin only after:

1. Sprint 1 action documents are present;
2. the first bounded slice is selected;
3. testing entry rules are explicit;
4. the current branch state is reviewed;
5. a Sprint 1 Entry Control Pass is completed.

## Boundary Verdict

Sprint 1 is bounded to controlled implementation entry.

This document does not authorize broad implementation.
