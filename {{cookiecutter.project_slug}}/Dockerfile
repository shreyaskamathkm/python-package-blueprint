# syntax=docker/dockerfile:1
ARG PYTHON_VERSION=3.10.13
FROM python:${PYTHON_VERSION}-slim-buster as builder

# Prevents python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps python from buffering stdin/stdout.
ENV PYTHONUNBUFFERED=1

# Pip and poetry configuration
ENV PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.8.2 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1

# Add poetry to path
ENV PATH="$POETRY_HOME/bin:$PATH"

# Install poetry
RUN apt-get update \
    && apt-get install -y curl \
    && curl -sSL https://install.python-poetry.org | python3 -

# Copy poetry configuration files
WORKDIR /app
COPY poetry.lock pyproject.toml ./

# Install dependencies
RUN poetry install --no-root --no-dev

# --- Second Stage ---
FROM python:${PYTHON_VERSION}-slim-buster as production

# Copy virtual env from builder
ENV VENV_PATH=/app/.venv
COPY --from=builder ${VENV_PATH} ${VENV_PATH}

# Add virtual env to path
ENV PATH="${VENV_PATH}/bin:$PATH"

# Copy application code
COPY {{cookiecutter.project_slug}} /app/{{cookiecutter.project_slug}}

WORKDIR /app

# Set the default command to run the CLI
CMD ["cli", "--help"]

