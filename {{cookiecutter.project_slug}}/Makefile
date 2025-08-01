CMD := poetry run
TESTS_DIR := tests

help:  ## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z0-9_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)
.PHONY: help

##@ Development

test: ## Run tests
	$(CMD) pytest --cov={{cookiecutter.project_slug}} $(TESTS_DIR)/
.PHONY: test

lint: ## Lint the code
	$(CMD) ruff check ./{{cookiecutter.project_slug}} ./tests
.PHONY: lint

typecheck: ## Run type checking
	$(CMD) mypy ./{{cookiecutter.project_slug}} ./tests
.PHONY: typecheck

test-all: test lint typecheck ## Run all tests, linting, and type checking
.PHONY: test-all

##@ Installation

edit-install: ## Install the package in editable mode
	pip install -e .
.PHONY: edit-install

install: ## Install the package
	pip install .
.PHONY: install