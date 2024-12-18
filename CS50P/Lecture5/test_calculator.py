import pytest

from calculator import square #type in terminal "pytest test_calculator.py"

def test_square():
    assert square(2) == 4
def test_negavtive():
    assert square(-3) == 9
def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError): #we expect typerror with string, will be successful
        square("cat")
