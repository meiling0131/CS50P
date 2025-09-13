from plates import is_valid

def test_is_valid():
    assert is_valid("cs50") == True
    assert is_valid("cs05") == False
    assert is_valid("cs50a") == False
    assert is_valid("OUTATIME") == False
    assert is_valid("50cs") == False
    assert is_valid("a") == False
    assert is_valid("PI3.14") == False
    assert is_valid("123456") == False
    assert is_valid("ABC*&%") == False