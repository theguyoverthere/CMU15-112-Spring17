import os, sys
from unittest import TestCase

# Locate src package
sys.path.append(os.path.abspath(os.path.join(__file__,
                                             os.pardir,
                                             os.pardir,
                                             os.pardir,
                                             os.pardir)))

from src.Week5.Practice.isKnightsTour import getNextLocation

class TestGetNextLocation(TestCase):
    def test_GetNextLocation_Move_Exists(self):
        self.assertEqual(getNextLocation([[1,2,3],
                                          [2,3,1],
                                          [3,2,1]], 0, 0, 2), (2, 1))

    def test_GetNextLocation_Move_Does_Not_Exist(self):
        self.assertEqual(getNextLocation([[1,2,3],
                                         [2,3,1],
                                         [3,2,1]], 0, 0, 5), (-1, -1))
