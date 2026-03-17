from __future__ import annotations


def mean_regression(values: list[float]) -> float:
    """Return a trivial baseline prediction for regression tasks."""
    if not values:
        raise ValueError("values must not be empty")
    return sum(values) / len(values)
