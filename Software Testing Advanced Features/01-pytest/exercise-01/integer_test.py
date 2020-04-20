def test_string_join():
    assert "." in ".".join(["a", "b", "c"])
    assert "." not in ".".join([])
