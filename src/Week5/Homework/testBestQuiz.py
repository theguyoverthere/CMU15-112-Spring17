from unittest import TestCase
from src.Week5.Homework.bestQuiz import bestQuiz

class TestBestQuiz(TestCase):
    gradebook = [[88, 80, 91],
                 [68, 100, -1]
                 ]

    def test_Best_Quiz_Empty_List(self):
        self.assertEqual(bestQuiz([]), None)

    def test_Best_Quiz_Empty_SubList(self):
        self.assertEqual(bestQuiz([[], []]), None)

    def test_Best_Quiz(self):
        self.assertEqual(bestQuiz(self.gradebook), 2)
