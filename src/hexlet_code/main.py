from .cli import parse_args
from .gendiff import generate_diff


def main():
    args = parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == "__main__":
    main()
