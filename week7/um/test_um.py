from um import count

def test_um():
    assert count("dummy") == 0
    assert count("") == 0
    assert count("hello, um ,I am happy") == 1
    assert count("umath") == 0
    assert count("um, ok, um, haha") == 2