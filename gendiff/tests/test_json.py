import json

from gendiff.diff import generate_diff


def test_json_format():
    file1 = 'gendiff/tests/test_data/nested1.json'
    file2 = 'gendiff/tests/test_data/nested2.json'
    
    result = generate_diff(file1, file2, 'json')
    
    parsed = json.loads(result)
    assert isinstance(parsed, dict)
    
    assert 'common' in parsed
    assert parsed['common']['type'] == 'nested'