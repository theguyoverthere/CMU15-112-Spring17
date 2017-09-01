from src.Week9.Homework.friendsOfFriends import friendsOfFriends
from unittest import TestCase

class TestFriendOfFriends(TestCase):

    def test_FriendOfFriends(self):
        d = dict()
        d["fred"] = set(["wilma", "betty", "barney", "bam-bam"])
        d["wilma"] = set(["fred", "betty", "dino"])
        d["betty"] = set(["fred", "wilma"])
        d["dino"] = set(["wilma", "bam-bam"])
        d["bam-bam"] = set(["dino", "fred"])
        d["barney"] = set(["fred"])

        print(friendsOfFriends(d))
        self.assertEqual(friendsOfFriends(d),
                         {'fred': {'dino'},
                          'wilma': {'barney', 'bam-bam'},
                          'betty': {'dino', 'barney', 'bam-bam'},
                          'dino': {'fred', 'betty'},
                          'bam-bam': {'wilma', 'barney', 'betty'},
                          'barney': {'wilma', 'bam-bam', 'betty'}})

