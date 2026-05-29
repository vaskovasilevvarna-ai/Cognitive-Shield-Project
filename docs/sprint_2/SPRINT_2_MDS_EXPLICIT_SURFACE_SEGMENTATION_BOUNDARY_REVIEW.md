# Sprint 2 MDS Explicit Surface Segmentation Boundary Review

Status: Boundary review — before admitting explicit surface segmentation behavior.

## Purpose

This document records the Sprint 2 boundary review for the next Message Decomposition Specification (MDS) micro-slice after the stable MDS surface stack.

The purpose is to decide whether the project may admit explicit surface segmentation while preventing drift into claim extraction, implicit inference, relation inference, full DecompositionResult construction, Canonical Message Object (CMO) construction, Agent Communication Protocol (ACP) routing, Analysis generation, runtime pipeline execution, or downstream pipeline logic.

This review does not admit implementation by itself.

## Baseline

Sprint 2 has completed:

- Sprint 2 Entry Control Pass
- Pre-real MDS behavior scope refinement
- MDS surface preparation pass
- MDS surface unit boundary review
- MDS surface unit pass
- MDS surface bundle boundary review
- MDS surface bundle pass
- Python Tests workflow validation

Current MDS surface stack:

- surface-level MDS preparation: CLOSED
- single surface unit boundary: CLOSED
- surface bundle boundary: CLOSED
- Python Tests workflow: GREEN

Current restricted areas:

- claim extraction: HOLD
- implicit inference: HOLD
- framing extraction: HOLD
- relation inference: HOLD
- full DecompositionResult construction: HOLD
- CMO construction: HOLD
- ACP routing: HOLD
- Analysis generation: NOT STARTED
- runtime pipeline execution: NOT ADMITTED
- downstream pipeline logic: NOT ADMITTED

## Boundary Question

Can the project admit explicit surface segmentation as the next MDS micro-slice?

## Verdict

Verdict:

`ADMIT REVIEW WITH HARD SAFEGUARDS`

The project may admit a future explicit surface segmentation implementation only if it remains:

- surface-only;
- explicit-boundary-only;
- non-analytical;
- non-claim;
- non-inferential;
- non-runtime.

This boundary review does not yet implement segmentation.

## Admitted Future Scope

The future implementation may include only:

- splitting source text by explicit surface boundaries;
- preserving each segment as surface text;
- creating multiple surface units;
- assigning stable surface unit identifiers;
- preserving the original order of surface units;
- returning a minimal surface segmentation result;
- testing that no claim, framing, relation, CMO, ACP, Analysis, taxonomy, or risk fields are exposed.

Allowed boundary types may include only clearly visible textual boundaries such as:

- line breaks;
- paragraph breaks;
- simple sentence-ending punctuation, if used conservatively.

## Not Admitted

The following remain not admitted:

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

## Critical Boundary Distinction

Explicit surface segmentation is not claim extraction.

A surface segment is only a visible text span.

A surface segment must not be treated as:

- a claim unit;
- a framing unit;
- a relation object;
- a context carrier;
- evidence;
- a risk signal;
- a verdict;
- an analytical conclusion.

## Hard Safeguards

Any future implementation after this review must preserve the following safeguards:

1. The behavior must remain local to the MDS layer.
2. The behavior may split only by explicit visible surface boundaries.
3. The behavior must preserve original segment text.
4. The behavior must preserve segment order.
5. The behavior must not infer meaning.
6. The behavior must not classify claims.
7. The behavior must not create claim units.
8. The behavior must not create framing units.
9. The behavior must not create relation objects.
10. The behavior must not create context carriers.
11. The behavior must not calculate uncertainty.
12. The behavior must not construct a full DecompositionResult.
13. The behavior must not call CMO, ACP, Analysis, taxonomy, risk, governance, or output modules.
14. The behavior must not trigger runtime pipeline execution.
15. Tests must prove that forbidden fields are absent.
16. Closure documentation must state that claim extraction remains on HOLD.

## Required Test Boundary

Future tests may verify:

- a single-line input returns one surface segment;
- a multi-line input returns multiple surface segments;
- empty or whitespace-only input is blocked or returns no valid surface segments;
- segment order is preserved;
- segment text is preserved;
- each surface unit has a stable identifier;
- no claim fields are exposed;
- no framing fields are exposed;
- no relation fields are exposed;
- no CMO, ACP, Analysis, taxonomy, risk, governance, or output fields are exposed.

Future tests must not verify:

- claim extraction;
- implicit inference;
- framing extraction;
- relation inference;
- semantic grouping;
- evidence assessment;
- risk scoring;
- decomposition result construction;
- downstream pipeline behavior.

## Recommended Source Area

Preferred source file:

- `src/cognitive_shield/core/message_decomposition_specification_mds/surface_segmentation.py`

Reason:

The existing `surface_preparation.py`, `surface_units.py`, and `surface_bundle.py` should remain stable.

A separate `surface_segmentation.py` file keeps explicit segmentation isolated and reversible.

## Candidate Function Name

Preferred function name:

- `segment_surface_text_explicit`

Acceptable alternatives:

- `build_explicit_surface_segments`
- `split_surface_text_explicit`

Function names should avoid:

- `extract_claims`
- `infer`
- `analyze`
- `decompose_claims`
- `construct_decomposition_result`

## Admitted Output Shape

A future explicit surface segmentation helper may return a minimal dictionary containing only fields such as:

- `mds_stage`
- `segmentation_status`
- `surface_units`

Each surface unit may contain only:

- `surface_unit_id`
- `source_text`
- `unit_type`
- `surface_status`
- `order_index`

Allowed `unit_type`:

- `surface_text`

Allowed `segmentation_status` values:

- `surface_segments_created`
- `blocked_invalid_surface_text`

## Documentation Discipline

This boundary review is justified because explicit surface segmentation opens a higher-risk MDS boundary than preparation, single unit creation, or bundling.

After this review, small repository checks may remain in chat unless they reveal a blocker.

A closure note is required only if explicit surface segmentation behavior is implemented.

## No-Drift Confirmation

Confirmed:

- MDS surface stack remains bounded;
- explicit surface segmentation is admitted only as a future review-approved micro-slice;
- claim extraction remains on HOLD;
- implicit inference remains on HOLD;
- framing extraction remains on HOLD;
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

If this review is accepted, create the explicit surface segmentation pass in compressed mode:

1. source file;
2. test file;
3. closure note.

Recommended files:

- `src/cognitive_shield/core/message_decomposition_specification_mds/surface_segmentation.py`
- `tests/unit/test_mds_surface_segmentation.py`
- `docs/sprint_2/SPRINT_2_MDS_EXPLICIT_SURFACE_SEGMENTATION_PASS_CLOSURE_NOTE.md`

## Verdict Summary

Explicit surface segmentation boundary: ADMITTED FOR CONTROLLED IMPLEMENTATION WITH HARD SAFEGUARDS.

Claim extraction: HOLD.

Implicit inference: HOLD.

Framing extraction: HOLD.

Relation inference: HOLD.

Full DecompositionResult construction: HOLD.

Runtime pipeline execution: NOT ADMITTED.

Downstream pipeline logic: NOT ADMITTED.
