# Project Structure

The structure of your generated project depends heavily on how you answer the `include_ml_stack` prompt.

## Standard Structure (`include_ml_stack="no"`)

If you choose **no**, you get a clean, flat layout perfect for general-purpose Python libraries.

```
<project_slug>/
├── .github/            # GitHub Actions workflows
├── docs/               # Documentation (MkDocs)
├── tests/              # Unit tests
├── <project_slug>/     # Source code
│   ├── __init__.py
│   ├── cli.py          # Command-line interface entry point
│   └── ...
├── .gitignore
├── Makefile            # Helper commands
├── mkdocs.yml          # Documentation config
├── pyproject.toml      # Project configuration and dependencies
└── README.md
```

## ML Structure (`include_ml_stack="yes"`)

If you choose **yes**, the template generates a structure optimized for Machine Learning engineering and research.

```
<project_slug>/
├── .github/
├── .vscode/            # VS Code settings
├── artifacts/          # Directory for build artifacts/outputs
├── configs/            # Hydra configuration files
│   ├── experiment/     # Experiment configs
│   ├── data/           # Data configs
│   ├── model/          # Model configs
│   ├── optimizer/      # Optimizer configs
│   ├── scheduler/      # Scheduler configs
│   └── config.yaml     # Main config
├── datasets/           # Directory for storing datasets
├── docs/
├── notebooks/          # Jupyter notebooks
├── tests/
├── <project_slug>/
│   ├── __init__.py
│   ├── cli.py
│   ├── schema.py       # Pydantic schemas for config validation
│   ├── models/         # PyTorch models
│   ├── data/           # Data loaders/processing
│   ├── train.py        # Training script
│   └── utils/          # Utility functions
├── .gitignore
├── Dockerfile          # Docker container definition
├── Makefile
├── mkdocs.yml
├── pyproject.toml
└── README.md
```

### Key ML Components

- **`configs/`**: Uses [Hydra](https://hydra.cc/) for hierarchical configuration management.
- **`artifacts/`, `datasets/`, `notebooks/`**: Placeholders for common ML workflow artifacts. *Note: specific paths are often ignored in `.gitignore`.*
- **`models/`**: Place your PyTorch `nn.Module` definitions here.
- **`schema.py`**: Defines structured configurations using Pydantic/Hydra for type safety.
