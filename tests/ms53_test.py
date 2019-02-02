import unittest
from main.question53 import my1, my2, my3, book3


class MSTestCase(unittest.TestCase):
    def test_my1_binary_search1(self):
        nums = [1, 2, 3, 4, 5]
        num = 2
        self.assertEqual(1, my1._binary_search1(nums, num))
        num = 1
        self.assertEqual(0, my1._binary_search1(nums, num))
        num = 5
        self.assertEqual(4, my1._binary_search1(nums, num))

        nums = [1, 2, 3, 3, 3, 4, 6]
        num = 3
        self.assertIn(my1._binary_search1(nums, num), [2, 3, 4])

    def test_my1_num_time(self):
        nums = [1, 2, 3, 3, 3, 4, 6]
        num = 3
        self.assertEqual(3, my1.num_time1(nums, num))
        self.assertEqual(0, my1.num_time1(nums, 10))

    def test_my1_binary_search2(self):
        nums = [1, 2, 3, 3, 3, 4, 6]
        num = 3
        self.assertEqual(3, my1._binary_search2(nums, num))
        self.assertEqual(0, my1._binary_search2(nums, 10))

    def test_my1_num_time2(self):
        nums = [1, 2, 3, 3, 3, 4, 6]
        num = 3
        self.assertEqual(3, my1.num_time2(nums, num))
        self.assertEqual(0, my1.num_time2(nums, 10))

    def test_my2_miss_num(self):
        nums = [0, 1, 2, 3, 4, 6, 7, 8]
        self.assertEqual(5, my2.miss_num(nums))

        nums = [1, 2, 3, 4, 5]
        self.assertEqual(0, my2.miss_num(nums))

        nums = [0, 1, 2, 3, 4]
        with self.assertRaises(ValueError):
            my2.miss_num(nums)

    def test_my3_index_equal_num(self):
        nums = [-3, -1, 1, 3, 5]
        self.assertEqual(3, my3.index_equal_num(nums))
        self.assertIsNone(my3.index_equal_num([-3, -1, 1, -3, 5]))

    def test_book3_index_equal_num(self):
        nums = [-3, -1, 1, 3, 5]
        self.assertEqual(3, book3.index_equal_num(nums))
        self.assertIsNone(book3.index_equal_num([-3, -1, 1, -3, 5]))


if __name__ == '__main__':
    unittest.main()
