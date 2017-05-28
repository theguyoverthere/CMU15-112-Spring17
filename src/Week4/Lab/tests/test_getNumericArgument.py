from unittest import TestCase
from src.Week4.Lab.solvesCryptarithm import getNumericArgument

class TestGetNumericArgument(TestCase):
    def test_getNumericArgument_all_indices_present(self):
        self.assertEquals(getNumericArgument("NUMBER", "UMNZP-BLER"), 201689)

    def test_getNumericArgument_some_indices_present(self):
        self.assertEquals(getNumericArgument("NUMBER", "U-NZP-BLER"), 20689)
