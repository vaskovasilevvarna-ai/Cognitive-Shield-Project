# Sprint 1 MDS to CMO Preview Entry Control Note

Status: Entry control note — Message Decomposition Specification (MDS) to Canonical Message Object (CMO) preview slice.

## Purpose

This note opens the Sprint 1 entry control review for the minimal Message Decomposition Specification (MDS) to Canonical Message Object (CMO) preview slice.

The purpose is to admit only a bounded preview of the MDS to CMO boundary.

This note does not admit real MDS output conversion, real Canonical Message Object (CMO) construction, runtime pipeline execution, downstream pipeline logic, taxonomy behavior, risk scoring, governance behavior, output rendering, or merge to `main`.

## Baseline

The following checkpoints are already closed:

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

The Pre-Real MDS Behavior Admission Review fixed:

- real MDS behavior: HOLD
- preview-level boundary work: ADMITTED WITH HARD SAFEGUARDS
- runtime pipeline execution: NOT ADMITTED
- downstream pipeline logic: NOT ADMITTED

## Admission Question

The admission question is:

Can the project admit the smallest possible MDS to CMO preview slice without opening real MDS output conversion, real CMO construction, runtime pipeline execution, or downstream pipeline logic?

## Admission Verdict

Verdict:

`ADMIT WITH HARD SAFEGUARDS`

The admitted slice is a preview-only boundary helper.

It may show that a future MDS output could be prepared for a future CMO boundary, but it must not construct a real `DecompositionResult` or a real Canonical Message Object (CMO).

## Admitted Scope

Admitted now:

- a bounded preview helper;
- a preview dictionary / readiness object;
- a fixed target stage for future Canonical Message Object (CMO);
- a narrow unit test for preview shape;
- a closure note after the pass.

Potential admitted file:

- `src/cognitive_shield/pipeline/mds_to_cmo_preview.py`

Potential admitted test:

- `tests/unit/test_mds_to_cmo_preview.py`

Potential closure note:

- `docs/sprint_1/SPRINT_1_MDS_TO_CMO_PREVIEW_PASS_CLOSURE_NOTE.md`

## Allowed Preview Fields

The preview helper may return only minimal boundary information such as:

- `source_stage`
- `target_stage`
- `handoff_status`
- `conversion_status`

Allowed source stage:

- `message_decomposition_specification_mds`

Allowed target stage:

- `canonical_message_object_cmo`

Allowed handoff status:

- `preview_only`

Allowed conversion status:

- `not_started`

## Non-Scope

The following are not admitted:

- real MDS output conversion;
- real `DecompositionResult` construction;
- surface segment conversion;
- claim unit conversion;
- framing unit conversion;
- relation object conversion;
- context carrier conversion;
- global narrative structure conversion;
- decomposition uncertainty conversion;
- traceability map conversion;
- real Canonical Message Object (CMO) construction;
- CMO builder behavior;
- CMO mapper behavior beyond preview shape;
- claim graph construction;
- context assembly;
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

1. The file must be a preview or readiness boundary, not a production conversion engine.
2. Function names must include `preview` or `readiness`.
3. The output must be a minimal dictionary or equivalent preview object.
4. The output must not be a `DecompositionResult`.
5. The output must not be a `CanonicalMessageObject`.
6. The implementation must not call real MDS service, mapper, or validator behavior beyond scaffold-level identity.
7. The implementation must not call real CMO builder or mapper behavior.
8. The implementation must not create surface segments, claim units, framing units, relation objects, context carriers, global structure, uncertainty layers, or traceability layers.
9. Tests must verify preview shape only.
10. Tests must verify that no real conversion or construction fields are exposed.
11. Closure documentation must state that real MDS output conversion and real CMO construction remain not admitted.

## Required Test Boundary

Future tests may verify:

- the preview returns the expected source stage;
- the preview returns the expected target stage;
- the preview returns `handoff_status: preview_only`;
- the preview returns `conversion_status: not_started`;
- the preview contains no MDS output conversion fields;
- the preview contains no CMO construction fields.

Future tests must not verify:

- real decomposition output construction;
- real MDS service behavior;
- real CMO construction;
- surface layer construction;
- claim layer construction;
- relation layer construction;
- context layer construction;
- uncertainty layer construction;
- downstream pipeline behavior.

## No-Drift Confirmation

Confirmed:

- real MDS behavior remains on HOLD;
- real MDS output conversion has not started;
- real CMO construction has not started;
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

`src/cognitive_shield/pipeline/mds_to_cmo_preview.py`

## Verdict

MDS to CMO preview entry control is open.

Only preview-level boundary behavior is admitted.

Real MDS output conversion remains not admitted.

Real Canonical Message Object (CMO) construction remains not admitted.

Runtime pipeline execution remains not admitted.
