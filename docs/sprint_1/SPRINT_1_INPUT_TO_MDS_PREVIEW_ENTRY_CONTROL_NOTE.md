# Sprint 1 Input to MDS Preview Entry Control Note

Status: Entry control note — Input to Message Decomposition Specification (MDS) preview slice.

## Purpose

This note opens the Sprint 1 entry control review for the minimal Input to Message Decomposition Specification (MDS) preview slice.

The purpose is to admit only a bounded preview of the Input to MDS boundary.

This note does not admit real Message Decomposition Specification (MDS) behavior, runtime pipeline execution, downstream pipeline logic, taxonomy behavior, risk scoring, governance behavior, output rendering, or merge to `main`.

## Baseline

The following checkpoints are already closed:

- Sprint 1 Phase A bounded scaffold checkpoint
- Phase A Repository Verification Pass
- Phase A Exit Audit / Snapshot
- Test Sanity Refresh after Phase A Verification
- Pipeline package scaffold
- Phase A shell scaffold
- Test Sanity Refresh after Phase A Shell

The following bounded scaffold blocks are closed:

- Input
- Message Decomposition Specification (MDS)
- Canonical Message Object (CMO)
- Agent Communication Protocol (ACP)
- Analysis

## Admission Question

The admission question is:

Can the project admit the smallest possible Input to MDS preview slice without opening real runtime pipeline behavior or real MDS analytical behavior?

## Admission Verdict

Verdict:

`ADMIT WITH HARD SAFEGUARDS`

The admitted slice is a preview-only boundary helper.

It may show that a valid `InputMessage` can be prepared for a future MDS handoff, but it must not perform decomposition.

## Admitted Scope

Admitted now:

- a bounded preview helper;
- use of the stable `InputMessage` contract;
- use of minimal Input source validation;
- a preview dictionary / readiness object;
- a narrow unit test for preview shape;
- a closure note after the pass.

Potential admitted file:

- `src/cognitive_shield/pipeline/input_to_mds_preview.py`

Potential admitted test:

- `tests/unit/test_input_to_mds_preview.py`

Potential closure note:

- `docs/sprint_1/SPRINT_1_INPUT_TO_MDS_PREVIEW_PASS_CLOSURE_NOTE.md`

## Allowed Behavior

The preview helper may return only minimal boundary information such as:

- `message_id`
- `language`
- `source_status`
- `target_stage`
- `handoff_status`

Allowed target stage:

- `message_decomposition_specification_mds`

Allowed handoff status:

- `preview_only`

## Non-Scope

The following are not admitted:

- real input normalization;
- transcript parsing;
- language routing;
- source-type inference;
- real Message Decomposition Specification (MDS) behavior;
- surface segmentation;
- claim extraction;
- implicit claim inference;
- framing extraction;
- relation inference;
- context assembly;
- `DecompositionResult` construction;
- Canonical Message Object (CMO) construction;
- Agent Communication Protocol (ACP) routing;
- Analysis generation;
- taxonomy behavior;
- label-to-verdict logic;
- risk scoring;
- confidence or uncertainty evaluation;
- governance behavior;
- output rendering;
- runtime pipeline execution;
- downstream pipeline logic;
- merge to `main`.

## Hard Safeguards

Any future implementation in this pass must preserve the following safeguards:

1. The file must be a preview or readiness boundary, not a production pipeline engine.
2. Function names must include `preview` or `readiness`.
3. The output must be a minimal dictionary or equivalent preview object.
4. The output must not be a `DecompositionResult`.
5. The implementation must not call real MDS service or mapper behavior.
6. The implementation must not create surface segments, claim units, framing units, relation objects, or context carriers.
7. Tests must verify preview shape only.
8. Tests must not validate decomposition behavior.
9. Closure documentation must state that real MDS behavior remains not admitted.

## Required Test Boundary

Future tests may verify:

- valid `InputMessage` produces a preview-only handoff;
- the preview contains the expected target stage;
- the preview contains no decomposition fields;
- invalid input remains blocked or marked invalid if validation is used.

Future tests must not verify:

- surface segmentation;
- claim extraction;
- relation extraction;
- decomposition output construction;
- downstream pipeline behavior.

## No-Drift Confirmation

Confirmed:

- real behavior implementation has not started;
- runtime pipeline execution has not started;
- downstream pipeline logic has not started;
- taxonomy behavior has not started;
- risk scoring has not started;
- governance behavior has not started;
- output rendering has not started;
- merge to `main` has not been performed.

## Recommended Next Step

Recommended next step:

Create the bounded preview pass in compressed mode:

1. source file;
2. unit test;
3. closure note.

The recommended source file is:

`src/cognitive_shield/pipeline/input_to_mds_preview.py`

## Verdict

Input to MDS preview entry control is open.

Only preview-level boundary behavior is admitted.

Real Input to MDS runtime execution remains not admitted.

Real Message Decomposition Specification (MDS) behavior remains not admitted.
