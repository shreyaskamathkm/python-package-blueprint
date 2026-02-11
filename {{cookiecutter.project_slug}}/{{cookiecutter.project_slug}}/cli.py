"""Command-line interface for {{cookiecutter.project_name}}."""

import logging
{% if cookiecutter.include_ml_stack == "yes" %}
import hydra
from omegaconf import DictConfig, OmegaConf
from {{cookiecutter.project_slug}}.config import Config
{% else %}
from pathlib import Path
import click
from {{cookiecutter.project_slug}}.schema import AppConfig
{% endif %}

logger = logging.getLogger(__name__)

{% if cookiecutter.include_ml_stack == "yes" %}
@hydra.main(version_base=None, config_path="../configs", config_name="config")
def main(cfg: Config) -> None:
    """Run the application with Hydra configuration."""
    logger.info(OmegaConf.to_yaml(cfg))
    logger.info(f"Running experiment: {cfg.experiment_name}")
    # Application logic here

{% else %}
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
    # For non-ML projects, basic config loading if needed
    if config_path:
        config = AppConfig.from_yaml(Path(config_path))
        logger.info(f"Running with config: {config}")
    else:
        logger.info("Running without config.")
    # Add your application logic here
{% endif %}

if __name__ == "__main__":
    {% if cookiecutter.include_ml_stack == "yes" %}
    main()
    {% else %}
    cli()
    {% endif %}
