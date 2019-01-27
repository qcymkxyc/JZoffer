import unittest
from main.question48 import my1, book1


class MSTestCase(unittest.TestCase):
    def test_my1_longest_substr(self):
        s = "arabcacfr"
        long_subs = my1.longest_substr(s)
        self.assertEqual(4, len(long_subs))

        s = ""
        long_subs = my1.longest_substr(s)
        self.assertEqual(0, len(long_subs))

        s = "a"
        long_subs = my1.longest_substr(s)
        self.assertEqual(1, len(long_subs))

    def test_book1_longest_substr(self):
        s = "arabcacfr"
        self.assertEqual(4, book1.longest_substr(s))

        s = ""
        self.assertEqual(0, book1.longest_substr(s))

        s = "a"
        self.assertEqual(1, book1.longest_substr(s))


if __name__ == '__main__':
    unittest.main()
