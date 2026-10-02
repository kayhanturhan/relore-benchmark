# C04 — Stale Cache Returns Deleted Item

## Group

source-only

## Problem

An item that has already been loaded into cache may still be returned even after the repository no longer contains it.

## Starting State

The bug exists directly in the cache/service behavior.

Repository history is not required.

## Agent Prompt

Fix the stale-cache behavior so that deleted or missing items are not returned from cache incorrectly.

Inspect the implementation and tests, make the smallest correct change, and ensure all tests pass.

## Relevant History

None.

## Expected Behavior

The agent should:

1. inspect the service cache lookup behavior,
2. inspect the failing test,
3. identify the stale-cache problem,
4. implement a minimal fix,
5. run the tests.

## Expected Solution

The service must not return stale cached data when the repository no longer contains the item.

## Failure Conditions

- stale cached items are still returned,
- valid cached reads stop working,
- unrelated behavior changes,
- tests fail.

## Validation

The dedicated stale-cache test and the full test suite must pass.

## Verification Command

```bash
pytest -q tests/test_service.py::test_get_item_does_not_return_stale_cached_item
```
