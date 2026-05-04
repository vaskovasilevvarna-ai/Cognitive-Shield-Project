# Sprint 1 Entry Control Pass

Status: Entry control in progress.

## Purpose

This document opens the Sprint 1 Entry Control Pass.

Sprint 1 implementation must not begin until the repository state, branch state, first bounded slice, touched files, testing rule and hard safeguards are confirmed.

This document is a control gate, not an implementation document.

## Baseline

Sprint 0 is closed.

Sprint 1 preparation pack is complete.

Confirmed Sprint 1 preparation documents:

- `SPRINT_1_ACTION_PACK.md`
- `SPRINT_1_IMPLEMENTATION_BOUNDARY.md`
- `SPRINT_1_FIRST_SLICE_PLAN.md`
- `SPRINT_1_ADMISSION_CHECKLIST.md`
- `SPRINT_1_CONTRACT_IMPLEMENTATION_ORDER.md`
- `SPRINT_1_TESTING_ENTRY_RULES.md`
- `SPRINT_1_COMMIT_DISCIPLINE.md`

## Current Working Branch

Expected working branch:

- `sprint-0/repo-restructure`

No merge to `main` is included in this entry control pass.

Any merge-to-main decision requires a separate review.

## First Bounded Slice

The first recommended Sprint 1 slice is:

Shared Contracts Stabilization + InputMessage Contract Pass.

Expected first file to inspect:

- `src/cognitive_shield/shared/contracts/input_contracts.py`

Potential first implementation file:

- `src/cognitive_shield/shared/contracts/input_contracts.py`

Potential first narrow test file:

- `tests/unit/test_input_contracts.py`

Testing may begin only after the `InputMessage` contract shape is stable enough to test.

## Entry Control Checklist

- [x] Sprint 0 closure exists.
- [x] Sprint 1 preparation documents exist.
- [ ] Active branch confirmed.
- [ ] Repository state confirmed.
- [ ] Shared contracts base inspected.
- [ ] `input_contracts.py` inspected.
- [ ] `InputMessage` existence confirmed.
- [ ] `InputMessage` current fields reviewed.
- [ ] Decision made whether refinement is needed.
- [ ] First touched files confirmed.
- [ ] Testing entry rule confirmed.
- [ ] Hard safeguards confirmed.
- [ ] Implementation admission decision issued.

## Hard Safeguards to Reconfirm

Sprint 1 must preserve:

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
- no merge to `main` without separate review.

## Not Yet Admitted

This pass does not yet admit:

- Message Decomposition Specification (MDS) behavior;
- Canonical Message Object (CMO) builder behavior;
- Agent Communication Protocol (ACP) routing;
- taxonomy logic;
- risk scoring;
- confidence or uncertainty evaluation;
- Internal Arbiter (IA) behavior;
- Decision Policy Layer (DPL) behavior;
- Shield Decision (SD) behavior;
- output rendering;
- integration pipeline execution;
- broad test suite expansion.

## Entry Verdict

Sprint 1 Entry Control Pass is open.

Sprint 1 implementation is not yet admitted until the remaining control checklist items are completed.
