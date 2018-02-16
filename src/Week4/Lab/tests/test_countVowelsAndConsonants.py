import sys, os
from unittest import TestCase

# Locate src package
sys.path.append(os.path.abspath(os.path.join(__file__,
                                             os.pardir,
                                             os.pardir,
                                             os.pardir,
                                             os.pardir,
                                             os.pardir)))

from src.Week4.Lab.makeLetterTypePieChart import countVowelsAndConsonants

class TestCountVowelsAndConsonants(TestCase):
    def test_countVowelsAndConsonants_All_Vowels(self):
        self.assertEquals(countVowelsAndConsonants("AEIOU"), [5, 0, 0, 5])

    def test_countVowelsAndConsonants_All_Consonants(self):
        self.assertEquals(countVowelsAndConsonants("BCDZ"), [0, 4, 0, 4])

    def test_countVowelsAndConsonants_All_Non_Vowels_Consonants(self):
        self.assertEquals(countVowelsAndConsonants("!@#$%&*"), [0, 0, 7, 7])

    def test_countVowelsAndConsonants_Vowels_Consonants_Mixed_Case(self):
        self.assertEquals(countVowelsAndConsonants("AeIXY"), [3, 2, 0, 5])

    def test_countVowelsAndConsonants_Vowels_Consonants_Others_Mixed_Case(self):
        self.assertEquals(countVowelsAndConsonants("AeI!@XY"), [3, 2, 2, 7])

    def test_countVowelsAndConsonants_All_Spaces(self):
        self.assertEquals(countVowelsAndConsonants("     "), [0, 0, 0, 0])

    def test_countVowelsAndConsonants_Everything_Together(self):
        self.assertEquals(countVowelsAndConsonants("AdE@c&*  U*_oiIP"),
                          [6, 3, 5, 14])