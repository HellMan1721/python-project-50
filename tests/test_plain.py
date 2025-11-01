from hexlet_code.generate_diff import generate_diff

def test_plain_json():
    result = generate_diff('tests/test_data/file1.json', 'tests/test_data/file2.json', 'plain')
    with open('tests/test_data/expected_plain.txt') as f:
        expected = f.read().strip()
    assert result == expected

def test_plain_yaml():
    result = generate_diff('tests/test_data/filepath1.yaml', 'tests/test_data/filepath2.yaml', 'plain')
    with open('tests/test_data/expected_plain.txt') as f:
        expected = f.read().strip()
    assert result == expected
