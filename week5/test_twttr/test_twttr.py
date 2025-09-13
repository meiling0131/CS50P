from twttr import shorten

def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("Jolin") == "Jln"
    assert shorten("Merlin") == "Mrln"
    assert shorten("12ae") == "12"
    assert shorten("AEIOU") == ""
    assert shorten("aeiou") == ""
    assert shorten("No, he is a boy") == "N, h s  by"