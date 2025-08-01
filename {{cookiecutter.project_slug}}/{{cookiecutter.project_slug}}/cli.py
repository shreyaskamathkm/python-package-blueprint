"""Command-line interface for {{cookiecutter.project_name}}."""

import logging

import click

from {{cookiecutter.project_slug}}.schema import AppConfig

logger = logging.getLogger(__name__)


@click.group()
def cli() -> None:
    """A command-line interface for {{cookiecutter.project_name}}."""
    pass


@cli.command("run")
@click.option(
    "--config-path",
    type=click.Path(exists=True),
    help="Path to the config file.",
)
def run(config_path: str) -> None:
    """Runs the application."""
    config = AppConfig.from_yaml(config_path)
    logger.info(f"Running with config: {config}")
    # Add your application logic here


if __name__ == "__main__":
    cli()
