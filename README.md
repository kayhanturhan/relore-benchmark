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
- Local Ubuntu development environment
- Git repository
- GitHub repository

The purpose of Phase 1 was to establish a small and understandable
codebase that can later be used to create controlled repository-history
and bug-fixing scenarios.

### Phase 2 — Repository History

Status: In Progress

Controlled repository history is being created using:

- commits
- feature branches
- GitHub issues
- pull requests
- PR descriptions
- review comments
- maintainer decisions
- rejected approaches
- previously attempted solutions

#### Completed History

##### Issue #1 / PR #2 — Item Update Endpoint

An item update capability was added to the application.

The implementation introduced:

- `ItemUpdate`
- repository update support
- service update support
- `PUT /items/{id}`
- cache invalidation after successful updates
- API, service, and repository tests

PR #2 was reviewed and merged.

A maintainer decision was recorded stating that cache invalidation
belongs in the service layer and that the repository should remain
focused on persistence responsibilities.

##### Issue #3 / PR #4 — Write-Through Cache Experiment

A write-through cache strategy was evaluated.

The experimental implementation replaced cache invalidation with
immediate cache updates after successful item updates.

The approach appeared reasonable and passed the automated tests.

During review, however, the approach was rejected.

The repository history preserves the maintainer decision and the
reasoning behind keeping cache invalidation instead of write-through
cache updates.

PR #4 was closed without being merged.

This rejected implementation is intentionally preserved as part of
the benchmark's repository memory.

#### Next History Scenario

The next controlled scenario will create a fix that already exists
in another branch and pull request.

The pull request will intentionally remain open.

A later benchmark issue will describe the same underlying problem.

The experiment will then evaluate whether the coding agent:

1. discovers the existing branch or pull request,
2. understands that a fix already exists,
3. reuses or references the existing work,

instead of independently implementing a duplicate solution.

### Phase 3 — Controlled Benchmark Cases

Status: Planned

Approximately 10–20 controlled issues will be created.

Some issues will be intentionally simple and solvable using only:

- source code
- tests

Other issues will require repository history.

History-dependent cases may involve:

- previous architectural decisions
- rejected implementations
- regression information
- maintainer review comments
- existing fixes in another branch or pull request
- previously attempted solutions

The purpose is to create situations where repository history can
materially influence the coding agent's implementation decision.

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

The agent may inspect Git and GitHub history using the available tools.

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

The following should remain as consistent as possible between both runs:

- model
- prompt
- timeout
- token budget
- repository state
- issue description

## Metrics

For each benchmark case, the following metrics will be recorded:

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

In addition to quantitative metrics, each benchmark run should record
the agent's investigation process.

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

Several representative cases will be analyzed in detail.

## Expected Result

The benchmark is designed to answer the following question:

> When the same coding agent works on the same problem, does providing
> Relore help it use repository history more effectively and make better
> implementation decisions?

The goal is not to measure general real-world bug-fixing performance.

The goal is to isolate and observe the incremental value of Relore
repository memory in a small and controlled environment.