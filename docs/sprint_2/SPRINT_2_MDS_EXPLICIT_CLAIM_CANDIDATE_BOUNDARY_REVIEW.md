# Sprint 2 MDS Explicit Claim Candidate Boundary Review

Status: Boundary review — before admitting explicit claim candidate behavior.

## Purpose

This document records the Sprint 2 boundary review for the next Message Decomposition Specification (MDS) micro-slice after the stable MDS surface layer.

The purpose is to decide whether the project may admit explicit claim candidate boundary behavior while preventing drift into full claim extraction, implicit inference, relation inference, truth assessment, taxonomy behavior, risk scoring, Canonical Message Object (CMO) construction, Agent Communication Protocol (ACP) routing, Analysis generation, runtime pipeline execution, or downstream pipeline logic.

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
- MDS explicit surface segmentation boundary review
- MDS explicit surface segmentation pass
- Python Tests workflow validation

Current MDS surface layer:

- surface-level MDS preparation: CLOSED
- single surface unit boundary: CLOSED
- surface bundle boundary: CLOSED
- explicit surface segmentation: CLOSED
- Python Tests workflow: GREEN

Current restricted areas:

- full claim extraction: HOLD
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

Can the project admit explicit claim candidate boundary behavior as the next MDS micro-slice?

## Verdict

Verdict:

`ADMIT REVIEW WITH HARD SAFEGUARDS`

The project may admit a future explicit claim candidate implementation only if it remains:

- explicit-text-only;
- candidate-only;
- non-inferential;
- non-truth-evaluating;
- non-taxonomic;
- non-risk-scoring;
- non-runtime.

This boundary review does not yet implement claim candidate behavior.

## Critical Boundary Distinction

An explicit claim candidate is not a confirmed claim.

An explicit claim candidate is only a visible surface text span that may later be reviewed for claim-unit admissibility.

An explicit claim candidate must not be treated as:

- a verified claim;
- a truth-bearing conclusion;
- evidence;
- a framing unit;
- a relation object;
- a risk signal;
- a taxonomy label;
- a verdict;
- a downstream analytical object.

## Admitted Future Scope

The future implementation may include only:

- reading existing surface units;
- selecting surface units that are non-empty and visibly assertion-like at a shallow textual level;
- creating explicit claim candidate records;
- preserving the original surface text;
- preserving source surface unit identity;
- assigning stable claim candidate identifiers;
- returning candidate status only;
- testing that no inference, relation, taxonomy, risk, or downstream fields are exposed.

Allowed candidate status values may include:

- `claim_candidate_created`
- `not_claim_candidate`

## Not Admitted

The following remain not admitted:

- full claim extraction;
- implicit claim inference;
- hidden claim reconstruction;
- truth assessment;
- evidence assessment;
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

Any future implementation after this review must preserve the following safeguards:

1. The behavior must remain local to the MDS layer.
2. The behavior may only inspect explicit surface text.
3. The behavior must preserve original surface text.
4. The behavior must preserve source surface unit identity.
5. The behavior must not infer hidden or implicit claims.
6. The behavior must not assess truth.
7. The behavior must not assess evidence.
8. The behavior must not create relation objects.
9. The behavior must not create framing units.
10. The behavior must not create taxonomy labels.
11. The behavior must not create risk signals.
12. The behavior must not construct a full DecompositionResult.
13. The behavior must not call CMO, ACP, Analysis, taxonomy, risk, governance, or output modules.
14. The behavior must not trigger runtime pipeline execution.
15. Tests must prove that forbidden fields are absent.
16. Closure documentation must state that full claim extraction remains on HOLD.

## Candidate Function Name

Preferred function name:

- `build_explicit_claim_candidates`

Acceptable alternatives:

- `identify_explicit_claim_candidates`
- `build_claim_candidate_boundary`

Function names should avoid:

- `extract_claims`
- `infer_claims`
- `analyze_claims`
- `score_claims`
- `validate_truth`
- `construct_decomposition_result`

## Recommended Source Area

Preferred source file:

- `src/cognitive_shield/core/message_decomposition_specification_mds/claim_candidates.py`

Reason:

The existing surface preparation, surface unit, surface bundle, and surface segmentation files should remain focused on surface-level behavior.

A separate `claim_candidates.py` file keeps the candidate boundary explicit and reversible.

## Admitted Output Shape

A future explicit claim candidate helper may return a minimal dictionary containing only fields such as:

- `mds_stage`
- `candidate_status`
- `claim_candidates`

Each claim candidate may contain only:

- `claim_candidate_id`
- `source_surface_unit_id`
- `source_text`
- `candidate_type`
- `candidate_status`
- `order_index`

Allowed `candidate_type`:

- `explicit_claim_candidate`

Allowed candidate statuses:

- `claim_candidate_created`
- `not_claim_candidate`

## Required Test Boundary

Future tests may verify:

- explicit assertion-like surface text can create a claim candidate;
- non-assertion-like or empty surface text is blocked or produces no candidate;
- source surface unit identity is preserved;
- source text is preserved;
- candidate order is preserved;
- no implicit claims are created;
- no framing fields are exposed;
- no relation fields are exposed;
- no evidence, taxonomy, risk, governance, CMO, ACP, Analysis, or output fields are exposed.

Future tests must not verify:

- truth assessment;
- evidence assessment;
- implicit claim inference;
- semantic relation inference;
- framing classification;
- taxonomy labeling;
- risk scoring;
- decomposition result construction;
- downstream pipeline behavior.

## Documentation Discipline

This boundary review is justified because explicit claim candidate behavior is the first MDS step adjacent to claim handling.

After this review, small repository checks may remain in chat unless they reveal a blocker.

A closure note is required only if explicit claim candidate behavior is implemented.

## No-Drift Confirmation

Confirmed:

- MDS surface layer remains bounded;
- explicit claim candidate behavior is admitted only as a future review-approved micro-slice;
- full claim extraction remains on HOLD;
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

If this review is accepted, create the explicit claim candidate pass in compressed mode:

1. source file;
2. test file;
3. closure note.

Recommended files:

- `src/cognitive_shield/core/message_decomposition_specification_mds/claim_candidates.py`
- `tests/unit/test_mds_claim_candidates.py`
- `docs/sprint_2/SPRINT_2_MDS_EXPLICIT_CLAIM_CANDIDATE_PASS_CLOSURE_NOTE.md`

## Verdict Summary

Explicit claim candidate boundary: ADMITTED FOR CONTROLLED IMPLEMENTATION WITH HARD SAFEGUARDS.

Full claim extraction: HOLD.

Implicit inference: HOLD.

Truth assessment: HOLD.

Framing extraction: HOLD.

Relation inference: HOLD.

Full DecompositionResult construction: HOLD.

Runtime pipeline execution: NOT ADMITTED.

Downstream pipeline logic: NOT ADMITTED.
