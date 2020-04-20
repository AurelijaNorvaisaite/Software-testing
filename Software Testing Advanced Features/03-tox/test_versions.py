# This file will be tested on different python versions using tox

def test_dict_keys_ordered():
    """This test will always pass for Python > 3.7. It passes for current distribution of
    3.6 also. Python < 3.6 will fail here, except for lucky situations where the random
    order will match our order"""
    key_order = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k")
    d = {k: k for k in key_order}
    assert tuple(d.keys()) == key_order

def greeting(name):
    return f"Hello, {name}"

def test_greeting():
    assert greeting("Kate") == "Hello, Kate"
