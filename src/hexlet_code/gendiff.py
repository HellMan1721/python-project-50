#!/usr/bin/env python3
import argparse
import json


def read_file(filepath):
    with open(filepath) as f:
        return json.load(f)


def generate_diff(file_path1, file_path2):
    data1 = read_file(file_path1)
    data2 = read_file(file_path2)

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


def parse_args():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file", help="path to first file")
    parser.add_argument("second_file", help="path to second file")
    parser.add_argument(
        "-f", "--format",
        default="stylish",
        help="set format of output"
    )
    return parser.parse_args()


def main():
    args = parse_args()
    print(f"Comparing: {args.first_file} VS {args.second_file}")
    print(f"Output format: {args.format}")
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == "__main__":
    main()
