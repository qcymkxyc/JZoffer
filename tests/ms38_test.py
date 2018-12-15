import unittest
from main.question38 import my1


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


if __name__ == '__main__':
    unittest.main()
