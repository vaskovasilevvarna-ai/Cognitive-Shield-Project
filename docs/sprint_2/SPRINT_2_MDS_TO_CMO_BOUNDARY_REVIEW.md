# Sprint 2 MDS-to-CMO Boundary Review

Status: Boundary review — before admitting MDS-to-CMO transition behavior.

## Purpose

This document records the Sprint 2 boundary review for the transition from Message Decomposition Specification (MDS) output to Canonical Message Object (CMO) eligibility.

The purpose is to decide whether the project may admit a bounded MDS-to-CMO boundary eligibility step while preventing drift into real Canonical Message Object (CMO) construction, Agent Communication Protocol (ACP) routing, Analysis generation, runtime pipeline execution, downstream pipeline logic, taxonomy behavior, risk scoring, governance behavior, or output rendering.

This review does not admit implementation by itself.

## Baseline

Sprint 2 has completed:

- Sprint 2 Entry Control Pass
- Pre-real MDS behavior scope refinement
- MDS surface preparation pass
- MDS surface unit pass
- MDS surface bundle pass
- MDS explicit surface segmentation pass
- MDS explicit claim candidate pass
- MDS explicit claim unit pass
- MDS explicit claim unit bundle pass
- MDS minimal assembly pass
- MDS bounded DecompositionResult pass
- Python Tests workflow validation

Current MDS state:

- MDS early structural stack: CLOSED
- bounded DecompositionResult shell: CLOSED
- Python Tests workflow: GREEN

Current restricted areas:

- real CMO construction: HOLD
- CanonicalMessageObject creation: HOLD
- MDS-to-CMO conversion: HOLD until explicitly admitted
- ACP routing: HOLD
- Analysis generation: NOT STARTED
- runtime pipeline execution: NOT ADMITTED
- downstream pipeline logic: NOT ADMITTED
- taxonomy behavior: NOT STARTED
- risk scoring: NOT STARTED
- governance behavior: NOT STARTED
- output rendering: NOT STARTED

## Boundary Question

Can the project admit a bounded MDS-to-CMO boundary eligibility step as the next Sprint 2 micro-slice?

## Verdict

Verdict:

`ADMIT REVIEW WITH HARD SAFEGUARDS`

The project may admit a future MDS-to-CMO boundary eligibility implementation only if it remains:

- eligibility-only;
- structural only;
- non-converting;
- non-runtime;
- non-analytical;
- not real CMO construction;
- not ACP routing;
- not Analysis generation;
- not downstream pipeline logic.

This boundary review does not yet implement MDS-to-CMO behavior.

## Critical Boundary Distinction

A bounded MDS DecompositionResult is not a Canonical Message Object (CMO).

An MDS-to-CMO boundary eligibility check is not CMO construction.

CMO eligibility is not CanonicalMessageObject creation.

CMO eligibility is not ACP handoff.

CMO eligibility is not runtime pipeline execution.

CMO eligibility is only a local boundary check confirming whether the bounded MDS DecompositionResult has the minimal structural shape required to be considered for a future CMO construction step.

It must not create, convert, enrich, infer, analyze, score, route, or dispatch anything.

## Admitted Future Scope

The future implementation may include only:

- reading an existing bounded MDS DecompositionResult shell;
- checking whether the required MDS-local structural keys are present;
- checking whether the decomposition result status is acceptable;
- returning boundary eligibility status;
- preserving the original decomposition result unchanged;
- testing that no CMO, ACP, Analysis, taxonomy, risk, governance, output, or runtime fields are exposed.

Allowed eligibility statuses may include:

- `eligible_for_cmo_boundary`
- `not_eligible_for_cmo_boundary`

## Not Admitted

The following remain not admitted:

- real Canonical Message Object (CMO) construction;
- CanonicalMessageObject creation;
- MDS-to-CMO conversion;
- CMO field mapping;
- CMO schema population;
- CMO normalization;
- ACP routing;
- ACPBundle creation;
- ACPMessage dispatch;
- Analysis generation;
- EvidenceAnalysisOutput generation;
- NarrativeAnalysisOutput generation;
- CognitiveAnalysisOutput generation;
- Analysis bundle generation;
- taxonomy behavior;
- label-to-verdict logic;
- risk scoring;
- confidence or uncertainty evaluation;
- governance behavior;
- output rendering;
- runtime pipeline execution;
- downstream pipeline logic;
- merge to `main`.

Also still not admitted:

- implicit claim inference;
- hidden claim reconstruction;
- truth assessment;
- evidence assessment;
- framing extraction;
- relation inference;
- semantic interpretation beyond already admitted MDS-local structure.

## Hard Safeguards

Any future implementation after this review must preserve the following safeguards:

1. The behavior must remain a boundary eligibility check only.
2. The behavior must not construct a Canonical Message Object (CMO).
3. The behavior must not create CMO fields.
4. The behavior must not map MDS fields into a CMO schema.
5. The behavior must not call CMO construction modules.
6. The behavior must not call ACP modules.
7. The behavior must not call Analysis modules.
8. The behavior must not call taxonomy, risk, governance, or output modules.
9. The behavior must not infer hidden or implicit meaning.
10. The behavior must not assess truth.
11. The behavior must not assess evidence.
12. The behavior must not create relation objects.
13. The behavior must not create risk signals.
14. The behavior must not trigger runtime pipeline execution.
15. The original DecompositionResult shell must be preserved unchanged.
16. Tests must prove that forbidden downstream fields are absent.
17. Closure documentation must state that real CMO construction remains on HOLD.

## Candidate Function Name

Preferred function name:

- `check_mds_to_cmo_boundary_eligibility`

Acceptable alternatives:

- `is_decomposition_result_cmo_eligible`
- `build_mds_to_cmo_boundary_status`

Function names should avoid:

- `convert_to_cmo`
- `build_cmo`
- `create_canonical_message_object`
- `dispatch_to_acp`
- `run_pipeline`
- `analyze`
- `score`
- `evaluate`

## Recommended Source Area

Preferred source file:

- `src/cognitive_shield/core/canonical_message_object_cmo/mds_boundary.py`

Alternative if the CMO package is not ready for behavior files:

- `src/cognitive_shield/core/message_decomposition_specification_mds/cmo_boundary.py`

Preferred choice should be made after source inspection of the current CMO package structure.

## Admitted Output Shape

A future MDS-to-CMO boundary helper may return a minimal dictionary containing only fields such as:

- `boundary_status`
- `source_stage`
- `target_stage`
- `decomposition_result_status`
- `decomposition_result`

Allowed source stage:

- `message_decomposition_specification_mds`

Allowed target stage:

- `canonical_message_object_cmo`

Allowed boundary statuses:

- `eligible_for_cmo_boundary`
- `not_eligible_for_cmo_boundary`

The boundary status object must not expose:

- `canonical_message_object`
- `cmo`
- `acp_bundle`
- `acp_message`
- `analysis_bundle`
- `taxonomy_labels`
- `risk_profile`
- `governance_signal`
- `output_payload`
- `truth_value`
- `evidence_assessment`

## Required Test Boundary

Future tests may verify:

- a valid bounded DecompositionResult shell can be marked eligible for the CMO boundary;
- an empty or invalid DecompositionResult shell is marked not eligible;
- original DecompositionResult shell is preserved unchanged;
- source stage is MDS;
- target stage is CMO;
- no CMO object is created;
- no ACP fields are exposed;
- no Analysis fields are exposed;
- no taxonomy, risk, governance, output, truth, evidence, relation, or runtime fields are exposed.

Future tests must not verify:

- CMO construction;
- CMO field mapping;
- CMO schema population;
- ACP routing;
- Analysis generation;
- truth assessment;
- evidence assessment;
- taxonomy labeling;
- risk scoring;
- downstream pipeline behavior.

## Documentation Discipline

This boundary review is justified because MDS-to-CMO is the first cross-layer transition boundary after the bounded MDS DecompositionResult shell.

After this review, source inspection is required before implementation.

A closure note is required only if MDS-to-CMO boundary eligibility behavior is implemented.

## No-Drift Confirmation

Confirmed:

- MDS bounded DecompositionResult remains MDS-local;
- MDS-to-CMO boundary behavior is admitted only as a future review-approved eligibility check;
- real CMO construction remains on HOLD;
- CanonicalMessageObject creation remains on HOLD;
- ACP routing remains on HOLD;
- Analysis generation remains on HOLD;
- taxonomy behavior has not started;
- risk scoring has not started;
- governance behavior has not started;
- output rendering has not started;
- runtime pipeline execution has not started;
- downstream pipeline logic has not started;
- merge to `main` has not been performed.

## Recommended Next Step

Recommended next step:

Inspect the current CMO package structure before coding.

Inspect first:

- `src/cognitive_shield/core/canonical_message_object_cmo/`

Then decide:

- use `src/cognitive_shield/core/canonical_message_object_cmo/mds_boundary.py`;
- or use `src/cognitive_shield/core/message_decomposition_specification_mds/cmo_boundary.py`;
- or hold implementation if CMO package structure is not ready.

If accepted after inspection, create the MDS-to-CMO boundary eligibility pass in compressed mode:

1. source file;
2. test file;
3. closure note.

Recommended likely files:

- `src/cognitive_shield/core/canonical_message_object_cmo/mds_boundary.py`
- `tests/unit/test_cmo_mds_boundary.py`
- `docs/sprint_2/SPRINT_2_MDS_TO_CMO_BOUNDARY_ELIGIBILITY_PASS_CLOSURE_NOTE.md`

## Verdict Summary

MDS-to-CMO boundary review: ADMITTED FOR CONTROLLED ELIGIBILITY IMPLEMENTATION WITH HARD SAFEGUARDS.

Real CMO construction: HOLD.

CanonicalMessageObject creation: HOLD.

ACP routing: HOLD.

Analysis generation: HOLD.

Runtime pipeline execution: NOT ADMITTED.

Downstream pipeline logic: NOT ADMITTED.
