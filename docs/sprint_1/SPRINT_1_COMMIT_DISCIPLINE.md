# Sprint 1 Commit Discipline

Status: Draft v0.1 — commit and working discipline document.

## Purpose

This document defines the commit discipline for Sprint 1.

Sprint 1 introduces bounded implementation work, so commit discipline must become stricter than in Sprint 0.

The goal is to preserve traceability, prevent mixed-responsibility changes and keep each implementation step small enough to review.

## Core Working Method

Sprint 1 continues the working method established during Sprint 0:

1. one small step;
2. verification;
3. commit;
4. short confirmation;
5. next small step.

No multi-module implementation bursts should be committed without explicit admission.

## Commit Size Rule

Each commit should normally touch one of the following:

- one document;
- one contract;
- one narrow test;
- one bounded module file;
- one small correction related to the same role.

Avoid commits that mix:

- contract changes and behavior implementation;
- tests and unrelated module changes;
- docs and broad code changes;
- multiple architecture layers;
- core, output and education responsibilities.

## Recommended Commit Message Format

Preferred format:

```text
[sprint-1][area] short action description
[sprint-1][docs] add implementation boundary
[sprint-1][contracts] refine InputMessage contract
[sprint-1][tests] add InputMessage unit test
[sprint-1][shared] add traceability helper
If GitHub UI makes short messages easier, the message may remain simpler, but it should still be role-specific and bounded.

Commit Description Rule

When using an extended description, include:

why the change exists;
what boundary it preserves;
what it does not implement.

Example:
Refine the InputMessage contract as the first bounded Sprint 1 slice.

This does not introduce Message Decomposition Specification (MDS) behavior or downstream pipeline logic.
Branch Discipline

Sprint 1 preparation continues on the current working branch until a separate branch review is performed.

No merge to main is included in Sprint 1 entry work.

A merge decision requires a separate review.

Review Before Commit

Before each commit, check:

Am I in the correct branch?
Is this change part of the admitted current step?
Does this touch only the intended file or small file group?
Does this introduce implementation logic too early?
Does this bypass an architecture layer?
Does this mix responsibilities?
Is the commit message clear?
No-Drift Commit Safeguards

A commit must not:

introduce free-form coding;
hide policy logic in code;
convert taxonomy labels into verdict behavior;
suppress uncertainty or conflict;
add broad tests before stable contracts;
implement downstream behavior before admitted;
mix Education Core behavior into Shield Core;
introduce UI / UX product decisions;
merge to main without separate review.
Recovery Rule

If a commit attempt fails in GitHub UI:

stop retrying after one or two attempts;
refresh the target folder;
check whether the file was created anyway;
do not create duplicate files;
return to the last known clean step;
continue only after the repository state is clear.
Closure Criteria

Sprint 1 commit discipline is established when:

commit messages are role-specific;
commits stay small;
changes remain traceable to the current admitted slice;
no multi-layer mixed commits are introduced;
failed UI attempts are recovered without duplicate or drift files.
Verdict

Sprint 1 must proceed through small, traceable and bounded commits.

Commit discipline is part of the implementation safeguards, not an optional workflow preference.
