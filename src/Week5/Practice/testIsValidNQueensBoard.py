from unittest import TestCase
from src.Week5.Practice.nQueensChecker import isValidNQueensBoard

class TestNQueensChecker(TestCase):

    def test_isValidNQueensBoard_8x8_with_8_queens(self):
        self.assertTrue(isValidNQueensBoard([[0, 0, 0, 1, 0, 0, 0, 0],
                                             [0, 0, 0, 0, 0, 0, 1, 0],
                                             [0, 0, 1, 0, 0, 0, 0, 0],
                                             [0, 0, 0, 0, 0, 0, 0, 1],
                                             [0, 1, 0, 0, 0, 0, 0, 0],
                                             [0, 0, 0, 0, 1, 0, 0, 0],
                                             [1, 0, 0, 0, 0, 0, 0, 0],
                                             [0, 0, 0, 0, 0, 1, 0, 0],]))


    def test_isValidNQueensBoard_8x8_with_12_queens(self):
        self.assertFalse(isValidNQueensBoard([[1, 0, 0, 1, 0, 0, 0, 0],
                                             [0, 1, 0, 0, 0, 0, 1, 0],
                                             [0, 0, 1, 0, 1, 0, 0, 0],
                                             [0, 0, 0, 0, 0, 0, 0, 1],
                                             [0, 1, 0, 0, 0, 0, 0, 0],
                                             [0, 0, 0, 0, 1, 0, 0, 0],
                                             [1, 0, 0, 1, 0, 0, 0, 0],
                                             [0, 0, 0, 0, 0, 1, 0, 0],]))


    def test_isValidNQueensBoard_2x3_with_2_queens(self):
        self.assertFalse(isValidNQueensBoard([[1, 0, 0],
                                              [0, 1, 0]]))

print(isValidNQueensBoard([[0, 0, 0, 1, 0, 0, 0, 0],
                                             [0, 0, 0, 0, 0, 0, 1, 0],
                                             [0, 0, 1, 0, 0, 0, 0, 0],
                                             [1, 0, 0, 1, 0, 0, 0, 0],
                                             [0, 1, 0, 0, 0, 0, 0, 0],
                                             [0, 0, 0, 0, 1, 0, 0, 0],
                                             [1, 0, 0, 0, 0, 0, 0, 0],
                                             [0, 0, 0, 0, 0, 1, 0, 0]]))