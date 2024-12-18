from bank import value

def test_values():
    assert value("Hello") == 0
    assert value("Heya") == 20
    assert value("Sup") == 100

def test_case():
    assert value("HeLlo") == 0
    assert value("heYa") == 20
    assert value("sUp") == 100

def test_phrase():
    assert value("Hello Mister") == 0
    assert value("heYa Pal") == 20
    assert value("sUp John") == 100
