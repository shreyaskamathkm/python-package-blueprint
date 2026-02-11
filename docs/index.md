# Python Package Blueprint

A modern, batteries-included [Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for creating robust Python packages.

## Key Features

- **Modern Packaging**: Uses `pyproject.toml` (PEP 621) and standard `build` backend.
- **Testing**: Pre-configured with `pytest` and code coverage.
- **Code Quality**: Linting and formatting with `ruff`, type checking with `mypy`.
- **CI/CD**: GitHub Actions for testing, linting, and type checking.
- **Versioning**: Automated version management with `bump-my-version`.
- **Publishing**: Automated PyPI publishing workflow.
- **Development**: `Makefile` for common development tasks.
- **ML Ready (Optional)**: Can optionally include a full Machine Learning stack (PyTorch, Hydra, MLflow).

## Quick Start

1.  **Install Cookiecutter**:
    ```bash
    pip install cookiecutter
    ```

2.  **Generate a New Project**:
    ```bash
    cookiecutter gh:shreyaskamathkm/python-package-blueprint
    ```
