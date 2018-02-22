import sys, os
sys.path.append(os.path.abspath(os.path.join(__file__,
                                             os.pardir,
                                             os.pardir,
                                             os.pardir,
                                             os.pardir,
                                             os.pardir)))
from unittest import TestCase
from src.Week10.Lab.powerSum import powerSum
from src.Week10.Lab.powerSum import power

class TestAlternatingSum(TestCase):

    # Obvious ones, stated explicitly
    def test_AlternatingSum_negative_n(self):
        self.assertEqual(powerSum(-1, 2), 0)

    def test_AlternatingSum_negative_k(self):
        self.assertEqual(powerSum(1, -7), 0)

    def test_AlternatingSum_negative_n_k(self):
        self.assertEqual(powerSum(-11, -7), 0)

    def test_AlternatingSum_zero_n_k(self):
        self.assertEqual(powerSum(0, 0), 0)

    def test_AlternatingSum_positive_n_k_0(self):
        self.assertEqual(powerSum(2, 3), power(1, 3) + power(2, 3))

    def test_AlternatingSum_positive_n_k_1(self):
        self.assertEqual(powerSum(5, 2), power(1, 2) +
                                         power(2, 2) +
                                         power(3, 2) +
                                         power(4, 2) +
                                         power(5, 2))
