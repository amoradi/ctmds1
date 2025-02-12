import unittest
from unittest.mock import patch
import io
import sys
import numpy as np
from generate_random_prices import (
    generate_random_prices, 
    main,
    ERR_NOT_INTEGER,
    ERR_NO_ARGUMENT
)

class TestGenerateRandomPrices(unittest.TestCase):
    def setUp(self):
        self.held_output = io.StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_generate_random_prices_return_value(self):
        """Test the returned array from generate_random_prices"""
        prices = generate_random_prices(3)
        
        self.assertIsInstance(prices, np.ndarray)
        self.assertEqual(len(prices), 3)
        self.assertTrue(all(0 <= x <= 100 for x in prices))
        
        # Better decimal place testing
        for price in prices:
            self.assertAlmostEqual(price, round(price, 2), places=2)

    def test_generate_random_prices_with_printing(self):
        """Test if printing works correctly when enabled"""
        prices = generate_random_prices(3, print_output=True)
        output = self.held_output.getvalue().strip().split('\n')
        
        self.assertEqual(len(output), 3)
        # Verify printed values match returned array
        for printed, returned in zip(output, prices):
            self.assertEqual(float(printed), returned)

    def test_generate_random_prices_without_printing(self):
        """Test that nothing is printed when print_output is False"""
        _ = generate_random_prices(3, print_output=False)
        self.assertEqual(self.held_output.getvalue().strip(), '')

    @patch('sys.argv', ['script.py', '3'])
    def test_main_valid_input(self):
        """Test main function with valid input"""
        result = main()
        self.assertIsInstance(result, np.ndarray)
        self.assertEqual(len(result), 3)
        
        # Check that it printed (main always prints)
        output = self.held_output.getvalue().strip().split('\n')
        self.assertEqual(len(output), 3)

    @patch('sys.argv', ['script.py', 'abc'])
    def test_main_non_digit_input(self):
        """Test main function with non-digit input"""
        result = main()
        self.assertIsNone(result)
        self.assertEqual(
            self.held_output.getvalue().strip(),
            ERR_NOT_INTEGER
        )

    @patch('sys.argv', ['script.py'])
    def test_main_missing_argument(self):
        """Test main function with missing argument"""
        result = main()
        self.assertIsNone(result)
        self.assertEqual(
            self.held_output.getvalue().strip(),
            ERR_NO_ARGUMENT
        )

    def test_random_distribution(self):
        """Test if numbers are reasonably distributed"""
        np.random.seed(42)  # Set seed for reproducibility
        prices = generate_random_prices(1000)
        
        # Test mean is roughly 50 (allowing for some randomness)
        self.assertTrue(45 < np.mean(prices) < 55)
        
        # Test all numbers are within bounds
        self.assertTrue(all(0 <= x <= 100 for x in prices))
        
        # Test uniqueness (random numbers should not all be the same)
        self.assertTrue(len(set(prices)) > 1)

if __name__ == '__main__':
    unittest.main()
