import os, sys
from unittest import TestCase

# Locate src package
sys.path.append(os.path.abspath(os.path.join(__file__,
                                             os.pardir,
                                             os.pardir,
                                             os.pardir,
                                             os.pardir)))

from src.Week5.Practice.nQueensChecker import multipleQueensOnRightDiagonals

class TestMultipleQueensOnRightDiagonals(TestCase):

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