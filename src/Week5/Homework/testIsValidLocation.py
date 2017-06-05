from unittest import TestCase
from src.Week5.Homework.isKingsTour import isValidLocation

class TestValidLocation(TestCase):

    def test_IsValidLocation_False(self):
        self.assertFalse(isValidLocation([[1,2,3],
                                          [2,3,1],
                                          [3,2,1]], 2, 10))

    def test_IsValidLocation_True(self):
        self.assertTrue(isValidLocation([[1,2,3],
                                         [1,3,1],
                                         [0,2,1]], 2, 1))
