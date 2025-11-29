import os

from diff import generate_diff


def read_file(path):
    with open(path) as f:
        return f.read().strip()


def test_flat_json():
    file1 = os.path.join('gendiff', 'tests', 'test_data', 'file1.json')
    file2 = os.path.join('gendiff', 'tests', 'test_data', 'file2.json')
    expected = read_file(
        os.path.join('gendiff', 'tests', 'test_data', 'expected.txt')
        )
    assert generate_diff(file1, file2) == expected


def test_flat_yaml():
    file1 = os.path.join('gendiff', 'tests', 'test_data', 'filepath1.yaml')
    file2 = os.path.join('gendiff', 'tests', 'test_data', 'filepath2.yaml')
    expected = read_file(
        os.path.join('gendiff', 'tests', 'test_data', 'expected.txt')
        )
    assert generate_diff(file1, file2) == expected


def test_nested_json():
    file1 = os.path.join('gendiff', 'tests', 'test_data', 'nested1.json')
    file2 = os.path.join('gendiff', 'tests', 'test_data', 'nested2.json')
    expected = read_file(
        os.path.join('gendiff', 'tests', 'test_data', 'expected_nested.txt')
        )
    assert generate_diff(file1, file2) == expected


def test_nested_yaml():
    file1 = os.path.join('gendiff', 'tests', 'test_data', 'nested1.yaml')
    file2 = os.path.join('gendiff', 'tests', 'test_data', 'nested2.yaml')
    expected = read_file(
        os.path.join('gendiff', 'tests', 'test_data', 'expected_nested.txt')
        )
    assert generate_diff(file1, file2) == expected


def test_mixed_formats():
    file1 = os.path.join('gendiff', 'tests', 'test_data', 'nested1.json')
    file2 = os.path.join('gendiff', 'tests', 'test_data', 'nested2.yaml')
    expected = read_file(
        os.path.join('gendiff', 'tests', 'test_data', 'expected_nested.txt')
        )
    assert generate_diff(file1, file2) == expected