import os, sys
from unittest import TestCase

# Locate src package
sys.path.append(os.path.abspath(os.path.join(__file__,
                                             os.pardir,
                                             os.pardir,
                                             os.pardir,
                                             os.pardir)))

from src.Week5.Practice.isKnightsTour import locateStartPosition

class TestLocateStartingPosition(TestCase):

    # The function searches for the value in row, column order. The function
    # returns the first location of the move.
    def test_LocateStartingPosition_Multiple_Locations(self):
        self.assertEquals(locateStartPosition([[41,  38,  55,  34,   3,  36,  19,  22],
                                               [54,  47,   2,  37,  20,  23,   4,  17],
                                               [39,  56,  33,  46,  35,  18,  21,  10],
                                               [48,  53,  40,  57,  24,  11,  16,   5],
                                               [59,  32,  45,  52,   1,  26,   9,  12],
                                               [44,  49,  58,  25,  62,  15,   6,  27],
                                               [31,  60,  51,  42,  29,   8,  13,  64],
                                               [50,  43,  30,  61,  14,  63,  28,  71]], 1),  (4, 4))

    def test_LocateStartingPosition_Single_Locations(self):
        self.assertEquals(locateStartPosition([[ 0,  59,  38,  33,  30,  17,   8,   63],
                                               [37,  34,  31,  60,   9,  62,  29,  16],
                                               [58,   1,  36,  39,  32,  27,  18,   7],
                                               [35,  48,  41,  26,  61,  10,  15,  28],
                                               [42,  57,   2,  49,  40,  23,   6,  19],
                                               [47,  50,  45,  54,  25,  20,  11,  14],
                                               [56,  43,  52,   3,  22,  13,  24,   5],
                                               [51,  46,  55,  44,  53,   4,  21,  12]], 1),  (2, 1))

    def test_LocateStartingPosition_Location_Absent(self):
        self.assertEquals(locateStartPosition([[ 0, 20, 17, 12,  3],
                                               [16, 11,  2,  7, 18],
                                               [21, 24, 19,  4, 13],
                                               [10, 15,  6, 23,  8],
                                               [25, 22,  9, 14,  5]], 1),  (-1, -1))