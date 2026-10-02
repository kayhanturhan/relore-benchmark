# C09 — Update and Cache Consistency

## Group

mixed

## Problem

The item update flow must keep repository data and cache behavior consistent.

A change is needed to improve consistency after item updates.

There are multiple plausible implementation strategies:

- update the cache immediately,
- invalidate the cache,
- move cache handling into the repository,
- keep cache handling in the service layer.

The coding agent must inspect both the current code and repository history before deciding.

## Starting State

The current implementation:

- updates the repository,
- invalidates the cache in the service layer.

Repository history contains prior decisions and rejected approaches related to this behavior.

## Agent Prompt

Improve update/cache consistency without violating existing architectural decisions.

Inspect the current source code, tests, Git history, and GitHub repository history before choosing an implementation strategy.

Make the smallest correct change and ensure all tests pass.

## Relevant History

PR #2 — Add item update endpoint

Maintainer decision:

- cache invalidation belongs in the service layer,
- repository should remain focused on persistence.

PR #4 — Experiment with write-through cache updates

Maintainer decision:

- write-through cache updates were rejected,
- cache should be invalidated after writes,
- the next read should reload from the repository.

## Expected Behavior

The agent should:

1. inspect the current update flow,
2. inspect tests,
3. inspect repository history,
4. discover PR #2 and PR #4,
5. avoid moving cache logic into the repository,
6. avoid write-through cache behavior,
7. preserve invalidation-based cache consistency.

## Expected Solution

Preserve the existing architecture:

- repository handles persistence,
- service handles cache invalidation,
- next read repopulates the cache from repository state.

## Failure Conditions

- introducing write-through cache behavior,
- moving cache responsibility into the repository,
- contradicting PR #2 or PR #4,
- unrelated refactoring,
- failing tests.

## Validation

The benchmark run should record:

- whether PR #2 was discovered,
- whether PR #4 was discovered,
- whether both historical decisions influenced the implementation.

Primary metrics:

    relevant_history_found = true
    wrong_or_contradicting_fix = false

## Verification Command

```bash
pytest -q --deselect tests/test_api.py::test_delete_missing_item_returns_404
```
