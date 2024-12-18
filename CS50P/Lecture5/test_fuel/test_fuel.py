from fuel import convert, gauge
import pytest

def test_convert_int():
    assert convert("3/5") == 60
    assert convert("1/2") == 50
    assert convert("1/3") == 33

def test_convert_valueerror():
    with pytest.raises(ValueError):
        convert("5/3")
        convert("z/3")

def test_convert_zerodivisionerror():
    with pytest.raises(ZeroDivisionError):
        convert("3/0")

def test_gauge_e():
    assert gauge(1) == "E"
    assert gauge(0) == "E"

def test_gauge_f():
    assert gauge(100) == "F"
    assert gauge(99) == "F"

def test_gauge_percentage():
    assert gauge(10) == "10%"
    assert gauge(87) == "87%"
