from calculator import square
import pytest
# def main():
#     print("debug2")
#     test_positive()
#     test_negative()
#     test_zero()
    # test_square()


def test_1_positive():
    assert square(2) == 4
    assert square(3) == 9


def test1_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def testzero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square('cat')

# def test_square():
    # assert square(2) == 4
    # assert square(3) == 9
    # assert square(-2) == 4
    # assert square(-3) == 9
    # assert square(0) == 0

    # try:
    #     assert square(2) == 4
    # except AssertionError:
    #     print("2 squared is not 4")
    # try:
    #     assert square(3) == 9
    # except AssertionError:
    #     print("3 squared is not 9")
    # try:
    #     assert square(-2) == 4
    # except AssertionError:
    #     print("-2 squared is not 4")
    # try:
    #     assert square(-3) == 9
    # except AssertionError:
    #     print("-3 squared is not 9")
    # try:
    #     assert square(0) == 0
    # except AssertionError:
    #     print("0 squared is not 0")
    # if square(2) != 4:
    #     print("2 square was not 4")
    # if square(3) != 9:
    #     print("3 square was not 9")

# if __name__ == "__main__":
#     print("debug1")
#     main()

