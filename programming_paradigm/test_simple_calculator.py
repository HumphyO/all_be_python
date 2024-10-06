import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(7, 5), 5)
        self.assertEqual(self.calc.subtract(-2, 2), 0)

    def test_miltiplication(self):
        """Test the miltiplication method."""
        result = self.calc.multiply(3, 4)

    def test_divition(self):
        """Test the divide method."""
        result = self.calc.divide(24, 6)