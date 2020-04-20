import pytest
from unittest.mock import Mock


def test_exceptions():
    m = Mock()
    m.get.return_value = "ok"
    m.get.side_effect = IndexError

    m.get.assert_not_called()
    with pytest.raises(IndexError):
        m.get(3)
    m.get.assert_called_once_with(3)
