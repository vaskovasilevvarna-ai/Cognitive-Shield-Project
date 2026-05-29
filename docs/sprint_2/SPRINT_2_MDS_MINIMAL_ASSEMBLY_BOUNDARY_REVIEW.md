# Sprint 2 MDS Minimal Assembly Boundary Review

Status: Boundary review — before admitting minimal MDS assembly behavior.

## Purpose

This document records the Sprint 2 boundary review for the next Message Decomposition Specification (MDS) micro-slice after explicit claim unit bundling.

The purpose is to decide whether the project may admit a minimal MDS-local assembly object while preventing drift into full DecompositionResult construction, Canonical Message Object (CMO) construction, Agent Communication Protocol (ACP) routing, Analysis generation, runtime pipeline execution, downstream pipeline logic, taxonomy behavior, risk scoring, governance behavior, or output rendering.

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
- Python Tests workflow validation

Current MDS early structural stack:

- surface preparation: CLOSED
- single surface unit: CLOSED
- surface bundle: CLOSED
- explicit surface segmentation: CLOSED
- explicit claim candidate boundary: CLOSED
- explicit claim unit boundary: CLOSED
- explicit claim unit bundle: CLOSED
- Python Tests workflow: GREEN

Current restricted areas:

- full DecompositionResult construction: HOLD
- CMO construction: HOLD
- ACP routing: HOLD
- Analysis generation: NOT STARTED
- implicit inference: HOLD
- hidden claim reconstruction: HOLD
- truth assessment: HOLD
- evidence assessment: HOLD
- framing extraction: HOLD
- relation inference: HOLD
- runtime pipeline execution: NOT ADMITTED
- downstream pipeline logic: NOT ADMITTED

## Boundary Question

Can the project admit a minimal MDS-local assembly object as the next MDS micro-slice?

## Verdict

Verdict:

`ADMIT REVIEW WITH HARD SAFEGUARDS`

The project may admit a future minimal MDS assembly implementation only if it remains:

- MDS-local;
- structural only;
- non-inferential;
- non-analytical;
- non-runtime;
- not a full DecompositionResult;
- not CMO-ready;
- not an ACP handoff object.

This boundary review does not yet implement minimal assembly behavior.

## Critical Boundary Distinction

A minimal MDS assembly object is not a DecompositionResult.

A minimal MDS assembly object is not a Canonical Message Object (CMO).

A minimal MDS assembly object is not an ACP handoff.

A minimal MDS assembly object is not an Analysis input bundle.

A minimal MDS assembly object is only a local container that groups already admitted MDS-local structures.

It must not perform new extraction, inference, classification, scoring, or downstream conversion.

## Admitted Future Scope

The future implementation may include only:

- reading an existing surface bundle;
- reading an existing explicit claim unit bundle;
- grouping them into a minimal MDS-local assembly object;
- preserving all included structures without rewriting meaning;
- returning MDS stage identity;
- returning assembly status;
- testing that no DecompositionResult, CMO, ACP, Analysis, taxonomy, risk, governance, output, or runtime fields are exposed.

Allowed assembly status values may include:

- `mds_minimal_assembly_created`
- `no_mds_structures`

## Not Admitted

The following remain not admitted:

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
2. The behavior may only assemble already admitted MDS-local structures.
3. The behavior must not create new surface units.
4. The behavior must not create new claim candidates.
5. The behavior must not create new claim units.
6. The behavior must not infer hidden or implicit claims.
7. The behavior must not rewrite meaning.
8. The behavior must not assess truth.
9. The behavior must not assess evidence.
10. The behavior must not create framing units.
11. The behavior must not create relation objects.
12. The behavior must not create taxonomy labels.
13. The behavior must not create risk signals.
14. The behavior must not construct a full DecompositionResult.
15. The behavior must not construct or prepare a Canonical Message Object (CMO).
16. The behavior must not call ACP, Analysis, taxonomy, risk, governance, or output modules.
17. The behavior must not trigger runtime pipeline execution.
18. Tests must prove that forbidden fields are absent.
19. Closure documentation must state that DecompositionResult construction remains on HOLD.

## Candidate Function Name

Preferred function name:

- `build_mds_minimal_assembly`

Acceptable alternatives:

- `assemble_mds_minimal_structures`
- `build_minimal_mds_assembly`

Function names should avoid:

- `construct_decomposition_result`
- `convert_to_cmo`
- `dispatch_to_acp`
- `run_pipeline`
- `analyze`
- `score`
- `evaluate`

## Recommended Source Area

Preferred source file:

- `src/cognitive_shield/core/message_decomposition_specification_mds/minimal_assembly.py`

Reason:

The existing surface, claim candidate, claim unit, and claim unit bundle files should remain stable.

A separate `minimal_assembly.py` file keeps the assembly boundary explicit and reversible.

## Admitted Output Shape

A future minimal MDS assembly helper may return a minimal dictionary containing only fields such as:

- `mds_stage`
- `assembly_status`
- `surface_bundle`
- `claim_unit_bundle`

Allowed assembly statuses:

- `mds_minimal_assembly_created`
- `no_mds_structures`

The assembly must not expose:

- `decomposition_result`
- `canonical_message_object`
- `acp_bundle`
- `analysis_bundle`
- `taxonomy_labels`
- `risk_profile`
- `governance_signal`
- `output_payload`

## Required Test Boundary

Future tests may verify:

- a valid surface bundle and claim unit bundle can be assembled;
- source surface structures are preserved;
- claim unit bundle structures are preserved;
- empty or missing structures return a bounded status;
- no new claim units are created;
- no DecompositionResult fields are exposed;
- no CMO fields are exposed;
- no ACP, Analysis, taxonomy, risk, governance, output, or runtime fields are exposed.

Future tests must not verify:

- full DecompositionResult construction;
- CMO construction;
- ACP routing;
- Analysis generation;
- truth assessment;
- evidence assessment;
- implicit claim inference;
- semantic relation inference;
- framing classification;
- taxonomy labeling;
- risk scoring;
- downstream pipeline behavior.

## Documentation Discipline

This boundary review is justified because minimal MDS assembly is the first step approaching an MDS-level assembled object.

After this review, small repository checks may remain in chat unless they reveal a blocker.

A closure note is required only if minimal assembly behavior is implemented.

## No-Drift Confirmation

Confirmed:

- MDS surface layer remains bounded;
- explicit claim candidate behavior remains candidate-only;
- explicit claim unit behavior remains structural only;
- explicit claim unit bundle behavior remains MDS-local;
- minimal MDS assembly behavior is admitted only as a future review-approved MDS-local structural micro-slice;
- full DecompositionResult construction remains on HOLD;
- CMO construction remains on HOLD;
- ACP routing remains on HOLD;
- Analysis generation has not started;
- implicit inference remains on HOLD;
- truth assessment remains on HOLD;
- evidence assessment remains on HOLD;
- relation inference remains on HOLD;
- runtime pipeline execution has not started;
- downstream pipeline logic has not started;
- taxonomy behavior has not started;
- risk scoring has not started;
- governance behavior has not started;
- output rendering has not started;
- merge to `main` has not been performed.

## Recommended Next Step

Recommended next step:

If this review is accepted, create the minimal MDS assembly pass in compressed mode:

1. source file;
2. test file;
3. closure note.

Recommended files:

- `src/cognitive_shield/core/message_decomposition_specification_mds/minimal_assembly.py`
- `tests/unit/test_mds_minimal_assembly.py`
- `docs/sprint_2/SPRINT_2_MDS_MINIMAL_ASSEMBLY_PASS_CLOSURE_NOTE.md`

## Verdict Summary

Minimal MDS assembly boundary: ADMITTED FOR CONTROLLED IMPLEMENTATION WITH HARD SAFEGUARDS.

Full DecompositionResult construction: HOLD.

CMO construction: HOLD.

ACP routing: HOLD.

Analysis generation: HOLD.

Implicit inference: HOLD.

Truth assessment: HOLD.

Evidence assessment: HOLD.

Relation inference: HOLD.

Runtime pipeline execution: NOT ADMITTED.

Downstream pipeline logic: NOT ADMITTED.
