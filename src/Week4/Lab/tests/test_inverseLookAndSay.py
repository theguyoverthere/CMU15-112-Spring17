from unittest import TestCase
from src.Week4.Lab.lookAndSay import lookAndSay
from src.Week4.Lab.inverseLookAndSay import inverseLookAndSay

class TestInverseLookAndSay(TestCase):

    def test_inverseLookAndSay_Empty_List(self):
        self.assertEquals(inverseLookAndSay([]), [])

    def test_inverseLookAndSay_All_Digits_Same(self):
        self.assertEquals(inverseLookAndSay([(3,1)]), [1,1,1])

    def test_inverseLookAndSay_All_Digits_Different(self):
        self.assertEquals(inverseLookAndSay([(1,-1), (1,2), (1,7)]), [-1,2,7])

    def test_inverseLookAndSay_Repeated_Digits(self):
        self.assertEquals(inverseLookAndSay([(2,3),(1,8),(3,-10)]),
                                            [3,3,8,-10,-10,-10])

    def test_InverseLookAndSay_List_Comprehensions(self):
        with self.subTest():
            self.assertEquals(inverseLookAndSay([(5,2), (2,5)]),
                                               ([2]*5 + [5]*2))
        with self.subTest():
            self.assertEquals(inverseLookAndSay([(2,5), (5,2)]),
                                               ([5]*2 + [2]*5))

