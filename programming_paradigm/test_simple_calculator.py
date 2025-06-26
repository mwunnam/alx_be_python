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

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 4), 8)
        self.assertEqual(self.calc.multiply(0, 4), 0)
        self.assertEqual(self.calc.multiply(0.5, 2), 1)

    def test_division(self):
         self.assertEqual(self.calc.divide(8, 2), 4)
         self.assertEqual(self.calc.divide(6, 2), 3)
         self.assertEqual(self.calc.divide(5, 2), 2.5)
         self.assertEqual(self.calc.divide(3, 0), None)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(4, 4), 0)
        self.assertEqual(self.calc.subtract(4, 5), -1)
        self.assertEqual(self.calc.subtract(4, 0), 4)

