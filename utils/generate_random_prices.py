import numpy as np


def generate_random_prices(num: int) -> np.ndarray:
    """
    Generate random prices between 0 and 100 with 2 decimal places

    Args:
        num (int): Number of prices to generate

    Returns:
        numpy.ndarray: Array of random prices
    """
    prices = np.round(np.random.uniform(0, 100, size=num), 2)

    return prices
