# Message Decomposition Specification (MDS)

Status: Sprint 1 bounded scaffold.

## Purpose

This folder contains the future implementation area for the Message Decomposition Specification (MDS).

MDS is the bounded, claim-centric, multi-layer structuring layer that prepares input messages for later analysis.

Its role is to transform an input message into explicit analytical structures without performing taxonomy classification, risk scoring, policy judgment or output rendering.

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
- `service.py`
- `mapper.py`

These files should be opened only through separate control passes.

## Current Non-Scope

This module must not yet implement:

- real message decomposition behavior;
- implicit claim extraction;
- relation inference;
- framing taxonomy classification;
- taxonomy labeling;
- risk scoring;
- confidence or uncertainty evaluation;
- Internal Arbiter (IA) behavior;
- Decision Policy Layer (DPL) behavior;
- Shield Decision (SD) behavior;
- output generation;
- end-to-end pipeline execution.

## Boundary Rules

MDS must preserve:

- explicit versus implicit content discipline;
- local, relational and global context preservation;
- decomposition uncertainty as a first-class signal;
- no taxonomy classification;
- no risk scoring;
- no policy judgment;
- no downstream pipeline shortcuts.

## Integration Position

Expected future position:

Input message → MDS → Canonical Message Object (CMO) → downstream analysis layers.

During Sprint 1, this README does not authorize full implementation of that flow.

## Verdict

MDS is open as a bounded scaffold.

Broad MDS implementation is not yet admitted.
