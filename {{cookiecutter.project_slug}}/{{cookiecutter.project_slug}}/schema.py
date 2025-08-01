"""Pydantic models for the application configuration."""

from pathlib import Path

import yaml
from pydantic import BaseModel


class AppConfig(BaseModel):
    """Main application configuration."""

    # Add your configuration fields here

    @classmethod
    def from_yaml(cls, config_path: Path) -> "AppConfig":
        """Load configuration from a YAML file."""
        with open(config_path, "r") as f:
            config_data = yaml.safe_load(f)
        return cls(**config_data)
