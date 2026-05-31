# Post-MVP Docs Classification

Status: Documentation-area classification document — after Post-MVP Root Files Classification.

## Purpose

This document records the documentation-area classification pass for the post-MVP cleanup phase of the Cognitive Shield project.

The purpose is to classify the main documentation zones before any archive movement, file movement, deletion, README rewrite, repository map rewrite, or documentation restructuring is admitted.

This document is classification-only.

This document does not admit deletion.

This document does not admit file movement.

This document does not admit archive movement.

This document does not admit documentation restructuring.

This document does not admit README rewriting.

This document does not admit new feature implementation.

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

Current cleanup branch:

- `post-mvp/repo-cleanup`

Cleanup status:

- inventory complete
- root files classified at policy level
- docs classification opened
- deletion not admitted
- file movement not admitted
- archive movement not admitted

## Classification Question

How should the documentation area be classified before cleanup decisions are made?

## Verdict

Verdict:

`DOCS CLASSIFICATION OPENED — NO CLEANUP ACTION YET`

The documentation area may be classified at policy level.

No documentation file may be deleted, moved, archived, renamed, or rewritten by this document.

## Classification Model

This classification uses the agreed post-MVP categories:

### ACTIVE

The document is part of the current MVP baseline, current repository operation, or current working process.

### KEEP

The document is important and should remain accessible, even if it is not part of active MVP execution.

### ARCHIVE

The document is historically important but may later move out of the active working path.

### REVIEW

The document requires human review before a decision.

### DELETE

The document is safe to delete only after explicit confirmation in a later pass.

This document does not execute any action.

## Protected Documentation Principles

The documentation area must preserve:

- architecture traceability;
- Sprint 4 MVP proof record;
- repo governance discipline;
- test and workflow rationale;
- project identity;
- evidence of decisions;
- clear distinction between MVP proof and production readiness.

Documentation cleanup must not erase the reasoning trail that led to the MVP functional proof.

## Documentation Zone 1 — `docs/sprint_4/`

Classification:

`ACTIVE / KEEP`

Reason:

Sprint 4 documents define the current MVP baseline.

They include the MVP functional proof plan, boundary reviews, closure confirmation, exit audit, MVP status note, merge readiness review, and post-merge verification.

These documents should remain near the active documentation path for now.

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

## Documentation Zone 2 — `docs/repo-governance/`

Classification:

`ACTIVE / KEEP`

Reason:

This folder should become the stable home for repository operating rules, cleanup records, coding rules, repository maps, and governance documents.

Current post-MVP cleanup documents belong here.

Action now:

- no deletion;
- no movement;
- preserve as active governance zone.

Later review may identify duplicate governance documents, but no action is admitted now.

## Documentation Zone 3 — `docs/sprint_3/`

Classification:

`KEEP / ARCHIVE CANDIDATE`

Reason:

Sprint 3 documents established the ACP structural chain and Protocol Router readiness.

They remain important for traceability because Sprint 4 MVP proof depends on the Sprint 3 ACP chain.

However, some Sprint 3 pass notes may later become archive candidates if they are superseded by Sprint 3 exit audit and Sprint 4 MVP proof records.

Action now:

- no deletion;
- no movement;
- mark as keep / archive candidate for later sprint-doc classification.

## Documentation Zone 4 — `docs/sprint_2/`

Classification:

`KEEP / ARCHIVE CANDIDATE`

Reason:

Sprint 2 documents established the CMO bounded construction chain and MDS-to-CMO boundary.

These documents remain important because the MVP proof chain still depends on MDS and CMO structural discipline.

Some detailed intermediate pass notes may later be archived if they are covered by closure reviews and exit audit snapshots.

Action now:

- no deletion;
- no movement;
- mark as keep / archive candidate for later sprint-doc classification.

## Documentation Zone 5 — `docs/sprint_1/`

Classification:

`REVIEW / ARCHIVE CANDIDATE`

Reason:

Sprint 1 documents are important historically, but many may have been superseded by later Sprint 2–4 closure documents.

They should not be deleted, but they may later be moved into an archive zone if no longer needed in the active documentation path.

Action now:

- no deletion;
- no movement;
- review during sprint-doc classification.

## Documentation Zone 6 — `docs/sprint_0/`

Classification:

`REVIEW / ARCHIVE CANDIDATE`

Reason:

Sprint 0 documents are early foundation records. They may contain important repository setup and design-pack decisions.

Some should remain accessible. Others may be historical and suitable for archive.

Action now:

- no deletion;
- no movement;
- review during sprint-doc classification.

## Documentation Zone 7 — Architecture Documents

Classification:

`KEEP / REVIEW`

Reason:

Architecture documents may contain important project decisions, system maps, module specifications, or historical design rationale.

Older architecture documents should not be deleted only because they are old.

They should be checked for:

- whether they are still current;
- whether they were superseded;
- whether they contain unique architectural reasoning;
- whether they belong in an active architecture folder or archive.

Action now:

- no deletion;
- no movement;
- classify later by content.

## Documentation Zone 8 — Old Planning Documents

Classification:

`REVIEW / ARCHIVE CANDIDATE`

Reason:

Old planning documents may be valuable historically but may no longer belong in the active documentation path.

Examples may include:

- early sprint plans;
- previous estimates;
- old roadmap drafts;
- old implementation notes;
- pre-MVP planning material.

Action now:

- no deletion;
- no movement;
- likely archive candidates after review.

## Documentation Zone 9 — Closure Notes And Exit Audits

Classification:

`KEEP / ARCHIVE CANDIDATE`

Reason:

Closure notes and exit audits preserve process discipline and decision history.

Sprint-level exit audits should generally be kept.

However, detailed intermediate closure notes may later be archived if they are too numerous for active navigation.

Action now:

- no deletion;
- no movement;
- decide later whether they remain in sprint folders or move to archive.

## Documentation Zone 10 — Duplicate Or Similar Documents

Classification:

`REVIEW`

Reason:

Documents with similar names may not be true duplicates. They may represent different checkpoints.

Examples:

- multiple readiness reviews;
- multiple boundary reviews;
- closure notes and exit audits;
- status notes and snapshots.

Each similar document must be reviewed before any archive or delete decision.

Action now:

- no deletion;
- no movement;
- list duplicates in a later duplicate review.

## Documentation Zone 11 — Generated Documents

Classification:

`REVIEW / DELETE CANDIDATE / ARCHIVE CANDIDATE`

Reason:

Generated files such as exported PDFs, temporary documents, or copied reports may not belong in the repository unless they serve a clear purpose.

Some may be useful as public-facing summaries. Others may be redundant artifacts.

Action now:

- no deletion;
- no movement;
- review later for purpose and replacement status.

## Documentation Zone 12 — Misplaced Documents

Classification:

`REVIEW`

Reason:

Some documents may be in the wrong folder.

Examples:

- sprint documents outside sprint folders;
- governance documents outside repo-governance;
- architecture notes placed at root;
- status notes placed in active folders by mistake.

Action now:

- no movement;
- list later during misplaced-files review.

## Documentation Zone 13 — Future Archive Structure

Classification:

`NOT YET ADMITTED`

Reason:

An archive folder may be useful, but archive structure creation is not admitted by this document.

Possible future archive paths:

- `docs/archive/pre-mvp/`
- `docs/archive/old-sprint-material/`
- `docs/archive/replaced-docs/`
- `docs/archive/legacy-planning/`

Action now:

- no archive folder creation;
- no movement into archive;
- open separate archive structure boundary review later.

## Documentation Classification Summary

| Documentation area | Classification | Action now |
| --- | --- | --- |
| `docs/sprint_4/` | ACTIVE / KEEP | preserve |
| `docs/repo-governance/` | ACTIVE / KEEP | preserve |
| `docs/sprint_3/` | KEEP / ARCHIVE CANDIDATE | review later |
| `docs/sprint_2/` | KEEP / ARCHIVE CANDIDATE | review later |
| `docs/sprint_1/` | REVIEW / ARCHIVE CANDIDATE | review later |
| `docs/sprint_0/` | REVIEW / ARCHIVE CANDIDATE | review later |
| architecture docs | KEEP / REVIEW | review later |
| old planning docs | REVIEW / ARCHIVE CANDIDATE | review later |
| closure notes / exit audits | KEEP / ARCHIVE CANDIDATE | review later |
| duplicates / similar docs | REVIEW | list later |
| generated docs | REVIEW | review later |
| misplaced docs | REVIEW | list later |
| future archive structure | NOT YET ADMITTED | no action |

## Date-Based Review Rule

Creation or modification date may help prioritize review.

However:

- old does not automatically mean obsolete;
- new does not automatically mean active;
- recently modified does not automatically mean current;
- old documents may contain important architectural rationale.

Date must be combined with:

- file path;
- file name;
- content;
- current role;
- replacement status;
- relation to MVP baseline;
- risk of deletion;
- historical value.

## Documentation Files That Should Be Protected

The following documents should be protected unless separately reviewed:

- `docs/sprint_4/MVP_STATUS_NOTE.md`
- `docs/sprint_4/SPRINT_4_EXIT_AUDIT_SNAPSHOT.md`
- `docs/sprint_4/SPRINT_4_POST_MERGE_VERIFICATION.md`
- `docs/sprint_4/SPRINT_4_MVP_PROOF_CLOSURE_CONFIRMATION.md`
- `docs/sprint_4/SPRINT_4_CLOSURE_READINESS_REVIEW.md`
- `docs/sprint_4/SPRINT_4_MERGE_READINESS_REVIEW.md`
- current repo-governance cleanup documents

These documents represent the current MVP and post-merge state.

## Not Admitted

The following are not admitted by this document:

- deleting documentation files;
- moving documentation files;
- archiving documentation files;
- renaming documentation files;
- creating archive folders;
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

The next classification step should focus specifically on sprint documentation.

Recommended next document:

- `docs/repo-governance/POST_MVP_SPRINT_DOCS_CLASSIFICATION.md`

Reason:

Sprint documents are likely the largest and most complex documentation group.

They should be handled before archive structure is created.

## No-Drift Confirmation

Confirmed:

- documentation classification is opened;
- documentation cleanup action is not admitted;
- deletion remains not admitted;
- movement remains not admitted;
- archive movement remains not admitted;
- archive structure creation remains not admitted;
- MVP proof documents remain protected;
- source code remains unchanged;
- tests remain unchanged;
- workflow remains unchanged;
- Functional Local Prototype Engine work has not started.

## Verdict Summary

Post-MVP Docs Classification: COMPLETE.

Docs area: CLASSIFIED AT POLICY LEVEL.

Deletion: NOT ADMITTED.

File movement: NOT ADMITTED.

Archive movement: NOT ADMITTED.

Archive structure creation: NOT ADMITTED.

Next document:

- `POST_MVP_SPRINT_DOCS_CLASSIFICATION.md`
