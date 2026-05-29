# Sprint 1 Admission Checklist

Status: Draft v0.1 — Sprint 1 entry checklist.

## Purpose

This checklist controls admission into Sprint 1.

Sprint 1 may begin only after the repository state, boundaries, first slice and testing rules are clear.

This checklist prevents free-form coding drift after Sprint 0 closure.

## Status Legend

- `[x]` = closed
- `[~]` = partial / explicitly deferred
- `[ ]` = remaining

## A. Sprint 0 Closure Baseline

- [x] Sprint 0 final closure judgment exists.
- [x] Sprint 1 admission readiness note exists.
- [x] B1 closure note exists.
- [x] B2 closure note exists.
- [x] B3 closure note exists.
- [x] Sprint 0 closure matrix exists.
- [x] Sprint 0 repository review exists.

Judgment:
Sprint 0 baseline is closed.

## B. Sprint 1 Preparation Documents

- [x] `SPRINT_1_ACTION_PACK.md`
- [x] `SPRINT_1_IMPLEMENTATION_BOUNDARY.md`
- [x] `SPRINT_1_FIRST_SLICE_PLAN.md`
- [ ] `SPRINT_1_CONTRACT_IMPLEMENTATION_ORDER.md`
- [ ] `SPRINT_1_TESTING_ENTRY_RULES.md`
- [ ] `SPRINT_1_COMMIT_DISCIPLINE.md`

Judgment:
Sprint 1 preparation documents are partially complete.

## C. Sprint 1 Entry Control

- [ ] Confirm active branch.
- [ ] Confirm no merge-to-main decision is included in Sprint 1 entry.
- [ ] Confirm current repository state.
- [ ] Review shared contracts base.
- [ ] Confirm first implementation slice.
- [ ] Confirm first touched files.
- [ ] Confirm testing entry rule.
- [ ] Confirm no broad implementation scope.

Judgment:
Sprint 1 entry control is not yet complete.

## D. First Bounded Slice

Target:
Shared Contracts Stabilization + InputMessage Contract Pass.

- [ ] Inspect `src/cognitive_shield/shared/contracts/input_contracts.py`.
- [ ] Confirm whether `InputMessage` already exists.
- [ ] Confirm current `InputMessage` fields.
- [ ] Decide whether refinement is needed.
- [ ] Confirm traceability expectations.
- [ ] Add minimal implementation change only if needed.
- [ ] Add one minimal unit test only after contract shape is stable.
- [ ] Add short slice closure note.

Judgment:
First bounded slice is not yet started.

## E. Testing Entry

- [ ] No test before stable contract.
- [ ] No broad test suite.
- [ ] No integration ambition before first contract slice.
- [ ] First test must be narrow and contract-driven.
- [ ] First test must not test downstream behavior.

Judgment:
Testing entry rules must be confirmed before code work.

## F. Hard Safeguards

- [ ] No free-form coding.
- [ ] No mixed-responsibility files.
- [ ] No ad hoc data passing.
- [ ] No label-to-verdict shortcut.
- [ ] No hidden UI adjudication.
- [ ] No premature Education Core autonomy.
- [ ] No bypass of Confidence / Uncertainty Model.
- [ ] No bypass of Internal Arbiter (IA).
- [ ] No bypass of Decision Policy Layer (DPL).
- [ ] No broad implementation without explicit admission.

Judgment:
Hard safeguards must be re-confirmed during Sprint 1 Entry Control Pass.

## G. Non-Admitted Work

The following remain not admitted during Sprint 1 entry:

- [~] full Message Decomposition Specification (MDS) behavior;
- [~] full Canonical Message Object (CMO) builder behavior;
- [~] Agent Communication Protocol (ACP) routing;
- [~] taxonomy logic;
- [~] Taxonomy-to-Risk Mapping logic;
- [~] Risk Scoring Model implementation;
- [~] Confidence / Uncertainty Model implementation;
- [~] Internal Arbiter (IA) behavior;
- [~] Decision Policy Layer (DPL) behavior;
- [~] Shield Decision (SD) behavior;
- [~] Canonical Output Schema (COS) rendering;
- [~] integration pipeline execution;
- [~] broad test coverage;
- [~] scenario libraries;
- [~] benchmark datasets;
- [~] Education Core training behavior;
- [~] UI / UX product refinement;
- [~] merge to `main`.

Judgment:
These are deferred by design, not forgotten.

## H. Sprint 1 Entry Verdict

Sprint 1 is not yet open for implementation.

Next required action:
Complete the remaining Sprint 1 preparation documents, then run a Sprint 1 Entry Control Pass.

## Checklist Verdict

Sprint 1 admission is prepared but not yet executed.
