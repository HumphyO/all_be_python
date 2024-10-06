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
        self.assertEqual(self.calc.multiply(9, 5), 7)
        self.assertEqual(self.calc.multiply(-6, 5), 2)

    def test_divition(self):
        """Test the divide method."""
        self.assertEqual(self.calc.divide(6, 4), 5)
        self.assertEqual(self.calc.divide(-13, 7), 1)