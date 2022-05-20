import unittest
from calculation import Calculator

class CalculatorTest(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_last_answer_init(self):
        value = self.calc.last_answer()
        self.assertEqual(value, 0.0)

    def test_add(self):
        value = self.calc.add(10, 5)
        self.assertEqual(value, 15.0)
        self.assertEqual(value, self.calc.last_answer())

    def test_subtract(self):
        value = self.calc.subtract(10, 5)
        self.assertEqual(value, 5.0)
        self.assertEqual(value, self.calc.last_answer())

    def test_subtract_negative(self):
        value = self.calc.subtract(5, 10)
        self.assertEqual(value, -5.0)
        self.assertEqual(value, self.calc.last_answer())

    def test_multiply(self):
        value = self.calc.multiply(3, 2)
        self.assertEqual(value, 6.0)
        self.assertEqual(value, self.calc.last_answer())

    def test_divide(self):
        value = self.calc.divide(10, 5)
        self.assertEqual(value, 2.0)
        self.assertEqual(value, self.calc.last_answer())

    def test_divide_by_zero(self):
        self.assertRaises(ZeroDivisionError, self.calc.divide, 5, 0)