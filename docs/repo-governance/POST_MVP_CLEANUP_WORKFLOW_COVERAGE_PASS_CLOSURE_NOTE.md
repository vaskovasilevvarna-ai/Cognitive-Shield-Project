# Post-MVP Cleanup Workflow Coverage Pass Closure Note

Status: Closed — cleanup workflow coverage pass.

## Scope

This note closes the post-MVP cleanup workflow coverage pass.

The pass was limited to updating the Python Tests workflow so that pushes to the active cleanup branch trigger repository validation.

Cleanup branch added to workflow coverage:

- `post-mvp/repo-cleanup`

## Files Updated

- `.github/workflows/python-tests.yml`

## Files Added

- `docs/repo-governance/POST_MVP_CLEANUP_WORKFLOW_COVERAGE_PASS_CLOSURE_NOTE.md`

## What Changed

The Python Tests workflow push trigger was expanded from:

```yaml
on:
  push:
    branches:
      - active/mvp-foundation
      - main
