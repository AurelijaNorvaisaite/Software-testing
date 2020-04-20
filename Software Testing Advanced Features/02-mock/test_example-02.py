from db import DB
from unittest.mock import Mock


def test_db_connection_real():
    db = DB()  # db simulates slow database connection
    assert len(db.list_tables()) == 3
    assert db.list_tables() == ("users", "products", "orders")


def test_db_connection_mock():
    db = Mock()
    db.list_tables.return_value = ("users", "products", "orders")
    assert len(db.list_tables()) == 3
    assert db.list_tables() == ("users", "products", "orders")
