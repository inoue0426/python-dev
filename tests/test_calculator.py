import pytest

from src.python_dev import add, divide


def test_add_returns_sum() -> None:
    assert add(2, 3) == 5


def test_divide_returns_quotient() -> None:
    assert divide(10, 2) == 5


def test_divide_rejects_zero_denominator() -> None:
    with pytest.raises(ValueError, match="denominator must not be zero"):
        divide(10, 0)
