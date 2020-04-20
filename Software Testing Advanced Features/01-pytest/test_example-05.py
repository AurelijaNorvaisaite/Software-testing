import pytest


def shorten(text, max_length):
    if len(text) <= max_length:
        return text
    return text[: max_length - 3] + "..."


@pytest.mark.parametrize(
    "text",
    ["A simple statement.", "This is a longer sentence.", "An exclamation! How rude!"],
)
@pytest.mark.parametrize("max_length", [7, 5, 20, 700])
def test_shortened_text(text, max_length):
    short_text = shorten(text, max_length)
    assert len(short_text) > 0
    if len(text) > max_length:
        assert len(short_text) == max_length
