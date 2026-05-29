# Sprint 4 Workflow Update Boundary Review

Status: Boundary review — before admitting Python Tests workflow update.

## Purpose

This document records the Sprint 4 boundary review for updating the Python Tests GitHub Actions workflow.

The purpose is to decide whether the repository may update `.github/workflows/python-tests.yml` so that Sprint 4 MVP proof tests, smoke tests, contract tests, and all admitted unit tests are included in the GREEN / RED validation signal.

This document does not admit MVP proof implementation by itself.

This document does not admit real Agent Communication Protocol (ACP) routing.

This document does not admit ACPMessage dispatch, agent routing, agent orchestration, Analysis generation, runtime pipeline execution, downstream pipeline logic, taxonomy behavior, risk scoring, governance behavior, or output rendering.

## Baseline

Sprint 4 has completed:

- Sprint 4 Entry Control Pass
- Sprint 4 MVP Completion Control Review
- Sprint 4 Routing Preparation Review
- Sprint 4 Workflow Expansion Review
- Sprint 4 Test Structure Expansion Boundary Review
- Sprint 4 Test Structure Expansion Pass
- Sprint 4 Workflow Discovery Check

Current validation status:

- Python Tests workflow: GREEN
- Smoke-test scaffold: CLOSED
- `tests/smoke/README.md`: ADDED
- `tests/smoke/__init__.py`: ADDED
- MVP smoke test implementation: HOLD
- MVP functional proof implementation: HOLD
- Real ACP routing: NOT ADMITTED
- Routing implementation: HOLD
- ACPMessage dispatch: HOLD
- Analysis generation: HOLD
- runtime pipeline execution: NOT ADMITTED
- downstream pipeline logic: NOT ADMITTED
- merge to `main`: NOT PERFORMED

## Discovery Result

The current `.github/workflows/python-tests.yml` uses an explicit allow-list of test files.

The workflow does not currently run the full test suite with a broad command such as:

- `python -m pytest`
- `pytest`

The workflow currently runs a command shaped like:

```yaml
python -m pytest \
  tests/unit/test_input_normalizer.py \
  tests/unit/test_input_validator.py \
  ...
