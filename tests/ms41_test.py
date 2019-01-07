import unittest
from main.question41 import my1, book1
import random


class MyTestCase(unittest.TestCase):
    def test_my1_Median(self):
        median = my1.Median()
        for i in range(10):
            median.append(i)
            print("加入数字：{}".format(median.core))
            print("Median Num : {}".format(median))

        median_num = median.median_num()
        self.assertEqual(4.5, float(median_num))

    def test_book1_heap_sort(self):
        n = 20
        nums = list(range(n))
        random.shuffle(nums)

        book1.heap_sort(nums, mode="max")
        self.assertEqual(list(range(n)), nums)

        r = list(range(n))
        r.reverse()
        random.shuffle(nums)
        book1.heap_sort(nums, mode="min")
        self.assertEqual(r, nums)

    def test_book1_build_heap(self):
        book1._build_heap([10], 1, "max")
        book1._build_heap([], 0, "max")

    def test_book1_median(self):
        median = book1.Median()
        for i in range(20):
            median.insert(i)
            print("Median Num : {}".format(median))

        median_num = median.median()
        self.assertEqual(9.5, float(median_num))


if __name__ == '__main__':
    unittest.main()
