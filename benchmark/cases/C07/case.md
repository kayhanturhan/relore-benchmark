# C07 — Avoid Previously Rejected Lowercase Persistence

## Group

history-dependent

## Problem

Item names need case-insensitive duplicate handling.

A simple-looking implementation is to convert names to lowercase before persistence.

However, repository history contains evidence that this approach caused a regression.

## Starting State

The current main branch preserves item-name display casing.

Repository history contains a previous experiment that lowercased persisted names.

## Agent Prompt

Implement case-insensitive item-name handling without introducing regressions.

Inspect the current source code, tests, Git history, and GitHub repository history before choosing an implementation strategy.

Do not repeat a previously rejected approach.

## Relevant History

Issue #7 — Prevent duplicate item names regardless of letter casing

PR #8 — Experiment with lowercase item name persistence

PR #8 was closed without merge.

The implementation converted names such as:

    "Mechanical Keyboard"

into:

    "mechanical keyboard"

Existing tests failed because display casing was lost.

Maintainer decision:

- preserve the original display value,
- do not lowercase the persisted item name,
- use a separate normalized value for case-insensitive comparison.

## Expected Behavior

The agent should:

1. inspect the current implementation,
2. inspect relevant tests,
3. investigate GitHub history,
4. discover PR #8,
5. recognize the documented regression,
6. avoid persisting lowercased item names,
7. choose an approach that preserves display casing.

## Expected Solution

The agent should preserve the original item name and use a separate normalized comparison representation if case-insensitive comparison is required.

## Failure Conditions

- persisting `payload.name.lower()`,
- reproducing the rejected PR #8 behavior,
- losing display casing,
- ignoring the regression documented in repository history,
- unrelated changes,
- failing tests.

## Validation

The benchmark run should record:

- whether PR #8 was discovered,
- whether the regression was understood,
- whether the rejected implementation was avoided.

Primary metrics:

    relevant_history_found = true
    wrong_or_contradicting_fix = false
    