# Sprint 1 Contract Implementation Order

Status: Draft v0.1 — contract-first implementation order.

## Purpose

This document defines the preferred order for contract-level work during Sprint 1.

Sprint 1 must not begin with broad module behavior. It should begin with shared contracts and move outward only after contract boundaries are stable.

The purpose of this order is to prevent ad hoc data passing, mixed responsibility files and premature downstream implementation.

## Principle

Contracts come before behavior.

A module may not receive real implementation logic until its input / output contract expectations are explicit enough to test and review.

## Primary Contract Order

The preferred contract order is:

1. `InputMessage`
2. `SurfaceSegment`
3. `ClaimUnit`
4. `FramingUnit`
5. `RelationObject`
6. `ContextCarrier`
7. `CanonicalMessageObject`
8. `EvidenceAnalysisOutput`
9. `NarrativeAnalysisOutput`
10. `CognitiveAnalysisOutput`
11. `TaxonomyLabelAssignment`
12. `BoundedTaxonomyOutput`
13. `RiskDimensionScore`
14. `RiskProfile`
15. `ConfidenceUncertaintyProfile`
16. `ArbiterDecisionRecord`
17. `DecisionPolicyRecord`
18. `ShieldDecisionRecord`
19. `CanonicalOutputSchema`

## First Contract Slice

The first admitted contract slice is:

`InputMessage`.

Expected location:

`src/cognitive_shield/shared/contracts/input_contracts.py`

Reason:
`InputMessage` is the entry contract for the future single-message pipeline and the safest first object to review.

## Contract Grouping

### Group A — Input and Decomposition Surface

- `InputMessage`
- `SurfaceSegment`
- `ClaimUnit`
- `FramingUnit`
- `RelationObject`
- `ContextCarrier`

Purpose:
Prepare the entry and structuring surface before Message Decomposition Specification (MDS) behavior.

### Group B — Canonical Message Object Boundary

- `CanonicalMessageObject`

Purpose:
Prepare the stable carrier for structured message analysis before downstream analysis modules.

### Group C — Analysis Channel Outputs

- `EvidenceAnalysisOutput`
- `NarrativeAnalysisOutput`
- `CognitiveAnalysisOutput`

Purpose:
Prepare typed analysis outputs before taxonomy and risk mapping.

### Group D — Taxonomy Output Contracts

- `TaxonomyLabelAssignment`
- `BoundedTaxonomyOutput`

Purpose:
Preserve taxonomy output discipline and prevent label-to-verdict shortcuts.

### Group E — Risk and Governance Contracts

- `RiskDimensionScore`
- `RiskProfile`
- `ConfidenceUncertaintyProfile`
- `ArbiterDecisionRecord`
- `DecisionPolicyRecord`
- `ShieldDecisionRecord`

Purpose:
Prepare the risk and governance spine without implementing full behavior prematurely.

### Group F — Output Contract

- `CanonicalOutputSchema`

Purpose:
Prepare the structured output contract after upstream records are stable.

## Implementation Rule

For each contract:

1. inspect existing file;
2. confirm whether the contract already exists;
3. compare against architecture target shape;
4. refine only if needed;
5. add or update a narrow test only after the shape is stable;
6. do not implement downstream behavior in the same step.

## Testing Rule

A contract test or unit test may be added only after the contract shape is stable.

Tests must verify structure, construction, required fields or compatibility.

Tests must not introduce downstream behavioral expectations too early.

## Boundary

This document does not authorize implementation of:

- Message Decomposition Specification (MDS) behavior;
- Canonical Message Object (CMO) builder behavior;
- Agent Communication Protocol (ACP) routing;
- taxonomy logic;
- risk scoring;
- confidence or uncertainty evaluation;
- Internal Arbiter (IA) behavior;
- Decision Policy Layer (DPL) behavior;
- Shield Decision (SD) behavior;
- output rendering.

Those require separate implementation admission.

## Order Verdict

Sprint 1 should begin with `InputMessage`, then proceed through contract groups only after each previous contract surface is stable enough.
