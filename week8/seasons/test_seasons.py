from seasons import valid_date
import pytest


def test_correct():
    inp = "2025-10-13"
    assert valid_date(inp) == "Five hundred twenty-five thousand, six hundred minutes"
    inp = "2024-10-13"
    assert valid_date(inp) == "One million, fifty-one thousand, two hundred minutes"


def test_incorrect():
    with pytest.raises(SystemExit):
        valid_date("December 12,1999")
    with pytest.raises(SystemExit):
        valid_date("2025-30-40")
