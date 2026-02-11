import re
import sys

PROJECT_SLUG = "{{ cookiecutter.project_slug }}"

MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]*$"

def validate_project_slug(slug):
    """
    Validates that the project slug is a valid Python module name.
    """
    if not re.match(MODULE_REGEX, slug):
        print(f"ERROR: The project slug '{slug}' is not a valid Python module name.")
        print(f" - It must match the regex: {MODULE_REGEX}")
        print("  - Please use only alphanumeric characters and underscores.")
        print("  - It cannot start with a number.")
        return False
    return True

if __name__ == "__main__":
    if not validate_project_slug(PROJECT_SLUG):
        sys.exit(1)
