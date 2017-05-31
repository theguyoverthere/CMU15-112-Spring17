from unittest import TestCase
from src.Week5.Practice.nQueensChecker import *

class TestNQueensChecker(TestCase):

    def test_nQueensChecker_multiple_queens_along_row(self):
        with self.subTest():
            self.assertTrue(multipleQueensAlongRow([[0, 0, 1],
                                                    [0, 0, 0],
                                                    [1, 1, 0]]))

            self.assertTrue(multipleQueensAlongRow([[0, 0, 1, 0, 0],
                                                    [0, 0, 0, 0, 0],
                                                    [1, 1, 0, 1, 0],
                                                    [0, 0, 0, 0, 1],
                                                    [0, 0, 0, 0, 0]]))

    def test_nQueensChecker_multiple_queens_along_column(self):
        with self.subTest():
            self.assertTrue(multipleQueensAlongColumns([[1, 0, 0],
                                                        [0, 0, 0],
                                                        [1, 0, 0]]))

            self.assertTrue(multipleQueensAlongColumns([[0, 0, 1, 0, 0],
                                                        [0, 0, 1, 0, 0],
                                                        [1, 0, 1, 0, 0],
                                                        [0, 0, 1, 0, 0],
                                                        [0, 0, 1, 0, 0]]))

    def test_nQueensChecker_multiple_queens_along_right_diagonal(self):
        with self.subTest():
            self.assertTrue(multipleQueensOnRightDiagonals([[0, 1, 0],
                                                            [1, 0, 0],
                                                            [0, 0, 0]]))

            self.assertTrue(multipleQueensOnRightDiagonals([[0, 0, 1],
                                                            [0, 1, 0],
                                                            [1, 0, 0]]))

            self.assertTrue(multipleQueensOnRightDiagonals([[0, 0, 0],
                                                            [0, 0, 1],
                                                            [0, 1, 0]]))

            self.assertTrue(multipleQueensOnRightDiagonals([[0, 0, 1, 0, 0],
                                                            [0, 1, 0, 0, 0],
                                                            [1, 0, 0, 0, 0],
                                                            [0, 0, 0, 0, 0],
                                                            [0, 0, 0, 0, 0]]))

            self.assertTrue(multipleQueensOnRightDiagonals([[0, 0, 0, 0, 1],
                                                            [0, 0, 0, 1, 0],
                                                            [0, 0, 0, 0, 0],
                                                            [0, 1, 0, 0, 0],
                                                            [1, 0, 0, 0, 0]]))

            self.assertTrue(multipleQueensOnRightDiagonals([[0, 0, 0, 0, 0],
                                                            [0, 0, 0, 0, 0],
                                                            [0, 0, 0, 0, 1],
                                                            [0, 0, 0, 0, 0],
                                                            [0, 0, 1, 0, 0]]))

    def test_nQueensChecker_multiple_queens_along_left_diagonal(self):
        with self.subTest():
            self.assertTrue(multipleQueensOnLeftDiagonals([[0, 1, 0],
                                                           [0, 0, 1],
                                                           [0, 0, 0]]))

            self.assertTrue(multipleQueensOnLeftDiagonals([[1, 0, 1],
                                                           [0, 1, 0],
                                                           [1, 0, 1]]))

            self.assertTrue(multipleQueensOnLeftDiagonals([[0, 0, 0],
                                                           [1, 0, 0],
                                                           [0, 1, 0]]))

            self.assertTrue(multipleQueensOnLeftDiagonals([[0, 0, 1, 0, 0],
                                                           [0, 0, 0, 1, 0],
                                                           [0, 0, 0, 0, 1],
                                                           [0, 0, 0, 0, 0],
                                                           [0, 0, 0, 0, 0]]))

            self.assertTrue(multipleQueensOnLeftDiagonals([[1, 0, 0, 0, 0],
                                                           [0, 1, 0, 0, 0],
                                                           [0, 0, 0, 0, 0],
                                                           [0, 0, 0, 1, 0],
                                                           [0, 0, 0, 0, 1]]))

            self.assertTrue(multipleQueensOnLeftDiagonals([[0, 0, 0, 0, 0],
                                                           [0, 0, 0, 0, 0],
                                                           [1, 0, 0, 0, 0],
                                                           [0, 0, 0, 0, 0],
                                                           [0, 0, 1, 0, 0]]))


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
            #Vertical Duplicate - Column 3
            self.assertFalse(nQueensChecker([[0, 0, 0, 1, 0, 0, 0, 0],
                                             [0, 0, 0, 0, 0, 0, 1, 0],
                                             [0, 0, 1, 0, 0, 0, 0, 0],
                                             [1, 0, 0, 1, 0, 0, 0, 0],
                                             [0, 1, 0, 0, 0, 0, 0, 0],
                                             [0, 0, 0, 0, 1, 0, 0, 0],
                                             [1, 0, 0, 0, 0, 0, 0, 0],
                                             [0, 0, 0, 0, 0, 1, 0, 0]]))

            # Duplicate in Diagonal slanting towards right (Longest Diagonal)
            self.assertFalse(nQueensChecker([[0, 1, 0, 0, 0, 0, 0, 0],
                                             [0, 0, 0, 0, 0, 0, 1, 0],
                                             [0, 0, 0, 0, 0, 0, 0, 0],
                                             [0, 0, 0, 0, 0, 0, 0, 0],
                                             [0, 0, 0, 0, 0, 0, 0, 0],
                                             [0, 0, 0, 0, 0, 0, 0, 0],
                                             [0, 0, 0, 0, 0, 0, 0, 0],
                                             [1, 0, 0, 0, 0, 0, 0, 0],]))

            # Duplicate in Diagonal slanting towards left (Longest Diagonal)
            self.assertFalse(nQueensChecker([[1, 0, 0, 0, 0, 0, 0, 0],
                                             [0, 0, 0, 0, 0, 0, 1, 0],
                                             [0, 0, 0, 0, 0, 0, 0, 0],
                                             [0, 0, 0, 0, 0, 0, 0, 1],
                                             [0, 1, 0, 0, 0, 0, 0, 0],
                                             [0, 0, 0, 0, 1, 1, 0, 0],
                                             [0, 0, 0, 0, 0, 0, 0, 0],
                                             [0, 0, 0, 0, 0, 0, 0, 0],]))
