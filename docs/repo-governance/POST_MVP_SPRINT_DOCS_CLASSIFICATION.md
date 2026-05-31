# Post-MVP Sprint Documents Classification

Status: Sprint-document classification document — after Post-MVP Docs Classification.

## Purpose

This document records the sprint-document classification pass for the post-MVP cleanup phase of the Cognitive Shield project.

The purpose is to classify the sprint documentation folders before any archive movement, file movement, deletion, sprint-folder restructuring, or documentation cleanup action is admitted.

This document is classification-only.

This document does not admit deletion.

This document does not admit file movement.

This document does not admit archive movement.

This document does not admit sprint-folder restructuring.

This document does not admit source code changes.

This document does not admit test behavior changes.

This document does not admit workflow changes.

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

Current cleanup branch:

- `post-mvp/repo-cleanup`

Cleanup status:

- inventory complete
- root files classified at policy level
- docs area classified at policy level
- sprint-doc classification opened
- deletion not admitted
- file movement not admitted
- archive movement not admitted

## Classification Question

How should the sprint documentation folders be classified before cleanup decisions are made?

## Verdict

Verdict:

`SPRINT DOCS CLASSIFICATION OPENED — NO CLEANUP ACTION YET`

Sprint documentation may be classified at policy level.

No sprint document may be deleted, moved, archived, renamed, or rewritten by this document.

## Classification Model

This classification uses the agreed post-MVP categories:

### ACTIVE

The document or folder is part of the current MVP baseline, current repository operation, or current working process.

### KEEP

The document or folder is important and should remain accessible, even if it is not part of active MVP execution.

### ARCHIVE

The document or folder is historically important but may later move out of the active working path.

### REVIEW

The document or folder requires human review before a decision.

### DELETE

The document or file is safe to delete only after explicit confirmation in a later pass.

This document does not execute any action.

## Sprint Documentation Principles

Sprint documentation preserves project traceability.

Cleanup must not erase the reasoning trail that led from repository setup to MVP functional proof.

Sprint folders may contain:

- boundary reviews;
- pass closure notes;
- exit audits;
- implementation planning documents;
- workflow decisions;
- architectural decisions;
- repository discipline records.

Older sprint material may become archive candidates, but it must not be deleted only because it is old.

## Sprint 4 Classification

Folder:

- `docs/sprint_4/`

Classification:

`ACTIVE / KEEP`

Reason:

Sprint 4 defines the current MVP baseline.

It contains the documents that prove and explain:

- MVP functional proof;
- minimal non-dispatch routing result;
- workflow expansion;
- smoke-test validation;
- merge readiness;
- post-merge verification;
- MVP status.

Sprint 4 should remain in the active documentation path for now.

Protected Sprint 4 documents include:

- `docs/sprint_4/MVP_STATUS_NOTE.md`
- `docs/sprint_4/SPRINT_4_EXIT_AUDIT_SNAPSHOT.md`
- `docs/sprint_4/SPRINT_4_POST_MERGE_VERIFICATION.md`
- `docs/sprint_4/SPRINT_4_MVP_PROOF_CLOSURE_CONFIRMATION.md`
- `docs/sprint_4/SPRINT_4_CLOSURE_READINESS_REVIEW.md`
- `docs/sprint_4/SPRINT_4_MERGE_READINESS_REVIEW.md`

Action now:

- no deletion;
- no movement;
- no archive movement;
- preserve as active MVP baseline documentation.

## Sprint 3 Classification

Folder:

- `docs/sprint_3/`

Classification:

`KEEP / ARCHIVE CANDIDATE`

Reason:

Sprint 3 established the Agent Communication Protocol (ACP) structural chain and Protocol Router readiness.

Sprint 4 MVP proof depends on Sprint 3 outputs.

Therefore, Sprint 3 documentation remains important for traceability.

However, some detailed intermediate pass notes may later become archive candidates if they are sufficiently represented by Sprint 3 closure documents and Sprint 4 MVP proof records.

Action now:

- no deletion;
- no movement;
- no archive movement;
- review later for archive grouping.

## Sprint 2 Classification

Folder:

- `docs/sprint_2/`

Classification:

`KEEP / ARCHIVE CANDIDATE`

Reason:

Sprint 2 established the Message Decomposition Specification (MDS) to Canonical Message Object (CMO) boundary and bounded CMO construction chain.

Sprint 4 MVP proof depends on the bounded MDS / CMO foundation.

Therefore, Sprint 2 documentation remains important for architectural traceability.

Some intermediate pass documents may later be archived if they are replaced by closure notes and exit audits.

Action now:

- no deletion;
- no movement;
- no archive movement;
- review later for archive grouping.

## Sprint 1 Classification

Folder:

- `docs/sprint_1/`

Classification:

`REVIEW / ARCHIVE CANDIDATE`

Reason:

Sprint 1 contains early implementation and repository foundation material.

Some Sprint 1 documents may still be important for traceability.

However, many may have been superseded by Sprint 2, Sprint 3, and Sprint 4 closure records.

Sprint 1 should not be deleted, but parts of it may later move to archive if no longer needed in the active documentation path.

Action now:

- no deletion;
- no movement;
- no archive movement;
- review later before any archive decision.

## Sprint 0 Classification

Folder:

- `docs/sprint_0/`

Classification:

`REVIEW / ARCHIVE CANDIDATE`

Reason:

Sprint 0 contains early repository setup, design-pack, and initial governance material.

Some files may remain important as foundation records.

Others may be historical and suitable for archive.

Sprint 0 documents should be reviewed carefully because early repository decisions can still explain why the current structure exists.

Action now:

- no deletion;
- no movement;
- no archive movement;
- review later before any archive decision.

## Sprint Folder Summary

| Sprint folder | Classification | Action now |
| --- | --- | --- |
| `docs/sprint_4/` | ACTIVE / KEEP | preserve |
| `docs/sprint_3/` | KEEP / ARCHIVE CANDIDATE | review later |
| `docs/sprint_2/` | KEEP / ARCHIVE CANDIDATE | review later |
| `docs/sprint_1/` | REVIEW / ARCHIVE CANDIDATE | review later |
| `docs/sprint_0/` | REVIEW / ARCHIVE CANDIDATE | review later |

## Sprint Documents That Should Be Protected

The following document types should be protected unless separately reviewed:

- sprint exit audits;
- closure readiness reviews;
- merge readiness reviews;
- post-merge verification records;
- MVP proof records;
- workflow expansion records;
- boundary reviews that explain admitted behavior;
- documents that define current source or test behavior.

For Sprint 4, protection is strongest because Sprint 4 is the current MVP baseline.

## Sprint Documents That May Become Archive Candidates

The following document types may become archive candidates later:

- old intermediate pass notes;
- superseded planning documents;
- repeated checkpoint documents;
- early sprint scaffolding notes;
- documents replaced by later closure reviews;
- documents whose content is fully summarized by exit audits.

Archive candidate does not mean delete.

## Sprint Documents That May Become Delete Candidates

The following may become delete candidates only after explicit review:

- accidental duplicates;
- empty files;
- wrongly created copies;
- generated artifacts not intended for repository history;
- files with identical content already preserved elsewhere.

Deletion is not admitted by this document.

## Date-Based Review Rule

Date may help prioritize review, but it must not decide alone.

Important principles:

- old sprint document does not automatically mean obsolete;
- new sprint document does not automatically mean active;
- early sprint records may contain important architectural rationale;
- intermediate sprint notes may still explain why later decisions exist.

Date must be combined with:

- path;
- file name;
- content;
- relation to MVP baseline;
- replacement status;
- historical value;
- deletion risk.

## Archive-First Principle

If sprint documents are later removed from the active path, the preferred first action is archive movement, not deletion.

Possible future archive groupings:

- `docs/archive/pre-mvp/sprint_0/`
- `docs/archive/pre-mvp/sprint_1/`
- `docs/archive/pre-mvp/sprint_2/`
- `docs/archive/pre-mvp/sprint_3/`
- `docs/archive/replaced-docs/`
- `docs/archive/old-sprint-material/`

Archive structure creation is not admitted by this document.

## Not Admitted

The following are not admitted by this document:

- deleting sprint documents;
- moving sprint documents;
- archiving sprint documents;
- renaming sprint documents;
- creating archive folders;
- restructuring sprint folders;
- editing sprint documents;
- rewriting README;
- rewriting repository maps;
- editing source code;
- editing tests;
- editing workflows;
- changing MVP proof behavior;
- starting Functional Local Prototype Engine work;
- production release;
- public outreach.

## Required Next Step

The next classification step should review source and test areas.

Recommended next document:

- `docs/repo-governance/POST_MVP_SOURCE_TESTS_CLASSIFICATION.md`

Reason:

Before archive structure is created, the repository should confirm that source and test areas are protected and that no cleanup action risks the MVP proof chain.

After source and test classification, the project can open:

- `docs/repo-governance/POST_MVP_ARCHIVE_STRUCTURE_BOUNDARY_REVIEW.md`

## No-Drift Confirmation

Confirmed:

- sprint-document classification is opened;
- sprint cleanup action is not admitted;
- deletion remains not admitted;
- movement remains not admitted;
- archive movement remains not admitted;
- archive structure creation remains not admitted;
- Sprint 4 MVP proof documents remain protected;
- source code remains unchanged;
- tests remain unchanged;
- workflow remains unchanged;
- Functional Local Prototype Engine work has not started.

## Verdict Summary

Post-MVP Sprint Docs Classification: COMPLETE.

Sprint documents: CLASSIFIED AT POLICY LEVEL.

Sprint 4: ACTIVE / KEEP.

Sprint 3: KEEP / ARCHIVE CANDIDATE.

Sprint 2: KEEP / ARCHIVE CANDIDATE.

Sprint 1: REVIEW / ARCHIVE CANDIDATE.

Sprint 0: REVIEW / ARCHIVE CANDIDATE.

Deletion: NOT ADMITTED.

File movement: NOT ADMITTED.

Archive movement: NOT ADMITTED.

Archive structure creation: NOT ADMITTED.

Next document:

- `POST_MVP_SOURCE_TESTS_CLASSIFICATION.md`
