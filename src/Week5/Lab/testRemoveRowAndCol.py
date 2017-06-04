from unittest import TestCase
from src.Week5.Lab.removeRowAndCol import removeRowAndCol

class TestRemoveRowAndCol(TestCase):
    A = [
  [8, 3, 5, 4, 1, 6, 9, 2, 7 ],
  [2, 9, 6, 8, 5, 7, 4, 3, 1 ],
  [4, 1, 7, 2, 9, 3, 6, 5, 8 ],
  [5, 6, 9, 1, 3, 4, 7, 8, 2 ],
  [1, 2, 3, 6, 7, 8, 5, 4, 9 ],
  [7, 4, 8, 5, 2, 9, 1, 6, 3 ],
  [6, 5, 2, 7, 8, 1, 3, 9, 4 ],
  [9, 8, 1, 3, 4, 5, 2, 7, 6 ],
  [3, 7, 4, 9, 6, 2, 8, 1, 5 ]
]
    def test_removeRowAndCol(self):
        self.assertTrue(removeRowAndCol(self.A, 2, 3), [[8, 3, 5, 1, 6, 9, 2, 7 ],
                                                        [2, 9, 6, 5, 7, 4, 3, 1 ],
                                                        [5, 6, 9, 3, 4, 7, 8, 2 ],
                                                        [1, 2, 3, 7, 8, 5, 4, 9 ],
                                                        [7, 4, 8, 2, 9, 1, 6, 3 ],
                                                        [6, 5, 2, 8, 1, 3, 9, 4 ],
                                                        [9, 8, 1, 4, 5, 2, 7, 6 ],
                                                        [3, 7, 4, 6, 2, 8, 1, 5 ]])
