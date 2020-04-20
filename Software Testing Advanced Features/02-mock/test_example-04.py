import pytest
import datetime
from unittest.mock import patch


@pytest.fixture
def override_time():
    """Sets current date to 1999-12-31T23:59.00"""
    date = datetime.datetime(1999, 12, 31, 23, 59, 0)
    with patch("datetime.datetime") as patched_datetime:
        patched_datetime.now.return_value = date
        yield


def test_current_date(override_time):
    now = datetime.datetime.now()
    assert now.year == 1999
    assert now.month == 12
    assert now.day == 31


def test_current_date_no_override():
    assert datetime.datetime.now().year > 1999
