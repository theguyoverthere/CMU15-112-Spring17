from unittest import TestCase
from src.Week5.Practice.nQueensChecker import multipleQueensAlongColumns

class TestMultipleQueensAlongColumns(TestCase):

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

            self.assertFalse(multipleQueensAlongColumns([[0, 0, 1, 0, 0],
                                                         [0, 0, 0, 0, 0],
                                                         [1, 0, 0, 0, 0],
                                                         [0, 0, 0, 0, 0],
                                                         [0, 0, 0, 0, 0]]))
