import sys, os
sys.path.append(os.path.abspath(os.path.join(__file__,
                                             os.pardir,
                                             os.pardir,
                                             os.pardir,
                                             os.pardir,
                                             os.pardir)))
import unittest
from src.Week10.Lab.powersOf3ToN import powersOf3ToN

class TestPowersOf3ToN(unittest.TestCase):

    def setUp(self):
        pass

    def test_PowersOf3ToN_negative_input(self):
        self.assertEqual(powersOf3ToN(- 7), None)
        self.assertEqual(powersOf3ToN(- 1.7), None)

    def test_PowersOf3ToN_zero(self):
        self.assertEqual(powersOf3ToN(0), None)

    def test_PowersOf3ToN_positive_input(self):
        self.assertEqual(powersOf3ToN(0.5), None)
        self.assertEqual(powersOf3ToN(0.9999999999999999), None)
        self.assertEqual(powersOf3ToN(1), [1])
        self.assertEqual(powersOf3ToN(9), [1, 3, 9])
        self.assertEqual(powersOf3ToN(27), [1, 3, 9, 27])
        self.assertEqual(powersOf3ToN(2.99999999999999), [1])
        self.assertEqual(powersOf3ToN(27.00000000000001), [1, 3, 9, 27])
        self.assertEqual(powersOf3ToN(27.00000000000000), [1, 3, 9, 27])
        self.assertEqual(powersOf3ToN(107.00000000000000), [1, 3, 9, 27, 81])

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()