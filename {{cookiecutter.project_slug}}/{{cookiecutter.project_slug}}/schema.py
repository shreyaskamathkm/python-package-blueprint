"""Pydantic models for the application configuration."""

from pathlib import Path
from typing import TypeVar

import yaml
from pydantic import BaseModel

T = TypeVar("T", bound="AppConfig")


class AppConfig(BaseModel):
    """Main application configuration."""

    # Add your configuration fields here

    @classmethod
    def from_yaml(cls: type[T], config_path: Path) -> T:
        """Load configuration from a YAML file."""
        with open(config_path) as f:
            config_data = yaml.safe_load(f)
        return cls(**config_data)
