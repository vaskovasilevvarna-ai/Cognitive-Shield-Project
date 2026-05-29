# Shared Contract Schema Pack

## Purpose
This document defines the first shared schema pack for disciplined cross-module implementation.

The goal is to prevent ad hoc data passing and preserve architectural traceability.

## Core input contracts

### InputMessage
Fields:
- message_id
- raw_text
- language
- source_type
- timestamp
- metadata

### SurfaceSegment
Fields:
- segment_id
- text
- start_offset
- end_offset

### ClaimUnit
Fields:
- claim_id
- text
- source_segment_ids
- claim_type
- explicitness
- uncertainty_flags

### FramingUnit
Fields:
- framing_id
- text
- framing_mode
- source_segment_ids

### RelationObject
Fields:
- relation_id
- relation_type
- from_unit_id
- to_unit_id

### ContextCarrier
Fields:
- context_id
- context_type
- value
- linked_unit_ids

## Canonical structuring contract

### CanonicalMessageObject
Fields:
- message_id
- surface_segments
- claim_units
- framing_units
- relation_objects
- context_carriers
- global_narrative_structure
- decomposition_uncertainty
- traceability

## Analysis contracts

### EvidenceAnalysisOutput
Fields:
- message_id
- claim_assessments
- evidence_signals
- uncertainty_signals

### NarrativeAnalysisOutput
Fields:
- message_id
- framing_assessments
- narrative_signals
- uncertainty_signals

### CognitiveAnalysisOutput
Fields:
- message_id
- cognitive_pressure_signals
- attention_capture_signals
- uncertainty_signals

## Taxonomy contracts

### TaxonomyLabelAssignment
Fields:
- target_unit_id
- taxonomy_family
- label
- axis
- priority
- confidence_hint
- uncertainty_flags
- trace_ref

### BoundedTaxonomyOutput
Fields:
- message_id
- evidence_labels
- narrative_labels
- cognitive_labels
- multi_label_notes

## Risk and governance contracts

### RiskDimensionScore
Fields:
- dimension
- score_value
- drivers
- dampeners
- uncertainty_modifiers

### RiskProfile
Fields:
- message_id
- dimension_scores
- global_aggregation
- explainability_traces

### ConfidenceUncertaintyProfile
Fields:
- message_id
- confidence_band
- uncertainty_mode
- uncertainty_sources
- propagation_notes

### ArbiterDecisionRecord
Fields:
- message_id
- conflict_map
- validated_risk_profile
- adjusted_confidence_profile
- decision_readiness
- escalation_flags

### DecisionPolicyRecord
Fields:
- message_id
- policy_mode
- admissible_actions
- restrictions
- policy_rationale

### ShieldDecisionRecord
Fields:
- message_id
- decision_posture
- decision_summary
- governance_notes
- uncertainty_visibility_requirements

## Output contract

### CanonicalOutputSchema
Fields:
- message_id
- executive_signal
- claim_level_findings
- uncertainty_block
- conflict_block
- decision_block
- traceability_block

## Packaging rule
Shared public contracts should later live in:

- src/cognitive_shield/shared/contracts/

Module-specific internal schemas may also exist inside their respective module folders.

## Sprint 0 note
This document is a schema pack definition, not a final implementation schema engine.
