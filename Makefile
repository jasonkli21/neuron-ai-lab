.PHONY: sync format lint typecheck test check demo lab clean verify-env

sync:
	uv sync --all-groups

format:
	uv run ruff format .
	uv run ruff check --fix .

lint:
	uv run ruff format --check .
	uv run ruff check .

typecheck:
	uv run mypy

test:
	uv run pytest --cov=neuron_lab --cov-report=term-missing

check: verify-env lint typecheck test

verify-env:
	uv run python scripts/verify_environment.py

demo:
	mkdir -p outputs
	uv run python -m neuron_lab.demo --output outputs/lif_demo.png

lab:
	uv run jupyter lab

clean:
	rm -rf .pytest_cache .mypy_cache .ruff_cache htmlcov .coverage
	rm -rf src/*.egg-info src/neuron_lab/__pycache__ tests/__pycache__
	rm -f outputs/*.png
