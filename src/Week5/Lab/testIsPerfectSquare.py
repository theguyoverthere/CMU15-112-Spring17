import os, sys
from unittest import TestCase

# Locate src package
sys.path.append(os.path.abspath(os.path.join(__file__,
                                             os.pardir,
                                             os.pardir,
                                             os.pardir,
                                             os.pardir)))

from src.Week5.Lab.isLegalSudoku import isPerfectSquare

class TestIsPerfectSquare(TestCase):

    def test_isPerfectSquare(self):
        with self.subTest():
            self.assertTrue(isPerfectSquare(0))
            self.assertTrue(isPerfectSquare(225))

    def test_isPerfectSquare_Doubles(self):
        self.assertFalse(isPerfectSquare(100.00))

    def test_isPerfectSquare_Characters(self):
        self.assertFalse(isPerfectSquare('Hello There!'))

