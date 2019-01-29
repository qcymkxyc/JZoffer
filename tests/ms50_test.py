import unittest
from main.question50 import my1, book1


class MSTestCase(unittest.TestCase):
    def test_my1_first_once_ch(self):
        s = "abacedeff"
        self.assertEqual("b", my1.first_once_ch(s))

    def test_book1_first_once_ch(self):
        s = "abacedeff"
        self.assertEqual("b", book1.first_once_ch(s))


if __name__ == '__main__':
    unittest.main()
