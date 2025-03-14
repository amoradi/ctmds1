import numpy as np

from cli import random_prices


def test_random_prices_with_valid_arg():
    result = random_prices(3)
    assert isinstance(result, np.ndarray)
    assert len(result) == 3


def test_random_prices_with_valid_zero_arg():
    result = random_prices(0)
    assert isinstance(result, np.ndarray)
    assert len(result) == 0
