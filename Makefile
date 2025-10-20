.PHONY: install test lint

install:
	@echo "📦 Installing dependencies..."
	@. venv/Scripts/activate 2>/dev/null || source venv/bin/activate; \
	pip install -e .; \
	pip install -r requirements.txt 2>/dev/null || true

test:
	@echo "🧪 Running tests..."
	@. venv/Scripts/activate 2>/dev/null || source venv/bin/activate; \
	pytest --cov=src --cov-report=term --cov-report=xml tests

lint:
	@echo "🔍 Running linter..."
	@. venv/Scripts/activate 2>/dev/null || source venv/bin/activate; \
	ruff check src
