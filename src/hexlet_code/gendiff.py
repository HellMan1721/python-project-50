#!/usr/bin/env python3

from hexlet_code.diff_builder import build_diff
from hexlet_code.formatters.plain import plain
from hexlet_code.formatters.stylish import format_diff
from hexlet_code.parser.parse_args import parse_args
from hexlet_code.parser.parse_read import parse_read


def generate_diff(file_path1, file_path2, format_name='stylish'):

    data1 = parse_read(file_path1)
    data2 = parse_read(file_path2)

    diff = build_diff(data1, data2)

    if format_name == 'stylish':
        return format_diff(diff)
    elif format_name == 'plain':
        return plain(diff)
    else:
        raise ValueError(f'Unknown format: {format_name}')


def main():
    args = parse_args()
    fmt = getattr(args, 'format', 'stylish')
    result = generate_diff(args.first_file, args.second_file, fmt)
    print(result)


if __name__ == '__main__':
    main()