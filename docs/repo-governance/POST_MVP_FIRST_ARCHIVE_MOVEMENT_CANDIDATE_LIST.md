# Post-MVP First Archive Movement Candidate List

Status: Candidate list — before first archive movement pass.

## Purpose

This document records the candidate-list gate for the first possible archive movement pass in the post-MVP repository cleanup phase of the Cognitive Shield project.

The purpose is to define the exact rules and table format for selecting files that may later be moved into the archive structure.

This document does not move files.

This document does not delete files.

This document does not rename files.

This document does not edit source code.

This document does not edit tests.

This document does not edit workflows.

This document does not start Functional Local Prototype Engine implementation.

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
- Post-MVP Archive Movement Boundary Review: COMPLETE

Current archive structure:

- `docs/archive/`
- `docs/archive/pre-mvp/`
- `docs/archive/old-sprint-material/`
- `docs/archive/replaced-docs/`
- `docs/archive/legacy-planning/`

## Candidate List Question

Which files may be considered for the first archive movement pass?

## Verdict

Verdict:

`FIRST ARCHIVE MOVEMENT CANDIDATE LIST OPENED — EXACT FILES STILL REQUIRE REPO INSPECTION`

This document opens the first archive movement candidate-list phase.

However, exact file movement is not admitted until concrete source and destination paths are reviewed.

Because this document is written before full file-by-file inspection, it defines candidate groups and the required movement table format.

Actual movement requires a later compressed pass.

## Important Limitation

This document does not claim that specific files are already safe to move.

The next practical step must inspect actual repository file paths.

Candidate files must be selected from the repository UI or file tree and entered into the movement table before any move occurs.

No movement may happen based only on age, folder name, or intuition.

## Candidate Selection Principles

A file may be considered for archive movement only if all of the following are true:

1. It is not protected MVP baseline material.
2. It is not source code.
3. It is not a test file.
4. It is not a workflow file.
5. It is not a root project identity file.
6. It is not required for current MVP proof explanation.
7. It is historically useful enough to preserve.
8. It is no longer needed in the active documentation path.
9. It has an appropriate archive destination.
10. Python Tests workflow can remain GREEN after movement.

## Strongly Protected Files

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

The following areas must not be moved in the first archive movement pass:

- `src/`
- `tests/`
- `.github/`
- root project files;
- `docs/sprint_4/`;
- current `docs/repo-governance/` cleanup documents.

## Candidate Group A — Old Sprint Working Material

Potential archive destination:

- `docs/archive/old-sprint-material/`

Possible candidates:

- old intermediate sprint pass notes;
- repeated checkpoint notes;
- superseded sprint working notes;
- old sprint planning fragments;
- detailed intermediate closure fragments already summarized by later exit audits.

Required condition:

Only move files that are clearly superseded by later sprint closure documents, exit audits, or MVP proof records.

Do not move entire sprint folders.

Do not move Sprint 4 MVP proof records.

Candidate status:

`PENDING EXACT FILE SELECTION`

## Candidate Group B — Pre-MVP Historical Material

Potential archive destination:

- `docs/archive/pre-mvp/`

Possible candidates:

- historical pre-MVP planning documents;
- early repository setup notes;
- early architecture records no longer in active use;
- older working material from before Sprint 4 MVP proof.

Required condition:

Only move documents that are clearly historical and not required in active project navigation.

Do not move documents that still explain active architecture or current MVP behavior.

Candidate status:

`PENDING EXACT FILE SELECTION`

## Candidate Group C — Replaced Documents

Potential archive destination:

- `docs/archive/replaced-docs/`

Possible candidates:

- replaced repository maps;
- replaced status notes;
- older planning documents superseded by newer documents;
- duplicate documents where one canonical version is clearly active;
- older versions of documents now represented by closure reviews or exit audits.

Required condition:

Replacement status must be explicit.

If replacement status is unclear, classify the file as `REVIEW`, not `ARCHIVE`.

Candidate status:

`PENDING EXACT FILE SELECTION`

## Candidate Group D — Legacy Planning Material

Potential archive destination:

- `docs/archive/legacy-planning/`

Possible candidates:

- old roadmap drafts;
- early implementation estimates;
- preliminary strategy notes;
- outdated planning assumptions;
- non-current planning documents preserved for context.

Required condition:

Only move planning material that is no longer the active plan.

Do not move current post-MVP planning documents.

Do not move Functional Local Prototype Engine planning material if it becomes active later.

Candidate status:

`PENDING EXACT FILE SELECTION`

## First Archive Movement Candidate Table

The following table must be populated before the first archive movement pass.

No file may be moved unless it appears in this table with a clear reason.

| Source path | Destination path | Archive category | Reason for movement | Protected? | Move in first pass? |
| --- | --- | --- | --- | --- | --- |
| `PENDING_REPO_INSPECTION` | `PENDING_REPO_INSPECTION` | `PENDING` | exact file candidates must be selected after repo inspection | yes / no pending | no |

## Candidate Review Requirements

Before any candidate is moved, verify:

1. The source path exists.
2. The destination path is inside `docs/archive/`.
3. The file is not protected.
4. The file is not required for MVP proof.
5. The file is not source code.
6. The file is not a test file.
7. The file is not a workflow file.
8. The file is not a root identity file.
9. The file has historical value.
10. The file has a clear archive category.
11. The movement can be reversed if needed.

## Recommended First Movement Scope

The first movement pass should be intentionally small.

Recommended maximum size:

- 3 to 8 files

Reason:

A small first pass reduces the risk of accidental loss of navigation, broken references, or confusion.

If the first pass is successful and Python Tests workflow remains GREEN, later archive movement passes may handle additional groups.

## Files Not Suitable For First Movement

The first movement pass should not include:

- any Sprint 4 MVP proof document;
- any current repo-governance cleanup document;
- any file in `src/`;
- any file in `tests/`;
- any file in `.github/`;
- root README;
- root LICENSE;
- dependency or configuration files;
- current MVP status documents;
- current post-merge verification records.

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
- movement risk.

## Workflow Requirement

After any archive movement pass, the Python Tests workflow must return GREEN on:

- `post-mvp/repo-cleanup`

If Python Tests workflow returns RED, cleanup must stop until the issue is reviewed.

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

## Required Next Practical Step

The next practical step is repository inspection.

Recommended action:

1. Open the repository file tree in GitHub.
2. Inspect older sprint folders and loose documentation.
3. Identify 3 to 8 low-risk archive candidates.
4. Fill the candidate table with exact paths.
5. Review the candidate table before movement.
6. Only then create the first archive movement compressed pass.

## Recommended Next Document

Recommended next document after actual candidate inspection:

- `docs/repo-governance/POST_MVP_FIRST_ARCHIVE_MOVEMENT_PASS.md`

or, if more review is needed first:

- `docs/repo-governance/POST_MVP_FIRST_ARCHIVE_MOVEMENT_CANDIDATE_LIST_REVIEW.md`

## No-Drift Confirmation

Confirmed:

- candidate-list phase is opened;
- actual archive movement is not performed by this document;
- deletion remains not admitted;
- source code remains unchanged;
- tests remain unchanged;
- workflow remains unchanged;
- MVP proof behavior remains unchanged;
- Functional Local Prototype Engine work has not started.

## Verdict Summary

Post-MVP First Archive Movement Candidate List: COMPLETE.

Candidate groups: IDENTIFIED.

Exact file candidates: PENDING REPO INSPECTION.

Actual archive movement: NOT ADMITTED BY THIS DOCUMENT.

Deletion: NOT ADMITTED.

Source edits: NOT ADMITTED.

Test edits: NOT ADMITTED.

Workflow edits: NOT ADMITTED.

Next practical step:

- inspect repository and populate exact candidate table.
