"""Sample module and tests for practicing GitHub Actions.

Run locally with:  pytest test.py -v
"""


def add(a, b):
    return a + b


def is_even(n):
    return n % 2 == 0


def test_add():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-1, 1) == 0


def test_is_even():
    assert is_even(4)
    assert not is_even(7)
