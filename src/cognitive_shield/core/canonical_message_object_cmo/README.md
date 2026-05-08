# Canonical Message Object (CMO)

Status: Sprint 1 bounded scaffold.

## Purpose

This folder contains the future implementation area for the Canonical Message Object (CMO).

The Canonical Message Object (CMO) is intended to become the stable structured carrier between Message Decomposition Specification (MDS) outputs and downstream analysis layers.

Its role is to preserve structured analytical units, traceability, context, uncertainty and relation surfaces without performing taxonomy classification, risk scoring, policy judgment or output rendering.

## Sprint 1 Role

During Sprint 1, this module is opened only as a bounded scaffold.

The current role is to establish:

- module boundary;
- package identity;
- future file map;
- implementation non-scope;
- no-drift constraints.

## Intended Future Files

Expected future files:

- `contracts.py`
- `schemas.py`
- `validator.py`
- `builder.py`
- `mapper.py`

These files should be opened only through separate control passes.

## Current Non-Scope

This module must not yet implement:

- real Canonical Message Object (CMO) construction;
- Message Decomposition Specification (MDS) output conversion;
- surface segment aggregation;
- claim graph construction;
- relation inference;
- context assembly;
- taxonomy labeling;
- risk scoring;
- confidence or uncertainty evaluation;
- Internal Arbiter (IA) behavior;
- Decision Policy Layer (DPL) behavior;
- Shield Decision (SD) behavior;
- output generation;
- end-to-end pipeline execution.

## Boundary Rules

Canonical Message Object (CMO) must preserve:

- structured analytical units;
- traceability;
- local, relational and global context surfaces;
- uncertainty visibility;
- conflict preservation;
- no taxonomy classification;
- no risk scoring;
- no policy judgment;
- no downstream pipeline shortcuts.

## Integration Position

Expected future position:

Input message → Message Decomposition Specification (MDS) → Canonical Message Object (CMO) → downstream analysis layers.

During Sprint 1, this README does not authorize full implementation of that flow.

## Verdict

Canonical Message Object (CMO) is open as a bounded scaffold.

Real Canonical Message Object (CMO) builder behavior is not yet admitted.
