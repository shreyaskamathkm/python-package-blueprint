from pathlib import Path
import yaml
from {{cookiecutter.project_slug}}.schema import AppConfig


class TestAppConfig(AppConfig):
    dummy_field: str


def test_app_config_from_yaml(tmp_path: Path):
    """Test loading AppConfig from a YAML file."""
    config_data = {"dummy_field": "dummy_value"}
    config_path = tmp_path / "config.yaml"
    with open(config_path, "w") as f:
        yaml.dump(config_data, f)

    app_config = TestAppConfig.from_yaml(config_path)
    assert app_config.dummy_field == "dummy_value"
