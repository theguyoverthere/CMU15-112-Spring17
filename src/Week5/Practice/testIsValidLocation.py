from unittest import TestCase
from src.Week5.Practice.isKnightsTour import isValidLocation

class TestValidLocation(TestCase):
    def test_IsValidLocation(self):
        self.assertFalse(isValidLocation([[1,2,3],
                                        [2,3,1],
                                        [3,2,1]], 2, 10))

    def test_IsLatinSquare_4x4_Reduced(self):
        self.assertTrue(isValidLocation([[1,2,3],
                                         [1,3,1],
                                         [0,2,1]], 2, 1))
