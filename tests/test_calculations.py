import unittest
import logging
from io import StringIO
import calculations


class TestCalculationsLogging(unittest.TestCase):

    def setUp(self):
        # Create a string stream to capture logging output
        self.log_stream = StringIO()
        logging.basicConfig(stream=self.log_stream, level=logging.DEBUG)

    def test_add_logging(self):
        calculations.add(3, 4)
        self.assertIn("Adding 3 + 4", self.log_stream.getvalue())

    def test_subtract_logging(self):
        calculations.subtract(10, 5)
        self.assertIn("Subtracting 10 - 5", self.log_stream.getvalue())

    def test_multiply_logging(self):
        calculations.multiply(6, 7)
        self.assertIn("Multiplying 6 * 7", self.log_stream.getvalue())

    def test_divide_logging(self):
        calculations.divide(8, 2)
        self.assertIn("Dividing 8 by 2", self.log_stream.getvalue())

    def test_divide_by_zero_logging(self):
        with self.assertRaises(ValueError):
            calculations.divide(10, 0)
        self.assertIn("Attempted to divide by zero", self.log_stream.getvalue())

    def test_divide_by_0_logging(self):
        calculations.divide_by_0(10, 0)
        self.assertIn("Divisor was 0, defaulting to 1", self.log_stream.getvalue())

if __name__ == '__main__':
    unittest.main()