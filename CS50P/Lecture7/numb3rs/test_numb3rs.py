from numb3rs import validate

def test_byte_value():
     assert validate("1000.2000.3000.4000") == False
     assert validate("1000.255.1.3") == False
     assert validate("100.2555.1555.3555") == False
     assert validate("255.256.257.258") == False
     assert validate("10.255.1.3") == True

def test_byte_length():
     assert validate("1.1.1.1.1") == False
     assert validate("1.1.1") == False
     assert validate("cat") == False
     assert validate("1.1.1.1") == True
