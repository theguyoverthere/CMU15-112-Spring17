from unittest import TestCase
from src.Week5.Practice.nQueensChecker import multipleQueensAlongRow

class TestMultipleQueensAlongRow(TestCase):

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

            self.assertFalse(multipleQueensAlongRow([[0, 0, 1, 0, 0],
                                                     [0, 0, 0, 0, 0],
                                                     [1, 0, 0, 0, 0],
                                                     [0, 0, 0, 0, 1],
                                                     [0, 0, 0, 0, 0]]))