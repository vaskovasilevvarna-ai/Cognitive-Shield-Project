# Sprint 3 Routing-Adjacent Workflow Review

Status: Workflow coverage review — before admitting routing-adjacent Agent Communication Protocol (ACP) behavior.

## Purpose

This document records the Sprint 3 workflow coverage review required before opening routing-adjacent Agent Communication Protocol (ACP) behavior.

The purpose is to decide whether the current Python Tests workflow is sufficient before any Protocol Router boundary review or whether workflow expansion is required first.

This document does not admit Protocol Router behavior, ACP routing, ACPMessage dispatch, agent routing, agent orchestration, Analysis generation, runtime pipeline execution, downstream pipeline logic, taxonomy behavior, risk scoring, governance behavior, or output rendering.

This document does not admit implementation by itself.

## Baseline

Sprint 2 closed with boundaries.

Sprint 2 delivered the following controlled chain:

Input behavior nucleus  
→ Message Decomposition Specification (MDS) early structural stack  
→ bounded MDS DecompositionResult shell  
→ MDS-to-Canonical Message Object (CMO) boundary eligibility  
→ CMO minimal shell  
→ CMO structural contract  
→ CMO field envelope  
→ CMO minimal object  
→ CMO bounded construction candidate  
→ Agent Communication Protocol (ACP) boundary eligibility

Sprint 3 has completed:

- Sprint 3 Entry Control Pass
- Sprint 3 Workflow Coverage Review
- ACP minimal envelope boundary review
- ACP minimal envelope pass
- ACPBundle boundary review
- ACPBundle pass
- ACPMessage boundary review
- ACPMessage pass
- ACP Schema Validator boundary review
- ACP Schema Validator pass
- ACP Scope Guard boundary review
- ACP Scope Guard pass

Current validation status:

- Python Tests workflow: GREEN
- Current Python Tests workflow: sufficient for bounded structural ACP behavior
- Workflow expansion checkpoint: required before routing-adjacent or Analysis-adjacent behavior

Current ACP state:

ACP boundary eligibility  
→ ACP minimal envelope  
→ ACPBundle  
→ ACPMessage  
→ ACP Schema Validator  
→ ACP Scope Guard

Current restricted areas:

- ACP routing: HOLD
- ACPMessage dispatch: HOLD
- agent routing: HOLD
- agent orchestration: HOLD
- Protocol Router behavior: HOLD
- Contradiction Registrar behavior: HOLD
- Uncertainty Propagator behavior: HOLD
- Synthesis Exporter behavior: HOLD
- Analysis generation: NOT STARTED
- runtime pipeline execution: NOT ADMITTED
- downstream pipeline logic: NOT ADMITTED
- taxonomy behavior: NOT STARTED
- risk scoring: NOT STARTED
- governance behavior: NOT STARTED
- output rendering: NOT STARTED
- merge to `main`: NOT PERFORMED

## Review Question

Is the existing Python Tests workflow sufficient before opening Protocol Router boundary review?

## Verdict

Verdict:

`CURRENT PYTHON TESTS WORKFLOW IS SUFFICIENT FOR PROTOCOL ROUTER BOUNDARY REVIEW — NOT SUFFICIENT FOR ROUTING IMPLEMENTATION WITHOUT ADDITIONAL REVIEW`

The current Python Tests workflow is sufficient to open a Protocol Router boundary review document.

It is also sufficient for a future minimal Protocol Router implementation only if that implementation remains:

- routing-readiness-only;
- scope-guard-derived;
- structural only;
- non-dispatching;
- non-orchestrating;
- non-analytical;
- non-runtime;
- not actual ACP routing;
- not ACPMessage dispatch;
- not agent routing;
- not Analysis generation;
- not downstream pipeline logic.

However, before any actual routing decision, dispatch target, agent instruction, runtime routing behavior, or Analysis-adjacent behavior is implemented, workflow coverage must be reviewed again and likely expanded.

## Why Workflow Expansion Is Not Required Before Boundary Review

The next recommended step is not direct routing.

The next recommended step is:

- Protocol Router boundary review

A boundary review is documentation and control logic only.

It does not add Python behavior.

It does not require workflow expansion.

## Why Workflow Expansion Is Not Required Before Minimal Router Readiness Behavior

If later admitted, the first Protocol Router implementation must remain a minimal routing-readiness check only.

It may check whether an ACP Scope Guard result has:

- `acp_scope_allowed`
- required bounded fields
- preserved decomposition result
- preserved field envelope

It must not create:

- routing decision
- dispatch target
- agent route
- agent instruction
- analysis bundle
- runtime pipeline event

Such bounded structural behavior can still be covered by the existing Python Tests workflow, provided tests explicitly verify absence of forbidden fields.

## Why Workflow Expansion Is Required Before Real Routing

Real routing is a qualitative step beyond the current Sprint 3 chain.

Real routing may introduce:

- route selection;
- agent targeting;
- dispatch semantics;
- orchestration pressure;
- downstream flow expectations;
- possible Analysis-adjacent coupling;
- failure modes involving wrong agent path, premature dispatch, and implicit pipeline execution.

Therefore, real routing requires a later workflow expansion review before implementation.

## Current Workflow Coverage Is Sufficient For

The current Python Tests workflow is sufficient for:

- Python syntax validation;
- import validation;
- unit test execution;
- MDS structural tests;
- CMO bounded pre-ACP tests;
- ACP boundary eligibility tests;
- ACP minimal envelope tests;
- ACPBundle tests;
- ACPMessage tests;
- ACP Schema Validator minimal tests;
- ACP Scope Guard minimal tests;
- future Protocol Router boundary review;
- future minimal Protocol Router readiness behavior if separately admitted and tested as non-routing.

## Current Workflow Coverage Is Not Sufficient For

The current workflow is not sufficient by itself for:

- real ACP routing;
- ACPMessage dispatch;
- agent routing;
- agent orchestration;
- dispatch target creation;
- agent instruction creation;
- Analysis generation;
- runtime pipeline execution;
- downstream pipeline logic.

Before those behaviors, the project must perform a new workflow coverage review and consider expanding validation.

## Expansion Triggers

A workflow expansion review is required before admitting any of the following:

- actual routing decision creation;
- dispatch target creation;
- agent instruction creation;
- ACPMessage dispatch;
- agent routing;
- agent orchestration;
- Analysis generation;
- runtime pipeline execution;
- downstream pipeline logic;
- cross-module integration behavior beyond structural wrapping and status checks.

Potential future workflow additions may include:

- ACP-specific test grouping;
- contract tests;
- no-forbidden-field regression tests;
- routing no-dispatch tests;
- package-level integration smoke tests;
- stricter import checks;
- static formatting or linting;
- schema validation tests;
- boundary regression tests.

This review does not require those additions now.

## Recommended Next Gate

Recommended next repo document:

- `docs/sprint_3/SPRINT_3_PROTOCOL_ROUTER_BOUNDARY_REVIEW.md`

That document should decide whether to admit a minimal Protocol Router boundary.

It must not admit:

- real ACP routing;
- ACPMessage dispatch;
- agent routing;
- agent orchestration;
- dispatch target creation;
- agent instruction creation;
- Analysis generation;
- runtime pipeline execution;
- downstream pipeline logic.

## Not Admitted

The following remain not admitted after this workflow review:

- ACP routing;
- ACPMessage dispatch;
- agent routing;
- agent orchestration;
- real Protocol Router behavior;
- routing decision creation;
- dispatch target creation;
- agent instruction creation;
- Contradiction Registrar behavior;
- Uncertainty Propagator behavior;
- Synthesis Exporter behavior;
- Analysis generation;
- EvidenceAnalysisOutput generation;
- NarrativeAnalysisOutput generation;
- CognitiveAnalysisOutput generation;
- Analysis bundle generation;
- taxonomy behavior;
- label-to-verdict logic;
- risk scoring;
- confidence or uncertainty evaluation;
- governance behavior;
- output rendering;
- runtime pipeline execution;
- downstream pipeline logic;
- merge to `main`.

Also still not admitted:

- implicit claim inference;
- hidden claim reconstruction;
- truth assessment;
- evidence assessment;
- framing extraction;
- relation inference;
- semantic interpretation beyond admitted MDS-local, CMO-local, and ACP structural containers.

## Required Safeguards

The next Protocol Router boundary review must preserve the following safeguards:

1. Do not admit real routing by default.
2. Do not admit dispatch behavior.
3. Do not create dispatch targets.
4. Do not create agent instructions.
5. Do not call Analysis modules.
6. Do not trigger runtime pipeline execution.
7. Do not introduce downstream pipeline logic.
8. Preserve the ACP Scope Guard result.
9. Preserve the original bounded MDS DecompositionResult.
10. Preserve the existing CMO field envelope.
11. Preserve no-forbidden-field testing discipline.
12. Require another workflow coverage review before real routing implementation.

## No-Drift Confirmation

Confirmed:

- Sprint 2 closure state remains preserved.
- Sprint 3 is open and controlled.
- ACP boundary eligibility remains eligibility-only.
- ACP minimal envelope remains envelope-only.
- ACPBundle remains bundle-only.
- ACPMessage remains message-only.
- ACP Schema Validator remains schema-validation-only.
- ACP Scope Guard remains scope-check-only.
- Protocol Router behavior remains on HOLD.
- ACP routing remains on HOLD.
- ACPMessage dispatch remains on HOLD.
- agent orchestration remains on HOLD.
- Analysis generation remains on HOLD.
- taxonomy behavior has not started.
- risk scoring has not started.
- governance behavior has not started.
- output rendering has not started.
- runtime pipeline execution has not started.
- downstream pipeline logic has not started.
- merge to `main` has not been performed.

## Verdict Summary

Routing-adjacent workflow review: COMPLETE.

Current Python Tests workflow: SUFFICIENT FOR PROTOCOL ROUTER BOUNDARY REVIEW.

Current Python Tests workflow: SUFFICIENT FOR FUTURE MINIMAL ROUTER READINESS ONLY IF NON-ROUTING.

Workflow expansion: REQUIRED BEFORE REAL ROUTING, DISPATCH, AGENT ORCHESTRATION, ANALYSIS, RUNTIME, OR DOWNSTREAM BEHAVIOR.

Recommended next document:

- `SPRINT_3_PROTOCOL_ROUTER_BOUNDARY_REVIEW.md`

ACP routing: HOLD.

ACPMessage dispatch: HOLD.

Protocol Router implementation: HOLD until boundary review.

Analysis generation: HOLD.

Runtime pipeline execution: NOT ADMITTED.

Downstream pipeline logic: NOT ADMITTED.
