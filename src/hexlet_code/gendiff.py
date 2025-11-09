#!/usr/bin/env python3

from hexlet_code.diff_builder import build_diff
from hexlet_code.formatters.json_format import json_format
from hexlet_code.formatters.plain import plain
from hexlet_code.formatters.stylish import format_diff
from hexlet_code.parser.parse_args import parse_args
from hexlet_code.parser.parse_read import parse_read


def generate_diff(file_path1, file_path2, format_name='stylish'):
    """Generate difference between two files"""
    data1 = parse_read(file_path1)
    data2 = parse_read(file_path2)

    diff = build_diff(data1, data2)

    formatters = {
        'stylish': format_diff,
        'plain': plain,
        'json': json_format
    }

    if format_name not in formatters:
        raise ValueError(f'Unknown format: {format_name}')
    
    return formatters[format_name](diff)


def main():
    """Main function"""
    args = parse_args()
    format_name = getattr(args, 'format', 'stylish')
    result = generate_diff(args.first_file, args.second_file, format_name)
    print(result)


if __name__ == '__main__':
    main()