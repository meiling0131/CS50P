from bank import value

def test_value():
    assert value("hello") == 0
    assert value("Hello world") == 0
    assert value(" hello ") == 0
    assert value("hi") == 20
    assert value("What's happening") == 100



