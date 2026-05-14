# Sprint 1 CMO to ACP Preview Entry Control Note

Status: Entry control note — Canonical Message Object (CMO) to Agent Communication Protocol (ACP) preview slice.

## Purpose

This note opens the Sprint 1 entry control review for the minimal Canonical Message Object (CMO) to Agent Communication Protocol (ACP) preview slice.

The purpose is to admit only a bounded preview of the CMO to ACP boundary.

This note does not admit real Canonical Message Object (CMO) construction, real Agent Communication Protocol (ACP) routing, runtime pipeline execution, downstream pipeline logic, taxonomy behavior, risk scoring, governance behavior, output rendering, or merge to `main`.

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
- MDS to CMO Preview Entry Control
- MDS to CMO Preview Pass
- Test Sanity Refresh after MDS to CMO Preview
- Pre-Real CMO Construction Admission Review

The Pre-Real CMO Construction Admission Review fixed:

- real CMO construction: HOLD
- preview-level boundary work: ADMITTED WITH HARD SAFEGUARDS
- runtime pipeline execution: NOT ADMITTED
- downstream pipeline logic: NOT ADMITTED

## Admission Question

The admission question is:

Can the project admit the smallest possible CMO to ACP preview slice without opening real CMO construction, real ACP routing, runtime pipeline execution, or downstream pipeline logic?

## Admission Verdict

Verdict:

`ADMIT WITH HARD SAFEGUARDS`

The admitted slice is a preview-only boundary helper.

It may show that a future Canonical Message Object (CMO) could be prepared for a future Agent Communication Protocol (ACP) boundary, but it must not construct a real CMO, route ACP messages, dispatch agents, or execute runtime pipeline behavior.

## Admitted Scope

Admitted now:

- a bounded preview helper;
- a preview dictionary / readiness object;
- a fixed source stage for future Canonical Message Object (CMO);
- a fixed target stage for future Agent Communication Protocol (ACP);
- a narrow unit test for preview shape;
- a closure note after the pass.

Potential admitted file:

- `src/cognitive_shield/pipeline/cmo_to_acp_preview.py`

Potential admitted test:

- `tests/unit/test_cmo_to_acp_preview.py`

Potential closure note:

- `docs/sprint_1/SPRINT_1_CMO_TO_ACP_PREVIEW_PASS_CLOSURE_NOTE.md`

## Allowed Preview Fields

The preview helper may return only minimal boundary information such as:

- `source_stage`
- `target_stage`
- `handoff_status`
- `routing_status`

Allowed source stage:

- `canonical_message_object_cmo`

Allowed target stage:

- `agent_communication_protocol_acp`

Allowed handoff status:

- `preview_only`

Allowed routing status:

- `not_started`

## Non-Scope

The following are not admitted:

- real CMO construction;
- CanonicalMessageObject creation;
- CMO layer construction;
- claim graph construction;
- context assembly;
- traceability layer construction;
- real ACP routing;
- agent orchestration;
- message dispatch;
- protocol state machine;
- scope enforcement;
- schema validation engine;
- contradiction registration behavior;
- uncertainty propagation behavior;
- synthesis export behavior;
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

1. The file must be a preview or readiness boundary, not a production routing engine.
2. Function names must include `preview` or `readiness`.
3. The output must be a minimal dictionary or equivalent preview object.
4. The output must not be a `CanonicalMessageObject`.
5. The output must not be an `ACPBundle`.
6. The implementation must not call real CMO builder or mapper behavior.
7. The implementation must not call real ACP router, scope guard, schema validator, contradiction registrar, uncertainty propagator, or synthesis exporter behavior.
8. The implementation must not dispatch messages or agents.
9. Tests must verify preview shape only.
10. Tests must verify that no CMO construction or ACP routing fields are exposed.
11. Closure documentation must state that real CMO construction and real ACP routing remain not admitted.

## Required Test Boundary

Future tests may verify:

- the preview returns the expected source stage;
- the preview returns the expected target stage;
- the preview returns `handoff_status: preview_only`;
- the preview returns `routing_status: not_started`;
- the preview contains no CMO construction fields;
- the preview contains no ACP routing or orchestration fields.

Future tests must not verify:

- real CMO construction;
- ACP message routing;
- agent orchestration;
- message dispatch;
- contradiction registration;
- uncertainty propagation;
- synthesis export;
- downstream pipeline behavior.

## No-Drift Confirmation

Confirmed:

- real MDS behavior remains on HOLD;
- real CMO construction remains on HOLD;
- real ACP routing has not started;
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

`src/cognitive_shield/pipeline/cmo_to_acp_preview.py`

## Verdict

CMO to ACP preview entry control is open.

Only preview-level boundary behavior is admitted.

Real Canonical Message Object (CMO) construction remains not admitted.

Real Agent Communication Protocol (ACP) routing remains not admitted.

Runtime pipeline execution remains not admitted.
