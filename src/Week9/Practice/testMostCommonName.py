import os, sys

# Locate src package
sys.path.append(os.path.abspath(os.path.join(__file__,
                                             os.pardir,
                                             os.pardir,
                                             os.pardir,
                                             os.pardir)))

from unittest import TestCase
from src.Week9.Practice.mostCommonName import mostCommonName

class TestMostCommonName(TestCase):
    def test_mostCommonName(self):
        self.assertEqual(mostCommonName(["Jane", "Aaron", "Cindy", "Aaron"]),
                                 {"Aaron"})

        self.assertEqual(mostCommonName(["Jane", "Aaron", "Jane", "Cindy", "Aaron"]),
                                         {"Aaron", "Jane"})

        self.assertEqual(mostCommonName(["Cindy"]),
                                         {"Cindy"})

        self.assertEqual(mostCommonName(["Jane", "Aaron", "Cindy"]),
                                         {"Aaron", "Cindy", "Jane"})


