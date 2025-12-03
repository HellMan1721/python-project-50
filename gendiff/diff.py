# src/gendiff/diff.py
from gendiff.formatters.json_format import json_format
from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish
from gendiff.parsing import parse_read


def generate_diff(file_path1, file_path2, format_name="stylish"):
    data1 = parse_read(file_path1)
    data2 = parse_read(file_path2)

    diff_tree = build_diff_dict(data1, data2)

    formatters = {
        "stylish": stylish,
        "plain": plain,
        "json": json_format
    }
    formatter = formatters.get(format_name, stylish)
    return formatter(diff_tree)


def build_diff_dict(data1, data2):
    diff = {}
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))

    for key in all_keys:
        if key not in data1:
            diff[key] = {'type': 'added', 'value': data2[key]}
        elif key not in data2:
            diff[key] = {'type': 'removed', 'value': data1[key]}
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff[key] = {
                'type': 'nested',
                'children': build_diff_dict(data1[key], data2[key])
                }
        elif data1[key] == data2[key]:
            diff[key] = {
                'type': 'unchanged',
                'value': data1[key]
            }
        else:
            diff[key] = {
                'type': 'changed',
                'old_value': data1[key],
                'new_value': data2[key],
                }

    return diff