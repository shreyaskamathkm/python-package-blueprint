import hydra
from omegaconf import DictConfig, OmegaConf
import logging

log = logging.getLogger(__name__)

@hydra.main(version_base=None, config_path="../configs", config_name="config")
def train(cfg: DictConfig) -> None:
    log.info(OmegaConf.to_yaml(cfg))
    log.info("Starting training...")
    
    # Example access
    log.info(f"Training with model: {cfg.model.name}")
    log.info(f"Epochs: {cfg.training.epochs}")

if __name__ == "__main__":
    train()
