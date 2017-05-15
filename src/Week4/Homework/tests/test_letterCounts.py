from unittest import TestCase
from src.Week4.Homework.bestScrabbleScore import letterCounts

class TestLetterCounts(TestCase):

    def test_letterCounts_empty_string(self):
        self.assertEquals(letterCounts(""),[0]* 26)

    def test_letterCounts_single_character(self):
        with self.subTest():
            self.assertEquals(letterCounts("a"), [1, 0, 0, 0, 0,
                                                  0, 0, 0, 0, 0,
                                                  0, 0, 0, 0, 0,
                                                  0, 0, 0, 0, 0,
                                                  0, 0, 0, 0, 0, 0])

            self.assertEquals(letterCounts("Z"), [0, 0, 0, 0, 0,
                                                  0, 0, 0, 0, 0,
                                                  0, 0, 0, 0, 0,
                                                  0, 0, 0, 0, 0,
                                                  0, 0, 0, 0, 0, 1])

    def test_letterCounts_random_string(self):
        with self.subTest():
            self.assertEquals(letterCounts("Hello"),[0, 0, 0, 0, 1,
                                                     0, 0, 1, 0, 0,
                                                     0, 2, 0, 0, 1,
                                                     0, 0, 0, 0, 0,
                                                     0, 0, 0, 0, 0, 0])

        with self.subTest():
            self.assertEquals(letterCounts("Assert"),[1, 0, 0, 0, 1,
                                                      0, 0, 0, 0, 0,
                                                      0, 0, 0, 0, 0,
                                                      0, 0, 1, 2, 1,
                                                      0, 0, 0, 0, 0, 0])
