# Sprint 1 First Slice Plan

Status: Draft v0.1 — first bounded implementation slice.

## Purpose

This document defines the first bounded implementation slice for Sprint 1.

Sprint 1 must begin with a small, controlled and reversible implementation step.

The goal is to avoid free-form coding and to preserve the architecture-first discipline established during Sprint 0.

## First Slice Name

Shared Contracts Stabilization + InputMessage Contract Pass.

## Why This Slice Comes First

The first implementation step should not begin with full Message Decomposition Specification (MDS) logic or a full analytical pipeline.

It should begin with the shared contract surface because shared contracts prevent ad hoc data passing and protect traceability between modules.

The `InputMessage` contract is the safest first object to review because it is the entry object for the future single-message pipeline.

## First Slice Scope

This slice may include:

- review of `src/cognitive_shield/shared/contracts/input_contracts.py`;
- confirmation of the current `InputMessage` shape;
- minimal refinement of `InputMessage` only if needed;
- confirmation of traceability fields and naming discipline;
- one minimal unit test after the contract shape is stable;
- a short closure note for the slice.

## First Slice Non-Scope

This slice must not include:

- real Message Decomposition Specification (MDS) behavior;
- Canonical Message Object (CMO) builder logic;
- Agent Communication Protocol (ACP) routing;
- taxonomy labels;
- risk scoring;
- confidence or uncertainty evaluation;
- Internal Arbiter (IA) behavior;
- Decision Policy Layer (DPL) behavior;
- Shield Decision (SD) behavior;
- Canonical Output Schema (COS) rendering;
- integration pipeline execution;
- broad test suite expansion;
- examples or fixtures expansion.

## Expected Files Touched

Likely files:

- `src/cognitive_shield/shared/contracts/input_contracts.py`;
- `tests/unit/test_input_contracts.py` or another narrow unit test file;
- optional short note in `docs/sprint_1/`.

No other files should be touched unless explicitly admitted during the Sprint 1 Entry Control Pass.

## Proposed Micro-Steps

1. Inspect the current `input_contracts.py`.
2. Identify whether `InputMessage` already exists.
3. If it exists, review its fields.
4. If it does not exist, add the minimal `InputMessage` contract.
5. Confirm naming and traceability expectations.
6. Add one minimal unit test only after the contract shape is stable.
7. Add a short closure note for the slice.

## Minimal InputMessage Target Shape

The target shape should remain minimal and explicit:

- `message_id`;
- `raw_text`;
- `language`;
- `source_type`;
- `timestamp`;
- `metadata`.

The exact implementation form may be dataclass, Pydantic model, TypedDict or another explicit contract form, but the choice must be made during Sprint 1 Entry Control Pass and must remain consistent with the current repository style.

## Testing Rule

No test should be added before the contract shape is stable.

The first test should verify only the presence and minimal construction of the `InputMessage` contract.

It should not test downstream behavior.

## Closure Criteria

This slice is complete when:

- the `InputMessage` contract shape is confirmed;
- any minimal refinement is documented;
- one narrow unit test exists if appropriate;
- no downstream implementation logic has been introduced;
- the slice is closed with a short review note.

## Slice Verdict

This is the recommended first Sprint 1 implementation slice.

It is intentionally small, reversible and contract-first.
