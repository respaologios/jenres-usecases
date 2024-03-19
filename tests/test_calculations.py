import unittest
import calculations

class TestCalculations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculations.add(3, 4), 7)

    def test_subtract(self):
        self.assertEqual(calculations.subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(calculations.multiply(6, 7), 42)

    def test_divide(self):
        self.assertEqual(calculations.divide(8, 2), 4)
        with self.assertRaises(ValueError):
            calculations.divide(10, 0)

    def test_divide_by_0(self):
        self.assertEqual(calculations.divide_by_0(10, 0), 10)

if __name__ == '__main__':
    unittest.main()