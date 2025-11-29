from diff import generate_diff


def test_plain_json():
    result = generate_diff(
        'gendiff/tests/test_data/nested1.json', 
        'gendiff/tests/test_data/nested2.json', 
        'plain'
        )
    with open('gendiff/tests/test_data/expected_plain.txt') as f:
        expected = f.read().strip()
    assert result == expected


def test_plain_yaml():
    result = generate_diff(
        'gendiff/tests/test_data/nested1.yaml', 
        'gendiff/tests/test_data/nested2.yaml', 
        'plain'
        )
    with open('gendiff/tests/test_data/expected_plain.txt') as f:
        expected = f.read().strip()
    assert result == expected
