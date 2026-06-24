# Working Protocol — Cognitive Shield

## Purpose

This document defines the lightweight working protocol for the Cognitive Shield project after the closure of the Functional Local Prototype Engine phase.

Its purpose is to reduce chat overload while preserving architectural discipline.

---

## Core Working Model

The project now follows this working model:

```text
Repo = source of truth
Chat = working station
Session Starter = short index
```

The chat should not be used as the only memory of the project.

Project state, phase status, architecture references, proof gates, and working rules should increasingly live in repository documents.

---

## Session Mode

Default mode for future work:

```text
NO FULL CONTEXT MODE
```

Meaning:

* do not repeat the full architecture unless requested
* work only on the current gate or slice
* use repository documents as source references
* keep session starters short
* avoid large Markdown outputs unless explicitly needed
* split large documents into controlled parts when necessary

---

## Branch Discipline

`main` is never edited directly.

Normal flow:

```text
create branch from main
change only approved files
commit to branch
open pull request
wait for checks
merge only if GREEN
delete temporary branch after merge
```

Temporary branches may be deleted after merge.

Archive branches must not be deleted unless explicitly reviewed.

Protected archive branches:

```text
archive/gemini-ssa-integration
archive/mvp-foundation-pre-merge
```

---

## GitHub Tooling

Preferred tools:

```text
GitHub normal UI = create files, upload files, commit, open PR, merge, delete branch
github.dev = tree review and branch orientation
ChatGPT = planning, file packs, recovery guidance, verification discipline
```

The user is not expected to operate like a professional developer.

Instructions should be step-by-step and should identify the active branch clearly.

---

## Slice Discipline

A normal slice should be small.

Preferred scope:

```text
1–3 files
one purpose
one branch
one PR
one verification cycle
```

Avoid mixed batches.

Do not combine:

```text
functional implementation
documentation rewrite
workflow edits
cleanup
architecture redesign
```

in the same slice unless explicitly approved.

---

## Verification Discipline

Every slice must preserve:

```text
Python Tests: GREEN
JSON Validation Shield: GREEN
no workflow drift
no direct main edit
no architecture boundary violation
```

If checks turn RED:

```text
do not merge
read the first real error
identify exact cause
make the smallest fix commit
rerun checks
merge only after GREEN
```

Old historical RED runs may remain in Actions history. They are not active problems if later `main` runs are GREEN.

---

## Coding Boundaries

Do not introduce fake analytical behavior.

Forbidden unless the real corresponding layer exists and is tested:

```text
fake risk_score
fake confidence
fake verdict
fake Shield Decision
fake Internal Arbiter decision
fake Decision Policy Layer decision
fake taxonomy classification
fake education behavior
```

Explicit non-implementation markers are allowed and required when functionality is not implemented.

Valid boundary markers include:

```text
analysis_status = not_implemented
risk_status = not_evaluated
confidence_status = not_computed
verdict_status = not_produced
```

---

## Documentation Discipline

Documentation should be functional and tied to a gate or slice.

Avoid during ordinary implementation work:

```text
large conceptual documents
root public-facing rewrites
broad architecture expansion
README rewrite
white paper rewrite
manifesto rewrite
workflow documentation drift
```

Large architecture documents require a separate documentation gate.

---

## Root Public Documents

Do not rewrite root public-facing documents without an explicit gate.

Root public-facing documents include:

```text
README.md
CONTRIBUTING.md
CORE_PRINCIPLES.md
ETHICAL_GUIDELINES.md
MANIFESTO.md
THREAT_PATTERN_LIBRARY.md
WHITE_PAPER.md
```

---

## Workflow Files

Do not change GitHub Actions workflows unless a workflow review gate explicitly approves it.

Workflow coverage should be reviewed before or during later Sprint 3 / Sprint 4 style entry gates, or before phases that add new testable layers.

---

## Chat Load Control

To reduce chat instability:

* keep session starters short
* avoid pasting full architecture repeatedly
* use repository state documents instead
* use one gate per session when possible
* split large documents into parts
* stop and start a new chat after major closed checkpoints
* request concise mode when tired or when GitHub work is procedural

If the chat becomes slow or unstable, stop at the next safe checkpoint and open a new session with a short starter.

---

## Standard Session Starter Pattern

Use a short starter like:

```text
Активирай проект Когнитивен Щит.

NO FULL CONTEXT MODE.

Source of truth:
- docs/project-state/CURRENT_PROJECT_STATE.md
- docs/project-state/WORKING_PROTOCOL.md
- relevant phase gate document

Task today:
<one gate or one slice>

Do not start code until branch, file scope, verification, and rollback are defined.
```

---

## Recovery Discipline

When a mistake happens:

```text
stop
identify branch
identify changed files
check PR direction
check latest relevant workflow
do not panic
do not merge RED
do not create reverse PR
repair with smallest safe step
```

Common GitHub rule:

```text
base = where changes will merge into
compare = branch where changes come from
```

Correct PR direction normally:

```text
base: main
compare: feature-branch
```

---

## Gate Discipline

No new phase starts automatically.

Every new phase needs a gate with:

```text
goal
branch name
file scope
what must not change
verification
rollback
admission / hold verdict
```

---

## Current Recommended Next Gates

After Project Context Compression Foundation, possible next gates are:

```text
Architecture Master Reference Gate
Local Laptop Testing Gate
Minimal CLI Productization Gate
First Real Decomposition Slice Gate
```

Recommended sequence:

```text
1. finish context compression foundation
2. decide whether to add architecture master reference to docs
3. run Local Laptop Testing Gate
4. only then consider CLI productization or first real decomposition
```

---

## Final Rule

Implementation must serve the fixed architecture.

The project must never trade epistemic discipline for speed.
