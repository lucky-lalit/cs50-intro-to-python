from jar import Jar
import pytest


def test_init():
    jar = Jar(10)
    assert jar.capacity == 10
    jar = Jar()
    assert jar.capacity == 12


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(5)
    jar.deposit(3)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.deposit(20)


def test_withdraw():
    jar = Jar(10)
    jar.deposit(6)
    jar.withdraw(2)
    assert jar.size == 4
    with pytest.raises(ValueError):
        jar.withdraw(8)
