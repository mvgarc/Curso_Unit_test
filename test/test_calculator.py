import unittest

from src.calculator import sum,subtract,multiply,divide

class CalculatorTests(unittest.TestCase):

    def test_sum(self):
        assert sum(2, 3) == 5
