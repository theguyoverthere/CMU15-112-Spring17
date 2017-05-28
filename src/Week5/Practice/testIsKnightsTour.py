from unittest import TestCase
from src.Week5.Practice.isKnightsTour import isKnightsTour

class TestIsKnightsTour(TestCase):
    def test_isKnightsTour_8x8(self):
        with self.subTest():
            # Picked up from http://www.geeksforgeeks.org/backtracking-set-1-the-knights-tour-problem/
            self.assertTrue(isKnightsTour([[ 0,  59,  38,  33,  30,  17,   8,   63],
                                           [37,  34,  31,  60,   9,  62,  29,  16],
                                           [58,   1,  36,  39,  32,  27,  18,   7],
                                           [35,  48,  41,  26,  61,  10,  15,  28],
                                           [42,  57,   2,  49,  40,  23,   6,  19],
                                           [47,  50,  45,  54,  25,  20,  11,  14],
                                           [56,  43,  52,   3,  22,  13,  24,   5],
                                           [51,  46,  55,  44,  53,   4,  21,  12]]))

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

    def test_isKnightsTour_5x5_1_Not_Present(self):
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