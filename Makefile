install:
	uv pip install -e .
	uv pip install -r requirements.txt

run:
	uv run hexlet-python-package

test:
	pytest --cov=src --cov-report=term --cov-report=xml tests

lint:
	ruff check src

check: test lint

build:
	uv build

