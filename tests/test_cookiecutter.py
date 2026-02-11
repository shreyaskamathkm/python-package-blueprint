import os
import pytest
from cookiecutter.main import cookiecutter

def test_bake_project(cookies):
    result = cookies.bake(extra_context={"project_name": "Test Project"})

    assert result.exit_code == 0
    assert result.exception is None

    assert result.project_path.name == "test_project"
    assert result.project_path.is_dir()

    # Check for some expected files
    assert (result.project_path / "README.md").is_file()
    assert (result.project_path / "pyproject.toml").is_file()
    assert (result.project_path / ".gitignore").is_file()
    assert (result.project_path / "docs" / "index.md").is_file()
    assert (result.project_path / "docs" / "getting-started.md").is_file()

def test_bake_project_with_cli(cookies):
    result = cookies.bake(extra_context={"project_name": "CLI Project", "include_cli": "yes"})

    assert result.exit_code == 0
    assert result.exception is None
    
    # Check for CLI specific files/content if any (adjust based on actual template content)
    # For now just checking it generates without error

def test_bake_project_no_ml(cookies):
    result = cookies.bake(extra_context={"project_name": "No ML Project", "include_ml_stack": "no"})

    assert result.exit_code == 0
    assert result.exception is None
    
    # Verify ML specific folders are NOT present
    assert not (result.project_path / "configs").exists()
    assert not (result.project_path / "datasets").exists()
    assert not (result.project_path / "notebooks").exists()
    assert not (result.project_path / "artifacts").exists()

def test_bake_project_with_ml(cookies):
    result = cookies.bake(extra_context={"project_name": "ML Project", "include_ml_stack": "yes"})

    assert result.exit_code == 0
    assert result.exception is None
    
    # Verify ML specific folders ARE present
    assert (result.project_path / "configs").exists()
    assert (result.project_path / "datasets").exists()
    assert (result.project_path / "notebooks").exists()
    assert (result.project_path / "artifacts").exists()
    assert (result.project_path / "configs" / "optimizer" / "adam.yaml").exists()
    assert (result.project_path / "configs" / "scheduler" / "step_lr.yaml").exists()
    assert (result.project_path / "ml_project" / "config" / "config.py").exists()
    assert not (result.project_path / "ml_project" / "schema.py").exists()
