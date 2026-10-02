# C01 — Incorrect Discount Calculation

## Group

source-only

## Problem

The application contains a calculation bug in an item-related utility.

A percentage discount is applied incorrectly.

## Starting State

The bug should exist directly in the source code.

No repository history is required to understand or solve the issue.

## Agent Prompt

Fix the incorrect discount calculation.

Inspect the source code and tests, identify the bug, implement the smallest correct fix, and ensure all tests pass.

## Relevant History

None.

This case is intentionally designed to be solvable using only source code and tests.

## Expected Behavior

The agent should:

1. inspect the relevant implementation,
2. inspect the failing tests,
3. identify the incorrect calculation,
4. make a minimal fix,
5. run the tests.

The agent should not need to inspect GitHub history.

## Expected Solution

Correct the discount calculation without making unrelated changes.

## Failure Conditions

- incorrect calculation remains,
- unrelated code is changed,
- existing behavior regresses,
- tests fail.

## Validation

The dedicated discount tests and full test suite must pass.

## Verification Command

```bash
pytest -q tests/test_pricing_service.py::test_apply_discount
```
