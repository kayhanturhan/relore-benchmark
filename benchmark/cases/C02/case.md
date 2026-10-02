# C02 — Item Name Validation Edge Case

## Group

source-only

## Problem

Item names containing only whitespace are currently accepted.

## Starting State

The bug exists in the validation model.

Repository history is not required.

## Agent Prompt

Prevent item names that contain only whitespace from being accepted.

Inspect the implementation and tests, make the smallest correct change, and ensure all tests pass.

## Relevant History

None.

## Expected Behavior

The agent should:

1. inspect the Pydantic model,
2. inspect the failing validation test,
3. identify that `min_length=1` does not reject whitespace-only strings,
4. implement a minimal validation fix,
5. run the tests.

## Expected Solution

Whitespace-only item names should be rejected.

## Failure Conditions

- whitespace-only names are still accepted,
- valid names are rejected,
- unrelated behavior changes,
- tests fail.

## Validation

The dedicated validation test and full test suite must pass.

## Verification Command

```bash
pytest -q tests/test_api.py::test_rejects_whitespace_only_name
```
