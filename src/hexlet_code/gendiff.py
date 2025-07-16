#!/usr/bin/env python3

import json

from hexlet_code.parser.parse_args import parse_args
from hexlet_code.parser.parse_read import parse_read


def generate_diff(file_path1, file_path2):
    data1 = parse_read(file_path1)
    data2 = parse_read(file_path2)

    all_keys = sorted(set(data1.keys()) | set(data2.keys()))

    lines = ['{']
    for key in all_keys:
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                lines.append(f"    {key}: {json.dumps(data1[key])}")
            else:
                lines.append(f"  - {key}: {json.dumps(data1[key])}")
                lines.append(f"  + {key}: {json.dumps(data2[key])}")
        elif key in data1:
            lines.append(f"  - {key}: {json.dumps(data1[key])}")
        else:
            lines.append(f"  + {key}: {json.dumps(data2[key])}")
    lines.append('}')
    return '\n'.join(lines)


def main():
    args = parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)

