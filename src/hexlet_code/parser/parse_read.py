import json
import os

import yaml


def parse_read(filepath):
    _, ext = os.path.splitext(filepath)

    with open(filepath) as f:
        if ext in ['.yml', '.yaml']:
            return yaml.safe_load(f)
        elif ext == '.json':
            return json.load(f)
        else:
            raise ValueError(f"Unsupported file extension: {ext}")

