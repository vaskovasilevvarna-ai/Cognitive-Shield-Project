# Naming Rules

## Purpose
These naming rules preserve architectural clarity and reduce ambiguity during implementation.

## General rule
Use explicit, role-based names.

Avoid vague names.

Bad examples:
- helpers.py
- misc.py
- logic.py
- engine.py

Good examples:
- validator.py
- mapper.py
- scorer.py
- policy_engine.py
- builder.py

## Folder naming
Folders must use:

- snake_case
- full architectural name
- abbreviation included when the abbreviation is already fixed in the architecture

Examples:
- message_decomposition_specification_mds
- canonical_message_object_cmo
- agent_communication_protocol_acp
- decision_policy_layer_dpl
- internal_arbiter_ia

## File naming
Files must describe the role they perform.

Examples:
- contracts.py
- schemas.py
- service.py
- validator.py
- mapper.py
- scorer.py
- propagation.py
- safeguards.py

## Class naming
Use PascalCase.

Examples:
- CanonicalMessageObject
- RiskProfile
- ConfidenceUncertaintyProfile
- DecisionPolicyRecord
- ShieldDecisionRecord

## Function naming
Use snake_case.

Functions should communicate action + object.

Examples:
- build_canonical_message_object
- validate_claim_unit
- map_taxonomy_to_risk
- score_risk_dimensions
- evaluate_confidence_band
- build_shield_decision

## Responsibility naming rule
One module = one responsibility.

Names must reflect the fixed architectural role.

A module name must never hide a second role inside it.

## Public contract naming rule
Any object used across module boundaries must have a stable, explicit contract name.

Examples:
- InputMessage
- CanonicalMessageObject
- BoundedTaxonomyOutput
- RiskProfile
- CanonicalOutputSchema
