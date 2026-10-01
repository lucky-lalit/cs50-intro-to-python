import pytest
from twttr import shorten


def test_mix():
    assert shorten("Hello welcome to Jungle") == "Hll wlcm t Jngl"
    assert shorten("hello better luck") == "hll bttr lck"


def test_capital():
    assert shorten("HELLO WELCOME TO JUNGLE") == "HLL WLCM T JNGL"


def test_number():
    assert shorten("hello 123 goodbyy!!") == "hll 123 gdbyy!!"
