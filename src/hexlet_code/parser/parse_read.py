import json
import yaml
import os


def parse_read(filepath):
    """Parse JSON or YAML file and return data"""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        if not content:
            raise ValueError(f"File is empty: {filepath}")

        extension = os.path.splitext(filepath)[1].lower()

        try:
            if extension in ['.yml', '.yaml']:
                return yaml.safe_load(content)
            elif extension == '.json':
                return json.loads(content)
            else:
                raise ValueError(f"Unsupported file format: {extension}")
        except (json.JSONDecodeError, yaml.YAMLError) as e:
            raise ValueError(f"Failed to parse {filepath}: {str(e)}")