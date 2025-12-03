.PHONY: install test lint git-push check test-coverage

install:
	@echo "📦 Installing dependencies..."
	@if command -v uv >/dev/null 2>&1; then \
		echo "Using uv to install dependencies..."; \
		uv sync; \
	else \
		. venv/Scripts/activate 2>/dev/null || source venv/bin/activate; \
		pip install -e .; \
		pip install -r requirements.txt 2>/dev/null || true; \
	fi

test:
	@echo "🧪 Running tests..."
	@pytest tests

lint:
	@echo "🔍 Running linter..."
	@ruff check gendiff
	@ruff check tests

git-push:
	@echo "🚀 Pushing to GitHub..."
	git add .
	git diff --quiet && git diff --cached --quiet || (git commit -m "update" && git push)

check: lint test
	@echo "✅ All checks passed"

test-coverage:
	@echo "🧪 Running tests with coverage..."
	@pytest --cov=gendiff --cov-report=term --cov-report=xml tests

