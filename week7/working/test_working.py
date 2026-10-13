from working import convert
import pytest


def test_correct():
    inp = "9 AM to 5 PM"
    assert convert(inp) == "09:00 to 17:00"
    inp = "9:00 AM to 5:00 PM"
    assert convert(inp) == "09:00 to 17:00"
    inp = "10 AM to 8:50 PM"
    assert convert(inp) == "10:00 to 20:50"
    inp = "10:30 PM to 8 AM"
    assert convert(inp) == "22:30 to 08:00"


def test_incorrect():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")
