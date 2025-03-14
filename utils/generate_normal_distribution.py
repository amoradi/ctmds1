import numpy as np


def generate_normal_distribution(mean: int, size: int = 24, decimals=2) -> np.ndarray:
    """
    Generate numbers following a normal distribution.

    Args:
        mean: Mean (average) of the distribution
        size: Number of values to generate

    Returns:
        Array of normally distributed numbers
    """
    return np.round(np.random.normal(loc=mean, scale=1, size=size), decimals)
