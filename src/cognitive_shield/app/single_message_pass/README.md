# Single Message Pass

## Purpose
This package contains the minimal Sprint 0 shell for the single-message end-to-end analytical pass.

## Current scope
Current files:
- `__init__.py`
- `pipeline.py`
- `dependencies.py`
- `run.py`

## Sprint 0 role
This package is a bounded shell only.

It does not yet implement:
- real orchestration
- module wiring
- production dependency injection
- integration with tests
- full execution flow

## Next expected use
This package will later serve as the narrow MVP nucleus for:

input text -> analysis pipeline shell -> shared contracts -> bounded output
