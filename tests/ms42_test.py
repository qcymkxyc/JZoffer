import unittest
from main.question42 import book1


class MSTestCase(unittest.TestCase):
    def test_book1_max_sub_nums(self):
        nums = [1, -2, 3, 10, -4, 7, 2, -5]
        self.assertEqual(([3, 10, -4, 7, 2], 18), book1.max_sub_nums(nums))

        nums = [1, 2, 3, 4, 5]
        self.assertEqual((nums, sum(nums)), book1.max_sub_nums(nums))

        nums = [-1, -2, -3, -4, -5]
        self.assertEqual(([], 0), book1.max_sub_nums(nums))


if __name__ == '__main__':
    unittest.main()
