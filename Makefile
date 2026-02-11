.PHONY: install test

install:
	pip install -e .[dev]

test:
	pytest

docs-serve:
	mkdocs serve

docs-build:
	mkdocs build

