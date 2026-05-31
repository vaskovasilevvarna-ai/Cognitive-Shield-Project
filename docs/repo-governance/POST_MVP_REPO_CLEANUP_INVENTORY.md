# Post-MVP Repo Cleanup Inventory

Status: Inventory document — after Post-MVP Repo Cleanup Control Pass.

## Purpose

This document records the initial repository inventory for the post-MVP cleanup phase of the Cognitive Shield project.

The purpose is to identify the main repository zones that must be reviewed before any cleanup, archive movement, file movement, or deletion is admitted.

This document is inventory-only.

This document does not classify individual files yet.

This document does not admit deletion.

This document does not admit file movement.

This document does not admit archive movement.

This document does not admit new feature implementation.

## Baseline

The project has reached the following confirmed state:

- Sprint 4: CLOSED WITH MVP FUNCTIONAL PROOF
- MVP foundation: MERGED INTO `main`
- Post-merge verification: COMPLETE
- Python Tests on `main`: GREEN
- MVP Status Note: PRESENT
- Sprint 4 Exit Audit Snapshot: PRESENT
- Post-MVP Repo Cleanup Control Pass: COMPLETE

Current cleanup branch:

- `post-mvp/repo-cleanup`

Source baseline branch:

- `main`

Cleanup status:

- inventory and classification only
- deletion not admitted
- file movement not admitted
- archive movement not admitted

## Inventory Question

Which repository zones must be reviewed before cleanup decisions can be made?

## Verdict

Verdict:

`REPOSITORY INVENTORY OPENED — NO CLASSIFICATION OR CLEANUP YET`

The repository cleanup inventory may begin.

This document identifies the repository zones that should be reviewed in later classification documents.

No file-level decision is made by this document.

## Inventory Principles

The inventory must follow these principles:

1. Do not delete files during inventory.
2. Do not move files during inventory.
3. Do not archive files during inventory.
4. Do not rewrite README or repository maps during inventory.
5. Do not edit source or tests during inventory.
6. Do not change workflow files during inventory.
7. Record repository zones before making file-level decisions.
8. Use classification only in later documents.
9. Preserve the Sprint 4 MVP proof baseline.
10. Keep cleanup separate from new feature development.

## Classification Model For Later Use

Later classification documents should assign files or file groups to one of the following categories:

### ACTIVE

The file is part of the current MVP baseline or active repository structure.

### KEEP

The file is important and should remain, even if not part of active MVP execution.

### ARCHIVE

The file is historically important but should be moved out of the active working path.

### REVIEW

The file requires human review before a decision.

### DELETE

The file is safe to delete only after explicit confirmation.

This inventory document does not assign these classifications yet.

## Inventory Zone 1 — Root Files

The root directory should be reviewed because it defines project identity and repository usability.

Inventory targets include:

- README files;
- license files;
- dependency files;
- project configuration files;
- pytest configuration;
- package configuration;
- Makefile or command helpers;
- root-level notes;
- accidental duplicate files;
- old loose documents;
- misplaced sprint files;
- temporary files.

Protected root-level priorities:

- project identity;
- license;
- Python test configuration;
- dependency configuration;
- repository entry point clarity.

No root files may be deleted during inventory.

## Inventory Zone 2 — GitHub Configuration

The `.github/` directory should be reviewed because it controls repository automation.

Inventory targets include:

- `.github/workflows/`;
- Python Tests workflow;
- JSON validation workflow if present;
- Pages deployment workflow if present;
- other automation files.

Protected files include:

- `.github/workflows/python-tests.yml`

The Python Tests workflow is part of the MVP proof validation state and must be preserved unless separately reviewed.

No workflow changes are admitted by this document.

## Inventory Zone 3 — Source Code

The `src/` directory should be reviewed as the current implementation foundation.

Inventory targets include:

- `src/cognitive_shield/app/`;
- `src/cognitive_shield/core/`;
- `src/cognitive_shield/shared/`;
- package marker files;
- scaffold files;
- MVP proof helper;
- ACP modules;
- MDS / CMO related modules;
- placeholder modules;
- possibly outdated or duplicate scaffold modules.

Protected MVP source files include:

- `src/cognitive_shield/app/mvp_functional_proof.py`
- `src/cognitive_shield/core/agent_communication_protocol_acp/routing_result.py`

No source file changes are admitted by this document.

## Inventory Zone 4 — Tests

The `tests/` directory should be reviewed because it now supports MVP proof validation.

Inventory targets include:

- `tests/unit/`;
- `tests/contract/`;
- `tests/smoke/`;
- package marker files;
- README files;
- old placeholder tests;
- duplicate tests;
- tests that no longer match current scope;
- missing test documentation.

Protected MVP test files include:

- `tests/smoke/test_mvp_functional_proof.py`
- `tests/unit/test_acp_routing_result.py`

The smoke test area is part of Sprint 4 MVP proof validation.

No test changes are admitted by this document.

## Inventory Zone 5 — Main Documentation Folder

The `docs/` directory should be reviewed because it contains architecture, sprint records, governance, and possible historical duplicates.

Inventory targets include:

- architecture documents;
- sprint documents;
- repo governance documents;
- old planning documents;
- status notes;
- closure documents;
- possible duplicates;
- misplaced documents;
- old drafts;
- archive candidates.

No documentation files may be moved or deleted during inventory.

## Inventory Zone 6 — Sprint 0 Documents

The `docs/sprint_0/` area should be reviewed as historical foundation material.

Inventory questions:

- Which Sprint 0 documents are still active references?
- Which are historical but important?
- Which are replaced by later Sprint closure documents?
- Which should be archived later?
- Are there duplicate or misplaced files?

No Sprint 0 files are classified yet.

## Inventory Zone 7 — Sprint 1 Documents

The `docs/sprint_1/` area should be reviewed as the first implementation-stage record.

Inventory questions:

- Which documents are still needed for traceability?
- Which are superseded by Sprint 2–4?
- Which documents explain important boundaries?
- Which are candidates for archive?
- Which are possible duplicates?

No Sprint 1 files are classified yet.

## Inventory Zone 8 — Sprint 2 Documents

The `docs/sprint_2/` area should be reviewed because Sprint 2 established MDS-to-CMO and CMO construction boundaries.

Inventory questions:

- Which documents remain important to the MVP baseline?
- Which are historical closure records?
- Which are replaced by later summary documents?
- Which should remain accessible?
- Which are archive candidates?

No Sprint 2 files are classified yet.

## Inventory Zone 9 — Sprint 3 Documents

The `docs/sprint_3/` area should be reviewed because Sprint 3 established the ACP structural chain and Protocol Router readiness.

Inventory questions:

- Which documents remain active architectural references?
- Which are historical pass notes?
- Which are closure records?
- Which are candidates for archive?
- Which should remain near active MVP docs?

No Sprint 3 files are classified yet.

## Inventory Zone 10 — Sprint 4 Documents

The `docs/sprint_4/` area should be reviewed carefully because Sprint 4 contains the MVP functional proof closure.

Inventory targets include:

- MVP Completion Control Review;
- Routing Preparation Review;
- Workflow Expansion Review;
- Real Routing Boundary Review;
- MVP Functional Proof Plan;
- MVP Proof Closure Confirmation;
- Sprint 4 Closure Readiness Review;
- Sprint 4 Exit Audit Snapshot;
- MVP Status Note;
- Post-Merge Verification;
- Merge Readiness Review.

Protected Sprint 4 documents include:

- `docs/sprint_4/MVP_STATUS_NOTE.md`
- `docs/sprint_4/SPRINT_4_EXIT_AUDIT_SNAPSHOT.md`
- `docs/sprint_4/SPRINT_4_POST_MERGE_VERIFICATION.md`

Sprint 4 documents should not be aggressively archived because they define the current MVP baseline.

No Sprint 4 files are classified yet.

## Inventory Zone 11 — Repo Governance Documents

The `docs/repo-governance/` area should be reviewed because it should become the stable home for repository operating rules.

Inventory targets include:

- coding rules;
- repository maps;
- testing skeletons;
- cleanup control documents;
- merge readiness documents;
- governance notes;
- old or duplicate repository maps;
- future cleanup inventory and classification documents.

This zone may later become the main home for cleanup and repo maintenance records.

No repo-governance files are classified yet.

## Inventory Zone 12 — Possible Archive Area

The repository should later consider an archive structure.

Possible future archive location:

- `docs/archive/`

Possible future archive subfolders:

- `docs/archive/pre-mvp/`
- `docs/archive/old-sprint-material/`
- `docs/archive/replaced-docs/`
- `docs/archive/legacy-planning/`

Archive structure is not admitted by this document.

A separate archive structure boundary review is required before creating or moving files into archive folders.

## Inventory Zone 13 — Possible Duplicates And Misplaced Files

The cleanup phase should look for:

- duplicated README files;
- duplicate repository maps;
- old closure notes outside sprint folders;
- sprint files in wrong folders;
- root-level documents that belong in `docs/`;
- documents with similar names but different content;
- temporary files;
- accidental upload artifacts;
- outdated scaffold documents.

No duplicate deletion is admitted by this document.

Duplicates must first be listed in a later classification document.

## Inventory Zone 14 — Protected MVP Baseline Files

The following files are protected during cleanup unless separately reviewed:

- `.github/workflows/python-tests.yml`
- `src/cognitive_shield/app/mvp_functional_proof.py`
- `tests/smoke/test_mvp_functional_proof.py`
- `src/cognitive_shield/core/agent_communication_protocol_acp/routing_result.py`
- `tests/unit/test_acp_routing_result.py`
- `docs/sprint_4/MVP_STATUS_NOTE.md`
- `docs/sprint_4/SPRINT_4_EXIT_AUDIT_SNAPSHOT.md`
- `docs/sprint_4/SPRINT_4_POST_MERGE_VERIFICATION.md`

These files represent the MVP proof and post-merge validation state.

## Not Admitted

The following are not admitted by this document:

- file deletion;
- file movement;
- archive movement;
- source code modification;
- test behavior modification;
- workflow modification;
- README rewrite;
- root restructure;
- MVP proof behavior changes;
- Functional Local Prototype Engine implementation;
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

## Required Next Classification Documents

Recommended next documents:

1. `POST_MVP_ROOT_FILES_CLASSIFICATION.md`
2. `POST_MVP_DOCS_CLASSIFICATION.md`
3. `POST_MVP_SPRINT_DOCS_CLASSIFICATION.md`
4. `POST_MVP_SOURCE_TESTS_CLASSIFICATION.md`
5. `POST_MVP_ARCHIVE_STRUCTURE_BOUNDARY_REVIEW.md`

The first recommended classification document is:

- `docs/repo-governance/POST_MVP_ROOT_FILES_CLASSIFICATION.md`

## Required Evidence For Classification

Later classification should rely on:

- file path;
- file name;
- content purpose;
- relation to MVP baseline;
- relation to later documents;
- duplicate status;
- risk of deletion;
- date as supporting signal only.

Date may help prioritize review, but it must not decide alone.

## No-Drift Confirmation

Confirmed:

- cleanup remains inventory-only;
- classification has not started;
- deletion is not admitted;
- movement is not admitted;
- archive movement is not admitted;
- source code remains unchanged;
- tests remain unchanged;
- workflow remains unchanged;
- MVP proof behavior remains unchanged;
- Functional Local Prototype Engine work has not started.

## Verdict Summary

Post-MVP Repo Cleanup Inventory: COMPLETE.

Inventory zones: IDENTIFIED.

Classification: NOT STARTED.

Deletion: NOT ADMITTED.

File movement: NOT ADMITTED.

Archive movement: NOT ADMITTED.

Next document:

- `POST_MVP_ROOT_FILES_CLASSIFICATION.md`
