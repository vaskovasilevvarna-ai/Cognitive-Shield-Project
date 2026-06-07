# Post-MVP Archive Movement Boundary Review

Status: Archive movement boundary review — after Post-MVP Archive Structure Pass.

## Purpose

This document records the boundary review for the first possible archive movement phase in the post-MVP repository cleanup process.

The purpose is to decide whether the project may begin moving selected historical documentation groups into the already-created archive structure.

This document does not move files by itself.

This document does not admit deletion.

This document does not admit source code changes.

This document does not admit test behavior changes.

This document does not admit workflow changes.

This document does not admit README rewriting.

This document does not admit repository map rewriting.

This document does not admit Functional Local Prototype Engine implementation.

## Baseline

The project has reached the following confirmed state:

- Sprint 4: CLOSED WITH MVP FUNCTIONAL PROOF
- MVP foundation: MERGED INTO `main`
- Post-merge verification: COMPLETE
- Python Tests on `main`: GREEN
- MVP Status Note: PRESENT
- Cleanup branch: `post-mvp/repo-cleanup`
- Python Tests on cleanup branch: GREEN
- Post-MVP Repo Cleanup Control Pass: COMPLETE
- Post-MVP Repo Cleanup Inventory: COMPLETE
- Post-MVP Root Files Classification: COMPLETE
- Post-MVP Docs Classification: COMPLETE
- Post-MVP Sprint Docs Classification: COMPLETE
- Post-MVP Source And Tests Classification: COMPLETE
- Post-MVP Archive Structure Boundary Review: COMPLETE
- Post-MVP Archive Structure Pass: COMPLETE
- Cleanup workflow coverage: ENABLED

Current archive structure:

- `docs/archive/`
- `docs/archive/pre-mvp/`
- `docs/archive/old-sprint-material/`
- `docs/archive/replaced-docs/`
- `docs/archive/legacy-planning/`

## Boundary Question

Can the project admit a first controlled archive movement pass?

## Verdict

Verdict:

`ADMIT FIRST ARCHIVE MOVEMENT PLANNING — SPECIFIC FILE MOVEMENT REQUIRES SEPARATE PASS`

The project may begin planning archive movement.

This review admits identifying candidate groups for archive movement.

This review does not move files.

This review does not delete files.

This review does not admit broad folder migration.

This review requires a separate archive movement compressed pass before any files are actually moved.

## Archive Movement Principle

Archive movement must be conservative.

Archive movement means:

- the file remains in the repository;
- the file remains available for historical review;
- the file is moved out of the active documentation path;
- the file is preserved for traceability.

Archive movement does not mean:

- the file is deleted;
- the file is invalid;
- the file is unimportant;
- the file should be ignored permanently.

## First Movement Scope

The first archive movement pass should be small and low-risk.

It should focus only on clearly historical or superseded documentation groups.

It should not move active MVP baseline files.

It should not move current repo-governance cleanup documents.

It should not move source files.

It should not move test files.

It should not move workflow files.

## Candidate Group 1 — Old Sprint Working Material

Possible archive destination:

- `docs/archive/old-sprint-material/`

Candidate type:

- old intermediate sprint pass notes;
- repeated checkpoint notes;
- superseded working notes;
- old sprint planning fragments;
- detailed intermediate closure fragments already summarized by later exit audits.

Recommended classification:

`ARCHIVE CANDIDATE`

Condition:

Only move files that are clearly superseded by later sprint closure documents, exit audits, or MVP proof records.

Do not move entire sprint folders.

Do not move Sprint 4 MVP proof records.

## Candidate Group 2 — Pre-MVP Historical Material

Possible archive destination:

- `docs/archive/pre-mvp/`

Candidate type:

- historical pre-MVP planning documents;
- early repository setup notes;
- early architecture records that are no longer active;
- older working material from before Sprint 4 MVP proof.

Recommended classification:

`ARCHIVE CANDIDATE`

Condition:

Only move documents that are clearly historical and not required in the active navigation path.

Do not move documents that still explain active architecture or current MVP behavior.

## Candidate Group 3 — Replaced Documents

Possible archive destination:

- `docs/archive/replaced-docs/`

Candidate type:

- replaced repository maps;
- replaced status notes;
- older planning documents superseded by newer documents;
- duplicated documents where one canonical version is clearly active;
- older versions of documents now represented by closure reviews or exit audits.

Recommended classification:

`ARCHIVE CANDIDATE`

Condition:

Replacement status must be explicit.

If it is unclear whether a document is replaced, classify it as `REVIEW`, not `ARCHIVE`.

## Candidate Group 4 — Legacy Planning Material

Possible archive destination:

- `docs/archive/legacy-planning/`

Candidate type:

- old roadmap drafts;
- early implementation estimates;
- preliminary strategy notes;
- outdated planning assumptions;
- non-current planning documents preserved for context.

Recommended classification:

`ARCHIVE CANDIDATE`

Condition:

Only move planning material that is no longer the active plan.

Do not move current post-MVP planning documents.

Do not move Functional Local Prototype Engine planning documents if they become active later.

## Protected Files

The following files must not be moved during the first archive movement pass:

- `.github/workflows/python-tests.yml`
- `src/cognitive_shield/app/mvp_functional_proof.py`
- `tests/smoke/test_mvp_functional_proof.py`
- `src/cognitive_shield/core/agent_communication_protocol_acp/routing_result.py`
- `tests/unit/test_acp_routing_result.py`
- `docs/sprint_4/MVP_STATUS_NOTE.md`
- `docs/sprint_4/SPRINT_4_EXIT_AUDIT_SNAPSHOT.md`
- `docs/sprint_4/SPRINT_4_POST_MERGE_VERIFICATION.md`
- `docs/sprint_4/SPRINT_4_MVP_PROOF_CLOSURE_CONFIRMATION.md`
- `docs/sprint_4/SPRINT_4_CLOSURE_READINESS_REVIEW.md`
- `docs/sprint_4/SPRINT_4_MERGE_READINESS_REVIEW.md`
- current post-MVP cleanup governance documents.

These files represent the current MVP and post-merge state.

## Strongly Protected Areas

The following areas should not be moved in the first archive movement pass:

- `src/`
- `tests/`
- `.github/`
- root project files;
- `docs/sprint_4/`;
- current `docs/repo-governance/` cleanup documents.

## Areas Requiring Careful Review

The following areas may contain archive candidates, but should not be moved as whole folders:

- `docs/sprint_0/`
- `docs/sprint_1/`
- `docs/sprint_2/`
- `docs/sprint_3/`
- old planning documents;
- duplicate or similar documents;
- replaced status notes;
- old repository maps.

Each candidate must be selected intentionally.

## First Archive Movement Pass Rule

The first archive movement pass should include only a small, explicit list of files.

It should not move whole sprint folders.

It should not move all old files by date.

It should not move anything merely because it is old.

Each moved file must have:

- source path;
- destination path;
- reason for movement;
- archive category;
- confirmation that it is not protected;
- confirmation that it is not required for MVP proof.

## Required Future Movement Table

The first archive movement pass should include a table like this:

| Source path | Destination path | Archive category | Reason | Protected? |
| --- | --- | --- | --- | --- |
| `example/source.md` | `docs/archive/old-sprint-material/example/source.md` | old sprint material | superseded by exit audit | no |

This boundary review does not populate the final movement table.

The table must be created in the next movement pass.

## Deletion Rule

Deletion remains not admitted.

If a file appears unnecessary, it should first be classified as:

`DELETE CANDIDATE`

but deletion requires a separate delete candidate review and a separate deletion pass.

No deletion is allowed during archive movement.

## Date-Based Rule

Date may help prioritize review, but it must not decide movement by itself.

Important principles:

- old does not automatically mean archive;
- new does not automatically mean active;
- recently modified does not automatically mean current;
- early documents may contain important architectural rationale.

Archive movement must be based on:

- content;
- current role;
- replacement status;
- relation to MVP baseline;
- historical value;
- navigation impact;
- deletion or movement risk.

## Workflow Requirement

After any archive movement pass, the Python Tests workflow must return GREEN on:

- `post-mvp/repo-cleanup`

If workflow returns RED, cleanup must stop until the issue is reviewed.

## Recommended Next Pass

If this review is accepted, the next pass should be:

- `POST_MVP_FIRST_ARCHIVE_MOVEMENT_PASS.md`

or:

- `POST_MVP_FIRST_ARCHIVE_MOVEMENT_CANDIDATE_LIST.md`

Recommended next document:

- `docs/repo-governance/POST_MVP_FIRST_ARCHIVE_MOVEMENT_CANDIDATE_LIST.md`

Reason:

Before moving files, the project should list exact candidates.

This keeps archive movement controlled and reversible.

## Not Admitted

The following are not admitted by this document:

- moving files immediately;
- deleting files;
- renaming files;
- moving entire sprint folders;
- moving Sprint 4 MVP proof documents;
- moving source files;
- moving test files;
- moving workflow files;
- editing source code;
- editing tests;
- editing workflows;
- rewriting README;
- rewriting repository maps;
- changing MVP proof behavior;
- starting Functional Local Prototype Engine work;
- production release;
- public outreach.

## Required Safeguards

Archive movement must preserve the following safeguards:

1. Do not move protected MVP files.
2. Do not move source files.
3. Do not move test files.
4. Do not move workflow files.
5. Do not move entire sprint folders.
6. Do not delete files.
7. Use explicit candidate lists.
8. Preserve historical traceability.
9. Preserve active MVP documentation.
10. Require Python Tests workflow GREEN after movement.
11. Keep archive movement separate from Functional Local Prototype Engine work.

## No-Drift Confirmation

Confirmed:

- archive structure exists;
- archive movement planning is now admitted;
- actual archive movement is not performed by this document;
- deletion remains not admitted;
- source code remains unchanged;
- tests remain unchanged;
- workflow remains unchanged;
- MVP proof behavior remains unchanged;
- Functional Local Prototype Engine work has not started.

## Verdict Summary

Post-MVP Archive Movement Boundary Review: COMPLETE.

Archive movement planning: ADMITTED.

Actual archive movement: REQUIRES SEPARATE PASS.

Deletion: NOT ADMITTED.

Source edits: NOT ADMITTED.

Test edits: NOT ADMITTED.

Workflow edits: NOT ADMITTED.

Next document:

- `POST_MVP_FIRST_ARCHIVE_MOVEMENT_CANDIDATE_LIST.md`
