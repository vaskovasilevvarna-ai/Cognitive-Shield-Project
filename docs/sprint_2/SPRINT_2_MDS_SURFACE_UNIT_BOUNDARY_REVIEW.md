# Sprint 2 MDS Surface Unit Boundary Review

Status: Boundary review — before admitting minimal MDS surface unit behavior.

## Purpose

This document records the Sprint 2 boundary review for the next Message Decomposition Specification (MDS) micro-slice after surface-level preparation.

The purpose is to determine whether the project may admit a minimal surface unit boundary without opening real segmentation, claim extraction, implicit inference, relation inference, full DecompositionResult construction, Canonical Message Object (CMO) construction, Agent Communication Protocol (ACP) routing, Analysis generation, runtime pipeline execution, or downstream pipeline logic.

## Baseline

Sprint 2 has completed:

- Sprint 2 Entry Control Pass
- Pre-real MDS behavior scope refinement
- MDS surface preparation pass
- MDS surface preparation repository verification
- Python Tests workflow validation

Current MDS state:

- surface-level MDS preparation: CLOSED
- surface preparation repository verification: PASS
- Python Tests workflow: GREEN
- claim extraction: HOLD
- implicit inference: HOLD
- relation inference: HOLD
- full DecompositionResult construction: HOLD

## Boundary Question

Can the project admit a minimal MDS surface unit boundary?

## Verdict

Verdict:

`ADMIT WITH HARD SAFEGUARDS`

The project may admit only a minimal single-surface-unit boundary.

This does not admit real segmentation.

This does not admit claim extraction.

This does not admit framing extraction.

This does not admit relation inference.

This does not admit full DecompositionResult construction.

## Admitted Scope

The admitted next micro-slice may include only:

- creating one minimal surface unit from the whole prepared source text;
- preserving the original source text;
- assigning a stable surface unit identifier;
- marking the unit as surface-level only;
- returning a minimal surface unit dictionary or simple typed structure;
- testing that no claim, framing, relation, CMO, ACP, Analysis, taxonomy, or risk fields are exposed.

The surface unit is not a claim unit.

The surface unit is not a framing unit.

The surface unit is not a decomposition result.

## Recommended Source Area

Preferred source file:

- `src/cognitive_shield/core/message_decomposition_specification_mds/surface_units.py`

Reason:

The existing MDS service scaffold should remain unchanged.

The existing surface preparation file should remain focused on preparation status.

A separate `surface_units.py` file keeps the new boundary explicit and reversible.

## Candidate Function Name

Preferred function name:

- `build_minimal_surface_unit`

Acceptable alternatives:

- `build_single_surface_unit`
- `create_surface_unit_minimal`

Function names should avoid:

- `decompose`
- `extract_claim`
- `infer`
- `segment`
- `analyze`
- `construct_decomposition_result`

## Admitted Output Shape

The first minimal surface unit may return only fields such as:

- `surface_unit_id`
- `source_text`
- `unit_type`
- `surface_status`
- `mds_stage`

Allowed `unit_type`:

- `surface_text`

Allowed `surface_status`:

- `surface_unit_created`
- `invalid_surface_text`

Allowed `mds_stage`:

- `message_decomposition_specification_mds`

## Not Admitted

The following remain not admitted:

- splitting text into multiple surface segments;
- claim extraction;
- implicit claim inference;
- framing extraction;
- relation inference;
- context carrier construction;
- global narrative structure construction;
- decomposition uncertainty calculation;
- traceability map construction beyond minimal surface identity;
- full DecompositionResult construction;
- real MDS output conversion;
- real Canonical Message Object (CMO) construction;
- CanonicalMessageObject creation;
- real Agent Communication Protocol (ACP) routing;
- ACPBundle creation;
- ACPMessage dispatch;
- real Analysis generation;
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

## Hard Safeguards

Any implementation after this review must preserve the following safeguards:

1. The behavior must remain local to the MDS layer.
2. The behavior must create at most one surface unit.
3. The behavior must preserve the original source text.
4. The behavior must not split text into multiple analytical segments.
5. The behavior must not create claim units.
6. The behavior must not create framing units.
7. The behavior must not create relation objects.
8. The behavior must not perform implicit inference.
9. The behavior must not construct a full DecompositionResult.
10. The behavior must not call CMO, ACP, Analysis, taxonomy, risk, governance, or output modules.
11. The behavior must not trigger runtime pipeline execution.
12. Tests must prove that forbidden fields are absent.
13. Closure documentation must state that real decomposition remains not admitted.

## Required Test Boundary

Future tests may verify:

- a valid prepared source text creates one minimal surface unit;
- the original text is preserved;
- the surface unit has a stable identifier;
- the unit type is `surface_text`;
- invalid or whitespace-only source text is blocked;
- no claim fields are exposed;
- no framing fields are exposed;
- no relation fields are exposed;
- no CMO, ACP, Analysis, taxonomy, risk, governance, or output fields are exposed.

Future tests must not verify:

- multi-segment decomposition;
- claim extraction;
- implicit inference;
- framing extraction;
- relation inference;
- decomposition result construction;
- CMO construction;
- ACP routing;
- Analysis generation;
- downstream pipeline behavior.

## Documentation Discipline

This boundary review is justified because it opens a new MDS behavior boundary.

After this review, small repository checks may remain in chat unless they reveal a blocker.

A closure note is required only if the surface unit behavior is implemented.

## No-Drift Confirmation

Confirmed:

- surface-level preparation remains the only completed MDS behavior so far;
- minimal surface unit boundary may be admitted only under hard safeguards;
- claim extraction remains on HOLD;
- implicit inference remains on HOLD;
- relation inference remains on HOLD;
- full DecompositionResult construction remains on HOLD;
- CMO construction remains on HOLD;
- ACP routing remains on HOLD;
- Analysis generation has not started;
- runtime pipeline execution has not started;
- downstream pipeline logic has not started;
- taxonomy behavior has not started;
- risk scoring has not started;
- governance behavior has not started;
- output rendering has not started;
- merge to `main` has not been performed.

## Recommended Next Step

Recommended next step:

Create the minimal surface unit pass in compressed mode:

1. source file;
2. test file;
3. closure note.

Recommended files:

- `src/cognitive_shield/core/message_decomposition_specification_mds/surface_units.py`
- `tests/unit/test_mds_surface_units.py`
- `docs/sprint_2/SPRINT_2_MDS_SURFACE_UNIT_PASS_CLOSURE_NOTE.md`

## Verdict Summary

Minimal MDS surface unit boundary: ADMITTED WITH HARD SAFEGUARDS.

Real segmentation: HOLD.

Claim extraction: HOLD.

Implicit inference: HOLD.

Relation inference: HOLD.

Full DecompositionResult construction: HOLD.

Runtime pipeline execution: NOT ADMITTED.

Downstream pipeline logic: NOT ADMITTED.
