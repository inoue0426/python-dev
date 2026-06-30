# python-dev

Python development baseline for linting, type checking, testing, coverage, and dead-code detection.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
make install-dev
```

## Local checks

Run lint checks:

```bash
make lint
```

Run type checks with unreachable-code warnings enabled:

```bash
make type
```

Run dead-code checks:

```bash
make deadcode
```

Run tests:

```bash
pytest
```

Run tests with coverage:

```bash
make coverage
```

Run all quality checks:

```bash
make check
```

## Template package

This repository includes a small template package under `src/python_dev` and tests under `tests`.

```text
src/python_dev/
  __init__.py
  calculator.py

tests/
  test_calculator.py
```

The template module exposes:

- `add(left: int, right: int) -> int`
- `divide(numerator: float, denominator: float) -> float`

Example:

```python
from src.python_dev import add, divide

print(add(2, 3))
print(divide(10, 2))
```

## pre-commit

Install hooks:

```bash
pre-commit install
```

Run hooks manually:

```bash
pre-commit run --all-files
```

## Tools

| Tool | Purpose |
|---|---|
| `ruff` | Unused imports, unused variables, and lint checks |
| `mypy` | Type checks and unreachable-code warnings |
| `vulture` | Possible unused functions, classes, and variables |
| `coverage` | Code coverage during tests |
| `pytest` | Test runner |
| `pre-commit` | Local checks before commit |

## Notes on vulture

`vulture` reports possible dead code, but Python frameworks can call functions dynamically.

Examples that may look unused to static analysis:

- FastAPI route handlers
- pytest fixtures
- Click commands
- Celery tasks

Add known false positives to `vulture_whitelist.py`.

## Recommended workflow

```bash
make install-dev
pre-commit install
make check
pytest
make coverage
```
