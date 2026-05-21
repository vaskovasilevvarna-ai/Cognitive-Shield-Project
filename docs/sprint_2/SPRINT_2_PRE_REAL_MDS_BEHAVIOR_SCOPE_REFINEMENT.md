# Sprint 2 Pre-Real MDS Behavior Scope Refinement

Status: Scope refinement — before admitting real Message Decomposition Specification (MDS) behavior.

## Purpose

This document records the Sprint 2 scope refinement before any real Message Decomposition Specification (MDS) behavior is admitted.

The purpose is to define the smallest admissible MDS-side behavior slice and to prevent uncontrolled transition from Sprint 1 Input behavior into broad analytical decomposition.

This document does not admit broad MDS implementation, claim extraction, implicit claim inference, relation inference, Canonical Message Object (CMO) construction, Agent Communication Protocol (ACP) routing, Analysis generation, runtime pipeline execution, downstream pipeline logic, taxonomy behavior, risk scoring, governance behavior, output rendering, or merge to `main`.

## Baseline

Sprint 1 closed with boundaries as:

- MVP foundation sprint;
- Phase A scaffold sprint;
- Phase A preview-chain sprint;
- minimal Input behavior nucleus sprint.

Sprint 2 has opened with:

- `docs/sprint_2/README.md`;
- `docs/sprint_2/SPRINT_2_ENTRY_CONTROL_PASS.md`.

Current state:

- Input behavior nucleus: Closed
- Phase A scaffold layer: Closed
- Phase A preview chain: Closed
- Real MDS behavior: HOLD
- Real CMO construction: HOLD
- Real ACP routing: HOLD
- Real Analysis generation: Not started
- Runtime pipeline execution: Not started
- Downstream pipeline logic: Not started
- Merge to `main`: Not performed

## Scope Question

The Sprint 2 opening question is:

What is the smallest admissible real MDS-side behavior slice?

## Scope Refinement Verdict

Verdict:

`ADMIT WITH HARD SAFEGUARDS — SURFACE-LEVEL MDS PREPARATION ONLY`

Sprint 2 may admit only a minimal surface-level MDS preparation slice.

This does not admit claim extraction.

This does not admit implicit claims.

This does not admit relation inference.

This does not admit full `DecompositionResult` construction.

## Admitted First MDS Slice

The first admissible MDS-side behavior may include only:

- accepting already prepared Input-side text;
- creating a minimal surface-level preparation result;
- preserving original text;
- reporting preparation status;
- preserving traceable source identity where available;
- returning a minimal readiness / preparation object;
- tests proving that no claim, framing, relation, or downstream fields are produced.

The first MDS slice should be treated as:

`surface-level preparation`

not:

`message decomposition`

## Recommended First Source Area

Potential source file:

- `src/cognitive_shield/core/message_decomposition_specification_mds/service.py`

Alternative, if the existing service file should remain untouched:

- `src/cognitive_shield/core/message_decomposition_specification_mds/surface_preparation.py`

The preferred approach should be chosen only after source inspection.

## Candidate Function Name

Preferred candidate function name:

- `prepare_mds_surface_minimal`

Acceptable alternatives:

- `build_mds_surface_preparation`
- `prepare_surface_text_for_mds`

Function names should avoid:

- `decompose`
- `extract_claims`
- `infer`
- `analyze`
- `run_pipeline`
- `execute`

## Admitted Output Shape

The first MDS-side behavior may return a minimal dictionary or simple typed result containing only fields such as:

- `source_text`
- `preparation_status`
- `mds_stage`
- `surface_status`

Allowed statuses:

- `prepared`
- `blocked`

Allowed MDS stage:

- `message_decomposition_specification_mds`

## Not Admitted

The following remain not admitted:

- broad MDS implementation;
- surface segmentation into multiple analytical units;
- claim extraction;
- implicit claim inference;
- framing extraction;
- relation inference;
- context carrier construction;
- global narrative structure construction;
- decomposition uncertainty calculation;
- traceability map construction beyond minimal source identity;
- `DecompositionResult` construction;
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

Any first MDS-side behavior must preserve the following safeguards:

1. The behavior must remain local to the MDS layer.
2. The behavior must not call CMO modules.
3. The behavior must not call ACP modules.
4. The behavior must not call Analysis modules.
5. The behavior must not create claim units.
6. The behavior must not create framing units.
7. The behavior must not create relation objects.
8. The behavior must not perform implicit inference.
9. The behavior must not construct a full `DecompositionResult`.
10. The behavior must not trigger runtime pipeline execution.
11. Tests must prove that forbidden fields are absent.
12. Closure documentation must state that real decomposition remains not admitted.

## Required Test Boundary

Future tests may verify:

- valid surface text can be prepared;
- empty or whitespace-only surface text is blocked;
- preparation status is returned;
- original text is preserved after Input-side preparation;
- no claim fields are exposed;
- no framing fields are exposed;
- no relation fields are exposed;
- no CMO / ACP / Analysis fields are exposed.

Future tests must not verify:

- claim extraction;
- implicit claim inference;
- relation inference;
- decomposition result construction;
- CMO construction;
- ACP routing;
- Analysis generation;
- downstream pipeline behavior.

## Documentation Discipline

Sprint 2 documentation should remain lighter than Sprint 1.

A repo document is justified for this scope refinement because it changes the project state from:

`Real MDS behavior: HOLD`

to:

`First MDS-side behavior may be admitted only as surface-level preparation`

Small sanity checks after this pass may remain in chat unless a blocker appears.

## No-Drift Confirmation

Confirmed:

- real claim extraction remains not admitted;
- implicit inference remains not admitted;
- relation inference remains not admitted;
- full MDS decomposition remains not admitted;
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

Inspect the current MDS source files before editing.

Inspect first:

- `src/cognitive_shield/core/message_decomposition_specification_mds/service.py`

Then decide:

- `service.py: SAFE TO EDIT`
- `service.py: NO CHANGE NEEDED`
- or `use separate surface_preparation.py`

## Verdict Summary

First MDS-side behavior: ADMITTED WITH HARD SAFEGUARDS.

Allowed scope: surface-level MDS preparation only.

Claim extraction: HOLD.

Implicit inference: HOLD.

Relation inference: HOLD.

Full DecompositionResult construction: HOLD.

Runtime pipeline execution: NOT ADMITTED.

Downstream pipeline logic: NOT ADMITTED.
