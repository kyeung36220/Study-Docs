from project import encrypt, decrypt, existing_login
import pytest

def test_decrypt():
    assert decrypt("789789") == "123123"


def test_encrypt():
    assert encrypt("123123") == "789789"


def test_filenotfound():
    with pytest.raises(FileNotFoundError):
        existing_login()
