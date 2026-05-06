# Active Branch Policy

Status: Active repository governance note.

## Purpose

This document records the active working branch policy for the Cognitive Shield repository.

The project previously used:

`active/mvp-foundation`

replaced:

`sprint-0/repo-restructure`

as the active working branch after Sprint 0 closure and Sprint 1 entry work began.

## Rationale

The old branch name reflected Sprint 0 repository restructuring work.

That name became outdated after:

- Sprint 0 was closed;
- Sprint 1 preparation documents were added;
- Sprint 1 Entry Control Pass was opened;
- shared contracts and narrow unit test passes began.

The new branch name is broader and more durable.

## Active Branch

Current active working branch:

`active/mvp-foundation`

This branch is intended to carry the early MVP foundation work across Sprint 1, Sprint 2 and later early implementation sprints, unless a separate branch policy decision changes this.

## What This Branch Means

`active/mvp-foundation` means:

- active working line;
- MVP foundation work;
- architecture-first implementation;
- bounded commits;
- shared contracts and scaffold stabilization;
- no production readiness implied.

## What This Branch Does Not Mean

This branch does not mean:

- merge to `main`;
- public release readiness;
- broad implementation permission;
- production stability;
- completed MVP;
- bypass of Sprint entry control passes.

## Sprint Tracking

Sprint progress is tracked through:

- `docs/sprint_1/`
- future `docs/sprint_2/`
- future `docs/sprint_3/`
- commit messages;
- closure notes;
- entry control passes;
- Exit Audits and Snapshots.

Sprint identity should be carried by documents and commit messages, not necessarily by the branch name.

## Merge Boundary

Merge to `main` remains a separate decision.

No merge to `main` is authorized by this branch rename.

A merge decision requires a separate review.

## Working Discipline

Work on `active/mvp-foundation` must continue to follow:

- small steps;
- verification before commit;
- contract-first implementation;
- no test before stable contract;
- no free-form coding;
- no hidden policy logic;
- no label-to-verdict shortcut;
- no downstream behavior before admission.

## Verdict

`active/mvp-foundation` is the active working branch for early MVP foundation work.

The rename is a repository hygiene action, not an implementation scope expansion.
