# Sprint 1 ACP Scaffold Entry Control Note

Status: Entry control note — Agent Communication Protocol (ACP) scaffold.

## Purpose

This note opens the Sprint 1 entry control review for the Agent Communication Protocol (ACP) scaffold.

The purpose is to prepare a bounded scaffold for the future Agent Communication Protocol (ACP) layer without introducing real agent routing, orchestration, contradiction registration, uncertainty propagation, synthesis export, downstream analysis behavior, governance behavior or pipeline execution.

This is a control note, not an implementation note.

## Baseline

The following Sprint 1 checkpoints are already closed:

- Shared Layer Pass;
- Message Decomposition Specification (MDS) bounded scaffold;
- Canonical Message Object (CMO) bounded scaffold;
- Sprint 1 Midpoint Matrix;
- Sprint 1 Test Sanity Pass.

## Reason for Opening ACP Next

Agent Communication Protocol (ACP) is the next logical scaffold after Message Decomposition Specification (MDS) and Canonical Message Object (CMO), because it will later govern disciplined exchange between specialized analysis components.

The current order preserves the intended architecture:

Input message → Message Decomposition Specification (MDS) → Canonical Message Object (CMO) → Agent Communication Protocol (ACP) / analysis coordination → downstream analysis layers.

Opening ACP as a scaffold now helps prevent later ad hoc communication between modules.

## Current Admission Level

Agent Communication Protocol (ACP) is admitted only as a bounded scaffold.

Admitted now:

- package marker / folder inspection;
- README boundary;
- schema identity constants;
- contract boundary placeholder;
- narrow tests for scaffold identity and imports;
- closure notes.

Not admitted now:

- real protocol routing;
- agent orchestration;
- Scope Guard behavior;
- Schema Validator behavior;
- Contradiction Registrar behavior;
- Uncertainty Propagator behavior;
- Synthesis Exporter behavior;
- analysis execution;
- risk scoring;
- governance decisions;
- output generation;
- end-to-end pipeline execution.

## Expected Folder

Expected future folder:

`src/cognitive_shield/core/agent_communication_protocol_acp/`

If the folder does not exist, it may be opened as a package scaffold only.

## Recommended First Files

Recommended initial scaffold files:

1. `__init__.py`
2. `README.md`
3. `schemas.py`
4. `contracts.py`

Only the first one or two should be opened initially unless a separate control pass admits more.

## Future Non-Scope

The following must remain out of scope during the first ACP scaffold pass:

- real routing;
- real agent-to-agent messaging;
- protocol state machine;
- contradiction registration behavior;
- uncertainty propagation behavior;
- synthesis export behavior;
- orchestration logic;
- analysis behavior;
- risk behavior;
- governance behavior;
- output behavior;
- end-to-end pipeline behavior.

## No-Drift Confirmation

This entry control pass must preserve:

- no real Agent Communication Protocol (ACP) behavior;
- no routing engine;
- no agent orchestration;
- no Message Decomposition Specification (MDS) behavior expansion;
- no Canonical Message Object (CMO) behavior expansion;
- no taxonomy behavior;
- no label-to-verdict logic;
- no risk scoring;
- no governance behavior;
- no output rendering;
- no downstream pipeline logic;
- no broad implementation;
- no merge to `main`.

## Recommended Next Repo Step

The next repo step should inspect whether the folder exists:

`src/cognitive_shield/core/agent_communication_protocol_acp/`

If it exists, inspect its contents.

If it does not exist, the next admissible step is to create the folder with a minimal `__init__.py` package marker and then add a bounded README.

## Verdict

Agent Communication Protocol (ACP) scaffold entry control is open.

Agent Communication Protocol (ACP) is admitted only as a bounded scaffold.

Real Agent Communication Protocol (ACP) routing, orchestration and protocol behavior are not admitted.
