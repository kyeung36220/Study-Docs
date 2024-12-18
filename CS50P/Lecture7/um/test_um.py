from um import count
import pytest

def test_count():
    assert count("yummy") == 0

def test_unspaced_um():
    assert count("Um, yes I love um... crepes.") == 2

def test_case():
    assert count("Um, yes I love uM... crepes.") == 2
