# Sprint 1 Bounded Implementation Entry Plan

Status: Draft v0.1 — bounded implementation entry document.

## Purpose

This document defines the controlled entry from Sprint 1 shared-layer stabilization into bounded implementation work.

The purpose is not to start broad implementation.

The purpose is to create a disciplined bridge from stable shared contracts and helpers toward the first admitted module-level implementation slice.

## Baseline

The following Sprint 1 foundation work is already closed:

- Shared input contracts pass;
- Shared analysis contracts pass;
- Shared taxonomy contracts pass;
- Shared risk and governance contracts pass;
- Shared output contracts pass;
- Base types pass;
- Traceability helpers pass;
- Common schema helpers pass;
- Base errors pass;
- System constants pass;
- Shared Layer Pass closure note.

The shared layer now has narrow unit tests and closure notes.

## Current Implementation State

Confirmed:

- shared contracts are present;
- shared helpers are present;
- shared constants are present;
- narrow unit tests exist for the shared layer;
- documentation-only Sprint 0 wording corrections were applied where needed;
- no downstream behavior has been introduced.

Not yet started:

- Message Decomposition Specification (MDS) behavior;
- Canonical Message Object (CMO) builder behavior;
- Agent Communication Protocol (ACP) routing;
- taxonomy behavior;
- risk scoring;
- Confidence / Uncertainty Model behavior;
- Internal Arbiter (IA) behavior;
- Decision Policy Layer (DPL) behavior;
- Shield Decision (SD) behavior;
- output rendering;
- pipeline execution.

## Bounded Implementation Principle

Sprint 1 implementation may proceed only in bounded slices.

Each slice must:

1. have a clear module boundary;
2. depend on already stable shared contracts;
3. avoid downstream behavior;
4. avoid hidden policy logic;
5. add tests only after the target shape is stable;
6. close with a short review note.

## First Candidate Layer

The first candidate implementation layer is:

Message Decomposition Specification (MDS)

Reason:

- MDS is the first analytical structuring layer;
- it consumes input message structures;
- it prepares downstream canonical structure;
- it must exist before downstream taxonomy, risk or output behavior can be meaningful.

## First Candidate Slice

Recommended first bounded implementation slice:

MDS entry scaffold and contract-aware validator shell.

This means:

- inspect the existing MDS module folder;
- confirm current placeholder state;
- add or refine only minimal module-level files if needed;
- avoid full decomposition logic;
- avoid implicit claim extraction behavior;
- avoid taxonomy classification;
- avoid risk scoring;
- avoid policy judgment.

## Admitted Work for First Slice

The first bounded MDS slice may include:

- MDS module inspection;
- README / placeholder alignment review;
- minimal public module contract review;
- minimal validator shell only if explicitly admitted;
- narrow tests for module presence or simple validator behavior only after the shape is stable;
- closure note for the MDS entry slice.

## Not Admitted in First Slice

The first bounded implementation slice must not include:

- real message decomposition behavior;
- implicit claim extraction;
- relation inference;
- framing taxonomy classification;
- risk scoring;
- taxonomy-to-risk mapping;
- confidence evaluation;
- Arbiter behavior;
- Decision Policy Layer behavior;
- Shield Decision behavior;
- output generation;
- full pipeline execution.

## Hard Safeguards

This implementation entry must preserve:

- no free-form coding;
- no mixed-responsibility files;
- no hidden policy logic;
- no label-to-verdict shortcut;
- no bypass of Confidence / Uncertainty Model;
- no bypass of Internal Arbiter (IA);
- no bypass of Decision Policy Layer (DPL);
- no premature output or UI adjudication;
- no broad test suite expansion;
- no merge to main.

## Recommended Next Control Pass

Before touching code, the next control pass should inspect:

`src/cognitive_shield/core/message_decomposition_specification_mds/`

The inspection should answer:

1. What files already exist?
2. Are there placeholders only?
3. Is there a README?
4. Is there an `__init__.py`?
5. Are there any premature implementation files?
6. What is the smallest safe implementation slice?

## Entry Verdict

Sprint 1 may move toward bounded implementation.

However, broad implementation is not admitted.

The next step is an MDS module entry control pass, not free-form coding.
