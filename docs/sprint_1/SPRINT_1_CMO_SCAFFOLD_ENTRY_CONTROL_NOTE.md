# Sprint 1 CMO Scaffold Entry Control Note

Status: Entry control note — Canonical Message Object (CMO) scaffold.

## Purpose

This note opens the Sprint 1 entry control review for the Canonical Message Object (CMO) scaffold.

The purpose is to prepare a bounded scaffold for the future Canonical Message Object (CMO) layer without introducing real Canonical Message Object (CMO) builder behavior, Message Decomposition Specification (MDS) behavior, downstream pipeline logic, taxonomy behavior, risk scoring or output generation.

This is a control note, not an implementation note.

## Baseline

The following Sprint 1 checkpoints are already closed:

- Shared Layer Pass;
- Message Decomposition Specification (MDS) Module Entry Control;
- Message Decomposition Specification (MDS) Contract Boundary Pass;
- Message Decomposition Specification (MDS) Schema Boundary Pass;
- Message Decomposition Specification (MDS) Validator Scaffold Pass;
- Message Decomposition Specification (MDS) Service Scaffold Pass;
- Message Decomposition Specification (MDS) Mapper Scaffold Pass;
- Sprint 1 Test Sanity Pass.

## Reason for Opening CMO Next

Canonical Message Object (CMO) is the next logical scaffold after Message Decomposition Specification (MDS) because it is the future stable carrier for structured message analysis.

The current order preserves the intended architecture:

Input message → Message Decomposition Specification (MDS) → Canonical Message Object (CMO) → downstream analysis layers.

Opening CMO as a scaffold before real MDS behavior helps prevent ad hoc data passing later.

## Current Admission Level

Canonical Message Object (CMO) is admitted only as a bounded scaffold.

Admitted now:

- package marker / folder inspection;
- README boundary;
- schema identity constants;
- contract boundary placeholder;
- narrow tests for scaffold identity and imports;
- closure note.

Not admitted now:

- real Canonical Message Object (CMO) builder behavior;
- conversion from Message Decomposition Specification (MDS) output to CMO;
- surface segment aggregation;
- claim graph construction;
- relation inference;
- context assembly;
- taxonomy labeling;
- risk scoring;
- confidence or uncertainty evaluation;
- downstream pipeline execution.

## Expected Folder

Expected future folder:

`src/cognitive_shield/core/canonical_message_object_cmo/`

If the folder does not exist, it may be opened as a package scaffold only.

## Recommended First Files

Recommended initial scaffold files:

1. `__init__.py`
2. `README.md`
3. `schemas.py`
4. `contracts.py`

Only the first one or two should be opened initially unless a separate control pass admits more.

## Future Non-Scope

The following must remain out of scope during the first CMO scaffold pass:

- real CMO construction;
- CMO validation behavior;
- graph building;
- semantic normalization;
- decomposition repair;
- taxonomy integration;
- risk integration;
- output integration;
- end-to-end pipeline execution.

## No-Drift Confirmation

This entry control pass must preserve:

- no real Message Decomposition Specification (MDS) behavior;
- no Canonical Message Object (CMO) builder behavior;
- no Agent Communication Protocol (ACP) routing;
- no taxonomy behavior;
- no label-to-verdict logic;
- no Taxonomy-to-Risk Mapping logic;
- no risk scoring;
- no governance behavior;
- no output rendering;
- no downstream pipeline logic;
- no broad implementation;
- no merge to `main`.

## Recommended Next Repo Step

The next repo step should inspect whether the folder exists:

`src/cognitive_shield/core/canonical_message_object_cmo/`

If it exists, inspect its contents.

If it does not exist, the next admissible step is to create the folder with a minimal `__init__.py` package marker and then add a bounded README.

## Verdict

Canonical Message Object (CMO) scaffold entry control is open.

Canonical Message Object (CMO) is admitted only as a bounded scaffold.

Real Canonical Message Object (CMO) builder behavior is not admitted.
