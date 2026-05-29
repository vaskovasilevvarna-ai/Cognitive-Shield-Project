# Core Input

Status: Sprint 1 bounded scaffold.

## Purpose

This folder contains the future implementation area for core Input handling.

The Input layer is intended to become the entry point for raw text, transcript, or message input before Message Decomposition Specification (MDS).

Its role is to prepare a future normalized input envelope without performing analysis, decomposition, taxonomy classification, risk scoring, governance decisions, output rendering, or downstream pipeline execution.

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

- `schemas.py`
- `contracts.py`
- `validator.py`
- `normalizer.py`

These files should be opened only through separate control passes.

## Current Non-Scope

This module must not yet implement:

- real input normalization;
- transcript parsing;
- language routing;
- source-type inference;
- ingestion pipeline behavior;
- Message Decomposition Specification (MDS) behavior;
- Canonical Message Object (CMO) construction;
- Agent Communication Protocol (ACP) routing;
- Analysis behavior;
- taxonomy behavior;
- risk scoring;
- governance behavior;
- output generation;
- end-to-end pipeline execution.

## Boundary Rules

Input must preserve:

- raw input boundary;
- explicit language field discipline;
- no hidden analysis;
- no decomposition behavior;
- no downstream pipeline shortcuts.

## Integration Position

Expected future position:

Raw input → Input envelope → Message Decomposition Specification (MDS).

During Sprint 1, this README does not authorize full implementation of that flow.

## Verdict

Input is open as a bounded scaffold.

Real input processing behavior is not yet admitted.
