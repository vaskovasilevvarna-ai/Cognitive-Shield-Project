# Post-MVP Repo Cleanup Control Pass

Status: Control pass — before any post-MVP repository cleanup.

## Purpose

This document opens the controlled post-MVP repository cleanup phase for the Cognitive Shield project.

The purpose is to organize, classify, archive, and eventually clean old or redundant repository files after Sprint 4 was closed with MVP functional proof and merged into `main`.

This document does not admit deletion.

This document does not admit file movement yet.

This document does not admit new feature implementation.

This document does not admit changes to the MVP functional proof chain.

This document does not admit production release or public outreach.

## Baseline

Sprint 4 has been completed and merged into `main`.

Confirmed baseline:

- Sprint 4: CLOSED WITH MVP FUNCTIONAL PROOF
- MVP foundation: MERGED INTO MAIN
- Post-merge verification: COMPLETE
- Python Tests on `main`: GREEN
- MVP Status Note: PRESENT
- Sprint 4 Exit Audit Snapshot: PRESENT
- MVP functional proof smoke test: GREEN
- Minimal non-dispatch routing result: CLOSED

Current cleanup branch:

- `post-mvp/repo-cleanup`

Source baseline branch:

- `main`

## Control Question

Can the project open a post-MVP repository cleanup phase?

## Verdict

Verdict:

`POST-MVP REPO CLEANUP MAY OPEN — INVENTORY AND CLASSIFICATION ONLY`

The repository cleanup phase may begin, but only as a controlled inventory and classification process.

No deletion is admitted by this document.

No file movement is admitted by this document.

No archive movement is admitted by this document.

The first required step is repository inventory.

## Why Cleanup Comes Now

Cleanup is appropriate now because the project has reached a stable MVP baseline.

The repository now contains:

- a working MVP functional proof;
- GREEN workflow validation;
- Sprint 4 closure documentation;
- MVP status documentation;
- post-merge verification.

Before starting the next major functional phase, the repository should be made clearer, safer, and easier to navigate.

This is especially important because the next phase, Functional Local Prototype Engine, will add more code, tests, contracts, and documentation.

## Cleanup Branch Rule

All cleanup work must happen on a dedicated cleanup branch.

Current branch:

- `post-mvp/repo-cleanup`

The cleanup branch must be based on the updated `main` branch after Sprint 4 merge.

Cleanup must not be performed directly on `main`.

Cleanup must eventually be merged back through a separate Pull Request.

## Main Branch Protection Principle

`main` is now the stable MVP baseline.

Therefore:

- do not edit `main` directly;
- do not delete files from `main` directly;
- do not reorganize `main` without PR review;
- do not mix cleanup with new feature development;
- do not mix cleanup with Functional Local Prototype Engine implementation.

## Cleanup Scope

The cleanup phase may review:

- root-level files;
- duplicate files;
- old sprint documents;
- misplaced documents;
- outdated scaffold files;
- redundant notes;
- old planning artifacts;
- old repository maps;
- docs folder structure;
- archive candidates;
- README clarity;
- repository governance documents;
- tests and source file organization.

The cleanup phase must not alter the validated MVP proof behavior unless separately reviewed.

## Classification Model

Every reviewed file or file group must be assigned one of the following classifications:

### ACTIVE

The file is part of the current MVP baseline or currently active repository structure.

Examples:

- current source files;
- current tests;
- current workflows;
- MVP proof files;
- current status notes;
- current repo-governance files.

### KEEP

The file is important and should remain, even if it is not part of the active runtime or MVP proof chain.

Examples:

- important architecture records;
- stable project maps;
- essential governance documents;
- important historical decisions still needed for context.

### ARCHIVE

The file is historically important but should not remain in the active working path.

Examples:

- old sprint notes;
- replaced planning artifacts;
- historical architecture drafts;
- previous maps superseded by newer documents.

Archive does not mean delete.

### REVIEW

The file requires human review before a decision.

Examples:

- unclear purpose;
- possible duplicate;
- old but potentially important;
- new but possibly temporary;
- connected to past architecture decisions.

REVIEW files must not be deleted.

### DELETE

The file is safe to delete only if it is clearly unnecessary.

Examples:

- accidental duplicate;
- empty temporary file;
- wrong-location copy;
- obsolete scaffold replaced by active version;
- clearly broken or irrelevant file.

DELETE classification requires explicit confirmation before deletion.

## Date-Based Sorting Rule

Creation or modification date may be used as a signal, but not as the final decision rule.

Important principle:

- old file does not automatically mean obsolete;
- new file does not automatically mean active;
- recently modified file may still be historical;
- old architecture file may remain strategically important.

Date must be combined with:

- content relevance;
- current role;
- replacement status;
- architectural value;
- deletion risk.

## Archive-First Policy

The cleanup phase must follow an archive-first policy.

This means:

1. classify files first;
2. move historically useful files to archive before considering deletion;
3. delete only obvious duplicates or confirmed unnecessary files;
4. preserve architectural traceability.

Preferred archive location:

- `docs/archive/`

Possible later subfolders:

- `docs/archive/pre-mvp/`
- `docs/archive/old-sprint-material/`
- `docs/archive/replaced-docs/`

Archive folder creation is not admitted by this document. It should be admitted in a later archive structure boundary review.

## No-Deletion Rule

No files may be deleted during the initial cleanup control phase.

Deletion requires:

1. inventory;
2. classification;
3. explicit delete candidate list;
4. review;
5. separate deletion pass;
6. GREEN workflow after deletion.

This document does not admit deletion.

## No-Movement Rule

No files may be moved during this initial control pass.

File movement requires:

1. inventory;
2. classification;
3. archive or relocation plan;
4. separate movement pass;
5. GREEN workflow after movement.

This document does not admit movement.

## Required First Cleanup Document

The next required document is:

- `docs/repo-governance/POST_MVP_REPO_CLEANUP_INVENTORY.md`

That document should inventory the main repository zones and define the first file groups for classification.

## Recommended Cleanup Sequence

Recommended sequence:

1. Post-MVP Repo Cleanup Control Pass.
2. Repo Cleanup Inventory.
3. Root files classification.
4. Docs classification.
5. Sprint documents classification.
6. Source and tests classification.
7. Archive structure boundary review.
8. Archive-first movement pass.
9. Delete candidates review.
10. Minimal delete pass only if safe.
11. README / Repository Map refresh.
12. Cleanup closure readiness review.
13. Cleanup exit audit snapshot.
14. Cleanup pull request into `main`.

## Inventory Targets

The inventory should cover at minimum:

- root files;
- `.github/`;
- `src/`;
- `tests/`;
- `docs/`;
- `docs/sprint_0/`;
- `docs/sprint_1/`;
- `docs/sprint_2/`;
- `docs/sprint_3/`;
- `docs/sprint_4/`;
- `docs/repo-governance/`;
- possible duplicate or misplaced files;
- old loose documents.

## Not Admitted

The following are not admitted by this document:

- file deletion;
- file movement;
- archive movement;
- root restructuring;
- README rewrite;
- workflow change;
- source code modification;
- test behavior modification;
- MVP proof behavior modification;
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

## Required Safeguards

The cleanup phase must preserve the following safeguards:

1. Keep `main` stable.
2. Work only on `post-mvp/repo-cleanup`.
3. Do not delete before classification.
4. Do not move before classification.
5. Use archive-first handling for historical material.
6. Preserve Sprint 4 MVP proof files.
7. Preserve Python Tests workflow.
8. Preserve README, LICENSE, and root project identity unless separately reviewed.
9. Keep cleanup separate from new feature implementation.
10. Require GREEN workflow after any later movement or deletion.

## Protected MVP Files

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

## Expected Commit Discipline

Cleanup should use small commits.

Recommended commit style:

- one commit for inventory;
- one commit for each classification document;
- one commit for archive structure;
- one commit per archive movement batch;
- one commit per confirmed delete batch;
- one commit for README / repository map refresh;
- one commit for closure note.

Avoid large mixed commits.

## No-Drift Confirmation

Confirmed:

- Sprint 4 MVP baseline exists on `main`.
- Cleanup branch has been created.
- Cleanup is admitted only as inventory and classification.
- No deletion is admitted.
- No movement is admitted.
- MVP proof behavior must remain unchanged.
- Functional Local Prototype Engine work has not started.
- Production readiness is not claimed.
- Public outreach is not started.

## Verdict Summary

Post-MVP Repo Cleanup Control Pass: COMPLETE.

Cleanup phase: OPENED.

Current branch: `post-mvp/repo-cleanup`.

Cleanup scope: INVENTORY AND CLASSIFICATION ONLY.

Deletion: NOT ADMITTED.

File movement: NOT ADMITTED.

Archive movement: NOT ADMITTED.

Next document:

- `POST_MVP_REPO_CLEANUP_INVENTORY.md`
