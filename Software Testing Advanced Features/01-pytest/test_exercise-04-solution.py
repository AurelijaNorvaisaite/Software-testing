import pytest
from collections import Counter

def is_anagram(word, other_word):
    """is_anagram checks whether other_word is an anagram of word"""
    if len(word) == 0 or len(other_word) == 0:
        return False
    return Counter(word) == Counter(other_word)

def validate_coordinates(latitude, longitude):
    """validate_coordinates checks whether provided latitude and 
    longitude constitute a valid pair of GPS coordinates"""
    return -90.0 <= latitude <= 90 and -180.0 <= longitude <= 180.0

@pytest.mark.parametrize(
    "w, ow", [("arc", "car"), ("rat", "tar"), ("stressed", "desserts")]
)
def test_is_anagram_positive(w, ow):
    assert is_anagram(w, ow)

@pytest.mark.parametrize(
    "w, ow", [("arc", "cars"), ("rat", "tattered"), ("stressed", "deserts")]
)
def test_is_anagram_negative(w, ow):
    assert is_anagram(w, ow) is False

@pytest.mark.parametrize("latitude", [35.1, -2.0, -90.0])
@pytest.mark.parametrize("longitude", [7.0, 180.0, -64.3331])
def test_coordinates_positive(latitude, longitude):
    assert validate_coordinates(latitude, longitude)

@pytest.mark.parametrize("latitude", [120.0, -360.0])
@pytest.mark.parametrize("longitude", [1500.3, -360.0])
def test_coordinates_negative(latitude, longitude):
    assert validate_coordinates(latitude, longitude) is False
