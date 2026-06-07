# Post-MVP Root Files Classification

Status: Root-level classification document — after Post-MVP Repo Cleanup Inventory.

## Purpose

This document records the first repository classification pass for the post-MVP cleanup phase of the Cognitive Shield project.

The purpose is to classify the root-level repository files and root-level risks before any deletion, movement, archive movement, README rewrite, or root restructuring is admitted.

This document is classification-only.

This document does not admit deletion.

This document does not admit file movement.

This document does not admit archive movement.

This document does not admit root restructuring.

This document does not admit README rewriting.

This document does not admit source code changes.

This document does not admit test behavior changes.

## Baseline

The project has reached the following confirmed state:

- Sprint 4: CLOSED WITH MVP FUNCTIONAL PROOF
- MVP foundation: MERGED INTO `main`
- Post-merge verification: COMPLETE
- Python Tests on `main`: GREEN
- MVP Status Note: PRESENT
- Post-MVP Repo Cleanup Control Pass: COMPLETE
- Post-MVP Repo Cleanup Inventory: COMPLETE

Current cleanup branch:

- `post-mvp/repo-cleanup`

Cleanup status:

- inventory complete
- root-level classification opened
- deletion not admitted
- file movement not admitted
- archive movement not admitted

## Classification Question

How should root-level repository files be classified before cleanup decisions are made?

## Verdict

Verdict:

`ROOT FILES CLASSIFICATION OPENED — NO CLEANUP ACTION YET`

The root-level repository area may be classified.

No root file may be deleted, moved, archived, or rewritten by this document.

## Classification Model

This classification uses the agreed post-MVP categories:

### ACTIVE

The file is part of the current MVP baseline or active repository operation.

### KEEP

The file is important and should remain, even if it is not part of active execution.

### ARCHIVE

The file is historically important but should later move out of the active path.

### REVIEW

The file requires human review before a decision.

### DELETE

The file is safe to delete only after explicit confirmation in a later pass.

This document does not execute any action.

## Protected Root Principles

The root directory defines the visible identity and basic usability of the repository.

Root cleanup must protect:

- project identity;
- license clarity;
- dependency clarity;
- test configuration;
- local development usability;
- MVP status clarity;
- contributor orientation.

Root cleanup must not damage the validated MVP proof baseline.

## Expected Root Files — Preliminary Classification

The following root files are expected or likely present based on the current repository work.

Actual file presence should be verified in GitHub before any future action.

### `README.md`

Classification:

`ACTIVE / KEEP`

Reason:

The root README is the primary public and repository-facing entry point.

It should remain in the root.

It may need a later README refresh, but this classification does not admit rewriting.

Required later review:

- ensure README reflects MVP-level functional proof accurately;
- ensure it does not imply production readiness;
- ensure it points to MVP status and relevant docs.

Action now:

- no deletion;
- no movement;
- no rewrite.

### `LICENSE`

Classification:

`KEEP`

Reason:

The license is a root-level project identity and legal file.

It must remain at root level.

Action now:

- no deletion;
- no movement.

### `pyproject.toml`

Classification:

`ACTIVE`

Reason:

This file supports Python project configuration and tooling.

It is part of the active development baseline.

Action now:

- no deletion;
- no movement;
- no edit.

### `pytest.ini`

Classification:

`ACTIVE`

Reason:

This file supports repository test behavior.

Since Python Tests workflow is central to the MVP proof validation state, pytest configuration must be preserved unless separately reviewed.

Action now:

- no deletion;
- no movement;
- no edit.

### `requirements.txt`

Classification:

`ACTIVE`

Reason:

This file supports dependency setup.

The Python Tests workflow installs test dependencies directly, but the requirements file remains useful for local development and contributor clarity.

Action now:

- no deletion;
- no movement.

### `.editorconfig`

Classification:

`KEEP`

Reason:

This file supports editor consistency and repository hygiene.

It should remain unless a later tooling review decides otherwise.

Action now:

- no deletion;
- no movement.

### `Makefile`

Classification:

`REVIEW / KEEP CANDIDATE`

Reason:

A Makefile may be useful for local developer commands, but it should be reviewed for current accuracy.

If it contains obsolete commands, it may need update later.

If it is accurate, it should remain.

Action now:

- no deletion;
- no movement;
- review content later.

### `.gitignore`

Classification:

`ACTIVE / KEEP`

Reason:

If present, `.gitignore` protects the repository from accidental generated files and local artifacts.

It should remain at root level.

Action now:

- no deletion;
- no movement.

## Root-Level Files Requiring Review

The following root-level file types should be classified as `REVIEW` if present:

- loose sprint documents;
- old planning notes;
- temporary Markdown files;
- duplicate README files;
- duplicate requirements files;
- accidentally uploaded reports;
- generated PDFs not intended for repo history;
- exported documents from working sessions;
- old architecture notes outside `docs/`;
- files that appear to belong under `docs/`;
- files that appear to belong under `docs/archive/`;
- files that appear to belong under `tests/` or `src/`.

Reason:

Root-level clutter reduces repository clarity.

However, no loose file should be deleted only because it is old.

Each such file must be reviewed for content value and replacement status.

Action now:

- list during later root file inspection;
- classify as REVIEW until confirmed.

## Root-Level Delete Candidates

The following may become `DELETE` candidates later, but deletion is not admitted now:

- clearly empty accidental files;
- duplicate files with identical content;
- generated artifacts that do not belong in source control;
- broken temporary files;
- wrongly named copies;
- files created by mistake during GitHub upload;
- files already replaced by newer canonical files and confirmed safe.

Deletion requires a later delete candidate review.

Action now:

- no deletion.

## Root-Level Archive Candidates

The following may become `ARCHIVE` candidates later, but archive movement is not admitted now:

- old root-level planning documents;
- historical notes that have value but do not belong in root;
- replaced project maps;
- early working drafts;
- pre-MVP status notes superseded by Sprint 4 MVP documents.

Action now:

- no movement;
- no archive creation;
- mark for later review if found.

## Root-Level Files That Should Not Move

The following file types should normally remain at root level:

- `README.md`
- `LICENSE`
- `.gitignore`
- `.editorconfig`
- `pyproject.toml`
- `pytest.ini`
- `requirements.txt`
- `Makefile` if still valid

Reason:

These are standard root-level project files and support repository usability.

## Root-Level Files That Should Usually Not Stay In Root

The following file types should generally not remain in root unless there is a strong reason:

- sprint notes;
- long architecture reports;
- old generated documents;
- working drafts;
- project planning exports;
- duplicate maps;
- temporary files;
- old status documents superseded by Sprint 4 closure records.

Such files should be reviewed for later movement to:

- `docs/`;
- `docs/repo-governance/`;
- `docs/archive/`;
- another appropriate location.

No movement is admitted by this document.

## Date-Based Review Rule

Creation or modification date may help prioritize review.

However:

- old does not mean obsolete;
- new does not mean active;
- recently modified does not mean current;
- historical files may remain important.

Date must be combined with:

- path;
- content;
- current role;
- replacement status;
- risk of deletion;
- relation to MVP baseline.

## Root Classification Summary

Preliminary root-level classification:

| File or file type | Classification | Action now |
| --- | --- | --- |
| `README.md` | ACTIVE / KEEP | preserve |
| `LICENSE` | KEEP | preserve |
| `pyproject.toml` | ACTIVE | preserve |
| `pytest.ini` | ACTIVE | preserve |
| `requirements.txt` | ACTIVE | preserve |
| `.editorconfig` | KEEP | preserve |
| `.gitignore` if present | ACTIVE / KEEP | preserve |
| `Makefile` if present | REVIEW / KEEP candidate | review later |
| loose sprint documents | REVIEW | no movement |
| loose architecture drafts | REVIEW / ARCHIVE candidate | no movement |
| generated artifacts | REVIEW / DELETE candidate | no deletion |
| duplicate root files | REVIEW / DELETE candidate | no deletion |

## Not Admitted

The following are not admitted by this document:

- deleting root files;
- moving root files;
- archiving root files;
- renaming root files;
- rewriting README;
- editing configuration files;
- editing workflow files;
- editing source code;
- editing tests;
- changing MVP proof behavior;
- starting Functional Local Prototype Engine work;
- public outreach;
- production release.

## Required Next Step

The next classification step should review the broader documentation area.

Recommended next document:

- `docs/repo-governance/POST_MVP_DOCS_CLASSIFICATION.md`

Alternative if more precision is needed first:

- `docs/repo-governance/POST_MVP_ROOT_FILES_REVIEW_LIST.md`

The preferred next document is:

- `POST_MVP_DOCS_CLASSIFICATION.md`

Reason:

The largest cleanup risk is likely inside `docs/`, not in the protected root files.

## No-Drift Confirmation

Confirmed:

- root classification is opened;
- root cleanup action is not admitted;
- deletion remains not admitted;
- movement remains not admitted;
- archive movement remains not admitted;
- root project identity remains protected;
- MVP proof behavior remains unchanged;
- source code remains unchanged;
- tests remain unchanged;
- workflow remains unchanged;
- Functional Local Prototype Engine work has not started.

## Verdict Summary

Post-MVP Root Files Classification: COMPLETE.

Root files: CLASSIFIED AT POLICY LEVEL.

Deletion: NOT ADMITTED.

File movement: NOT ADMITTED.

Archive movement: NOT ADMITTED.

README rewrite: NOT ADMITTED.

Next document:

- `POST_MVP_DOCS_CLASSIFICATION.md`
