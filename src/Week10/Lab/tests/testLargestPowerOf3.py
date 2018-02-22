import sys, os

sys.path.append(os.path.abspath(os.path.join(__file__,
                                             os.pardir,
                                             os.pardir,
                                             os.pardir,
                                             os.pardir,
                                             os.pardir)))
import unittest
from src.Week10.Lab.powersOf3ToN import largestPowerOf3

class TestLargestPowerOf3(unittest.TestCase):

    def test_LargestPowerOf3_negative_n(self):
        self.assertEqual(largestPowerOf3(-7.8), None,
                         msg="None expected for n < 0.")
        self.assertEqual(largestPowerOf3(-1.0), None,
                         msg="None expected for n < 0.")
        self.assertEqual(largestPowerOf3(-3), None,
                         msg = "None expected for n < 0.")

    def test_LargestPowerOf3_positive_n_below_1(self):
        self.assertEqual(largestPowerOf3(0.8), None,
                         msg="None expected for n >=0 and n < 1.")
        self.assertEqual(largestPowerOf3(0.99999999), None,
                         msg="None expected for n >=0 and n < 1.")
        self.assertEqual(largestPowerOf3(0), None,
                         msg="None expected for n >=0 and n < 1.")


    def test_LargestPowerOf3_positive_n_above_1(self):
        self.assertEqual(largestPowerOf3(1), 1)
        self.assertEqual(largestPowerOf3(2), 1)
        self.assertEqual(largestPowerOf3(3), 3)
        self.assertEqual(largestPowerOf3(7), 3)
        self.assertEqual(largestPowerOf3(100), 81)


if __name__ == "__main__":
    unittest.main()

