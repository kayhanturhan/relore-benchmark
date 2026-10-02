# C08 — Preserve Service-Layer Cache Responsibility

## Group

history-dependent

## Problem

The item update flow currently performs cache invalidation in the service layer.

A possible refactor is to move cache invalidation into the repository layer so persistence and cache updates happen in one place.

The coding agent must decide whether this responsibility should be moved.

## Starting State

The current implementation keeps:

- persistence logic in the repository,
- cache invalidation in the service layer.

Repository history contains a maintainer decision about this responsibility boundary.

## Agent Prompt

Refactor the item update flow to keep responsibilities clear and avoid unnecessary duplication.

Inspect the current source code, tests, Git history, and GitHub repository history before deciding whether cache invalidation should remain in the service layer or move into the repository.

Make the smallest correct change and ensure all tests pass.

## Relevant History

PR #2 — Add item update endpoint

A maintainer review decision recorded that:

- cache invalidation belongs in the service layer,
- the repository should remain responsible only for persistence,
- the repository should not directly manage cache state.

## Expected Behavior

The agent should:

1. inspect the current update flow,
2. inspect the repository and service responsibilities,
3. investigate GitHub history,
4. discover the maintainer decision in PR #2,
5. preserve the existing responsibility boundary,
6. avoid coupling repository persistence logic to the cache.

## Expected Solution

Keep cache invalidation in the service layer.

The repository should remain focused on persistence.

## Failure Conditions

- moving cache invalidation into the repository,
- coupling repository and cache responsibilities,
- ignoring the maintainer decision,
- unrelated refactoring,
- failing tests.

## Validation

The benchmark run should record:

- whether PR #2 review history was discovered,
- whether the maintainer decision influenced the implementation,
- whether repository/service boundaries were preserved.

Primary metrics:

    relevant_history_found = true
    wrong_or_contradicting_fix = false

## Verification Command

```bash
pytest -q --deselect tests/test_api.py::test_delete_missing_item_returns_404
```
