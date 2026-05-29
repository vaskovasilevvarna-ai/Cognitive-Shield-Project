# Sprint 1 Testing Entry Rules

Status: Draft v0.1 — testing entry control document.

## Purpose

This document defines when tests may be added during Sprint 1.

Sprint 1 must not turn the placeholder test layer from Sprint 0 into a broad or premature test suite.

Testing in Sprint 1 should be narrow, contract-driven and added only after the relevant contract shape is stable enough to test.

## Core Rule

No test before stable contract.

A test may be added only after the contract, schema or bounded interface it tests has been reviewed and considered stable enough for the current slice.

## Admitted Testing

Sprint 1 may include:

- one narrow unit test for the first stable shared contract;
- structure / construction tests for explicit contracts;
- import / presence tests only when they serve a clear boundary purpose;
- later contract tests only after both sides of a boundary are explicit enough.

## Non-Admitted Testing

Sprint 1 entry must not introduce:

- broad unit test suite;
- broad contract test suite;
- integration test expansion;
- scenario evaluation tests;
- benchmark-style tests;
- behavioral tests for modules that do not yet have admitted implementation;
- tests that imply hidden policy decisions;
- tests that convert taxonomy labels into verdict expectations;
- tests that require downstream modules not yet admitted.

## First Test Candidate

The first admitted test candidate is a narrow test for the `InputMessage` contract.

Expected location:

`tests/unit/test_input_contracts.py`

Possible scope:

- `InputMessage` can be imported;
- `InputMessage` can be constructed with minimal required fields;
- expected fields are present;
- metadata defaults or handling are explicit if the implementation supports it.

The first test must not check:

- Message Decomposition Specification (MDS) behavior;
- Canonical Message Object (CMO) construction;
- taxonomy labels;
- risk scoring;
- uncertainty evaluation;
- pipeline execution;
- output rendering.

## Testing Sequence

For each tested contract:

1. review contract file;
2. confirm contract exists or add minimal contract;
3. confirm contract shape;
4. add one narrow test;
5. run or mark test execution separately;
6. do not expand test scope without explicit admission.

## Contract Test Entry Rule

Contract tests between modules may begin only when both sides of the boundary exist as explicit contracts.

Example:
A test for Message Decomposition Specification (MDS) → Canonical Message Object (CMO) is not admitted until both the MDS output contract and CMO input / structure contract are explicit enough.

## Integration Test Boundary

Integration tests remain deferred during Sprint 1 entry work.

The existing integration placeholder from Sprint 0 is not a license to start full pipeline testing.

Full integration testing requires explicit admission after the first module contracts and bounded implementation path are stable.

## No-Drift Testing Safeguards

Tests must not:

- introduce behavior before code is admitted;
- encode hidden policy logic;
- enforce verdict-like expectations;
- suppress uncertainty or conflict by expected output design;
- force a downstream module into existence prematurely;
- turn examples or fixtures into benchmark datasets.

## Closure Criteria

Sprint 1 testing entry is clean when:

- the first test is tied to a stable contract;
- the test remains narrow;
- the test does not imply downstream behavior;
- no broad suite is introduced;
- testing scope is documented and traceable to the current slice.

## Verdict

Sprint 1 testing may begin only as contract-driven, narrow testing after the relevant contract shape is stable.

Testing is allowed to support bounded implementation, not to pull the project into premature full-system behavior.
