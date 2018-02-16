import os, sys
from unittest import TestCase

# Locate src package
sys.path.append(os.path.abspath(os.path.join(__file__,
                                             os.pardir,
                                             os.pardir,
                                             os.pardir,
                                             os.pardir)))

from src.Week5.Practice.isKnightsTour import isKnightsTour

class TestIsKnightsTour(TestCase):
    def test_isKnightsTour_8x8(self):
        with self.subTest():
            # Picked up from http://www.geeksforgeeks.org/backtracking-set-1-the-knights-tour-problem/
            self.assertTrue(isKnightsTour([[ 1,  60,  39,  34,  31,  18,   9,  64],
                                           [38,  35,  32,  61,  10,  63,  30,  17],
                                           [59,   2,  37,  40,  33,  28,  19,   8],
                                           [36,  49,  42,  27,  62,  11,  16,  29],
                                           [43,  58,   3,  50,  41,  24,   7,  20],
                                           [48,  51,  46,  55,  26,  21,  12,  15],
                                           [57,  44,  53,   4,  23,  14,  25,   6],
                                           [52,  47,  56,  45,  54,   5,  22,  13]]))

            # Picked up from https://www.thanassis.space/knightstour.html
            self.assertTrue(isKnightsTour([[ 1,  38,  55,  34,   3,  36,  19,  22],
                                           [54,  47,   2,  37,  20,  23,   4,  17],
                                           [39,  56,  33,  46,  35,  18,  21,  10],
                                           [48,  53,  40,  57,  24,  11,  16,   5],
                                           [59,  32,  45,  52,  41,  26,   9,  12],
                                           [44,  49,  58,  25,  62,  15,   6,  27],
                                           [31,  60,  51,  42,  29,   8,  13,  64],
                                           [50,  43,  30,  61,  14,  63,  28,  7]]))

    def test_isKnightsTour_5x5(self):
        # Picked up from https://www.thanassis.space/knightstour.html
            self.assertTrue(isKnightsTour([[ 1, 20, 17, 12,  3],
                                           [16, 11,  2,  7, 18],
                                           [21, 24, 19,  4, 13],
                                           [10, 15,  6, 23,  8],
                                           [25, 22,  9, 14,  5]]))

    def test_isKnightsTour_5x5_Starts_At_0(self):
        # Picked up from https://www.thanassis.space/knightstour.html
            self.assertFalse(isKnightsTour([[ 0, 20, 17, 12,  3],
                                           [16, 11,  2,  7, 18],
                                           [21, 24, 19,  4, 13],
                                           [10, 15,  6, 23,  8],
                                           [25, 22,  9, 14,  5]]))

    def test_isKnightsTour_5x5_Random_Numbers(self):
        # Picked up from https://www.thanassis.space/knightstour.html
            self.assertFalse(isKnightsTour([[ 1, 40, 17, 12,  3],
                                           [16, 17,  2,  7, 18],
                                           [41, 27, 19, 54, 14],
                                           [20, 15,  6, 23, 78],
                                           [25, 22,  9,  4, 15]]))