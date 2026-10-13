from numb3rs import validate


def test_corr():
    inp = "255.2.3.4"
    assert validate(inp) == True
    inp = "1.2.3.4"
    assert validate(inp) == True


def test_incorr():
    inp = "cat"
    assert validate(inp) == False
    inp = "295.0.0.0"
    assert validate(inp) == False
    inp = "1.1.1.999"
    assert validate(inp) == False
