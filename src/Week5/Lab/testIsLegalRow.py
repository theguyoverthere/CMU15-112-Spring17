import os, sys
from unittest import TestCase

# Locate src package
sys.path.append(os.path.abspath(os.path.join(__file__,
                                             os.pardir,
                                             os.pardir,
                                             os.pardir,
                                             os.pardir)))

from src.Week5.Lab.isLegalSudoku import isLegalRow

class TestIsLegalRow(TestCase):

    def test_isLegalRow(self):
        with self.subTest():
            self.assertFalse(isLegalRow([[ 5, 3, 0,  0, 7, 0,  0, 0, 0 ],
                                         [ 6, 0, 0,  1, 9, 5,  0, 0, 0 ],
                                         [ 0, 9, 8,  0, 0, 0,  0, 6, 0 ],

                                         [ 8, 0, 0,  0, 6, 0,  0, 0, 3 ],
                                         [ 4, 0, 0,  8, -1, 3, 0, 0, 1 ],
                                         [ 7, 0, 0,  0, 2, 0,  0, 0, 6 ],

                                         [ 0, 6, 0,  0, 0, 0,  2, 8, 0 ],
                                         [ 0, 0, 0,  4, 1, 9,  0, 0, 5 ],
                                         [ 0, 0, 0,  0, 8, 0,  0, 7, 9 ]], 4))

            self.assertTrue(isLegalRow([[ 5, 3, 0,  0, 7, 0,  0, 0, 0 ],
                                        [ 6, 0, 0,  1, 9, 5,  0, 0, 0 ],
                                        [ 0, 9, 8,  0, 0, 0,  0, 6, 0 ],

                                        [ 8, 0, 0,  0, 6, 0,  0, 0, 3 ],
                                        [ 4, 0, 0,  8, -1, 3, 0, 0, 1 ],
                                        [ 7, 0, 0,  0, 2, 0,  0, 0, 6 ],

                                        [ 0, 6, 0,  0, 0, 0,  2, 8, 0 ],
                                        [ 0, 0, 0,  4, 1, 9,  0, 0, 5 ],
                                        [ 0, 0, 0,  0, 8, 0,  0, 7, 9 ]], 0))
