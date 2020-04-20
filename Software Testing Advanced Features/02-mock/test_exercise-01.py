"""
1. Write a fixture returning a mocked database object:
    - count() with any parameters should return 1
    - list_tables() should return („users”)
    - get() should return a dictionary with username, first_name, last_name
      and email keys
2. Use the fixture and test each of those functions; Don't forget to check
   parameters passed to them.
"""
import pytest
from unittest.mock import Mock


@pytest.fixture()
def mock_db():
    db = Mock()
    db.count.return_value = 1
    db.list_tables.return_value = ("users",)
    db.get.return_value = {
        "username": "drake123",
        "first_name": "Daniel",
        "last_name": "Smith",
        "email": "drake123@yahoo.com",
    }
    return db


def test_count(mock_db):
    mock_db.count.assert_not_called()
    assert mock_db.count() == 1
    mock_db.count.assert_called_once()


def test_list_tables(mock_db):
    mock_db.list_tables.assert_not_called()
    assert mock_db.list_tables() == ("users",)
    mock_db.list_tables.assert_called_once()


def test_get(mock_db):
    mock_db.get.assert_not_called()
    assert mock_db.get("users")["username"] == "drake123"
    mock_db.get.assert_called_once_with("users")
