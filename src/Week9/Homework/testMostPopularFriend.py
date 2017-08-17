from src.Week9.Homework.mostPopularFriend import mostPopularFriend
from unittest import TestCase

class TestMostPopularFriend(TestCase):

    def test_mostPopularFriend_empty_dictionary(self):
        d = dict()
        self.assertEqual(mostPopularFriend(d), "")

    def test_mostPopularFriend(self):
        d = dict()
        d["fred"]  = set(["wilma", "betty", "barney"])
        d["wilma"] = set(["fred", "betty", "dino"])

        self.assertEqual(mostPopularFriend(d), "betty")
