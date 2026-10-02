# C03 — Incorrect HTTP Status for Missing Item Deletion

## Group

source-only

## Problem

Deleting a non-existent item returns the wrong HTTP status.

## Starting State

The bug exists directly in the API route behavior.

Repository history is not required.

## Agent Prompt

Fix the HTTP behavior when deleting an item that does not exist.

Inspect the implementation and tests, make the smallest correct change, and ensure all tests pass.

## Relevant History

None.

## Expected Behavior

The agent should:

1. inspect the delete endpoint,
2. inspect the failing API test,
3. identify the incorrect HTTP response behavior,
4. implement a minimal fix,
5. run the tests.

## Expected Solution

Deleting a missing item should return HTTP 404.

## Failure Conditions

- missing items still return 204,
- valid deletes stop working,
- unrelated API behavior changes,
- tests fail.

## Validation

The dedicated API test and the full test suite must pass.

## Verification Command

```bash
pytest -q tests/test_api.py::test_delete_missing_item_returns_404
```
