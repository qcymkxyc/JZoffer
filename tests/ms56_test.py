import unittest
from main.question56 import book1


class MSTestCase(unittest.TestCase):
    def test_book1_unique_num(self):
        nums = [2, 4, 3, 6, 3, 2, 5, 5]
        self.assertEqual((6, 4), book1.unique_num(nums))


if __name__ == '__main__':
    unittest.main()
