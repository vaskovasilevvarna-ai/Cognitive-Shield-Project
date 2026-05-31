# Post-MVP Source And Tests Classification

Status: Source and tests classification document — after Post-MVP Sprint Docs Classification.

## Purpose

This document records the source-code and test-area classification pass for the post-MVP cleanup phase of the Cognitive Shield project.

The purpose is to classify the `src/` and `tests/` areas before any source cleanup, test cleanup, archive movement, file movement, deletion, or refactor is admitted.

This document is classification-only.

This document does not admit deletion.

This document does not admit file movement.

This document does not admit archive movement.

This document does not admit source code edits.

This document does not admit test behavior edits.

This document does not admit workflow edits.

This document does not admit Functional Local Prototype Engine implementation.

## Baseline

The project has reached the following confirmed state:

- Sprint 4: CLOSED WITH MVP FUNCTIONAL PROOF
- MVP foundation: MERGED INTO `main`
- Post-merge verification: COMPLETE
- Python Tests on `main`: GREEN
- MVP Status Note: PRESENT
- Post-MVP Repo Cleanup Control Pass: COMPLETE
- Post-MVP Repo Cleanup Inventory: COMPLETE
- Post-MVP Root Files Classification: COMPLETE
- Post-MVP Docs Classification: COMPLETE
- Post-MVP Sprint Docs Classification: COMPLETE

Current cleanup branch:

- `post-mvp/repo-cleanup`

Cleanup status:

- inventory complete
- root files classified at policy level
- docs area classified at policy level
- sprint docs classified at policy level
- source and tests classification opened
- deletion not admitted
- file movement not admitted
- archive movement not admitted

## Classification Question

How should the source and test areas be classified before cleanup decisions are made?

## Verdict

Verdict:

`SOURCE AND TESTS CLASSIFICATION OPENED — NO CLEANUP ACTION YET`

The `src/` and `tests/` areas may be classified at policy level.

No source file or test file may be deleted, moved, archived, renamed, rewritten, or refactored by this document.

## Classification Model

This classification uses the agreed post-MVP categories:

### ACTIVE

The file or folder is part of the current MVP baseline, current repository operation, or current test validation path.

### KEEP

The file or folder is important and should remain accessible, even if it is not part of active MVP execution.

### ARCHIVE

The file or folder is historically important but may later move out of the active working path.

### REVIEW

The file or folder requires human review before a decision.

### DELETE

The file is safe to delete only after explicit confirmation in a later pass.

This document does not execute any action.

## Source And Test Protection Principles

The source and test areas are more sensitive than documentation.

Cleanup must not damage:

- MVP functional proof behavior;
- smoke-test validation;
- unit-test validation;
- contract-test validation;
- package imports;
- Python Tests workflow;
- bounded architectural module structure.

Source and test cleanup must be more conservative than documentation cleanup.

## Protected MVP Source Files

The following source files are protected during cleanup unless separately reviewed:

- `src/cognitive_shield/app/mvp_functional_proof.py`
- `src/cognitive_shield/core/agent_communication_protocol_acp/routing_result.py`

Classification:

`ACTIVE / PROTECTED`

Reason:

These files represent the Sprint 4 MVP functional proof and minimal non-dispatch routing result.

They are part of the validated MVP baseline.

Action now:

- no deletion;
- no movement;
- no rename;
- no refactor;
- no behavior change.

## Protected MVP Test Files

The following test files are protected during cleanup unless separately reviewed:

- `tests/smoke/test_mvp_functional_proof.py`
- `tests/unit/test_acp_routing_result.py`

Classification:

`ACTIVE / PROTECTED`

Reason:

These tests validate the MVP functional proof and minimal non-dispatch routing result.

They participate in the GREEN Python Tests workflow.

Action now:

- no deletion;
- no movement;
- no rename;
- no rewrite;
- no behavior change.

## Source Zone 1 — `src/cognitive_shield/app/`

Classification:

`ACTIVE / KEEP`

Reason:

The `app/` area contains application-level wiring and now includes the MVP functional proof helper.

It should remain active because it is the correct place for bounded application-level proof wiring.

Action now:

- preserve;
- no movement;
- no source edits.

## Source Zone 2 — `src/cognitive_shield/core/`

Classification:

`ACTIVE / KEEP`

Reason:

The `core/` area contains the project’s bounded core modules and architectural implementation chain.

It includes the Agent Communication Protocol (ACP) package and related MVP-supporting modules.

Action now:

- preserve;
- no movement;
- no source edits.

## Source Zone 3 — `src/cognitive_shield/core/agent_communication_protocol_acp/`

Classification:

`ACTIVE / KEEP`

Reason:

The ACP package contains the Sprint 3 and Sprint 4 chain used by the MVP proof:

- ACP minimal envelope;
- ACPBundle;
- ACPMessage;
- ACP Schema Validator;
- ACP Scope Guard;
- Protocol Router readiness;
- minimal non-dispatch routing result.

Some deeper ACP scaffolds may not yet be active behavior, but they are architectural placeholders for future work.

Action now:

- preserve;
- no deletion;
- no movement;
- classify individual inactive scaffolds later if needed.

## Source Zone 4 — `src/cognitive_shield/shared/`

Classification:

`ACTIVE / REVIEW`

Reason:

The `shared/` area likely contains contracts, common schemas, base errors, traceability helpers, dependencies, and constants.

These may be important for current or future implementation.

Action now:

- preserve;
- no deletion;
- no movement;
- review later for duplicate or unused helper files only after source inspection.

## Source Zone 5 — Package Marker Files

Classification:

`ACTIVE / KEEP`

Reason:

Files such as `__init__.py` preserve Python package structure and import behavior.

They may appear small or empty, but they can be necessary for package organization and test discovery.

Action now:

- no deletion;
- no movement.

## Source Zone 6 — Placeholder Or Scaffold Modules

Classification:

`REVIEW / KEEP CANDIDATE`

Reason:

Some modules may be placeholders for future architecture layers, such as:

- Analysis generation;
- taxonomy behavior;
- risk scoring;
- governance behavior;
- output rendering;
- education-related layers;
- ACP internal modules not yet active.

These should not be deleted merely because they are not yet used.

They may represent planned architecture.

Action now:

- no deletion;
- no movement;
- review later if they are duplicate, misplaced, or obsolete.

## Test Zone 1 — `tests/unit/`

Classification:

`ACTIVE / KEEP`

Reason:

Unit tests validate admitted bounded behavior.

This folder participates in the Python Tests workflow.

Action now:

- preserve;
- no deletion;
- no movement;
- no test rewrites.

## Test Zone 2 — `tests/contract/`

Classification:

`ACTIVE / REVIEW`

Reason:

Contract tests support boundary discipline and interface validation.

Even if the current contract tests are minimal, the folder is part of the expanded workflow discovery.

Action now:

- preserve;
- no deletion;
- no movement;
- later review may clarify whether additional contract README or markers are needed.

## Test Zone 3 — `tests/smoke/`

Classification:

`ACTIVE / KEEP`

Reason:

Smoke tests validate MVP-level functional proof.

The folder is part of the Sprint 4 MVP validation path.

Protected files include:

- `tests/smoke/test_mvp_functional_proof.py`
- `tests/smoke/README.md`
- `tests/smoke/__init__.py`

Action now:

- preserve;
- no deletion;
- no movement;
- no rewrite.

## Test Zone 4 — Test Package Marker Files

Classification:

`ACTIVE / KEEP`

Reason:

Files such as `__init__.py` in test folders help preserve test package structure.

They may be short or empty, but they should not be deleted during cleanup.

Action now:

- preserve;
- no deletion;
- no movement.

## Test Zone 5 — Placeholder Tests

Classification:

`REVIEW / KEEP CANDIDATE`

Reason:

Some tests may be placeholders or early scaffolds.

They should be reviewed carefully.

A placeholder test may be important if it protects a future boundary or ensures imports work.

Action now:

- no deletion;
- no movement;
- review later if duplicate, obsolete, or misleading.

## Test Zone 6 — Duplicate Or Obsolete Tests

Classification:

`REVIEW / DELETE CANDIDATE`

Reason:

Some tests may later prove to be duplicates or obsolete.

However, no test should be deleted without verifying:

- whether it protects an admitted behavior;
- whether it is still run by the workflow;
- whether it guards a boundary;
- whether a newer test fully replaces it.

Action now:

- no deletion;
- list later only if clear duplicate candidates are found.

## Source And Test Classification Summary

| Area | Classification | Action now |
| --- | --- | --- |
| `src/cognitive_shield/app/` | ACTIVE / KEEP | preserve |
| `src/cognitive_shield/app/mvp_functional_proof.py` | ACTIVE / PROTECTED | preserve |
| `src/cognitive_shield/core/` | ACTIVE / KEEP | preserve |
| ACP package | ACTIVE / KEEP | preserve |
| `routing_result.py` | ACTIVE / PROTECTED | preserve |
| `src/cognitive_shield/shared/` | ACTIVE / REVIEW | preserve |
| source package markers | ACTIVE / KEEP | preserve |
| placeholder source modules | REVIEW / KEEP CANDIDATE | review later |
| `tests/unit/` | ACTIVE / KEEP | preserve |
| `tests/unit/test_acp_routing_result.py` | ACTIVE / PROTECTED | preserve |
| `tests/contract/` | ACTIVE / REVIEW | preserve |
| `tests/smoke/` | ACTIVE / KEEP | preserve |
| `tests/smoke/test_mvp_functional_proof.py` | ACTIVE / PROTECTED | preserve |
| test package markers | ACTIVE / KEEP | preserve |
| placeholder tests | REVIEW / KEEP CANDIDATE | review later |
| duplicate or obsolete tests | REVIEW / DELETE CANDIDATE | no deletion |

## Source And Test Files That Must Not Be Changed During Cleanup

The following must not be changed during this cleanup classification stage:

- MVP proof helper;
- minimal routing result helper;
- MVP smoke test;
- minimal routing result unit test;
- Python package marker files;
- workflow-dependent test folders;
- admitted ACP chain files;
- source or test files required for GREEN workflow.

## Date-Based Review Rule

Date may help prioritize review, but it must not decide alone.

Important principles:

- old source file does not automatically mean obsolete;
- unused-looking scaffold may represent planned architecture;
- short package marker files may be structurally necessary;
- recently added files may still need review if misplaced;
- tests should not be removed merely because they look simple.

Date must be combined with:

- path;
- imports;
- test coverage role;
- relation to MVP baseline;
- architectural role;
- replacement status;
- risk of deletion.

## Not Admitted

The following are not admitted by this document:

- deleting source files;
- moving source files;
- archiving source files;
- renaming source files;
- refactoring source files;
- editing source behavior;
- deleting test files;
- moving test files;
- archiving test files;
- renaming test files;
- rewriting tests;
- changing workflow behavior;
- changing MVP proof behavior;
- starting Functional Local Prototype Engine implementation;
- full ACP routing;
- dispatch behavior;
- Analysis generation;
- taxonomy behavior;
- risk scoring;
- governance behavior;
- output rendering;
- runtime pipeline execution;
- downstream pipeline logic;
- production release;
- public outreach.

## Required Next Step

After source and test classification, the repository has enough policy-level classification to open archive planning.

Recommended next document:

- `docs/repo-governance/POST_MVP_ARCHIVE_STRUCTURE_BOUNDARY_REVIEW.md`

Reason:

Root, docs, sprint docs, source, and tests have now been classified at policy level.

The next safe step is to define archive structure before any movement is admitted.

## No-Drift Confirmation

Confirmed:

- source and test classification is opened;
- source cleanup action is not admitted;
- test cleanup action is not admitted;
- deletion remains not admitted;
- movement remains not admitted;
- archive movement remains not admitted;
- MVP proof source files remain protected;
- MVP proof test files remain protected;
- workflow remains unchanged;
- Functional Local Prototype Engine work has not started.

## Verdict Summary

Post-MVP Source And Tests Classification: COMPLETE.

Source area: CLASSIFIED AT POLICY LEVEL.

Tests area: CLASSIFIED AT POLICY LEVEL.

MVP proof source files: PROTECTED.

MVP proof test files: PROTECTED.

Deletion: NOT ADMITTED.

File movement: NOT ADMITTED.

Archive movement: NOT ADMITTED.

Source edits: NOT ADMITTED.

Test edits: NOT ADMITTED.

Next document:

- `POST_MVP_ARCHIVE_STRUCTURE_BOUNDARY_REVIEW.md`
