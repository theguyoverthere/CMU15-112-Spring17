import sys, os
sys.path.append(os.path.abspath(os.path.join(__file__,
                                             os.pardir,
                                             os.pardir,
                                             os.pardir,
                                             os.pardir,
                                             os.pardir)))
from unittest import TestCase
from src.Week10.Lab.alternatingSum import alternatingSum

class TestAlternatingSum(TestCase):
    def test_Alternating_Sum_Empty_List(self):
        self.assertEqual(alternatingSum([]), 0)

    def test_Alternating_Sum_Non_Empty_List(self):
        self.assertEqual(alternatingSum([1]), 1)
        self.assertEqual(alternatingSum([1, 2, 3, 4]), -2)
        self.assertEqual(alternatingSum([1, 2, 3, 4, 5]), 3)
