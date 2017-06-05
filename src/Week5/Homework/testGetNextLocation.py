from unittest import TestCase
from src.Week5.Homework.isKingsTour import getNextLocation

class TestGetNextLocation(TestCase):
    def test_GetNextLocation_Move_Exists(self):
        self.assertEqual(getNextLocation([[1,2,3],
                                         [2,3,1],
                                         [3,2,1]], 0, 0, 2), (0, 1))

    def test_GetNextLocation_Move_Exists_Edge_Case(self):
        self.assertEqual(getNextLocation([[1,2,3],
                                          [2,3,1],
                                          [3,2,1]], 1, 1, 1), (0, 0))


    def test_GetNextLocation_Move_Does_NotExists(self):
        self.assertEqual(getNextLocation([[1,2,3],
                                          [2,3,1],
                                          [3,2,1]], 0, 0, 7), (-1, -1))
