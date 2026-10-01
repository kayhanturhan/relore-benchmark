# Relore Repository Memory Benchmark

A controlled benchmark for evaluating the incremental value of
Relore repository memory for coding agents.

## Goal

The benchmark compares the same coding agent under two conditions:

### Baseline

Coding Agent + source code + tests + git + gh

### Relore

Coding Agent + source code + tests + git + gh + Relore

The main research question is:

> Does Relore help a coding agent discover and use relevant repository
> history, resulting in better implementation decisions?

## Demo Application

The benchmark uses a deliberately small FastAPI application.

The application manages simple `Item` objects and contains separate:

- API layer
- Service layer
- Repository layer
- Cache layer

This architecture is intentionally small while still allowing realistic
benchmark scenarios involving caching, validation, regressions,
architectural decisions, and competing implementations.

## API

- `GET /health`
- `GET /items`
- `GET /items/{id}`
- `POST /items`
- `PUT /items/{id}`
- `DELETE /items/{id}`

## Running the Application

Create and activate the virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the API:

```bash
uvicorn app.main:app --reload --port 8001 --app-dir src
```

Swagger UI:

```text
http://127.0.0.1:8001/docs
```

## Tests

Run:

```bash
pytest
```

## Benchmark Development

### Phase 1 — Demo Repository

Status: Complete

The initial benchmark repository contains:

- Small FastAPI application
- API layer
- Service layer
- Repository layer
- Cache layer
- Automated tests
- Git repository
- GitHub repository

Phase 1 established a deliberately small and understandable codebase
that can be used to create controlled repository-history and
bug-fixing scenarios.

### Phase 2 — Repository History

Status: Complete

Controlled repository history was created using:

- commits
- feature branches
- GitHub issues
- pull requests
- PR descriptions
- review comments
- maintainer decisions
- rejected approaches
- regression evidence
- previously attempted solutions

Four repository-history patterns were created.

#### Scenario 1 — Accepted Implementation

Issue #1 / PR #2

An item update capability was implemented.

The change introduced:

- `ItemUpdate`
- repository update support
- service update support
- `PUT /items/{id}`
- cache invalidation after successful updates
- automated tests

A maintainer decision was recorded that cache invalidation belongs
in the service layer while the repository remains responsible for
persistence.

PR #2 was merged.

#### Scenario 2 — Rejected Architectural Approach

Issue #3 / PR #4

A write-through cache strategy was evaluated.

The proposed implementation refreshed the cache immediately after
successful item updates instead of invalidating the cached entry.

The approach was reviewed and rejected.

The repository history records the decision to keep cache invalidation
after writes and reload the value from the repository on the next read.

PR #4 was closed without being merged.

#### Scenario 3 — Existing Fix in Another Pull Request

PR #5 / Issue #6

A fix for item-name whitespace normalization exists in:

    fix/item-name-normalization

PR #5 contains the implementation and tests but intentionally remains
open and unmerged.

Issue #6 describes the same underlying problem.

This scenario will evaluate whether a coding agent discovers the
existing implementation instead of independently creating a duplicate
solution.

#### Scenario 4 — Regression-Causing Approach

Issue #7 / PR #8

An experimental implementation converted persisted item names to
lowercase in order to simplify case-insensitive duplicate handling.

The implementation caused existing tests to fail because display
casing was lost.

Examples:

    "Laptop" -> "laptop"

    "Gaming Laptop" -> "gaming laptop"

The experiment produced:

    4 failed, 10 passed

The approach was rejected.

The maintainer decision recorded in repository history states that
display casing must be preserved and case-insensitive comparison
should instead use a separate normalized comparison value.

PR #8 was closed without being merged.

### Phase 3 — Controlled Benchmark Cases

Status: In Progress

Approximately 10–20 controlled benchmark cases will be created.

The initial benchmark will use 12 cases divided into three groups:

#### Source-Only Cases

These cases should be solvable using source code and tests without
requiring repository history.

#### History-Dependent Cases

These cases are designed so that repository history contains important
information that should influence the agent's decision.

#### Mixed Cases

These cases can be partially understood from source code but repository
history provides additional information that can improve the decision.

The benchmark cases should include examples involving:

- simple implementation bugs
- validation behavior
- cache behavior
- architectural decisions
- rejected implementations
- regressions
- existing fixes in another branch or pull request
- maintainer review decisions

### Phase 4 — Benchmark Execution

Status: Planned

Each benchmark case will be executed under two conditions.

#### Baseline

```text
Coding Agent
+ source code
+ tests
+ git
+ gh
```

The agent may inspect Git and GitHub history itself.

#### Relore

```text
Coding Agent
+ source code
+ tests
+ git
+ gh
+ Relore
```

The same repository will be indexed by Relore.

The following should remain as consistent as possible between runs:

- model
- prompt
- timeout
- token budget
- repository state
- issue description

## Metrics

For each benchmark case, record:

- bug solved
- correct patch
- tests passed
- relevant history found
- wrong or contradictory fix
- existing fix discovered
- tool calls
- tokens
- execution time
- cost

In addition to quantitative metrics, record the agent's investigation
process.

For each case:

```text
Problem
   ↓
What did the agent investigate?
   ↓
What did the agent discover using git / gh?
   ↓
What did the agent discover using Relore?
   ↓
Did repository history change the agent's decision?
   ↓
Generated patch
   ↓
Test result
```

Several representative cases should be analyzed in detail.

## Expected Result

The benchmark is designed to answer:

> When the same coding agent works on the same problem, does providing
> Relore help it use repository history more effectively and make better
> implementation decisions?

The goal is not to measure general real-world bug-fixing performance.

The goal is to isolate and observe the incremental value of Relore
repository memory in a small and controlled environment.