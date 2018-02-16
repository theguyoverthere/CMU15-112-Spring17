import os, sys
from unittest import TestCase

# Locate src package
sys.path.append(os.path.abspath(os.path.join(__file__,
                                             os.pardir,
                                             os.pardir,
                                             os.pardir,
                                             os.pardir,
                                             os.pardir)))
from src.Week4.Lab.solvesCryptarithm import solvesCryptarithm


class TestSolvesCryptarithm(TestCase):

    def test_solvesCryptarithm_True(self):
        with self.subTest():
            self.assertTrue(solvesCryptarithm("NUMBER+NUMBER=PUZZLE",
                                                "UMNZP-BLER"))
        with self.subTest():
            self.assertTrue(solvesCryptarithm("TILES+PUZZLES=PICTURE",
                                                "UISPELCZRT"))
        with self.subTest():
            self.assertTrue(solvesCryptarithm("COCA+COLA=OASIS",
                                                "LOS---A-CI"))
        with self.subTest():
            self.assertTrue(solvesCryptarithm("CROSS+ROADS=DANGER",
                                                "-DOSEARGNC"))

    def test_solvesCryptarithm_False(self):
        with self.subTest():
            self.assertFalse(solvesCryptarithm("SEND+MORE=MONEY","OMY--ENDR-"))

        with self.subTest():
            self.assertFalse(solvesCryptarithm("SEND+MORE=MONEY","OMY-ENDRS"))

        with self.subTest():
            self.assertFalse(solvesCryptarithm("SEND+MORE=MONY","OMY--ENDRS"))

        with self.subTest():
            self.assertFalse(solvesCryptarithm("SEND+MORE=MONEY","MOY--ENDRS"))

        with self.subTest():
            self.assertFalse(solvesCryptarithm("SEND+MORE=MONEY","----------"))

