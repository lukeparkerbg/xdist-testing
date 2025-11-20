# Testing pytest concurrent test run

Disclaimer: The tests that you include when using `pytest-xdist` must not share any state anywhere. You should be completely sure that two tests will not affect each other at all. They should not edit the same database tables, they should not read/write the same files, etc.

## Setup

```bash
uv init
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

## Tests

Concurrent version:

```bash
pytest -n logical -m 'xdist' -vvv tests/
```

Non-concurrent version:

```bash
pytest -vvv -m 'xdist' tests/
```
