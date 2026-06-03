# Cleanup Inventory — Sprint 1 Documentation

Status: Inventory and classification guide for `docs/sprint_1/`.

## Purpose

This document records the cleanup inventory logic for the Sprint 1 documentation folder.

The purpose is to classify the large set of Sprint 1 documents before any archive movement, deletion, or restructuring is admitted.

This document does not move files.

This document does not delete files.

This document does not rename files.

This document does not edit source code.

This document does not edit tests.

This document does not edit workflows.

This document does not start Functional Local Prototype Engine implementation.

## Baseline

Current cleanup branch:

- `post-mvp/repo-cleanup`

Current confirmed state:

- Sprint 4: CLOSED WITH MVP FUNCTIONAL PROOF
- MVP foundation: merged into `main`
- Python Tests on `main`: GREEN
- Python Tests on cleanup branch: GREEN
- Archive structure: CREATED
- Old `docs/sprint-0/` hyphen folder: CLEANED
- `docs/docs/` nested folder: CLEANED
- `docs/contracts/`: ACTIVE / KEEP
- `docs/testing/`: ACTIVE / KEEP
- `docs/sprint_0/`: KEEP / HISTORICAL ACTIVE REFERENCE
- Functional Local Prototype Engine: NOT STARTED

## Inventory Scope

Folder under review:

- `docs/sprint_1/`

Observed character of the folder:

- large number of Sprint 1 checkpoint documents;
- many scaffold closure notes;
- many boundary pass closure notes;
- many unit test pass closure notes;
- several entry-control and readiness documents;
- several summary / exit audit / admission documents.

This folder is not structurally broken.

This folder is not a nested path error.

This folder is documentation-heavy and requires curation.

## Classification Verdict

`docs/sprint_1/` should not be moved as a whole folder.

`docs/sprint_1/` should not be deleted.

`docs/sprint_1/` should be curated.

The recommended target state is:

- keep a small active Sprint 1 summary set in `docs/sprint_1/`;
- move detailed working-pass records to `docs/archive/old-sprint-material/sprint_1/`;
- preserve all historically useful documents;
- do not delete unique Sprint 1 material.

## Active / Keep Candidates

The following types should likely remain in `docs/sprint_1/`:

- Sprint 1 action packs;
- Sprint 1 admission documents;
- Sprint 1 implementation boundary documents;
- Sprint 1 closure readiness reviews;
- Sprint 1 exit audit snapshots;
- Sprint 1 phase-level exit audit snapshots;
- Sprint 1 final readiness or admission notes;
- documents that summarize a group of lower-level pass notes.

Examples include files matching:

- `SPRINT_1_ACTION_PACK.md`
- `SPRINT_1_ADMISSION_CHECKLIST.md`
- `SPRINT_1_IMPLEMENTATION_BOUNDARY.md`
- `SPRINT_1_FIRST_SLICE_PLAN.md`
- `SPRINT_1_CLOSURE_READINESS_REVIEW.md`
- `SPRINT_1_EXIT_AUDIT_SNAPSHOT.md`
- `SPRINT_1_PHASE_A_EXIT_AUDIT_SNAPSHOT.md`
- `SPRINT_1_PHASE_A_REPOSITORY_VERIFICATION_NOTE.md`

These files support active navigation and explain the Sprint 1 outcome.

## Archive Candidate Patterns

The following filename patterns are likely archive candidates:

- `*_SCAFFOLD_PASS_CLOSURE_NOTE.md`
- `*_SCAFFOLD_CLOSURE_SUMMARY_NOTE.md`
- `*_SCHEMA_BOUNDARY_PASS_CLOSURE_NOTE.md`
- `*_CONTRACT_BOUNDARY_PASS_CLOSURE_NOTE.md`
- `*_UNIT_TEST_PASS_CLOSURE_NOTE.md`
- `*_PASS_CLOSURE_NOTE.md`
- `*_TO_*_PREVIEW_PASS_CLOSURE_NOTE.md`
- `*_TO_*_PREVIEW_ENTRY_CONTROL_NOTE.md`
- `*_TEST_SANITY_REFRESH_*.md`
- highly granular module-level closure notes already summarized by higher-level Sprint 1 documents.

Recommended destination:

- `docs/archive/old-sprint-material/sprint_1/`

## Review Candidates

The following should not be moved automatically and require review:

- documents with `ADMISSION_REVIEW` in the name;
- documents with `ENTRY_CONTROL` in the name;
- documents with `READINESS` in the name;
- documents with `VERIFICATION` in the name;
- documents that may explain admitted behavior rather than only close a micro-pass.

These may remain active or be archived depending on whether a higher-level summary already covers them.

## Not Admitted

The following are not admitted by this inventory document:

- moving Sprint 1 files immediately;
- deleting Sprint 1 files;
- moving the whole `docs/sprint_1/` folder;
- editing Sprint 1 document contents;
- rewriting README;
- rewriting repository maps;
- editing source code;
- editing tests;
- editing workflows;
- changing MVP proof behavior;
- starting Functional Local Prototype Engine work.

## Proposed Automation Approach

Manual movement is not recommended for `docs/sprint_1/` because the folder contains many files.

Recommended approach:

1. Add a read-only inventory script.
2. Generate a Sprint 1 file classification report.
3. Review the generated report.
4. Approve a small movement batch.
5. Move files only after review.
6. Require Python Tests workflow GREEN after any movement.

Recommended future script:

- `scripts/cleanup_inventory.py`

Recommended future generated report:

- `docs/repo-governance/generated/CLEANUP_INVENTORY_SPRINT_1_GENERATED.md`

The script should initially be read-only.

It should not move files.

It should not delete files.

It should only classify and report.

## Proposed Inventory Categories

The generated inventory should use these categories:

- `KEEP_ACTIVE`
- `ARCHIVE_CANDIDATE`
- `REVIEW`
- `PROTECTED`
- `DO_NOT_MOVE`

## Proposed Report Columns

The generated inventory report should include:

| File | Suggested category | Reason | Suggested destination | Move now? |
| --- | --- | --- | --- | --- |
| `example.md` | `ARCHIVE_CANDIDATE` | scaffold closure note | `docs/archive/old-sprint-material/sprint_1/example.md` | no |

## First Automated Pass Boundary

The first automated pass must only generate an inventory report.

It must not perform movement.

It must not delete files.

It must not rewrite documents.

It must not change source, tests, workflows, or MVP behavior.

## No-Drift Confirmation

Confirmed:

- `docs/sprint_1/` requires curation, not deletion;
- manual movement is paused for this large folder;
- automation-assisted inventory is recommended;
- archive movement remains blocked until a generated inventory is reviewed;
- source code remains unchanged;
- tests remain unchanged;
- workflow commands remain unchanged;
- Functional Local Prototype Engine work has not started.

## Verdict Summary

Sprint 1 cleanup inventory: OPENED.

`docs/sprint_1/`: REVIEW / CURATION NEEDED.

Whole-folder archive: NOT ADMITTED.

Deletion: NOT ADMITTED.

Manual mass movement: NOT RECOMMENDED.

Next step:

- add read-only inventory script `scripts/cleanup_inventory.py`.
