import os, sys
from unittest import TestCase

# Locate src package
sys.path.append(os.path.abspath(os.path.join(__file__,
                                             os.pardir,
                                             os.pardir,
                                             os.pardir,
                                             os.pardir)))

from src.Week5.Lab.isLegalSudoku import areValidRows

class TestAreValidRows(TestCase):

    def test_areValidRows_Valid_Rows(self):
        with self.subTest():
            #First Column Invalid, but we're only looking for rows here.
            self.assertTrue(areValidRows([ [ 5, 3, 0,  0, 7, 0,  0, 0, 0 ],
                                           [ 6, 0, 0,  1, 9, 5,  0, 0, 0 ],
                                           [ 0, 9, 8,  0, 0, 0,  0, 6, 0 ],

                                           [ 8, 0, 0,  0, 6, 0,  0, 0, 3 ],
                                           [ 4, 0, 0,  8, 0, 3,  0, 0, 1 ],
                                           [ 7, 0, 0,  0, 2, 0,  0, 0, 6 ],

                                           [ 0, 6, 0,  0, 0, 0,  2, 8, 0 ],
                                           [ 6, 0, 0,  4, 1, 9,  0, 0, 5 ],
                                           [ 0, 0, 0,  0, 8, 0,  0, 7, 9 ]]))


            self.assertTrue(areValidRows([[8, 3, 5,  4, 1, 6,  9, 2, 7 ],
                                          [2, 9, 6,  8, 5, 7,  4, 3, 1 ],
                                          [4, 1, 7,  2, 9, 3,  6, 5, 8 ],

                                          [5, 6, 9,  1, 3, 4,  7, 8, 2 ],
                                          [1, 2, 3,  6, 7, 8,  5, 4, 0 ],
                                          [7, 4, 8,  5, 2, 9,  1, 6, 3 ],

                                          [6, 5, 2,  7, 8, 1,  3, 9, 4 ],
                                          [9, 8, 1,  3, 4, 5,  2, 7, 6 ],
                                          [3, 7, 4,  9, 6, 2,  8, 1, 5 ]]))


    def test_areValidRows_InValid_Rows(self):
        with self.subTest():
            self.assertFalse(areValidRows([[ 5, 3, 0,  0, 7, 0,  0, 0, 0 ],
                                             [ 6, 0, 0,  1, 9, 5,  0, 0, 0 ],
                                             [ 0, 9, 8,  0, 0, 0,  0, 6, 0 ],

                                             [ 8, 0, 0,  0, 6, 0,  0, 0, 3 ],
                                             [ 4, 0, 0,  8, -4, 3,  0, 0, 1 ],
                                             [ 7, 0, 0,  0, 2, 0,  0, 0, 6 ],

                                             [ 0, 6, 0,  0, 0, 0,  2, 8, 0 ],
                                             [ 0, 0, 0,  4, 1, 9,  0, 0, 5 ],
                                             [ 0, 0, 0,  0, 8, 0,  0, 7, 9 ]]))

            self.assertFalse(areValidRows([[5, 3, 7, 0, 7, 0, 0, 0, 0], #First Row is invalid
                                           [6, 0, 0, 1, 9, 5, 0, 0, 0],
                                           [0, 9, 8, 0, 0, 0, 0, 6, 0],

                                           [8, 0, 0, 0, 6, 0, 0, 0, 3],
                                           [4, 0, 0, 8, 4, 3, 0, 0, 1],
                                           [7, 0, 0, 0, 2, 0, 0, 0, 6],

                                           [0, 6, 0, 0, 0, 0, 2, 8, 0],
                                           [0, 0, 0, 4, 1, 9, 0, 0, 5],
                                           [0, 0, 0, 0, 8, 0, 0, 7, 9]]))



            self.assertFalse(areValidRows([[5, 3, 6, 0, 7, 0, 0, 0, 0],
                                           [6, 0, 0, 1, 9, 5, 0, 0, 0],
                                           [0, 9, 8, 0, 0, 0, 0, 6, 0],

                                           [8, 0, 0, 0, 6, 0, 0, 0, 3],
                                           [4, 0, 0, 8, 4, 3, 0, 0, 1],
                                           [7, 0, 0, 0, 2, 0, 0, 0, 6],

                                           [0, 6, 0, 0, 0, 0, 2, 8, 0],
                                           [0, 0, 0, 4, 1, 9, 0, 0, 5],
                                           [0, 0, 0, 0, 8, 0, 0, 7, 7]])) #Last Row is invalid
