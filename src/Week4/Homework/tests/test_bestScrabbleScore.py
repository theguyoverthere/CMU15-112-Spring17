from unittest import TestCase
from src.Week4.Homework.bestScrabbleScore import bestScrabbleScore


class TestBestScrabbleScore(TestCase):
    def dictionary1(self): return ["a", "b", "c"]
    def letterScores1(self): return [1] * 26

    def test_bestScrabbleScore_1(self):
        with self.subTest():
            self.assertEquals(bestScrabbleScore(self.dictionary1(),
                                                self.letterScores1(),
                                                list("b")), ("b", 1))

        with self.subTest():
            self.assertEquals(bestScrabbleScore(self.dictionary1(),
                                                self.letterScores1(),
                                                list("ace")), (["a", "c"], 1))

        with self.subTest():
            self.assertEquals(bestScrabbleScore(self.dictionary1(),
                                                self.letterScores1(),
                                                list("b")), ("b", 1))

        with self.subTest():
            self.assertEquals(bestScrabbleScore(self.dictionary1(),
                                                self.letterScores1(),
                                                list("z")), None)

    def dictionary2(self): return ["xyz", "zxy", "zzy", "yy", "yx", "wow"]
    def letterScores2(self): return [1+(i%5) for i in range(26)]

    def test_bestScrabbleScore_2(self):
        with self.subTest():
            self.assertEquals(
                bestScrabbleScore(self.dictionary2(),
                                  self.letterScores2(),
                                  list("xyz")), (["xyz", "zxy"], 10))

        with self.subTest():
            self.assertEquals(
                bestScrabbleScore(self.dictionary2(),
                                  self.letterScores2(),
                                  list("xyzy")), (["xyz", "zxy", "yy"], 10))

        with self.subTest():
            self.assertEquals(
                bestScrabbleScore(self.dictionary2(),
                                  self.letterScores2(),
                                  list("xyq")), ("yx", 9))

        with self.subTest():
            self.assertEquals(
                bestScrabbleScore(self.dictionary2(),
                                  self.letterScores2(),
                                  list("yzz")), ("zzy", 7))

        with self.subTest():
            self.assertEquals(
                bestScrabbleScore(self.dictionary2(),
                                  self.letterScores2(),
                                  list("wxz")), None)
