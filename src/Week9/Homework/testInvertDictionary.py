from src.Week9.Homework.invertDictionary import invertDictionary
from unittest import TestCase

class TestInvertDictionary(TestCase):

    def test_InvertDictionary_empty_dictionary(self):
        self.assertEqual(invertDictionary(dict()), dict())

    def test_InvertDictionary_non_unique_key_value(self):
        self.assertEqual(invertDictionary({1:2, 2:3, 3:4, 5:3}),
                        {2:set([1]), 3:set([2,5]), 4:set([3])})

    def test_InvertDictionary_unique_key_values(self):
        self.assertEqual(invertDictionary({1:2, 2:3, 3:4, 5:7}),
                        {2:set([1]), 3:set([2]), 4:set([3]), 7:set([5])})
