from collections import Counter
import pytest

@pytest.mark.parametrize(
    "word,other_word",
    [
        ("Flsea", "False"),
        ("Agf", "gfA"),
        ("kayak", "aaykk"),
        ("Kayak", "yaakK"),
        ("eurT", "True"),
        ("eslalF", "a"),
    ],
)
def test_is_anagram(word, other_word):
    """is_anagram checks whether other_word is an anagram of word"""
    if len(word) == 0 or len(other_word) == 0:
        with pytest.raises(AssertionError):
            assert False
        assert Counter(word) == Counter(other_word)





def validate_coordinates(latitude, longitude):
    """validate_coordinates checks whether provided latitude and 
    longitude constitute a valid pair of GPS coordinates"""
    assert -90.0 <= latitude <= 90 and -180.0 <= longitude <= 180.0

@pytest.mark.parametrize(
    "latitude,longitude",
    [
        (90, 180),
        (10, 90),
        (-10, -2),
        (-10, -20),
        (2, 30),
        (120, 50),
    ],
)
def test_validate_coordinates(latitude, longitude):
    with pytest.raises(AssertionError):
        assert validate_coordinates(latitude, longitude)

@pytest.mark.parametrize(
    "latitude,longitude",
    [
        (90, 180),
        (10, 90),
        (-10, -2),
        (-10, -20),
        (2, 30),
        (120, 50),
    ],
)
def test_coordinates_negative(latitude, longitude):
    assert validate_coordinates(latitude, longitude) is False