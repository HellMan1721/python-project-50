import os
from hexlet_code.gendiff import generate_diff

def test_flat_json():
    file1 = os.path.join('tests', 'test_data', 'file1.json')
    file2 = os.path.join('tests', 'test_data', 'file2.json')
    expected = open(os.path.join('tests', 'test_data', 'expected.txt')).read().strip()

    assert generate_diff(file1, file2) == expected

