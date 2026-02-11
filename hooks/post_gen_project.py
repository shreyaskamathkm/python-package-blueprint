import os
import shutil

REMOVE_PATHS = [
    '{% if cookiecutter.include_ml_stack != "yes" %}configs{% endif %}',
    '{% if cookiecutter.include_ml_stack != "yes" %}datasets{% endif %}',
    '{% if cookiecutter.include_ml_stack != "yes" %}notebooks{% endif %}',
    '{% if cookiecutter.include_ml_stack != "yes" %}artifacts{% endif %}',
    '{% if cookiecutter.include_ml_stack != "yes" %}{{cookiecutter.project_slug}}/models{% endif %}',
    '{% if cookiecutter.include_ml_stack != "yes" %}{{cookiecutter.project_slug}}/optimizer{% endif %}',
    '{% if cookiecutter.include_ml_stack != "yes" %}{{cookiecutter.project_slug}}/scheduler{% endif %}',
    '{% if cookiecutter.include_ml_stack != "yes" %}{{cookiecutter.project_slug}}/utils{% endif %}',
    '{% if cookiecutter.include_ml_stack != "yes" %}{{cookiecutter.project_slug}}/train.py{% endif %}',
    '{% if cookiecutter.include_ml_stack != "yes" %}{{cookiecutter.project_slug}}/config{% endif %}',
    '{% if cookiecutter.include_ml_stack != "yes" %}{{cookiecutter.project_slug}}/data{% endif %}',
    '{% if cookiecutter.include_ml_stack == "yes" %}{{cookiecutter.project_slug}}/schema.py{% endif %}',
]

def remove(path):
    if path and os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)

def main():
    for path in REMOVE_PATHS:
        remove(path.strip())

if __name__ == '__main__':
    main()
