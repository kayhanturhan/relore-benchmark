# C06 — Existing Fix Already Available in Open Pull Request

## Group

history-dependent

## Problem

Item names with leading or trailing whitespace are stored without normalization.

The issue appears to require a straightforward implementation change.

However, an existing open pull request already contains a fix for the same problem.

## Starting State

The main branch still contains the whitespace-normalization bug.

Issue #6 describes the problem.

PR #5 contains a complete implementation and tests but remains open and unmerged.

## Agent Prompt

Investigate and resolve the issue where item names retain unwanted leading and trailing whitespace.

Inspect the current source code, tests, Git history, and GitHub repository history before deciding whether a new implementation is necessary.

Avoid duplicating work that already exists.

## Relevant History

Issue #6 — Item names retain unwanted surrounding whitespace

PR #5 — Normalize item names before persistence

PR #5 already contains:

- normalization during item creation,
- normalization during item updates,
- automated tests.

## Expected Behavior

The agent should:

1. inspect the issue,
2. inspect current source code,
3. investigate GitHub history,
4. discover PR #5,
5. recognize that the fix already exists,
6. avoid creating a duplicate implementation,
7. report or reuse the existing work as appropriate.

## Expected Solution

The preferred outcome is discovery of PR #5 rather than independently recreating the same patch.

## Failure Conditions

- independently writing the same fix without discovering PR #5,
- creating a duplicate branch or pull request,
- ignoring existing implementation history,
- introducing a conflicting implementation.

## Validation

The run should record whether the agent discovered PR #5 before implementing a new fix.

Primary benchmark metric:

    existing_fix_discovered = true