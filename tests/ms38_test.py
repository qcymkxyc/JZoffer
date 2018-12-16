import unittest
from main.question38 import my1, my2


class MSTestCase(unittest.TestCase):
    def test_my1_whole_arrangement(self):
        s = "abc"
        arrangement = [
            "abc",
            "acb",
            "bac",
            "bca",
            "cab",
            "cba"
        ]
        self.assertEqual(arrangement, my1.whole_arrangement(s))
        self.assertEqual([""], my1.whole_arrangement(""))

    def test_my2_all_combination(self):
        s = "abc"
        combination = [
            "a", "b", "c",
            "ab", "bc", "ac",
            "abc"
        ]
        self.assertEqual(set(combination), set(my2.all_combination(s)))


if __name__ == '__main__':
    unittest.main()
