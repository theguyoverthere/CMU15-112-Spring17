import os, sys
from unittest import TestCase

# Locate src package
sys.path.append(os.path.abspath(os.path.join(__file__,
                                             os.pardir,
                                             os.pardir,
                                             os.pardir,
                                             os.pardir,
                                             os.pardir)))
from src.Week4.Homework.bestScrabbleScore import computeWordScore

class TestComputeWordScore(TestCase):

    def test_computerWordScore_Non_Empty_String(self):
        letterScores = [
   #  a, b, c, d, e, f, g, h, i, j, k, l, m
      1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3,
   #  n, o, p, q, r, s, t, u, v, w, x, y, z
      1, 1, 3,10, 1, 1, 1, 1, 4, 4, 8, 4,10
   ]
        self.assertEquals(computeWordScore("tarique", letterScores), 16)

    def test_computerWordScore_Empty_String(self):
        letterScores = [
   #  a, b, c, d, e, f, g, h, i, j, k, l, m
      1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3,
   #  n, o, p, q, r, s, t, u, v, w, x, y, z
      1, 1, 3,10, 1, 1, 1, 1, 4, 4, 8, 4,10
   ]
        self.assertEquals(computeWordScore("", letterScores), 0)