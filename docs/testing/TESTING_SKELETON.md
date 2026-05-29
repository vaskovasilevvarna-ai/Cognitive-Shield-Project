# Testing Skeleton

## Purpose
The testing skeleton protects contract discipline before feature richness.

It exists to validate structure, compatibility, uncertainty visibility, and bounded flow.

## Test layers

### 1. Unit tests
Unit tests validate local logic inside modules.

Examples:
- validators
- builders
- mappers
- scorers
- policy checks

### 2. Contract tests
Contract tests validate compatibility across module boundaries.

Required paths:
- MDS -> CMO
- CMO -> ACP
- ACP -> taxonomy
- taxonomy -> mapping
- mapping -> risk
- risk -> confidence/uncertainty
- confidence/uncertainty -> IA
- IA -> DPL
- DPL -> SD
- SD -> COS

### 3. Integration tests
Integration tests validate the first bounded MVP nucleus:

input -> MDS -> taxonomy -> mapping -> risk -> confidence/uncertainty -> IA -> DPL -> SD -> COS

### 4. Golden tests
Golden tests validate stable expected structures for selected reference examples.

They do not validate truth verdicts.
They validate:
- schema stability
- uncertainty visibility
- conflict visibility
- contract integrity

## Initial fixture set

### Fixture A — Clean structured message
Purpose:
validate the simplest happy-path analytical flow

### Fixture B — Mixed-signal message
Purpose:
validate coexistence of different signals without forced collapse

### Fixture C — Ambiguity-heavy message
Purpose:
validate uncertainty preservation and non-false stability

## Test tree

```text
tests/
├── unit/
├── contract/
├── integration/
├── fixtures/
└── golden/
