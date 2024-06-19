import json
from unittest.mock import patch

from src.utils import get_transactions_data


@patch("builtins.open")
def test_get_transactions_data(mock_open):
    mock_file = mock_open.return_value.__enter__.return_value

    mock_file.read.return_value = json.dumps([{"test": "test"}])
    assert get_transactions_data("test.json") == [{"test": "test"}]

    mock_file.read.return_value = json.dumps({})
    assert get_transactions_data("test.json") == []

    mock_file.read.return_value = json.dumps("testtest")
    assert get_transactions_data("test.json") == []

    mock_file.read.return_value = ""
    assert get_transactions_data("test.json") == []
