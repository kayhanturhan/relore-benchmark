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
- `DELETE /items/{id}`

## Running the Application

Create and activate the virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate