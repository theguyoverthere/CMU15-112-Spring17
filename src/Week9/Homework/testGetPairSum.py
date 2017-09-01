from src.Week9.Homework.getPairSum import getPairSum
from unittest import TestCase

class TestPairSum(TestCase):

    def test_getPairSum(self):
        self.assertEqual(getPairSum([1], 1), [])
        self.assertTrue(getPairSum([5, 2], 7) in [ [5, 2], [2, 5] ])
        self.assertTrue(getPairSum([10, -1, 1, -8, 3, 1], 2) in [[10, -8], [-8, 10], [-1, 3], [3, -1], [1, 1]])
        self.assertEqual(getPairSum([10, -1, 1, -8, 3, 1], 10), [])
        self.assertEqual(getPairSum([1, 4, 3], 2), [])
