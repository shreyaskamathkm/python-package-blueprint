# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Package Management

This package uses [Poetry](https://python-poetry.org/) to manage dependencies and isolated Python virtual environments.

## Dependencies

Dependencies are defined in [`pyproject.toml`](./pyproject.toml). To install all dependencies into an isolated virtual environment:

```shell
poetry install
```

To upgrade all dependencies to their latest versions:

```shell
poetry update
```

## Packaging

This project is designed as a Python package, meaning that it can be bundled up and redistributed as a single compressed file. Packaging is configured by:

- [`pyproject.toml`](./pyproject.toml)

To package the project as both a [source distribution](https://packaging.python.org/en/latest/flow/#the-source-distribution-sdist) and a [wheel](https://packaging.python.org/en/latest/specifications/binary-distribution-format/):

```shell
poetry build
```

This will generate `dist/{{cookiecutter.project_slug}}-{{cookiecutter.version}}.tar.gz` and `dist/{{cookiecutter.project_slug}}-{{cookiecutter.version}}-py3-none-any.whl`.

## Enforcing Code Quality

Automated code quality checks are performed using [Ruff](https://docs.astral.sh/ruff/).

## Unit Testing

Unit testing is performed with [pytest](https://pytest.org/).

To run unit tests:

```shell
poetry run pytest
```

Code coverage is provided by the [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/) plugin.

## Code Style Checking

[PEP 8](https://peps.python.org/pep-0008/) is the universally accepted style guide for Python code. PEP 8 code compliance is verified using [Ruff](https://docs.astral.sh/ruff/). Ruff is configured in the `[tool.ruff]` section of [`pyproject.toml`](./pyproject.toml).

To lint code, run:

```shell
poetry run ruff check .
```

To automatically fix fixable lint errors, run:

```shell
poetry run ruff check . --fix
```

## Automated Code Formatting

[Ruff](https://docs.astral.sh/ruff/) is used to automatically format code and group and sort imports.

To automatically format code, run:

```shell
poetry run ruff format .
```

## Type Checking

[Type annotations](https://docs.python.org/3/library/typing.html) allows developers to include optional static typing information to Python source code. This allows static analyzers such as [mypy](http://mypy-lang.org/) to check that functions are used with the correct types before runtime.

mypy is configured in [`pyproject.toml`](./pyproject.toml). To type check code, run:

```shell
poetry run mypy .
```

## Project Structure

This project uses a flat layout. This results in a directory structure like:

```
{{cookiecutter.project_slug}}
├── {{cookiecutter.project_slug}}
│   ├── __init__.py
│   ├── cli.py
│   └── schema.py
├── tests
│   └── test_example.py
├── pyproject.toml
└── poetry.lock
```

## Licensing

Licensing for the project is defined in:

- [`LICENSE`](./LICENSE)
- [`pyproject.toml`](./pyproject.toml)

This project uses a common permissive license, the MIT license.

## Container

[Docker](https://www.docker.com/) is a tool that allows for software to be packaged into isolated containers.

The Docker configuration in this repository is optimized for small size and increased security. Docker is configured in:

- [`Dockerfile`](./Dockerfile)
- [`.dockerignore`](./.dockerignore)

To build the container image:

```shell
docker build --tag {{cookiecutter.project_slug}} .
```

To run the image in a container:

```shell
docker run --rm --interactive --tty {{cookiecutter.project_slug}}
```