# Usage Guide

## Prerequisites

Before using this template, ensure you have the following installed:

- **Python 3.10+**: The template targets modern Python versions.
- **pip**: standard package installer for Python.
- **cookiecutter**: The command-line utility to create projects from templates.

```bash
pip install cookiecutter
```

## generating a new project

To generate a new project, run the following command structure:

```bash
cookiecutter gh:shreyaskamathkm/python-package-blueprint
```

### Configuration Prompts

You will be prompted to answer a few questions to configure your project. Here is what they mean:

- **`project_name`**: The human-readable name of your project (e.g., "My Awesome Package").
- **`project_slug`**: The directory name and package name (snake_case, e.g., `my_awesome_package`). This will be used for imports.
- **`description`**: A short description of your project.
- **`author`**: Your name and email address.
- **`version`**: The initial version of your package (default: `0.0.1`).
- **`include_ml_stack`**:  This is a crucial decision.
    - **`yes`**: Includes a complete Machine Learning stack with PyTorch, Hydra configs, MLflow tracking, and a more complex folder structure.
    - **`no`**: Generates a lean, standard Python package structure suitable for libraries or simple tools.

## Post-Generation Setup

Once the project is generated:

1.  **Navigate to the project directory**:
    ```bash
    cd <your-project-slug>
    ```

2.  **Initialize git**:
    ```bash
    git init
    # Make sure to create a repository on GitHub and follow instructions to push
    ```

3.  **Install dependencies**:
    ```bash
    pip install -e .[dev]
    # OR using the Makefile
    make install
    ```

4.  **Run tests to ensure everything is working**:
    ```bash
    make test
    ```
