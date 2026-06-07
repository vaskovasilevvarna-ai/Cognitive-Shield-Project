# Post-MVP First Archive Movement Candidate List Review

Status: Candidate list review — before first archive movement pass.

## Purpose

This document reviews the first concrete candidate list for post-MVP archive movement in the Cognitive Shield repository.

The purpose is to identify a small, low-risk first archive movement batch based on repository inspection.

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
- Post-MVP First Archive Movement Candidate List: COMPLETE

Current archive structure:

- `docs/archive/`
- `docs/archive/pre-mvp/`
- `docs/archive/old-sprint-material/`
- `docs/archive/replaced-docs/`
- `docs/archive/legacy-planning/`

## Review Question

Which exact files are suitable for the first archive movement pass?

## Verdict

Verdict:

`FIRST ARCHIVE MOVEMENT CANDIDATE REVIEW OPENED — SMALL LOW-RISK BATCH IDENTIFIED`

A small first archive movement batch may be prepared.

This review identifies exact candidate files.

Actual archive movement still requires a separate movement pass.

## Candidate Review Principle

The first archive movement pass must be small, reversible, and low-risk.

The first pass should not move:

- source files;
- test files;
- workflow files;
- root project identity files;
- Sprint 4 MVP proof documents;
- current repo-governance cleanup documents;
- entire sprint folders.

The first pass should prefer:

- misplaced documentation files;
- replaced configuration copies inside `docs/`;
- loose legacy planning documents inside `docs/`;
- files that are not part of the current MVP proof chain.

## First Candidate Batch

The following candidate batch is intentionally small.

| Source path | Destination path | Archive category | Reason for movement | Protected? | Move in first pass? |
| --- | --- | --- | --- | --- | --- |
| `docs/pyproject.toml` | `docs/archive/replaced-docs/pyproject.toml` | replaced-docs | Configuration-style file appears inside `docs/`; root-level configuration should remain active, while this copy should be preserved as a replaced/misplaced document rather than deleted. | no | yes |
| `docs/pytest.ini` | `docs/archive/replaced-docs/pytest.ini` | replaced-docs | Test configuration-style file appears inside `docs/`; active test configuration should remain at root, while this copy should be preserved as a replaced/misplaced document rather than deleted. | no | yes |
| `docs/blueprint_1_2.md` | `docs/archive/legacy-planning/blueprint_1_2.md` | legacy-planning | Loose blueprint document in `docs/`; likely historical planning material and safer to preserve in legacy planning archive than keep in active documentation root. | no | yes |

## Why This Batch Is Low Risk

This batch is low risk because:

1. It does not touch `src/`.
2. It does not touch `tests/`.
3. It does not touch `.github/`.
4. It does not touch root files.
5. It does not touch Sprint 4 MVP proof documents.
6. It does not touch current post-MVP cleanup governance documents.
7. It does not delete files.
8. It preserves candidate files in archive rather than removing them.
9. It is limited to three files.
10. It is reversible if needed.

## Files Not Included In First Batch

The following areas are intentionally not included in the first movement batch:

- `docs/sprint_4/`
- `docs/repo-governance/`
- `docs/sprint_3/`
- `docs/sprint_2/`
- `docs/sprint_1/`
- `docs/sprint_0/`
- `docs/sprint-0/`
- `docs/docs/`
- `docs/contracts/`
- `docs/testing/`
- root files;
- source files;
- test files;
- workflow files.

Reason:

These areas require additional inspection before any movement.

Whole-folder movement remains not admitted.

## Protected Files

The following files must not be moved in the first archive movement pass:

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

## Required Verification Before Movement

Before the movement pass, verify that each source path exists:

- `docs/pyproject.toml`
- `docs/pytest.ini`
- `docs/blueprint_1_2.md`

If any source file does not exist, remove it from the movement pass.

Before the movement pass, verify that each destination folder exists:

- `docs/archive/replaced-docs/`
- `docs/archive/legacy-planning/`

If a destination folder does not exist, stop and review the archive structure pass.

## Movement Method

The movement pass should preserve file contents.

Preferred movement operation:

- move file from source path to destination path;
- do not edit file content;
- do not rename content internally;
- do not delete source without preserving the file at destination;
- do not combine movement with README rewrite or repository map rewrite.

## Workflow Requirement

After the movement pass, Python Tests workflow must return GREEN on:

- `post-mvp/repo-cleanup`

If Python Tests workflow returns RED, cleanup must stop until the issue is reviewed.

## Not Admitted

The following are not admitted by this document:

- moving files immediately;
- deleting files;
- renaming files beyond archive path movement;
- moving entire folders;
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

## Recommended Next Pass

Recommended next document:

- `docs/repo-governance/POST_MVP_FIRST_ARCHIVE_MOVEMENT_PASS.md`

Recommended movement batch:

1. `docs/pyproject.toml` → `docs/archive/replaced-docs/pyproject.toml`
2. `docs/pytest.ini` → `docs/archive/replaced-docs/pytest.ini`
3. `docs/blueprint_1_2.md` → `docs/archive/legacy-planning/blueprint_1_2.md`

The next pass should include:

- exact movement list;
- movement instructions;
- closure note;
- Python Tests workflow GREEN confirmation.

## No-Drift Confirmation

Confirmed:

- exact candidate review is opened;
- actual archive movement is not performed by this document;
- deletion remains not admitted;
- source code remains unchanged;
- tests remain unchanged;
- workflow remains unchanged;
- MVP proof behavior remains unchanged;
- Functional Local Prototype Engine work has not started.

## Verdict Summary

Post-MVP First Archive Movement Candidate List Review: COMPLETE.

First candidate batch: IDENTIFIED.

Candidate count: 3 files.

Actual archive movement: REQUIRES SEPARATE PASS.

Deletion: NOT ADMITTED.

Source edits: NOT ADMITTED.

Test edits: NOT ADMITTED.

Workflow edits: NOT ADMITTED.

Next document:

- `POST_MVP_FIRST_ARCHIVE_MOVEMENT_PASS.md`
