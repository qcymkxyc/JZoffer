import unittest
from main1.question4 import book1


class MSTestCase(unittest.TestCase):
    def test_book1_find_num(self):
        matrix = [
            [1, 2, 8, 9],
            [2, 4, 9, 12],
            [4, 7, 10, 13],
            [6, 8, 11, 15]
        ]
        num = 7
        self.assertTrue(book1.find_num(matrix, num))
        self.assertFalse(book1.find_num(matrix, 16))
        self.assertFalse(book1.find_num(matrix, 5))
        self.assertFalse(book1.find_num(matrix, 0))


if __name__ == '__main__':
    unittest.main()
