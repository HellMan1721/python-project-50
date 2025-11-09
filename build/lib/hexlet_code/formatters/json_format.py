import json


def json_format(diff_tree):
    """Format diff as JSON string"""
    return json.dumps(diff_tree, indent=2)