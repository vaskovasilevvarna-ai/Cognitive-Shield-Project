# Coding Rules

## Purpose
These rules translate the bounded MVP implementation discipline into repository behavior.

## Rule 1 — No free-form coding
Every new file must map to:

- a fixed architectural module
- a public contract or explicit local role
- a bounded implementation responsibility

No file may invent a new hidden architecture.

## Rule 2 — No label-to-verdict shortcut
Taxonomy labels must never trigger final decision behavior directly.

Allowed flow:
taxonomy -> mapping -> risk -> confidence/uncertainty -> Internal Arbiter -> Decision Policy Layer -> Shield Decision

## Rule 3 — No bypass of core governance
No orchestration path may bypass:

- Confidence / Uncertainty Model
- Internal Arbiter (IA)
- Decision Policy Layer (DPL)

## Rule 4 — No hidden UI adjudication
Output and interface code must not:

- suppress uncertainty
- quiet conflict
- infer truth posture
- introduce hidden importance ranking through non-fixed logic

## Rule 5 — No premature educational autonomy
Education scaffold may preserve boundaries.
It may not introduce autonomous steering or rich training behavior into MVP core.

## Rule 6 — Conservative handling of open zones
When operationalization is still open, implementation must be:

- minimal
- explicit
- reversible
- non-interpretive

## Rule 7 — No mixed-responsibility files
A file must not combine:

- taxonomy logic + policy logic
- output formatting + risk logic
- educational shell + adjudication logic

## Rule 8 — Contracts before convenience
Cross-module behavior must be defined through explicit contracts before convenience shortcuts are introduced.

## Rule 9 — Traceability preservation
Outputs must preserve enough traceability to understand how they were produced.

## Rule 10 — Small commits
Each commit should be:

- small
- role-specific
- readable
- reversible
