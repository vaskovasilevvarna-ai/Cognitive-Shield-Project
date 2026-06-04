# Sprint 1 Documentation Index

Status: Active navigation index for Sprint 1 documentation.

## Purpose

This document provides a structured navigation index for the Sprint 1 documentation folder.

The purpose is to reduce navigation friction, prevent file-selection mistakes, and support disciplined post-MVP cleanup.

This index does not move files.

This index does not delete files.

This index does not rename files.

This index does not edit source code.

This index does not edit tests.

This index does not edit workflows.

This index does not start Functional Local Prototype Engine implementation.

## Baseline

Sprint 1 documentation is currently located in:

- `docs/sprint_1/`

Sprint 1 contains many checkpoint, scaffold, contract, boundary, test, preview, readiness, and closure documents.

Because the folder is large, working only from raw alphabetical GitHub ordering increases the risk of selecting the wrong file.

This index introduces stable working codes for Sprint 1 document groups.

## Working Rule

For future cleanup passes, use the document code first, then verify the full filename.

Example:

- working code: `ACP-A04`
- file: `SPRINT_1_ACP_SCOPE_GUARD_SCAFFOLD_PASS_CLOSURE_NOTE.md`

No file should be moved or deleted based only on the working code.

Always verify the full filename and path.

## Current Cleanup Method

The active cleanup method remains:

1. Copy raw source content.
2. Create correct archive file.
3. Verify archive file exists.
4. Delete old source copy only after verification.
5. Confirm Python Tests workflow GREEN.

Risky path rename from deep folders should not be used for large documentation cleanup.

## Section 01 — Core Sprint 1 Control Documents

These documents should remain active unless a later review decides otherwise.

| Code | File | Status |
| --- | --- | --- |
| CORE-01 | `SPRINT_1_ACTION_PACK.md` | KEEP_ACTIVE |
| CORE-02 | `SPRINT_1_ADMISSION_CHECKLIST.md` | KEEP_ACTIVE |
| CORE-03 | `SPRINT_1_IMPLEMENTATION_BOUNDARY.md` | KEEP_ACTIVE |
| CORE-04 | `SPRINT_1_FIRST_SLICE_PLAN.md` | KEEP_ACTIVE |
| CORE-05 | `SPRINT_1_CLOSURE_READINESS_REVIEW.md` | KEEP_ACTIVE |
| CORE-06 | `SPRINT_1_EXIT_AUDIT_SNAPSHOT.md` | KEEP_ACTIVE |
| CORE-07 | `SPRINT_1_PHASE_A_EXIT_AUDIT_SNAPSHOT.md` | KEEP_ACTIVE |
| CORE-08 | `SPRINT_1_PHASE_A_REPOSITORY_VERIFICATION_NOTE.md` | KEEP_ACTIVE |

## Section 02 — Agent Communication Protocol Documents

Agent Communication Protocol (ACP) Sprint 1 documents.

### ACP Archive Batch A — Scaffold Closure Notes

These are granular Sprint 1 working-pass records and are approved for archive movement in small batches.

Destination:

- `docs/archive/old-sprint-material/sprint_1/`

| Code | File | Status |
| --- | --- | --- |
| ACP-A01 | `SPRINT_1_ACP_CONTRADICTION_REGISTRAR_SCAFFOLD_PASS_CLOSURE_NOTE.md` | ARCHIVED / SOURCE REMOVED |
| ACP-A02 | `SPRINT_1_ACP_ROUTER_SCAFFOLD_PASS_CLOSURE_NOTE.md` | ARCHIVED / SOURCE REMOVED |
| ACP-A03 | `SPRINT_1_ACP_SCHEMA_VALIDATOR_SCAFFOLD_PASS_CLOSURE_NOTE.md` | ARCHIVED / SOURCE REMOVED AFTER RECOVERY |
| ACP-A04 | `SPRINT_1_ACP_SCOPE_GUARD_SCAFFOLD_PASS_CLOSURE_NOTE.md` | NEXT CANDIDATE |
| ACP-A05 | `SPRINT_1_ACP_SYNTHESIS_EXPORTER_SCAFFOLD_PASS_CLOSURE_NOTE.md` | NEXT CANDIDATE |
| ACP-A06 | `SPRINT_1_ACP_UNCERTAINTY_PROPAGATOR_SCAFFOLD_PASS_CLOSURE_NOTE.md` | NEXT CANDIDATE |

### ACP Other Documents

These documents require review or separate handling.

| Code | File | Status |
| --- | --- | --- |
| ACP-R01 | `SPRINT_1_ACP_CONTRACT_BOUNDARY_PASS_CLOSURE_NOTE.md` | ARCHIVE_CANDIDATE / REVIEW |
| ACP-R02 | `SPRINT_1_ACP_SCAFFOLD_CLOSURE_SUMMARY_NOTE.md` | ARCHIVE_CANDIDATE / REVIEW |
| ACP-R03 | `SPRINT_1_ACP_SCAFFOLD_ENTRY_CONTROL_NOTE.md` | REVIEW |
| ACP-R04 | `SPRINT_1_ACP_SCHEMA_BOUNDARY_PASS_CLOSURE_NOTE.md` | ARCHIVE_CANDIDATE / REVIEW |
| ACP-R05 | `SPRINT_1_ACP_TO_ANALYSIS_PREVIEW_ENTRY_CONTROL_NOTE.md` | REVIEW |
| ACP-R06 | `SPRINT_1_ACP_TO_ANALYSIS_PREVIEW_PASS_CLOSURE_NOTE.md` | ARCHIVE_CANDIDATE / REVIEW |

## Section 03 — Analysis Documents

Analysis-layer Sprint 1 documents.

| Code | Pattern / File Group | Status |
| --- | --- | --- |
| ANALYSIS-01 | Analysis scaffold closure notes | ARCHIVE_CANDIDATE |
| ANALYSIS-02 | Analysis contract boundary notes | ARCHIVE_CANDIDATE / REVIEW |
| ANALYSIS-03 | Analysis schema boundary notes | ARCHIVE_CANDIDATE / REVIEW |
| ANALYSIS-04 | Analysis entry-control notes | REVIEW |
| ANALYSIS-05 | Analysis summary notes | REVIEW |

## Section 04 — Canonical Message Object Documents

Canonical Message Object (CMO) Sprint 1 documents.

| Code | Pattern / File Group | Status |
| --- | --- | --- |
| CMO-01 | CMO scaffold closure notes | ARCHIVE_CANDIDATE |
| CMO-02 | CMO contract boundary notes | ARCHIVE_CANDIDATE / REVIEW |
| CMO-03 | CMO schema boundary notes | ARCHIVE_CANDIDATE / REVIEW |
| CMO-04 | CMO entry-control notes | REVIEW |
| CMO-05 | CMO preview-chain notes | REVIEW |

## Section 05 — Input Documents

Input-layer Sprint 1 documents.

| Code | Pattern / File Group | Status |
| --- | --- | --- |
| INPUT-01 | Input scaffold closure notes | ARCHIVE_CANDIDATE |
| INPUT-02 | Input contract boundary notes | ARCHIVE_CANDIDATE / REVIEW |
| INPUT-03 | Input schema boundary notes | ARCHIVE_CANDIDATE / REVIEW |
| INPUT-04 | Input validator notes | ARCHIVE_CANDIDATE / REVIEW |
| INPUT-05 | Input entry-control notes | REVIEW |
| INPUT-06 | Input to MDS preview notes | REVIEW |

## Section 06 — Message Decomposition Specification Documents

Message Decomposition Specification (MDS) Sprint 1 documents.

| Code | Pattern / File Group | Status |
| --- | --- | --- |
| MDS-01 | MDS scaffold closure notes | ARCHIVE_CANDIDATE |
| MDS-02 | MDS contract boundary notes | ARCHIVE_CANDIDATE / REVIEW |
| MDS-03 | MDS schema boundary notes | ARCHIVE_CANDIDATE / REVIEW |
| MDS-04 | MDS module entry-control notes | REVIEW |
| MDS-05 | MDS to CMO preview notes | REVIEW |

## Section 07 — Testing Documents

Sprint 1 testing and test sanity documents.

| Code | Pattern / File Group | Status |
| --- | --- | --- |
| TEST-01 | Unit test pass closure notes | ARCHIVE_CANDIDATE |
| TEST-02 | Test sanity pass plan | REVIEW |
| TEST-03 | Test sanity verification note | REVIEW |
| TEST-04 | Test sanity refresh notes | ARCHIVE_CANDIDATE |
| TEST-05 | Testing entry rules | REVIEW |

## Section 08 — Phase A Documents

Sprint 1 Phase A documents.

| Code | Pattern / File Group | Status |
| --- | --- | --- |
| PHASE-A01 | Phase A exit audit / verification documents | KEEP_ACTIVE / REVIEW |
| PHASE-A02 | Phase A shell scaffold pass closure notes | ARCHIVE_CANDIDATE |
| PHASE-A03 | Phase A preview-chain readiness documents | REVIEW |
| PHASE-A04 | Phase A integration shell entry-control documents | REVIEW |

## Section 09 — Review Queue

These document types require human review before movement.

| Code | Pattern | Reason |
| --- | --- | --- |
| REVIEW-01 | `*ADMISSION_REVIEW*` | may represent decision gate |
| REVIEW-02 | `*ENTRY_CONTROL*` | may represent active boundary discipline |
| REVIEW-03 | `*READINESS*` | may summarize readiness state |
| REVIEW-04 | `*VERIFICATION*` | may support proof / audit trail |
| REVIEW-05 | `*BOUNDARY*` | may encode important constraints |

## Section 10 — Archive Queue

These document types are likely archive candidates after review.

| Code | Pattern | Destination |
| --- | --- | --- |
| ARCHIVE-01 | `*_SCAFFOLD_PASS_CLOSURE_NOTE.md` | `docs/archive/old-sprint-material/sprint_1/` |
| ARCHIVE-02 | `*_SCAFFOLD_CLOSURE_SUMMARY_NOTE.md` | `docs/archive/old-sprint-material/sprint_1/` |
| ARCHIVE-03 | `*_UNIT_TEST_PASS_CLOSURE_NOTE.md` | `docs/archive/old-sprint-material/sprint_1/` |
| ARCHIVE-04 | `*_PASS_CLOSURE_NOTE.md` | `docs/archive/old-sprint-material/sprint_1/` |
| ARCHIVE-05 | `*_TEST_SANITY_REFRESH_*.md` | `docs/archive/old-sprint-material/sprint_1/` |

## Current ACP Batch Status

Current batch:

- Sprint 1 ACP Archive Batch A

Completed:

- `ACP-A01`
- `ACP-A02`
- `ACP-A03`

Recovery:

- `ACP-A03` required content correction.
- Correct archive content was restored.
- Source copy was removed.
- Python Tests workflow returned GREEN.

Remaining:

- `ACP-A04`
- `ACP-A05`
- `ACP-A06`

## Next Recommended Action

Continue with the remaining ACP Archive Batch A files only after branch check:

1. `ACP-A04` — `SPRINT_1_ACP_SCOPE_GUARD_SCAFFOLD_PASS_CLOSURE_NOTE.md`
2. `ACP-A05` — `SPRINT_1_ACP_SYNTHESIS_EXPORTER_SCAFFOLD_PASS_CLOSURE_NOTE.md`
3. `ACP-A06` — `SPRINT_1_ACP_UNCERTAINTY_PROPAGATOR_SCAFFOLD_PASS_CLOSURE_NOTE.md`

Use the safe method:

- copy raw content;
- create archive file;
- verify archive file exists and content title matches;
- delete source copy;
- confirm Python Tests workflow GREEN.

## Not Admitted

The following are not admitted by this index:

- moving files automatically;
- deleting files automatically;
- moving the whole `docs/sprint_1/` folder;
- renaming all Sprint 1 files;
- editing source code;
- editing tests;
- editing workflows;
- changing MVP proof behavior;
- starting Functional Local Prototype Engine work.

## No-Drift Confirmation

Confirmed:

- this index is navigational;
- this index does not perform cleanup actions;
- Sprint 1 curation remains review-based;
- deletion is limited to verified archived source copies;
- source code remains unchanged;
- tests remain unchanged;
- workflow commands remain unchanged;
- Functional Local Prototype Engine work has not started.
