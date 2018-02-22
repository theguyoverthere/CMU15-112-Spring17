import sys, os

sys.path.append(os.path.abspath(os.path.join(__file__,
                                             os.pardir,
                                             os.pardir,
                                             os.pardir,
                                             os.pardir,
                                             os.pardir)))
import unittest
from src.Week10.Lab.powerSum import power


class TestPower(unittest.TestCase):
    # Base = 0
    def test_Power_base_zero(self):
        self.assertEqual(power(0, -10), 0)
        self.assertEqual(power(0, 0), 1)
        self.assertEqual(power(0, 10), 0)

    # Base < 0
    def test_Power_base_negative_exponent_negative(self):
        self.assertEqual(power(-2, -3), -1/8)
        self.assertEqual(power(-3, 0), 1)
        self.assertEqual(power(-5, 3), -125)

    # Base > 0
    def test_Power_base_positive_negative_exponent(self):
        self.assertEqual(power(2, -3), 1/8)
        self.assertEqual(power(3, 0), 1)
        self.assertEqual(power(5, 3), 125)


if __name__ == "__main__":
    unittest.main()