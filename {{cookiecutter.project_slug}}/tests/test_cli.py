from pathlib import Path
import yaml
from click.testing import CliRunner
from {{cookiecutter.project_slug}}.cli import cli
from {{cookiecutter.project_slug}}.schema import AppConfig


class TestAppConfig(AppConfig):
    dummy_field: str


def test_run_command(tmp_path: Path):
    """Test the run command."""
    config_data = {"dummy_field": "dummy_value"}
    config_path = tmp_path / "config.yaml"
    with open(config_path, "w") as f:
        yaml.dump(config_data, f)

    # Monkeypatch the AppConfig to have the dummy field for the test
    cli.AppConfig = TestAppConfig

    runner = CliRunner()
    result = runner.invoke(cli, ["run", "--config-path", str(config_path)])
    assert result.exit_code == 0
