import os, sys
from unittest import TestCase

# Locate src package
sys.path.append(os.path.abspath(os.path.join(__file__,
                                             os.pardir,
                                             os.pardir,
                                             os.pardir,
                                             os.pardir)))

from src.Week5.Practice.isLatinSquare import isLatinSquare

class TestIsLatinSquare(TestCase):
    def test_IsLatinSquare_3x3_Reduced(self):
        self.assertTrue(isLatinSquare([[1,2,3],
                                       [2,3,1],
                                       [3,2,1]]))

    def test_IsLatinSquare_4x4_Reduced(self):
        self.assertTrue(isLatinSquare([[1, 2, 3, 4],
                                       [2, 3, 4, 1],
                                       [3, 4, 1, 2],
                                       [4, 1, 2, 3]]))

    def test_IsLatinSquare_5x5_Reduced(self):
        self.assertTrue(isLatinSquare([[1, 2, 3, 4, 5],
                                        [4, 5, 1, 3, 2],
                                        [5, 3, 4, 2, 1],
                                        [2, 4, 5, 1, 3],
                                        [3, 1, 2, 5, 4]]))

    def test_IsLatinSquare_7x7(self):
        self.assertTrue(isLatinSquare([[0, 1, 2, 3, 4, 5, 6, 7],
                                       [1, 0, 3, 2, 5, 4, 7, 6],
                                       [2, 3, 0, 1, 6, 7, 4, 5],
                                       [3, 2, 1, 0, 7, 6, 5, 4],
                                       [4, 5, 6, 7, 0, 1, 2, 3],
                                       [5, 4, 7, 6, 0, 1, 2, 3],
                                       [6, 7, 4, 5, 2, 3, 0, 1],
                                       [7, 6, 5, 4, 3, 2, 1, 0]]))

    def test_IsLatinSquare_4x4_text_Reduced(self):
        self.assertTrue(isLatinSquare([['A', 'B', 'C', 'D'],
                                       ['B', 'C', 'D', 'A'],
                                       ['C', 'D', 'A', 'B'],
                                       ['D', 'A', 'B', 'C']]))

    def test_IsLatinSquare_4x4_text_First_Row_Duplicate(self):
        self.assertFalse(isLatinSquare([['A', 'B', 'C', 'C'], #Duplicationg in First Row
                                       ['B', 'C', 'D', 'A'],
                                       ['C', 'D', 'A', 'B'],
                                       ['D', 'A', 'B', 'C']]))

    def test_IsLatinSquare_5x5_Last_Column_Duplicate(self):
        self.assertFalse(isLatinSquare([[1, 2, 3, 4, 5],
                                        [4, 5, 1, 3, 2],
                                        [5, 3, 4, 2, 1],
                                        [2, 4, 5, 1, 3],
                                        [3, 1, 2, 5, 3]])) #Duplication in Last Column

    def test_IsLatinSquare_7x7_Multiple_Duplicates(self):
        self.assertFalse(isLatinSquare([[0, 1, 2, 3, 4, 5, 6, 7],
                                        [1, 0, 3, 2, 5, 4, 7, 6],
                                        [2, 3, 0, 1, 6, 7, 4, 5],
                                        [3, 2, 1, 0, 7, 6, 5, 4],
                                        [4, 5, 6, 7, 1, 1, 2, 3],  # Duplicated 1 (Horizontally)
                                        [5, 4, 7, 6, 0, 1, 2, 3],  # Duplicated 1 (Vertically)
                                        [6, 7, 4, 5, 2, 3, 0, 1],
                                        [7, 6, 5, 4, 3, 2, 1, 0]]))
