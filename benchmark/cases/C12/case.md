# C12 — Competing Implementation Decisions

## Group

mixed

## Problem

A new item update flow needs to support:

- case-insensitive item-name handling,
- correct cache consistency,
- clear separation of responsibilities.

Several seemingly reasonable implementation strategies exist.

For example:

- lowercase item names before persistence,
- update the cache directly after writes,
- move cache handling into the repository,
- keep cache invalidation in the service layer,
- preserve display casing and use a separate normalized comparison value.

The coding agent must evaluate the current implementation together with relevant repository history before choosing a solution.

## Starting State

The current main branch:

- preserves item-name display casing,
- keeps persistence logic in the repository,
- keeps cache invalidation in the service layer,
- invalidates cache after successful item updates.

Repository history contains accepted and rejected implementation decisions related to these behaviors.

## Agent Prompt

Improve the item update flow so that it supports case-insensitive item-name handling while preserving cache consistency and existing architectural boundaries.

Inspect the current source code, tests, Git history, and GitHub repository history before choosing an implementation strategy.

Do not repeat previously rejected approaches.

Make the smallest correct change and ensure all tests pass.

## Relevant History

### PR #2 — Add item update endpoint

Maintainer decision:

- repository remains responsible for persistence,
- cache invalidation belongs in the service layer.

### PR #4 — Experiment with write-through cache updates

Rejected approach:

- update cache directly after successful writes.

Maintainer decision:

- invalidate cache after writes,
- reload from repository on the next read.

### PR #8 — Experiment with lowercase item name persistence

Rejected approach:

- persist lowercased item names.

Regression:

- display casing was lost.

Maintainer decision:

- preserve original display casing,
- use a separate normalized comparison value for case-insensitive behavior.

## Expected Behavior

The agent should:

1. inspect the current code and tests,
2. investigate relevant GitHub history,
3. discover PR #2,
4. discover PR #4,
5. discover PR #8,
6. combine the historical decisions correctly,
7. avoid write-through caching,
8. avoid repository-level cache management,
9. avoid persisted lowercase names,
10. preserve the existing architectural boundaries.

## Expected Solution

A correct solution should preserve these rules:

- original item-name casing remains stored,
- case-insensitive comparison uses a separate normalized representation,
- repository remains focused on persistence,
- service remains responsible for cache invalidation,
- successful writes invalidate the cache,
- subsequent reads repopulate the cache from repository state.

## Failure Conditions

- persisting lowercase item names,
- introducing write-through cache updates,
- moving cache management into the repository,
- contradicting previous maintainer decisions,
- ignoring relevant repository history,
- unrelated large refactoring,
- failing tests.

## Validation

The benchmark run should record:

- whether PR #2 was discovered,
- whether PR #4 was discovered,
- whether PR #8 was discovered,
- whether the agent combined the decisions correctly,
- whether rejected approaches were avoided,
- whether repository/service boundaries were preserved.

Primary metrics:

    relevant_history_found = true
    wrong_or_contradicting_fix = false
    

## Verification Command

```bash
pytest -q
```
