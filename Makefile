.PHONY: setup backend test lint

setup:
	uv sync
	test -f .env || cp .env.example .env

backend:
	PYTHONPATH=backend uv run uvicorn app.main:app --reload --port 8000

test:
	uv run pytest

lint:
	uv run ruff check .
