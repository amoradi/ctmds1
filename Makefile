DIRS = .

.PHONY: lint format typecheck pyright test coverage coverage-html benchmark

# Default to empty, can be overridden with make lint DIFF=1
DIFF_FLAG = $(if $(DIFF),--diff,)

lint:
	poetry run ruff check $(DIFF_FLAG) $(DIRS) && poetry run ruff check --select I --fix $(DIFF_FLAG) $(DIRS)

format:
	poetry run ruff format $(DIFF_FLAG) $(DIRS)

typecheck:
	poetry run pyright $(DIRS)

test:
	poetry run coverage run -m pytest tests --full-trace

coverage:
	poetry run coverage report -m

coverage-html:
	poetry run coverage html

benchmark:
	poetry run python3 benchmarks/bench_main.py

# Convenience target to run all checks
check: lint format typecheck test coverage coverage-html

