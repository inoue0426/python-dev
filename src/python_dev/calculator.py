"""Small template module used by tests and quality checks."""


def add(left: int, right: int) -> int:
    """Return the sum of two integers."""
    return left + right


def divide(numerator: float, denominator: float) -> float:
    """Return numerator divided by denominator.

    Raises:
        ValueError: If denominator is zero.
    """
    if denominator == 0:
        raise ValueError("denominator must not be zero")

    return numerator / denominator
