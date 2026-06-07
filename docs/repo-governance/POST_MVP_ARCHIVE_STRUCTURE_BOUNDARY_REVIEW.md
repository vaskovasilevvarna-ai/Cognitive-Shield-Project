# Post-MVP Archive Structure Boundary Review

Status: Archive structure boundary review — after Post-MVP Source And Tests Classification.

## Purpose

This document records the boundary review for creating a post-MVP archive structure in the Cognitive Shield repository.

The purpose is to decide whether the repository may introduce an archive folder structure before any file movement, archive movement, deletion, or restructuring is admitted.

This document admits archive structure planning only.

This document does not admit moving files into archive folders.

This document does not admit deletion.

This document does not admit source code changes.

This document does not admit test behavior changes.

This document does not admit workflow changes.

This document does not admit README rewriting.

This document does not admit Functional Local Prototype Engine implementation.

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
- Post-MVP Sprint Docs Classification: COMPLETE
- Post-MVP Source And Tests Classification: COMPLETE

Current cleanup branch:

- `post-mvp/repo-cleanup`

Cleanup status:

- inventory complete
- root files classified at policy level
- docs area classified at policy level
- sprint docs classified at policy level
- source and tests classified at policy level
- archive structure boundary review opened
- deletion not admitted
- file movement not admitted
- archive movement not admitted

## Boundary Question

Can the repository admit creation of an archive structure for post-MVP cleanup?

## Verdict

Verdict:

`ADMIT ARCHIVE STRUCTURE CREATION — NO FILE MOVEMENT YET`

The repository may admit creation of a controlled archive folder structure.

This review admits only archive folders and optional README files that explain archive purpose.

No existing project files may be moved into archive folders by this document.

No files may be deleted by this document.

## Why Archive Structure Is Needed

The repository contains many sprint and planning documents that preserve valuable architectural history.

Some older documents may no longer belong in the active documentation path, but they should not be deleted because they may contain:

- architectural reasoning;
- historical decisions;
- boundary review logic;
- earlier sprint context;
- implementation rationale;
- project traceability.

An archive structure allows the project to reduce active documentation noise without losing historical material.

## Archive-First Principle

The cleanup phase must follow archive-first handling.

This means:

1. classify files first;
2. create archive structure;
3. move historically useful files into archive only after movement is separately admitted;
4. delete only obvious duplicates or confirmed unnecessary files after a later delete review;
5. preserve traceability.

Archive does not mean obsolete.

Archive means:

- historically useful;
- no longer part of the active working path;
- preserved for traceability.

## Admitted Archive Structure

The following archive structure is admitted for creation:

```text
docs/archive/
docs/archive/README.md
docs/archive/pre-mvp/
docs/archive/pre-mvp/README.md
docs/archive/old-sprint-material/
docs/archive/old-sprint-material/README.md
docs/archive/replaced-docs/
docs/archive/replaced-docs/README.md
docs/archive/legacy-planning/
docs/archive/legacy-planning/README.md
