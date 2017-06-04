from unittest import TestCase
from src.Week5.Lab.isLegalSudoku import areLegalValues

class TestAreLegalValues(TestCase):
    def test_AreLegalValues_Length_Not_Perfect_Square(self):
        self.assertFalse(areLegalValues([1, 2, 3, 4, 5]))

    def test_AreLegalValues_Non_Integers(self):
        self.assertFalse(areLegalValues([1, '2', 3, 4, 5, 6, '7', 8, 9]))

    def test_AreLegalValues_Values_Less_Than_Zero(self):
        self.assertFalse(areLegalValues([-1, -2, 3, 4, 5, 0, 7, 8, 9]))

    def test_AreLegalValues_Values_More_Than_Length(self):
        self.assertFalse(areLegalValues([3, 4, 5, 6, 7, 8, 9, 10, 11]))

    def test_AreLegalValues_Repeated_Non_Zero_Values(self):
        self.assertFalse(areLegalValues([1, 2, 3, 4, 4, 6, 7, 8, 9]))

    def test_AreLegalValues_Length_Perfect_Square(self):
        self.assertTrue(areLegalValues([1, 2, 3, 4, 5, 6, 7, 8, 9]))
