# Sprint 2 CMO Minimal Object Boundary Review

Status: Boundary review — before admitting minimal Canonical Message Object (CMO) object behavior.

## Purpose

This document records the Sprint 2 boundary review for the next micro-slice after the controlled Canonical Message Object (CMO) field envelope pass.

The purpose is to decide whether the project may admit a minimal CMO object boundary while preventing drift into full Canonical Message Object construction, CMO schema population, CMO field mapping, CMO normalization, CMO enrichment, Agent Communication Protocol (ACP) routing, Analysis generation, runtime pipeline execution, downstream pipeline logic, taxonomy behavior, risk scoring, governance behavior, or output rendering.

This review does not admit implementation by itself.

## Baseline

Sprint 2 has completed:

- Sprint 2 Entry Control Pass
- Pre-real Message Decomposition Specification (MDS) behavior scope refinement
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
- CMO minimal shell pass
- CMO structural contract pass
- CMO field envelope pass
- Python Tests workflow validation

Current state:

- MDS early structural stack: CLOSED
- bounded DecompositionResult shell: CLOSED
- MDS-to-CMO boundary eligibility: CLOSED
- CMO minimal shell: CLOSED
- CMO structural contract: CLOSED
- CMO field envelope: CLOSED
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
- `src/cognitive_shield/core/canonical_message_object_cmo/minimal_shell.py`
- `src/cognitive_shield/core/canonical_message_object_cmo/structural_contract.py`
- `src/cognitive_shield/core/canonical_message_object_cmo/field_envelope.py`

Current restricted areas:

- full Canonical Message Object (CMO) construction: HOLD
- CanonicalMessageObject creation: HOLD
- CMO schema population: HOLD
- CMO field mapping: HOLD
- CMO normalization: HOLD
- CMO enrichment: HOLD
- ACP routing: HOLD
- Analysis generation: NOT STARTED
- runtime pipeline execution: NOT ADMITTED
- downstream pipeline logic: NOT ADMITTED
- taxonomy behavior: NOT STARTED
- risk scoring: NOT STARTED
- governance behavior: NOT STARTED
- output rendering: NOT STARTED

## Boundary Question

Can the project admit a minimal CMO object as the next Sprint 2 micro-slice?

## Verdict

Verdict:

`ADMIT REVIEW WITH HARD SAFEGUARDS`

The project may admit a future minimal CMO object implementation only if it remains:

- minimal-object-only;
- field-envelope-derived;
- structural only;
- non-normalizing;
- non-enriching;
- non-analytical;
- non-runtime;
- not full Canonical Message Object construction;
- not ACP handoff;
- not Analysis generation;
- not downstream pipeline logic.

This boundary review does not yet implement minimal CMO object behavior.

## Critical Boundary Distinction

A CMO field envelope is not a CanonicalMessageObject.

A minimal CMO object is not a full Canonical Message Object.

A minimal CMO object is not CMO schema population.

A minimal CMO object is not final CMO field mapping.

A minimal CMO object is not CMO normalization.

A minimal CMO object is not CMO enrichment.

A minimal CMO object is not ACP handoff.

A minimal CMO object is not an Analysis input bundle.

A minimal CMO object is only a bounded structural object that preserves the previously admitted CMO field envelope and marks the CMO layer as minimally object-shaped.

It must not normalize, enrich, infer, analyze, score, route, dispatch, or become downstream-ready.

## Admitted Future Scope

The future implementation may include only:

- reading an existing CMO field envelope;
- checking whether the field envelope status is `cmo_field_envelope_created`;
- preserving the original bounded MDS DecompositionResult;
- preserving the field envelope;
- returning a minimal CMO object status;
- returning source and target stage identity;
- exposing a minimal CMO object shell;
- testing that no full CMO schema, CMO mapping, ACP, Analysis, taxonomy, risk, governance, output, or runtime fields are exposed.

Allowed minimal CMO object statuses may include:

- `minimal_cmo_object_created`
- `not_ready_for_minimal_cmo_object`

## Not Admitted

The following remain not admitted:

- full Canonical Message Object (CMO) construction;
- full CanonicalMessageObject creation;
- complete CMO schema population;
- semantic CMO field mapping;
- CMO normalization;
- CMO enrichment;
- semantic enrichment;
- MDS-to-CMO conversion beyond already admitted eligibility, shell, structural contract, and field envelope boundaries;
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

1. The behavior must remain a minimal CMO object boundary only.
2. The behavior must require an existing CMO field envelope.
3. The behavior must require `cmo_field_envelope_created` status.
4. The behavior must preserve the original bounded MDS DecompositionResult.
5. The behavior must preserve the existing field envelope.
6. The behavior must not construct a full Canonical Message Object.
7. The behavior must not create a downstream-ready CanonicalMessageObject.
8. The behavior must not populate a complete CMO schema.
9. The behavior must not map MDS fields into final semantic CMO fields.
10. The behavior must not normalize MDS content.
11. The behavior must not enrich MDS content.
12. The behavior must not call ACP modules.
13. The behavior must not call Analysis modules.
14. The behavior must not call taxonomy, risk, governance, or output modules.
15. The behavior must not infer hidden or implicit meaning.
16. The behavior must not assess truth.
17. The behavior must not assess evidence.
18. The behavior must not create relation objects.
19. The behavior must not create risk signals.
20. The behavior must not trigger runtime pipeline execution.
21. The original CMO field envelope must be preserved unchanged.
22. Tests must prove that forbidden downstream fields are absent.
23. Closure documentation must state that full CMO construction remains on HOLD.

## Candidate Function Name

Preferred function name:

- `build_minimal_cmo_object`

Acceptable alternatives:

- `create_minimal_cmo_object`
- `build_cmo_object_minimal`

Function names should avoid:

- `build_cmo`
- `create_canonical_message_object`
- `map_mds_to_cmo`
- `populate_cmo_schema`
- `normalize_cmo`
- `enrich_cmo`
- `dispatch_to_acp`
- `run_pipeline`
- `analyze`
- `score`
- `evaluate`

## Recommended Source Area

Preferred source file:

- `src/cognitive_shield/core/canonical_message_object_cmo/minimal_object.py`

Reason:

The existing CMO scaffold files should remain stable.

The `mds_boundary.py` file should remain focused on boundary eligibility.

The `minimal_shell.py` file should remain focused on shell creation only.

The `structural_contract.py` file should remain focused on readiness contract only.

The `field_envelope.py` file should remain focused on minimal field envelope only.

A separate `minimal_object.py` file keeps the minimal CMO object boundary explicit and reversible.

## Admitted Output Shape

A future minimal CMO object helper may return a minimal dictionary containing only fields such as:

- `minimal_cmo_object_status`
- `source_stage`
- `target_stage`
- `cmo_field_envelope_status`
- `decomposition_result`
- `field_envelope`

Allowed minimal CMO object statuses:

- `minimal_cmo_object_created`
- `not_ready_for_minimal_cmo_object`

The minimal CMO object must not expose:

- `canonical_message_object`
- `CanonicalMessageObject`
- `full_cmo`
- `cmo_schema`
- `cmo_mapping`
- `mapped_fields`
- `normalized_content`
- `enriched_content`
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

- a valid CMO field envelope creates a minimal CMO object;
- a non-ready field envelope does not create a minimal CMO object;
- the original DecompositionResult is preserved unchanged;
- the field envelope is preserved;
- source stage is MDS;
- target stage is CMO;
- no full CMO object is created;
- no CMO schema fields are exposed;
- no CMO mapping fields are exposed;
- no normalized or enriched content is exposed;
- no ACP fields are exposed;
- no Analysis fields are exposed;
- no taxonomy, risk, governance, output, truth, evidence, relation, or runtime fields are exposed.

Future tests must not verify:

- full CMO construction;
- CanonicalMessageObject creation;
- CMO schema population;
- CMO field mapping;
- CMO normalization;
- CMO enrichment;
- ACP routing;
- Analysis generation;
- truth assessment;
- evidence assessment;
- taxonomy labeling;
- risk scoring;
- downstream pipeline behavior.

## Documentation Discipline

This boundary review is justified because the CMO minimal object begins to approach a real CMO-shaped structure while still forbidding full construction, schema population, mapping, enrichment, and downstream handoff.

After this review, small repository checks may remain in chat unless they reveal a blocker.

A closure note is required only if CMO minimal object behavior is implemented.

## No-Drift Confirmation

Confirmed:

- MDS bounded DecompositionResult remains MDS-local;
- MDS-to-CMO boundary eligibility remains an eligibility check only;
- CMO minimal shell remains shell-only and eligibility-derived;
- CMO structural contract remains contract-only and shell-derived;
- CMO field envelope remains envelope-only and contract-derived;
- CMO minimal object behavior is admitted only as a future review-approved minimal object boundary;
- full CMO construction remains on HOLD;
- CanonicalMessageObject creation remains on HOLD;
- CMO field mapping remains on HOLD;
- CMO schema population remains on HOLD;
- CMO normalization remains on HOLD;
- CMO enrichment remains on HOLD;
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

If this review is accepted, create the CMO minimal object pass in compressed mode:

1. source file;
2. test file;
3. closure note.

Recommended files:

- `src/cognitive_shield/core/canonical_message_object_cmo/minimal_object.py`
- `tests/unit/test_cmo_minimal_object.py`
- `docs/sprint_2/SPRINT_2_CMO_MINIMAL_OBJECT_PASS_CLOSURE_NOTE.md`

## Verdict Summary

CMO minimal object boundary: ADMITTED FOR CONTROLLED IMPLEMENTATION WITH HARD SAFEGUARDS.

Full CMO construction: HOLD.

CanonicalMessageObject creation: HOLD.

CMO field mapping: HOLD.

CMO schema population: HOLD.

CMO normalization: HOLD.

CMO enrichment: HOLD.

ACP routing: HOLD.

Analysis generation: HOLD.

Runtime pipeline execution: NOT ADMITTED.

Downstream pipeline logic: NOT ADMITTED.
