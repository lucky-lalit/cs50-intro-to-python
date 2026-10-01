import pytest
from fuel import convert
from fuel import gauge


def test_fraction():
    assert convert("1/4") == 25
    assert convert("1/2") == 50
    assert convert("3/4") == 75


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(25) == "25%"


def test_edge():
    assert convert("4/4") == 100
    assert convert("0/1") == 0


def test_error():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")
    with pytest.raises(ValueError):
        convert("three/four")
        # convert("-1/4")
        # convert("5/4")
    with pytest.raises(ValueError):
        convert("-1/4")
    # with pytest.raises(ValueError):
        # convert("5/4")
