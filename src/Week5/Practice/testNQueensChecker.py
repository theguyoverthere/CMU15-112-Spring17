from unittest import TestCase
from src.Week5.Practice.nQueensChecker import nQueensChecker

class TestNQueensChecker(TestCase):

    def test_nQueensChecker_Valid_nQueens_Board(self):
        self.assertTrue(nQueensChecker([[0, 0, 0, 1, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 0, 1, 0],
                                        [0, 0, 1, 0, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 0, 0, 1],
                                        [0, 1, 0, 0, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 1, 0, 0, 0],
                                        [1, 0, 0, 0, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 1, 0, 0],]))

    def test_nQueensChecker_Invalid_nQueens_Board(self):
        with self.subTest():
            #Vertical Duplicate - Column 3. Also on Left Diagonal
            self.assertFalse(nQueensChecker([[0, 0, 0, 1, 0, 0, 0, 0],
                                             [0, 0, 0, 0, 0, 0, 1, 0],
                                             [0, 0, 1, 0, 0, 0, 0, 0],
                                             [0, 0, 0, 1, 0, 0, 0, 0],
                                             [0, 1, 0, 0, 0, 0, 0, 0],
                                             [0, 0, 0, 0, 1, 0, 0, 0],
                                             [1, 0, 0, 0, 0, 0, 0, 0],
                                             [0, 0, 0, 0, 0, 1, 0, 0]]))

            # Duplicate in Diagonal slanting towards right (Longest Diagonal)
            self.assertFalse(nQueensChecker([[0, 0, 0, 0, 0, 0, 0, 1],
                                             [0, 0, 0, 0, 0, 0, 1, 0],
                                             [0, 0, 0, 0, 0, 1, 0, 0],
                                             [0, 0, 0, 0, 1, 0, 0, 0],
                                             [0, 0, 0, 1, 0, 0, 0, 0],
                                             [0, 0, 1, 0, 0, 0, 0, 0],
                                             [0, 1, 0, 0, 0, 0, 0, 0],
                                             [1, 0, 0, 0, 0, 0, 0, 0],]))

            # Duplicate in Diagonal slanting towards left (Longest Diagonal)
            self.assertFalse(nQueensChecker([[1, 0, 0, 0, 0, 0, 0, 0],
                                             [0, 1, 0, 0, 0, 0, 1, 0],
                                             [0, 0, 1, 0, 0, 0, 0, 0],
                                             [0, 0, 0, 1, 0, 0, 0, 1],
                                             [0, 0, 0, 0, 1, 0, 0, 0],
                                             [0, 0, 0, 0, 0, 1, 0, 0],
                                             [0, 0, 0, 0, 0, 0, 1, 0],
                                             [0, 0, 0, 0, 0, 0, 0, 1],]))
