from bank import value


def test_complete():
    inp = "hellowelcome"
    assert value(inp) == 0
    inp = "Hello welcome"
    assert value(inp) == 0


def test_firstletter():
    inp = "hiiwelcome"
    assert value(inp) == 20
    inp = "happybirthday"
    assert value(inp) == 20


def test_incoorect():
    inp = "goodmoring"
    assert value(inp) == 100
    inp = "welcome"
    assert value(inp) == 100
