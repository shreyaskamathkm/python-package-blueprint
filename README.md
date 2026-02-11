# Python Package Blueprint

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/shreyaskamathkm/python-package-blueprint/actions/workflows/test_cookiecutter.yml/badge.svg)](https://github.com/shreyaskamathkm/python-package-blueprint/actions/workflows/test_cookiecutter.yml)


[**Explore the Request Documentation**](https://shreyaskamathkm.github.io/python-package-blueprint/)

A modern, batteries-included [Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for creating robust Python packages.

## Features

- **Modern Packaging**: Uses `pyproject.toml` (PEP 621) and standard `build` backend.
- **Testing**: Pre-configured with `pytest` and code coverage.
- **Code Quality**: Linting and formatting with `ruff`, type checking with `mypy`.
- **CI/CD**: GitHub Actions for testing, linting, and type checking.
- **Versioning**: Automated version management with `bump-my-version`.
- **Publishing**: Automated PyPI publishing workflow.
- **Development**: `Makefile` for common development tasks.
- **Documentation**: Ready-to-go `mkdocs` setup with Material theme.
- **ML Support**: Optional full ML stack integration (Torch, Hydra, MLflow).

## Prerequisites

- Python 3.10+
- `pip`
- `cookiecutter`

## Usage

1.  **Install Cookiecutter**:
    ```bash
    pip install cookiecutter
    ```

2.  **Generate a New Project**:
    ```bash
    cookiecutter gh:shreyaskamathkm/python-package-blueprint
    ```

3.  **Answer the Prompts**:
    You will be asked for:
    - `project_name`: The human-readable name of your project.
    - `project_slug`: The directory name and package name (snake_case).
    - `description`: A short description.
    - `author`: Your name/email.
    - `version`: Initial version (default: 0.0.1).

4.  **Start Developing**:
    ```bash
    cd <your-project-slug>
    pip install -e .[dev]
    make test
    ```

## Contributing

Contributions are welcome! Please check out the [guidelines](CONTRIBUTING.md).

## License

Distributed under the MIT License. See `LICENSE` for more information.
