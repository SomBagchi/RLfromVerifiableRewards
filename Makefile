.PHONY: fmt lint typecheck test
fmt:
	uv run black --preview .
	uv run ruff format .
lint:
	uv run ruff check .
typecheck:
	uv run mypy .
test:
	uv run pytest -q
