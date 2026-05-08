# Agent Communication Protocol (ACP)

Status: Sprint 1 bounded scaffold.

## Purpose

This folder contains the future implementation area for the Agent Communication Protocol (ACP).

Agent Communication Protocol (ACP) is intended to become the bounded protocol-governance layer that organizes disciplined communication between specialized analysis components.

Its role is to preserve typed exchange, scope boundaries, uncertainty signals, contradiction visibility and synthesis discipline without performing final adjudication, risk scoring, policy judgment or output rendering.

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
- `router.py`
- `scope_guard.py`
- `schema_validator.py`
- `contradiction_registrar.py`
- `uncertainty_propagator.py`
- `synthesis_exporter.py`

These files should be opened only through separate control passes.

## Current Non-Scope

This module must not yet implement:

- real protocol routing;
- agent orchestration;
- agent-to-agent messaging;
- Scope Guard behavior;
- Schema Validator behavior;
- Contradiction Registrar behavior;
- Uncertainty Propagator behavior;
- Synthesis Exporter behavior;
- analysis execution;
- risk scoring;
- confidence or uncertainty evaluation;
- Internal Arbiter (IA) behavior;
- Decision Policy Layer (DPL) behavior;
- Shield Decision (SD) behavior;
- output generation;
- end-to-end pipeline execution.

## Boundary Rules

Agent Communication Protocol (ACP) must preserve:

- typed communication boundaries;
- mandate-constrained exchange;
- uncertainty visibility;
- contradiction preservation;
- scope discipline;
- no final adjudication;
- no risk scoring;
- no policy judgment;
- no downstream pipeline shortcuts.

## Integration Position

Expected future position:

Canonical Message Object (CMO) → Agent Communication Protocol (ACP) → analysis coordination / downstream analysis layers.

During Sprint 1, this README does not authorize full implementation of that flow.

## Verdict

Agent Communication Protocol (ACP) is open as a bounded scaffold.

Real ACP routing, orchestration and protocol behavior are not yet admitted.
