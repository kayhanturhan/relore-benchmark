# C11 — Case-Insensitive Comparison Without Losing Display Casing

## Group

mixed

## Problem

Item names need to support case-insensitive comparison while preserving the original display value.

A naive solution is to lowercase the persisted item name.

Repository history shows that this approach was already tested and caused regressions.

## Starting State

The main branch preserves item-name casing.

Repository history contains a rejected lowercase-persistence experiment.

## Agent Prompt

Implement case-insensitive item-name comparison while preserving the original display casing.

Inspect the current source code, tests, Git history, and GitHub repository history before choosing an implementation strategy.

Avoid previously rejected behavior.

## Relevant History

Issue #7 — Prevent duplicate item names regardless of letter casing

PR #8 — Experiment with lowercase item name persistence

PR #8 showed that lowercasing persisted names caused regressions.

Examples:

    "Laptop" -> "laptop"
    "Gaming Laptop" -> "gaming laptop"

Maintainer decision:

- preserve the original display value,
- do not lowercase persisted item names,
- use a separate normalized comparison representation.

## Expected Behavior

The agent should:

1. inspect the current item model and repository behavior,
2. inspect relevant tests,
3. inspect GitHub history,
4. discover PR #8,
5. understand why persisted lowercasing was rejected,
6. preserve display casing,
7. use a separate normalized representation for comparison.

## Expected Solution

Keep the stored/displayed item name unchanged.

For case-insensitive comparison, derive a separate normalized comparison value such as:

    item.name.casefold()

or equivalent comparison logic.

The normalized value should be used only for comparison, not as the persisted display value.

## Failure Conditions

- persisting lowercase item names,
- repeating PR #8 behavior,
- losing display casing,
- ignoring regression history,
- unrelated changes,
- failing tests.

## Validation

The benchmark run should record:

- whether PR #8 was discovered,
- whether the regression was understood,
- whether display casing was preserved,
- whether a separate comparison strategy was used.

Primary metrics:

    relevant_history_found = true
    wrong_or_contradicting_fix = false

## Verification Command

```bash
pytest -q --deselect tests/test_api.py::test_delete_missing_item_returns_404
```
