from twttr import shorten

def test_lowercase():
    assert shorten("Twitter") == "Twttr"
    assert shorten("Donald Trump") == "Dnld Trmp"
    assert shorten("AeIoU") == ""

def test_uppercase():
    assert shorten("POLAR") == "PLR"
    assert shorten("AEIOU") == ""

def test_novowels():
    assert shorten("nvwls") == "nvwls"

def test_numbers():
    assert shorten("123") == "123"

def test_punctuation():
    assert shorten("...") == "..."
