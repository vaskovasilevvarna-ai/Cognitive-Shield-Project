# Sprint 1 Minimal Input Behavior Admission Review

Status: Admission review — minimal Input-side behavior.

## Purpose

This document records the Sprint 1 admission review for the first minimal real Input-side behavior slice.

The purpose is to decide whether the project may admit a small, local, reversible Input behavior without opening Message Decomposition Specification (MDS) behavior, runtime pipeline execution, downstream pipeline logic, taxonomy behavior, risk scoring, governance behavior, output rendering, or merge to `main`.

## Baseline

The following checkpoints are already closed:

- Phase A bounded scaffold checkpoint
- Phase A Repository Verification Pass
- Phase A Exit Audit / Snapshot
- Test Sanity Refresh after Phase A Verification
- Pipeline package scaffold
- Phase A shell scaffold
- Test Sanity Refresh after Phase A Shell
- Phase A preview chain closure / readiness review
- Phase A preview chain exit audit / snapshot
- Input to MDS Preview Pass
- MDS to CMO Preview Pass
- CMO to ACP Preview Pass
- ACP to Analysis Preview Pass

The following restrictive admission reviews remain active:

- Real MDS behavior: HOLD
- Real CMO construction: HOLD
- Real ACP routing: HOLD

## Admission Question

Can the project admit the first minimal real Input-side behavior slice without opening MDS behavior, runtime pipeline execution, downstream pipeline logic, or analytical behavior?

## Verdict

Verdict:

`ADMIT WITH HARD SAFEGUARDS`

Minimal Input-side behavior is admitted only under strict local boundaries.

Input to MDS runtime execution remains on HOLD.

Real Message Decomposition Specification (MDS) behavior remains on HOLD.

Runtime pipeline execution remains not admitted.

Downstream pipeline logic remains not admitted.

## Admitted Scope

The project may admit only minimal local Input behavior such as:

- checking required `InputMessage` source fields;
- trimming leading and trailing whitespace from `raw_text`;
- preserving `message_id`;
- preserving `language` without language routing;
- returning an `InputMessage` or a minimal Input readiness result;
- testing the behavior with narrow unit tests.

## Not Admitted

The following remain not admitted:

- Input to MDS runtime execution;
- real Message Decomposition Specification (MDS) behavior;
- surface segmentation;
- claim extraction;
- implicit claim inference;
- framing extraction;
- relation inference;
- context assembly;
- `DecompositionResult` construction;
- real MDS output conversion;
- real Canonical Message Object (CMO) construction;
- CanonicalMessageObject creation;
- real Agent Communication Protocol (ACP) routing;
- ACPBundle creation;
- ACPMessage dispatch;
- real Analysis generation;
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

Any minimal Input behavior implementation must preserve the following safeguards:

1. The behavior must remain local to the Input layer.
2. The behavior must not call MDS modules.
3. The behavior must not call pipeline preview helpers as runtime execution.
4. The behavior must not create decomposition fields.
5. The behavior must not perform language routing.
6. The behavior must not infer source type.
7. The behavior must not alter semantic content.
8. The behavior must not perform taxonomy, risk, governance, or output logic.
9. The behavior must be reversible and small.
10. Unit tests must verify both permitted behavior and forbidden drift.
11. Closure documentation must state that MDS behavior remains on HOLD.

## Candidate Source Area

Potential source file for the first behavior slice:

- `src/cognitive_shield/core/input/normalizer.py`

Alternative source file, if a separate behavior file is preferred:

- `src/cognitive_shield/core/input/minimal_behavior.py`

The preferred first source area is `normalizer.py`, because the current admitted behavior is limited to minimal Input-side preparation.

## Candidate Function

A potential function name:

- `prepare_input_message_minimal`

The function name should avoid implying pipeline execution.

It should not include `to_mds`, `pipeline`, `execute`, or `run`.

## Required Test Boundary

Future tests may verify:

- leading and trailing whitespace in `raw_text` is trimmed;
- `message_id` is preserved;
- `language` is preserved;
- empty or invalid required fields remain invalid through existing validation;
- no decomposition fields are created;
- no MDS behavior is invoked.

Future tests must not verify:

- surface segmentation;
- claim extraction;
- relation extraction;
- decomposition output construction;
- CMO construction;
- ACP routing;
- Analysis output generation;
- downstream pipeline behavior.

## No-Drift Confirmation

Confirmed:

- real MDS behavior remains on HOLD;
- real CMO construction remains on HOLD;
- real ACP routing remains on HOLD;
- real Analysis generation has not started;
- runtime pipeline execution has not started;
- downstream pipeline logic has not started;
- taxonomy behavior has not started;
- risk scoring has not started;
- governance behavior has not started;
- output rendering has not started;
- merge to `main` has not been performed.

## Recommended Next Step

Recommended next step:

Inspect the current source file before editing:

`src/cognitive_shield/core/input/normalizer.py`

If the current scaffold can safely accept the minimal function, update it with a small local Input behavior function and add narrow tests.

If the file shape is unsuitable, create a separate minimal Input behavior file through a fresh control pass.

## Verdict Summary

Minimal Input-side behavior: ADMIT WITH HARD SAFEGUARDS.

Input to MDS runtime execution: HOLD.

Real MDS behavior: HOLD.

Runtime pipeline execution: NOT ADMITTED.

Downstream pipeline logic: NOT ADMITTED.
