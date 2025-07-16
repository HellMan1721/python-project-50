import os
from hexlet_code.gendiff import generate_diff


def test_flat_yaml():
    file1 = os.path.join('tests', 'test_data', 'filepath1.yaml')
    file2 = os.path.join('tests', 'test_data', 'filepath2.yaml')
    with open(os.path.join('tests', 'test_data', 'expected.txt')) as f:
        expected = f.read().strip()

    actual = generate_diff(file1, file2)
    assert actual == expected, f"\nExpected:\n{expected}\n\nActual:\n{actual}"

