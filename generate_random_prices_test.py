import sys
import pytest
import numpy as np
from generate_random_prices import generate_random_prices, main, ERR_NOT_INTEGER, ERR_NO_ARGUMENT

def test_generate_random_prices_returns_correct_length():
    """Test if function returns array of requested length"""
    result = generate_random_prices(3)
    assert len(result) == 3

def test_generate_random_prices_within_range():
    """Test if all prices are between 0 and 100"""
    result = generate_random_prices(100)
    assert all(0 <= price <= 100 for price in result)

def test_generate_random_prices_decimal_places():
    """Test if prices have 2 decimal places"""
    result = generate_random_prices(10)
    for price in result:
        assert abs(price - round(price, 2)) < 1e-10

def test_generate_random_prices_return_type():
    """Test if return value is numpy array"""
    result = generate_random_prices(5)
    assert isinstance(result, np.ndarray)

def test_random_distribution():
    """Test if numbers are reasonably distributed"""
    np.random.seed(42)  # For reproducibility
    result = generate_random_prices(1000)
    mean = np.mean(result)
    assert 45 < mean < 55  # Should be roughly centered around 50

def test_generate_random_prices_uniqueness():
    """Test if generated numbers aren't all the same"""
    result = generate_random_prices(100)
    assert len(set(result)) > 1

def test_main_with_invalid_arg(monkeypatch):
    """Test main function with non-digit input"""
    monkeypatch.setattr(sys, 'argv', ['script.py', 'abc'])
    result = main()
    assert result is None

def test_main_with_missing_arg(monkeypatch):
    """Test main function with missing argument"""
    monkeypatch.setattr(sys, 'argv', ['script.py'])
    result = main()
    assert result is None

def test_main_with_valid_arg(monkeypatch):
    """Test main function with valid input"""
    monkeypatch.setattr(sys, 'argv', ['script.py', '3'])
    result = main()
    assert isinstance(result, np.ndarray)
    assert len(result) == 3
