from plates import is_valid


def test_len():
    assert is_valid("HELLOY3") == False


def test_character():
    assert is_valid("23") == False


def test_order():
    assert is_valid("Hel2l") == False


def test_special_char():
    assert is_valid("hel4@") == False


def test_zero():
    assert is_valid("hell0") == False
