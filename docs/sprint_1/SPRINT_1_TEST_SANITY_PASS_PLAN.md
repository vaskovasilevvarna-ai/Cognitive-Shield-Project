# Sprint 1 Test Sanity Pass Plan

Status: Draft v0.1 — test sanity planning document.

## Purpose

This document defines the Sprint 1 test sanity pass after completion of the shared-layer pass and the bounded Message Decomposition Specification (MDS) scaffold pass.

The purpose is to verify that the accumulated narrow unit tests are structurally coherent before opening another core module or admitting real behavior implementation.

This pass does not introduce broad test expansion.

## Baseline

The following Sprint 1 checkpoints are already closed:

- Shared Layer Pass;
- Message Decomposition Specification (MDS) Contract Boundary Pass;
- Message Decomposition Specification (MDS) Schema Boundary Pass;
- Message Decomposition Specification (MDS) Validator Scaffold Pass;
- Message Decomposition Specification (MDS) Service Scaffold Pass;
- Message Decomposition Specification (MDS) Mapper Scaffold Pass;
- Sprint 1 Midpoint Matrix.

## Scope

The test sanity pass may include:

- verifying that expected unit test files exist;
- verifying that test files are placed under `tests/unit/`;
- checking that tests remain narrow and scaffold-level;
- checking that no test implies downstream behavior;
- checking that no test encodes hidden policy logic;
- checking that no test introduces label-to-verdict expectations;
- optionally running the existing unit tests if the repository environment supports it.

## Non-Scope

The test sanity pass must not include:

- broad test suite expansion;
- integration test expansion;
- benchmark dataset creation;
- scenario library creation;
- end-to-end pipeline testing;
- real Message Decomposition Specification (MDS) behavior testing;
- taxonomy behavior testing;
- risk scoring tests;
- governance behavior tests;
- output rendering tests;
- UI tests.

## Expected Unit Test Files

The following unit test files are expected to exist:

### Shared layer tests

- `tests/unit/test_input_contracts.py`
- `tests/unit/test_analysis_contracts.py`
- `tests/unit/test_taxonomy_contracts.py`
- `tests/unit/test_risk_contracts.py`
- `tests/unit/test_output_contracts.py`
- `tests/unit/test_base_types.py`
- `tests/unit/test_traceability.py`
- `tests/unit/test_common_schema.py`
- `tests/unit/test_base_errors.py`
- `tests/unit/test_system_constants.py`

### Message Decomposition Specification (MDS) scaffold tests

- `tests/unit/test_mds_contracts.py`
- `tests/unit/test_mds_schemas.py`
- `tests/unit/test_mds_validator.py`
- `tests/unit/test_mds_service.py`
- `tests/unit/test_mds_mapper.py`

## Sanity Criteria

The test sanity pass should confirm:

- test files are in the correct folder;
- test names are narrow and role-specific;
- tests verify construction, import, aliases, constants, helper output or scaffold behavior only;
- tests do not require downstream modules;
- tests do not introduce hidden architectural decisions;
- tests do not collapse risk, taxonomy or output logic into verdict behavior.

## Optional Local Test Command

If the local environment supports it, the expected command is:

```bash
pytest tests/unit
