import pytest


def test_greeen():
    assert 1 > 0


def test_identity_green():
    assert False is not True


def test_exception_fail():
    with pytest.raises(ZeroDivisionError):
        assert 1 / 0
