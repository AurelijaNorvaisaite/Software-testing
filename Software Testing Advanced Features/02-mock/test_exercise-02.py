"""
When DB.get() is called:
    - With non-existent table_name it raises a KeyError
    - With non-existent index it raises an IndexError

Use Mock() with side_effect to make the tests in 02-mock/test_exercise-02.py run faster.
"""

import pytest
from unittest.mock import Mock

def test_get_with_non_existent_table():
    db = Mock()
    db.get.side_effect = KeyError
    with pytest.raises(KeyError):
        db.get("non-existent db", 1)


def test_get_with_non_index():
    db = Mock()
    db.get.side_effect = IndexError
    db.count.return_value = 4
    next_user_idx = db.count("users")
    with pytest.raises(IndexError):
        db.get("users", next_user_idx)
