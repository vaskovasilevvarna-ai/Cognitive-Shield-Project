# Sprint 2 MDS Explicit Claim Unit Admissibility Review

Status: Admissibility review — before admitting explicit claim unit behavior.

## Purpose

This document records the Sprint 2 admissibility review for the next Message Decomposition Specification (MDS) micro-slice after explicit claim candidate behavior.

The purpose is to decide whether the project may admit explicit claim unit behavior while preventing drift into implicit claim inference, hidden claim reconstruction, truth assessment, evidence assessment, framing extraction, relation inference, full DecompositionResult construction, Canonical Message Object (CMO) construction, Agent Communication Protocol (ACP) routing, Analysis generation, runtime pipeline execution, or downstream pipeline logic.

This review does not admit implementation by itself.

## Baseline

Sprint 2 has completed:

- Sprint 2 Entry Control Pass
- Pre-real MDS behavior scope refinement
- MDS surface preparation pass
- MDS surface unit pass
- MDS surface bundle pass
- MDS explicit surface segmentation pass
- MDS explicit claim candidate boundary review
- MDS explicit claim candidate pass
- Python Tests workflow validation

Current MDS state:

- MDS surface layer: STABLE
- explicit surface segmentation: CLOSED
- explicit claim candidate boundary: CLOSED
- Python Tests workflow: GREEN

Current restricted areas:

- full claim extraction: HOLD
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

## Critical Distinction

A claim candidate is not a claim unit.

A claim unit is not a truth judgment.

A claim unit is not evidence assessment.

A claim unit is not a risk signal.

A claim unit is a bounded structural MDS object representing an explicitly admitted assertion-like text unit.

It must remain a structural decomposition object, not an analytical conclusion.

## Admissibility Question

Can the project admit explicit claim unit behavior as the next MDS micro-slice?

## Verdict

Verdict:

`ADMIT REVIEW WITH HARD SAFEGUARDS`

The project may admit a future explicit claim unit implementation only if it remains:

- explicit-candidate-derived;
- structural only;
- non-inferential;
- non-truth-evaluating;
- non-evidence-assessing;
- non-taxonomic;
- non-risk-scoring;
- non-runtime.

This admissibility review does not yet implement claim unit behavior.

## Admitted Future Scope

The future implementation may include only:

- reading existing explicit claim candidates;
- converting eligible explicit claim candidates into explicit claim units;
- preserving source claim candidate identity;
- preserving source surface unit identity;
- preserving source text;
- assigning stable claim unit identifiers;
- marking claim unit status;
- returning minimal claim unit records;
- testing that no truth, evidence, framing, relation, taxonomy, risk, CMO, ACP, Analysis, governance, or output fields are exposed.

Allowed claim unit status values may include:

- `claim_unit_created`
- `not_claim_unit`

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
2. The behavior may only convert existing explicit claim candidates.
3. The behavior must preserve source claim candidate identity.
4. The behavior must preserve source surface unit identity.
5. The behavior must preserve source text.
6. The behavior must not infer hidden or implicit claims.
7. The behavior must not rewrite claim meaning.
8. The behavior must not assess truth.
9. The behavior must not assess evidence.
10. The behavior must not create framing units.
11. The behavior must not create relation objects.
12. The behavior must not create taxonomy labels.
13. The behavior must not create risk signals.
14. The behavior must not construct a full DecompositionResult.
15. The behavior must not call CMO, ACP, Analysis, taxonomy, risk, governance, or output modules.
16. The behavior must not trigger runtime pipeline execution.
17. Tests must prove that forbidden fields are absent.
18. Closure documentation must state that implicit inference, truth assessment, evidence assessment, and relation inference remain on HOLD.

## Candidate Function Name

Preferred function name:

- `build_explicit_claim_units`

Acceptable alternatives:

- `create_explicit_claim_units`
- `build_claim_units_from_candidates`

Function names should avoid:

- `infer_claims`
- `extract_hidden_claims`
- `assess_truth`
- `evaluate_evidence`
- `score_claims`
- `analyze_claims`
- `construct_decomposition_result`

## Recommended Source Area

Preferred source file:

- `src/cognitive_shield/core/message_decomposition_specification_mds/claim_units.py`

Reason:

The existing surface and claim candidate files should remain stable.

A separate `claim_units.py` file keeps the structural claim unit boundary explicit and reversible.

## Admitted Output Shape

A future explicit claim unit helper may return a minimal dictionary containing only fields such as:

- `mds_stage`
- `claim_unit_status`
- `claim_units`

Each claim unit may contain only:

- `claim_unit_id`
- `source_claim_candidate_id`
- `source_surface_unit_id`
- `source_text`
- `unit_type`
- `claim_unit_status`
- `order_index`

Allowed `unit_type`:

- `explicit_claim_unit`

Allowed claim unit statuses:

- `claim_unit_created`
- `not_claim_unit`

## Required Test Boundary

Future tests may verify:

- explicit claim candidates can create explicit claim units;
- claim candidate identity is preserved;
- surface unit identity is preserved;
- source text is preserved;
- order is preserved;
- empty candidate lists return no claim units;
- non-candidate inputs do not create claim units;
- no implicit claims are created;
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

This admissibility review is justified because explicit claim unit behavior is the first structural claim-unit boundary in MDS.

After this review, small repository checks may remain in chat unless they reveal a blocker.

A closure note is required only if explicit claim unit behavior is implemented.

## No-Drift Confirmation

Confirmed:

- MDS surface layer remains bounded;
- explicit claim candidate behavior remains candidate-only;
- explicit claim unit behavior is admitted only as a future review-approved structural micro-slice;
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

If this review is accepted, create the explicit claim unit pass in compressed mode:

1. source file;
2. test file;
3. closure note.

Recommended files:

- `src/cognitive_shield/core/message_decomposition_specification_mds/claim_units.py`
- `tests/unit/test_mds_claim_units.py`
- `docs/sprint_2/SPRINT_2_MDS_EXPLICIT_CLAIM_UNIT_PASS_CLOSURE_NOTE.md`

## Verdict Summary

Explicit claim unit boundary: ADMITTED FOR CONTROLLED IMPLEMENTATION WITH HARD SAFEGUARDS.

Implicit inference: HOLD.

Hidden claim reconstruction: HOLD.

Truth assessment: HOLD.

Evidence assessment: HOLD.

Framing extraction: HOLD.

Relation inference: HOLD.

Full DecompositionResult construction: HOLD.

Runtime pipeline execution: NOT ADMITTED.

Downstream pipeline logic: NOT ADMITTED.
