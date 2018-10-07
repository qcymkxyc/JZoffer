import unittest
import random
import copy

from main.面试题11 import my1
from main.面试题11 import book1

class MSTest(unittest.TestCase):
    def setUp(self):
        self.nums = list(range(10))

        random.seed(1)
        reverse_index = random.randint(0,len(self.nums))

        self.reverse_nums = copy.copy(self.nums)
        self.reverse_nums.extend(self.reverse_nums[:reverse_index])
        self.reverse_nums = self.reverse_nums[-len(self.nums):]

    def test_my_find_min(self):
        min_num = my1.find_min(self.reverse_nums)
        self.assertEqual(min_num,min(self.reverse_nums))

    def test_book_binary_find_min(self):
        #旋转个数为0的情况
        min_num = book1.binary_find_min(self.nums)
        self.assertEqual(min_num,min(self.nums))

        #旋转数组为空的情况
        with self.assertRaises(TypeError):
            book1.binary_find_min(None)

        min_num = book1.binary_find_min(self.reverse_nums)
        self.assertEqual(min_num,min(self.reverse_nums))

        #边界测试
        nums = [1,0,1,1,1]
        min_num = book1.binary_find_min(nums)
        self.assertEqual(0,min_num)



if __name__ == '__main__':
    unittest.main()
