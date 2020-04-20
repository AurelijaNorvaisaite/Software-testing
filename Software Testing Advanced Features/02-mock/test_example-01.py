from unittest.mock import Mock

# Let's mock 'json' library
json = Mock()


def test_json_loads_called():
    assert isinstance(json, Mock)
    json.loads.assert_not_called()
    json_str = '{"example": 1}'
    json.loads(json_str)
    json.loads.assert_called_once_with(json_str)
