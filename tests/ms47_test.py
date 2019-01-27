import unittest
from main.question47 import my1, book1


class MSTestCase(unittest.TestCase):

    def setUp(self):
        self.matrix = [
            [1, 10, 3, 8],
            [12, 2, 9, 6],
            [5, 7, 4, 11],
            [3, 7, 16, 5]
        ]

    def test_my1_max_value(self):
        self.assertEqual(53, my1.max_value(self.matrix))

    def test_book1_max_value(self):
        self.assertEqual(53, book1.max_value(self.matrix))


if __name__ == '__main__':
    unittest.main()
