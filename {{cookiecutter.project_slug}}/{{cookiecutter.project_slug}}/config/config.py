"""Configuration definition for Hydra."""

from dataclasses import dataclass
from typing import Any

@dataclass
class TrainingConfig:
    """Training configuration."""
    epochs: int
    batch_size: int
    seed: int
    device: str

@dataclass
class ModelConfig:
    """Model configuration."""
    name: str
    params: dict[str, Any]

@dataclass
class Config:
    """Main configuration."""
    defaults: list[Any]
    experiment_name: str
    training: TrainingConfig
    model: ModelConfig
    data: Any
    optimizer: Any 
    scheduler: Any
