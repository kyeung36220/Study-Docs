from plates import is_valid

def test_alph_start():
    assert is_valid("1250") == False
    assert is_valid("CS50") == True

def test_length():
    assert is_valid("C") == False
    assert is_valid("CS500000000000000000000000000000") == False

def test_number_placement():
    assert is_valid("CS50P") == False

def test_zero_placement():
    assert is_valid("CS05") == False

def test_alphnumchar():
    assert is_valid("PI3.14") == False
    assert is_valid("Pi3?!4") == False

