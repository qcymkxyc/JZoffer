import unittest
from main.question40 import my1, book1, heap_sort
import random


class MSTestCase(unittest.TestCase):
    def setUp(self):
        self.nums = list(range(20))
        random.shuffle(self.nums)

    def test_my1_bubble_min(self):
        k = 4
        min_nums = my1.bubble_min(self.nums, k)
        self.assertEqual(list(range(k)), min_nums)

        k = 50
        with self.assertRaises(ValueError):
            my1.bubble_min(self.nums, k)

    def test_heap_sort(self):
        nums = [16, 7, 3, 20, 17, 8]
        import copy
        temp = copy.copy(nums)
        heap_sort.heap_sort(nums)
        self.assertEqual(sorted(temp),nums)

    def test_book1_get_least_num2(self):
        k = 10
        least_nums = book1.get_least_num2(self.nums, k)
        self.assertEqual(list(range(k)), least_nums)

        k = 1
        least_nums = book1.get_least_num2([10],k)
        self.assertEqual([10],least_nums)

        k = 10
        with self.assertRaises(IndexError):
            book1.get_least_num2([10], k)


if __name__ == '__main__':
    unittest.main()
