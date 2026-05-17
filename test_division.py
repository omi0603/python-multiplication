import pytest

from division import divide


def test_divide_positive_numbers():
    assert divide(10, 2) == 5


def test_divide_negative_numbers():
    assert divide(-10, 2) == -5
    assert divide(10, -2) == -5
    assert divide(-10, -2) == 5


def test_divide_decimals():
    assert divide(7.5, 2.5) == 3


def test_divide_by_zero_raises_value_error():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
