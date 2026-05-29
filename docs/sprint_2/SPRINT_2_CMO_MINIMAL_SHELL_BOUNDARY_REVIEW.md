# Sprint 2 CMO Minimal Shell Boundary Review

Status: Boundary review — before admitting minimal Canonical Message Object (CMO) shell behavior.

## Purpose

This document records the Sprint 2 boundary review for the next micro-slice after the controlled MDS-to-CMO boundary eligibility pass.

The purpose is to decide whether the project may admit a minimal Canonical Message Object (CMO) shell while preventing drift into full CMO construction, CMO schema population, CMO field mapping, Agent Communication Protocol (ACP) routing, Analysis generation, runtime pipeline execution, downstream pipeline logic, taxonomy behavior, risk scoring, governance behavior, or output rendering.

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
- MDS-to-CMO boundary eligibility pass
- Python Tests workflow validation

Current state:

- MDS early structural stack: CLOSED
- bounded DecompositionResult shell: CLOSED
- MDS-to-CMO boundary eligibility: CLOSED
- CMO scaffold: PRESENT
- Python Tests workflow: GREEN

Current CMO scaffold files:

- `src/cognitive_shield/core/canonical_message_object_cmo/README.md`
- `src/cognitive_shield/core/canonical_message_object_cmo/__init__.py`
- `src/cognitive_shield/core/canonical_message_object_cmo/builder.py`
- `src/cognitive_shield/core/canonical_message_object_cmo/contracts.py`
- `src/cognitive_shield/core/canonical_message_object_cmo/mapper.py`
- `src/cognitive_shield/core/canonical_message_object_cmo/schemas.py`
- `src/cognitive_shield/core/canonical_message_object_cmo/validator.py`
- `src/cognitive_shield/core/canonical_message_object_cmo/mds_boundary.py`

Current restricted areas:

- full CMO construction: HOLD
- CanonicalMessageObject creation: HOLD
- CMO schema population: HOLD
- CMO field mapping: HOLD
- ACP routing: HOLD
- Analysis generation: NOT STARTED
- runtime pipeline execution: NOT ADMITTED
- downstream pipeline logic: NOT ADMITTED
- taxonomy behavior: NOT STARTED
- risk scoring: NOT STARTED
- governance behavior: NOT STARTED
- output rendering: NOT STARTED

## Boundary Question

Can the project admit a minimal CMO shell as the next Sprint 2 micro-slice?

## Verdict

Verdict:

`ADMIT REVIEW WITH HARD SAFEGUARDS`

The project may admit a future minimal CMO shell implementation only if it remains:

- shell-only;
- structural only;
- eligibility-derived;
- non-mapping;
- non-runtime;
- non-analytical;
- not full Canonical Message Object construction;
- not ACP handoff;
- not Analysis generation;
- not downstream pipeline logic.

This boundary review does not yet implement minimal CMO shell behavior.

## Critical Boundary Distinction

MDS-to-CMO eligibility is not CMO construction.

A minimal CMO shell is not a full Canonical Message Object.

A minimal CMO shell is not CMO schema population.

A minimal CMO shell is not CMO field mapping.

A minimal CMO shell is not ACP handoff.

A minimal CMO shell is not an Analysis input bundle.

A minimal CMO shell is only a bounded placeholder container around an eligible MDS DecompositionResult.

It must not normalize, enrich, map, infer, analyze, score, route, or dispatch anything.

## Admitted Future Scope

The future implementation may include only:

- reading an existing MDS-to-CMO boundary eligibility result;
- checking whether the boundary status is eligible;
- preserving the original bounded MDS DecompositionResult;
- returning CMO shell status;
- returning source and target stage identity;
- exposing a minimal CMO shell object;
- testing that no full CMO, ACP, Analysis, taxonomy, risk, governance, output, or runtime fields are exposed.

Allowed CMO shell status values may include:

- `cmo_shell_created`
- `not_eligible_for_cmo_shell`

## Not Admitted

The following remain not admitted:

- full Canonical Message Object (CMO) construction;
- CanonicalMessageObject creation;
- CMO schema population;
- CMO field mapping;
- CMO normalization;
- CMO enrichment;
- MDS-to-CMO conversion beyond shell eligibility;
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

1. The behavior must remain a minimal CMO shell only.
2. The behavior must require an eligible MDS-to-CMO boundary status.
3. The behavior must preserve the original bounded MDS DecompositionResult.
4. The behavior must not construct a full Canonical Message Object.
5. The behavior must not populate a CMO schema.
6. The behavior must not map MDS fields into final CMO fields.
7. The behavior must not normalize or enrich MDS content.
8. The behavior must not call ACP modules.
9. The behavior must not call Analysis modules.
10. The behavior must not call taxonomy, risk, governance, or output modules.
11. The behavior must not infer hidden or implicit meaning.
12. The behavior must not assess truth.
13. The behavior must not assess evidence.
14. The behavior must not create relation objects.
15. The behavior must not create risk signals.
16. The behavior must not trigger runtime pipeline execution.
17. The original MDS boundary object must be preserved unchanged.
18. Tests must prove that forbidden downstream fields are absent.
19. Closure documentation must state that full CMO construction remains on HOLD.

## Candidate Function Name

Preferred function name:

- `build_minimal_cmo_shell`

Acceptable alternatives:

- `create_cmo_shell_minimal`
- `build_cmo_boundary_shell`

Function names should avoid:

- `build_cmo`
- `create_canonical_message_object`
- `map_mds_to_cmo`
- `populate_cmo_schema`
- `dispatch_to_acp`
- `run_pipeline`
- `analyze`
- `score`
- `evaluate`

## Recommended Source Area

Preferred source file:

- `src/cognitive_shield/core/canonical_message_object_cmo/minimal_shell.py`

Reason:

The existing CMO scaffold files should remain stable.

The `mds_boundary.py` file should remain focused on boundary eligibility.

A separate `minimal_shell.py` file keeps the CMO shell boundary explicit and reversible.

## Admitted Output Shape

A future minimal CMO shell helper may return a minimal dictionary containing only fields such as:

- `cmo_shell_status`
- `source_stage`
- `target_stage`
- `decomposition_result`
- `boundary_status`

Allowed source stage:

- `message_decomposition_specification_mds`

Allowed target stage:

- `canonical_message_object_cmo`

Allowed CMO shell statuses:

- `cmo_shell_created`
- `not_eligible_for_cmo_shell`

The minimal CMO shell must not expose:

- `canonical_message_object`
- `CanonicalMessageObject`
- `cmo_fields`
- `cmo_schema`
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

- an eligible MDS-to-CMO boundary result creates a minimal CMO shell;
- a non-eligible boundary result does not create a CMO shell;
- the original DecompositionResult is preserved unchanged;
- source stage is MDS;
- target stage is CMO;
- no full CMO object is created;
- no CMO schema fields are exposed;
- no ACP fields are exposed;
- no Analysis fields are exposed;
- no taxonomy, risk, governance, output, truth, evidence, relation, or runtime fields are exposed.

Future tests must not verify:

- full CMO construction;
- CMO schema population;
- CMO field mapping;
- ACP routing;
- Analysis generation;
- truth assessment;
- evidence assessment;
- taxonomy labeling;
- risk scoring;
- downstream pipeline behavior.

## Documentation Discipline

This boundary review is justified because the minimal CMO shell is the first controlled CMO-side object after MDS-to-CMO boundary eligibility.

After this review, source inspection is not required unless the CMO scaffold changes before implementation.

A closure note is required only if minimal CMO shell behavior is implemented.

## No-Drift Confirmation

Confirmed:

- MDS bounded DecompositionResult remains MDS-local;
- MDS-to-CMO boundary eligibility remains an eligibility check only;
- minimal CMO shell behavior is admitted only as a future review-approved shell boundary;
- full CMO construction remains on HOLD;
- CanonicalMessageObject creation remains on HOLD;
- CMO field mapping remains on HOLD;
- CMO schema population remains on HOLD;
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

If this review is accepted, create the minimal CMO shell pass in compressed mode:

1. source file;
2. test file;
3. closure note.

Recommended files:

- `src/cognitive_shield/core/canonical_message_object_cmo/minimal_shell.py`
- `tests/unit/test_cmo_minimal_shell.py`
- `docs/sprint_2/SPRINT_2_CMO_MINIMAL_SHELL_PASS_CLOSURE_NOTE.md`

## Verdict Summary

Minimal CMO shell boundary: ADMITTED FOR CONTROLLED IMPLEMENTATION WITH HARD SAFEGUARDS.

Full CMO construction: HOLD.

CanonicalMessageObject creation: HOLD.

CMO field mapping: HOLD.

CMO schema population: HOLD.

ACP routing: HOLD.

Analysis generation: HOLD.

Runtime pipeline execution: NOT ADMITTED.

Downstream pipeline logic: NOT ADMITTED.
