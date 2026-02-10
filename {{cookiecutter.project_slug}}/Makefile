TESTS_DIR := tests

help:  ## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z0-9_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)
.PHONY: help

##@ Development

test: ## Run tests
	pytest --cov={{cookiecutter.project_slug}} $(TESTS_DIR)/
.PHONY: test

lint: ## Lint the code
	ruff check ./{{cookiecutter.project_slug}} ./tests
.PHONY: lint

typecheck: ## Run type checking
	mypy ./{{cookiecutter.project_slug}} ./tests
.PHONY: typecheck

test-all: test lint typecheck ## Run all tests, linting, and type checking
.PHONY: test-all

format: ## Format the code
	ruff format .
.PHONY: format

##@ Installation

edit-install: ## Install the package in editable mode
	pip install -e .[dev]
.PHONY: edit-install

install: ## Install the package
	pip install .[dev]
.PHONY: install

##@ Release

bump-major: ## Bump the major version
	bump-my-version bump major
.PHONY: bump-major

bump-minor: ## Bump the minor version
	bump-my-version bump minor
.PHONY: bump-minor

bump-patch: ## Bump the patch version
	bump-my-version bump patch
.PHONY: bump-patch

##@ ML

train: ## Run training
	python -m {{cookiecutter.project_slug}}.train

experiment: ## Run specific experiment
	python -m {{cookiecutter.project_slug}}.train experiment=$(EXP)
.PHONY: train experiment