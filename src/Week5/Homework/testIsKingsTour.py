import os, sys
# Locate src package
sys.path.append(os.path.abspath(os.path.join(__file__,
                                             os.pardir,
                                             os.pardir,
                                             os.pardir,
                                             os.pardir)))

from unittest import TestCase
from src.Week5.Homework.isKingsTour import isKingsTour

class TestIsKingsTour(TestCase):

    def test_isKingsTour_True(self):
        with self.subTest():
            self.assertTrue(isKingsTour([[3, 2, 1],
                                         [6, 4, 9],
                                         [5, 7, 8]]))

            self.assertTrue(isKingsTour([ [  1, 14, 15, 16],
                                          [ 13,  2,  7,  6],
                                          [ 12,  8,  3,  5],
                                          [ 11, 10,  9,  4]]))

            # Picked from https://www.johndcook.com/blog/2011/04/13/a-magic-kings-tour/
            self.assertTrue(isKingsTour([[ 4,  3,  2,  1, 64, 63, 62, 61],
                                         [ 5, 54,  7,  8, 57, 58, 11, 60],
                                         [53,  6, 55, 56,  9, 10, 59, 12],
                                         [52, 51, 50, 49, 16, 15, 14, 13],
                                         [45, 46, 47, 48, 17, 18, 19, 20],
                                         [44, 27, 42, 41, 24, 23, 38, 21],
                                         [28, 43, 26, 25, 40, 39, 22, 37],
                                         [29, 30, 31, 32, 33, 34, 35, 36]]))

    def test_isKingsTour_False(self):
        with self.subTest():
            # Random Numbers. 2 cannot be reached from 1 in a single jump
            self.assertFalse(isKingsTour([[ 1,  40, 17, 12,  3],
                                           [16, 17,  2,  7, 18],
                                           [41, 27, 19, 54, 14],
                                           [20, 15,  6, 23, 78],
                                           [25, 22,  9,  4, 15]]))

            # Tour starts at 0 and ends at 15
            self.assertFalse(isKingsTour([[  0, 13, 14, 15],
                                          [ 12,  1,  6,  5],
                                          [ 11,  7,  2,  4],
                                          [ 10,  9,  8,  3]]))

            #Jump of two places between 7 and 8
            self.assertFalse(isKingsTour([[ 1, 2, 3 ],
                                          [ 7, 4, 8 ],
                                          [ 6, 5, 9 ]]))


