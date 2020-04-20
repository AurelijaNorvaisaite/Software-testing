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
    assert mock_db.count(55) == 1
    mock_db.count.assert_called_with(55)
    mock_db.count.assert_called_once()

def test_list_tables(mock_db):
    mock_db.list_tables.assert_not_called()
    assert mock_db.list_tables() == ("users",)
    mock_db.list_tables.assert_called_with()
    mock_db.list_tables.assert_called_once()

def test_get(mock_db):
    mock_db.get.assert_not_called()
    assert mock_db.get("users")["username"] == "drake123"
    mock_db.get.assert_called_with("users")
    mock_db.get.assert_called_once_with("users")

