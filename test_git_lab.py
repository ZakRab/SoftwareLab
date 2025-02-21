import unittest
from git_lab import (
    calculate_circle_area,
    celsius_to_fahrenheit,
    is_palindrome,
    calculate_triangle_area,
    is_prime,
    add_numbers,
    subtract_numbers,
    add_positive_numbers

)
import math

class TestUtils(unittest.TestCase):

    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)
    def test_subtract_numbers(self):
        self.assertEqual(subtract_numbers(2, 3), -1)
        self.assertEqual(subtract_numbers(-1, 1), -2)
    def test_add_positive_numbers(self):
        self.assertEqual(add_positive_numbers([1, -2, 3, 4]), 8)
        self.assertEqual(add_positive_numbers([-1, -2, -3]), 0)

if __name__ == '__main__':
    unittest.main()