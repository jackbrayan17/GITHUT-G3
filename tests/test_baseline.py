from src.models.baseline import mean_regression


def test_mean_regression_returns_average() -> None:
    assert mean_regression([1.0, 2.0, 3.0]) == 2.0
