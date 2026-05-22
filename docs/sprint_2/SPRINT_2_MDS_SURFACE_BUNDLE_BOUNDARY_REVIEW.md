# Sprint 2 MDS Surface Bundle Boundary Review

Status: Boundary review — before admitting minimal MDS surface bundle behavior.

## Purpose

This document records the Sprint 2 boundary review for the next Message Decomposition Specification (MDS) micro-slice after surface preparation and single surface unit creation.

The purpose is to determine whether the project may admit a minimal MDS surface bundle boundary without opening real segmentation, claim extraction, implicit inference, relation inference, full DecompositionResult construction, Canonical Message Object (CMO) construction, Agent Communication Protocol (ACP) routing, Analysis generation, runtime pipeline execution, or downstream pipeline logic.

## Baseline

Sprint 2 has completed:

- Sprint 2 Entry Control Pass
- Pre-real MDS behavior scope refinement
- MDS surface preparation pass
- MDS surface preparation repository verification
- MDS surface unit boundary review
- MDS surface unit pass
- Python Tests workflow validation

Current MDS state:

- surface-level MDS preparation: CLOSED
- single surface unit boundary: CLOSED
- Python Tests workflow: GREEN
- claim extraction: HOLD
- implicit inference: HOLD
- relation inference: HOLD
- full DecompositionResult construction: HOLD

## Boundary Question

Can the project admit a minimal MDS surface bundle boundary?

## Verdict

Verdict:

`ADMIT WITH HARD SAFEGUARDS`

The project may admit only a minimal surface bundle that combines:

- one surface preparation status;
- one single surface unit;
- a bundle-level status;
- the MDS stage identity.

This does not admit real segmentation.

This does not admit claim extraction.

This does not admit framing extraction.

This does not admit relation inference.

This does not admit full DecompositionResult construction.

## Admitted Scope

The admitted next micro-slice may include only:

- accepting source text;
- using the existing surface preparation helper;
- using the existing single surface unit helper;
- returning one minimal surface bundle;
- preserving original source text through the surface unit;
- exposing bundle status only;
- testing that no claim, framing, relation, CMO, ACP, Analysis, taxonomy, or risk fields are exposed.

The surface bundle is not a DecompositionResult.

The surface bundle is not a CMO-ready object.

The surface bundle is not an analytical interpretation.

## Recommended Source Area

Preferred source file:

- `src/cognitive_shield/core/message_decomposition_specification_mds/surface_bundle.py`

Reason:

The existing `surface_preparation.py` should remain focused on surface preparation.

The existing `surface_units.py` should remain focused on one minimal surface unit.

A separate `surface_bundle.py` file keeps the boundary explicit and reversible.

## Candidate Function Name

Preferred function name:

- `build_mds_surface_bundle`

Acceptable alternatives:

- `build_minimal_surface_bundle`
- `create_surface_bundle_minimal`

Function names should avoid:

- `decompose`
- `extract_claim`
- `infer`
- `segment`
- `analyze`
- `construct_decomposition_result`

## Admitted Output Shape

The minimal surface bundle may return only fields such as:

- `mds_stage`
- `bundle_status`
- `surface_preparation`
- `surface_unit`

Allowed `bundle_status` values:

- `surface_bundle_created`
- `blocked_invalid_surface_text`

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
- full traceability map construction;
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
2. The behavior may combine only existing surface preparation and surface unit helpers.
3. The behavior must create at most one surface unit.
4. The behavior must preserve the original source text.
5. The behavior must not split text into multiple analytical segments.
6. The behavior must not create claim units.
7. The behavior must not create framing units.
8. The behavior must not create relation objects.
9. The behavior must not perform implicit inference.
10. The behavior must not construct a full DecompositionResult.
11. The behavior must not call CMO, ACP, Analysis, taxonomy, risk, governance, or output modules.
12. The behavior must not trigger runtime pipeline execution.
13. Tests must prove that forbidden fields are absent.
14. Closure documentation must state that real decomposition remains not admitted.

## Required Test Boundary

Future tests may verify:

- valid source text creates a minimal surface bundle;
- the bundle includes surface preparation data;
- the bundle includes one surface unit;
- invalid or whitespace-only source text returns blocked bundle status;
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

A closure note is required only if the surface bundle behavior is implemented.

## No-Drift Confirmation

Confirmed:

- surface preparation remains bounded;
- single surface unit behavior remains bounded;
- minimal surface bundle boundary may be admitted only under hard safeguards;
- real segmentation remains on HOLD;
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

Create the minimal surface bundle pass in compressed mode:

1. source file;
2. test file;
3. closure note.

Recommended files:

- `src/cognitive_shield/core/message_decomposition_specification_mds/surface_bundle.py`
- `tests/unit/test_mds_surface_bundle.py`
- `docs/sprint_2/SPRINT_2_MDS_SURFACE_BUNDLE_PASS_CLOSURE_NOTE.md`

## Verdict Summary

Minimal MDS surface bundle boundary: ADMITTED WITH HARD SAFEGUARDS.

Real segmentation: HOLD.

Claim extraction: HOLD.

Implicit inference: HOLD.

Relation inference: HOLD.

Full DecompositionResult construction: HOLD.

Runtime pipeline execution: NOT ADMITTED.

Downstream pipeline logic: NOT ADMITTED.
