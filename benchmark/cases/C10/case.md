# C10 — Name Normalization During Updates

## Group

mixed

## Problem

Item names may contain leading or trailing whitespace during update operations.

The current main branch does not normalize those values before persistence.

A fix for the same behavior already exists in repository history.

## Starting State

The main branch still persists item names exactly as provided.

Repository history contains an open pull request with a complete normalization implementation.

## Agent Prompt

Fix item-name normalization for update operations.

Inspect the current source code, tests, Git history, and GitHub repository history before deciding whether a new implementation is required.

Avoid duplicating existing work.

## Relevant History

PR #5 — Normalize item names before persistence

PR #5 contains:

- normalization during item creation,
- normalization during item updates,
- automated tests.

PR #5 remains open and unmerged.

## Expected Behavior

The agent should:

1. inspect the repository update behavior,
2. inspect relevant tests,
3. inspect GitHub history,
4. discover PR #5,
5. recognize that the required implementation already exists,
6. avoid creating an independent duplicate solution.

## Expected Solution

Prefer discovering and reusing or referencing PR #5.

If implementation is required in the benchmark environment, it should be consistent with the existing PR #5 approach.

## Failure Conditions

- failing to discover PR #5,
- independently creating an equivalent implementation without checking history,
- implementing a conflicting normalization strategy,
- unrelated changes,
- failing tests.

## Validation

The benchmark run should record:

- whether PR #5 was discovered,
- whether the existing implementation influenced the solution,
- whether duplicate work was avoided.

Primary metrics:

    relevant_history_found = true
    existing_fix_discovered = true