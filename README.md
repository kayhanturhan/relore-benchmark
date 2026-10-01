# Relore Benchmark Demo Repository

Phase 1 of a controlled benchmark for evaluating repository memory.

## Purpose

This repository is intentionally small. It provides enough structure to create future benchmark cases involving source code, tests, cache behavior, architectural decisions, Git history, PR discussions, and rejected approaches.

## Application

A minimal FastAPI CRUD API for items.

### Endpoints

- `GET /health`
- `GET /items`
- `GET /items/{id}`
- `POST /items`
- `DELETE /items/{id}`

## Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --app-dir src --reload
```

## Test

```bash
pytest
```

## Benchmark roadmap

Phase 2 will establish the clean baseline and test suite before synthetic Git/GitHub history and controlled bug scenarios are introduced.
