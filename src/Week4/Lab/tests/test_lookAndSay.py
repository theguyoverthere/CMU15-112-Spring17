from unittest import TestCase, main
from src.Week4.Lab.lookAndSay import lookAndSay

class TestLookAndSay(TestCase):
    def test_lookAndSay_Empty_List(self):
        self.assertEquals(lookAndSay([]),[])

    def test_lookAndSay_All_Digits_Same(self):
        self.assertEquals(lookAndSay([1,1,1]),[(3,1)])

    def test_lookAndSay_All_Digits_Different(self):
        self.assertEquals(lookAndSay([-1,2,7]),[(1,-1),(1,2),(1,7)])

    def test_lookAndSay_Repeated_Digits(self):
        self.assertEquals(lookAndSay([3,3,8,-10,-10,-10]),[(2,3),(1,8),(3,-10)])

    def test_lookAndSay_List_Comprehensions(self):
        with self.subTest():
            self.assertEquals(lookAndSay([2]*5 + [5]*2),[(5,2), (2,5)])
        with self.subTest():
            self.assertEquals(lookAndSay([5]*2 + [2]*5),[(2,5), (5,2)])

if __name__ == '__main__':
    main()
