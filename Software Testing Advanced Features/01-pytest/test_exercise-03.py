import pytest

def test_nonexistent_element():
    ng = NaiveGetter()
    ng.l.append(1)
    assert ng.get_from_list(0) == 1
    with pytest.raises(IndexError):
        assert ng.get_from_list(1) != 1


def test_nonexistent_attribute():
    ng = NaiveGetter()
    with pytest.raises(AttributeError):
        ng.append(1)


def test_nonexistent_key():
    ng = NaiveGetter()
    with pytest.raises(KeyError):
        assert ng.get_from_dict("example") is not None


def test_iterator_stop():
    ng = NaiveGetter()
    ng.l = list(range(3))
    it = ng.get_list_iterator()
    assert next(it) == 0
    assert next(it) == 1
    assert next(it) == 2
    with pytest.raises(StopIteration):
        assert next(it) is None


class NaiveGetter:
    def __init__(self):
        self.l = []
        self.d = {}

    def get_from_list(self, i):
        return self.l[i]

    def get_from_dict(self, k):
        return self.d[k]

    def get_list_iterator(self):
        return iter(self.l)
