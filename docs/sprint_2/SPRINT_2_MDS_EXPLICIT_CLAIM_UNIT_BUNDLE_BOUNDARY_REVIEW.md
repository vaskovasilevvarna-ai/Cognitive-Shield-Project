# Sprint 2 MDS Explicit Claim Unit Bundle Boundary Review

Status: Boundary review — before admitting explicit claim unit bundle behavior.

## Purpose

This document records the Sprint 2 boundary review for the next Message Decomposition Specification (MDS) micro-slice after explicit claim unit behavior.

The purpose is to decide whether the project may admit a minimal explicit claim unit bundle while preventing drift into DecompositionResult construction, implicit inference, relation inference, truth assessment, evidence assessment, taxonomy behavior, risk scoring, Canonical Message Object (CMO) construction, Agent Communication Protocol (ACP) routing, Analysis generation, runtime pipeline execution, or downstream pipeline logic.

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
- MDS explicit claim unit admissibility review
- MDS explicit claim unit pass
- Python Tests workflow validation

Current MDS state:

- MDS surface layer: STABLE
- explicit surface segmentation: CLOSED
- explicit claim candidate boundary: CLOSED
- explicit claim unit boundary: CLOSED
- Python Tests workflow: GREEN

Current restricted areas:

- implicit inference: HOLD
- hidden claim reconstruction: HOLD
- truth assessment: HOLD
- evidence assessment: HOLD
- framing extraction: HOLD
- relation inference: HOLD
- full DecompositionResult construction: HOLD
- CMO construction: HOLD
- ACP routing: HOLD
- Analysis generation: NOT STARTED
- runtime pipeline execution: NOT ADMITTED
- downstream pipeline logic: NOT ADMITTED

## Boundary Question

Can the project admit a minimal explicit claim unit bundle as the next MDS micro-slice?

## Verdict

Verdict:

`ADMIT REVIEW WITH HARD SAFEGUARDS`

The project may admit a future explicit claim unit bundle implementation only if it remains:

- structural only;
- explicit-claim-unit-derived;
- non-inferential;
- non-truth-evaluating;
- non-evidence-assessing;
- non-taxonomic;
- non-risk-scoring;
- non-runtime;
- not a full DecompositionResult.

This boundary review does not yet implement claim unit bundle behavior.

## Critical Boundary Distinction

A claim unit bundle is not a DecompositionResult.

A claim unit bundle is not a Canonical Message Object (CMO).

A claim unit bundle is not an analytical conclusion.

A claim unit bundle is only a minimal MDS-local container for already admitted explicit claim units.

It must not perform new extraction, inference, classification, scoring, or downstream conversion.

## Admitted Future Scope

The future implementation may include only:

- reading existing explicit claim unit records;
- preserving claim unit records without rewriting meaning;
- grouping claim units into a minimal MDS-local bundle;
- preserving claim unit order;
- preserving source claim candidate identity;
- preserving source surface unit identity;
- returning bundle status;
- returning the MDS stage identity;
- testing that no truth, evidence, framing, relation, taxonomy, risk, CMO, ACP, Analysis, governance, output, or runtime fields are exposed.

Allowed bundle status values may include:

- `claim_unit_bundle_created`
- `no_claim_units`

## Not Admitted

The following remain not admitted:

- implicit claim inference;
- hidden claim reconstruction;
- claim completion beyond explicit text;
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
2. The behavior may only bundle existing explicit claim units.
3. The behavior must not create new claim units.
4. The behavior must preserve claim unit order.
5. The behavior must preserve source claim candidate identity.
6. The behavior must preserve source surface unit identity.
7. The behavior must preserve source text.
8. The behavior must not infer hidden or implicit claims.
9. The behavior must not rewrite claim meaning.
10. The behavior must not assess truth.
11. The behavior must not assess evidence.
12. The behavior must not create framing units.
13. The behavior must not create relation objects.
14. The behavior must not create taxonomy labels.
15. The behavior must not create risk signals.
16. The behavior must not construct a full DecompositionResult.
17. The behavior must not call CMO, ACP, Analysis, taxonomy, risk, governance, or output modules.
18. The behavior must not trigger runtime pipeline execution.
19. Tests must prove that forbidden fields are absent.
20. Closure documentation must state that DecompositionResult construction remains on HOLD.

## Candidate Function Name

Preferred function name:

- `build_explicit_claim_unit_bundle`

Acceptable alternatives:

- `bundle_explicit_claim_units`
- `build_claim_unit_bundle_minimal`

Function names should avoid:

- `construct_decomposition_result`
- `convert_to_cmo`
- `infer_claims`
- `evaluate_claims`
- `analyze_claims`
- `score_claims`

## Recommended Source Area

Preferred source file:

- `src/cognitive_shield/core/message_decomposition_specification_mds/claim_unit_bundle.py`

Reason:

The existing `claim_units.py` file should remain focused on claim unit creation.

A separate `claim_unit_bundle.py` file keeps the structural bundling boundary explicit and reversible.

## Admitted Output Shape

A future explicit claim unit bundle helper may return a minimal dictionary containing only fields such as:

- `mds_stage`
- `bundle_status`
- `claim_units`

Allowed bundle statuses:

- `claim_unit_bundle_created`
- `no_claim_units`

The bundle must not expose:

- `decomposition_result`
- `canonical_message_object`
- `acp_bundle`
- `analysis_bundle`
- `taxonomy_labels`
- `risk_profile`

## Required Test Boundary

Future tests may verify:

- explicit claim units can be bundled;
- claim unit order is preserved;
- source claim candidate identity is preserved;
- source surface unit identity is preserved;
- source text is preserved;
- empty claim unit lists return `no_claim_units`;
- non-claim-unit records are ignored or blocked;
- no truth fields are exposed;
- no evidence fields are exposed;
- no framing fields are exposed;
- no relation fields are exposed;
- no taxonomy, risk, CMO, ACP, Analysis, governance, or output fields are exposed.

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

This boundary review is justified because explicit claim unit bundling is the last safe MDS-local structural step before the project approaches higher-risk MDS assembly boundaries.

After this review, small repository checks may remain in chat unless they reveal a blocker.

A closure note is required only if explicit claim unit bundle behavior is implemented.

## No-Drift Confirmation

Confirmed:

- MDS surface layer remains bounded;
- explicit claim candidate behavior remains candidate-only;
- explicit claim unit behavior remains structural only;
- explicit claim unit bundle behavior is admitted only as a future review-approved MDS-local structural micro-slice;
- implicit inference remains on HOLD;
- hidden claim reconstruction remains on HOLD;
- truth assessment remains on HOLD;
- evidence assessment remains on HOLD;
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

If this review is accepted, create the explicit claim unit bundle pass in compressed mode:

1. source file;
2. test file;
3. closure note.

Recommended files:

- `src/cognitive_shield/core/message_decomposition_specification_mds/claim_unit_bundle.py`
- `tests/unit/test_mds_claim_unit_bundle.py`
- `docs/sprint_2/SPRINT_2_MDS_EXPLICIT_CLAIM_UNIT_BUNDLE_PASS_CLOSURE_NOTE.md`

## Verdict Summary

Explicit claim unit bundle boundary: ADMITTED FOR CONTROLLED IMPLEMENTATION WITH HARD SAFEGUARDS.

DecompositionResult construction: HOLD.

CMO construction: HOLD.

ACP routing: HOLD.

Implicit inference: HOLD.

Truth assessment: HOLD.

Evidence assessment: HOLD.

Relation inference: HOLD.

Runtime pipeline execution: NOT ADMITTED.

Downstream pipeline logic: NOT ADMITTED.
