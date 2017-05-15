from unittest import TestCase
from src.Week4.Homework.bestScrabbleScore import possibleToFormWord


class TestPossibleToFormWord(TestCase):
    def test_PossibleToFormWord_Empty_Strings(self):
        self.assertTrue(possibleToFormWord(" ", " "))

    def test_PossibleToFormWord_Empty_Hand(self):
        self.assertFalse(possibleToFormWord("Hello ", " "))

    def test_PossibleToFormWord_Empty_Word(self):
        self.assertTrue(possibleToFormWord(" ", "hello "))

    def test_PossibleToFormWord_possible_case(self):
        with self.subTest():
            self.assertTrue(possibleToFormWord(" Hello", "hello "))
        with self.subTest():
            self.assertTrue(possibleToFormWord("Scrambled Eggs",
                                               "gegs blemadrcs"))

    def test_PossibleToFormWord_impossible_case(self):
        with self.subTest():
            self.assertFalse(possibleToFormWord("Why", "hello "))
        with self.subTest():
            self.assertFalse(possibleToFormWord("hheelloo", "hello "))
