from gendiff import generate_diff
from gendiff.scripts.parse_args import parse_args


def main():
    args = parse_args()
    format_name = getattr(args, 'format', 'stylish')
    result = generate_diff(args.first_file, args.second_file, format_name)
    print(result)