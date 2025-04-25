import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(5,6), 11)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(15,10), 5)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(5,6), 30)

    def test_divide(self):
        self.assertEqual(self.calc.divide(15,5), 3)
        with self.assertRaises(ValueError):
            self.calc.divide(10,0)

