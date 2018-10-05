#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 18-9-30 上午11:51
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : sort_test.py
@Software: PyCharm

排序算法测试
    
"""
import unittest
import random
import copy

from main.other import book_sort
from main.other import my_sort

class SortTest(unittest.TestCase):
    def setUp(self):
        self.nums = list(range(1,11))
        self.test_nums = copy.copy(self.nums)
        random.seed(1)
        #[7, 9, 10, 8, 6, 4, 1, 5, 2, 3]
        random.shuffle(self.test_nums)

    def tearDown(self):
        pass

# *********************************************************
# *     书上
# *********************************************************

    def test_book_quick_sort(self):
        """c"""
        book_sort.quick_sort(self.test_nums)
        self.assertEqual(self.test_nums,self.nums)

    def test_book_heap_sort(self):
        self.test_nums = book_sort.heap_sort(self.test_nums)
        self.assertEqual(self.test_nums,self.nums)

# ********************************************************
# *     我的
# ********************************************************

    def test_my_bubble_sort(self):
        """测试冒泡排序"""
        my_sort.bubble_sort(self.test_nums)
        self.assertEqual(self.test_nums,self.nums)

    def test_my_insert_sort(self):
        """测试插入排序"""
        my_sort.insert_sort(self.test_nums)
        self.assertEqual(self.test_nums,self.nums)

    def test_my_binary_search_sort(self):
        """测试二分插入排序"""
        my_sort.binary_insert_sort(self.test_nums)
        self.assertEqual(self.test_nums,self.nums)

    def test_my_merge_sort(self):
        """测试归并排序"""
        self.test_nums = my_sort.merge_sort(self.test_nums)
        self.assertEqual(self.test_nums,self.nums)

    def test_my_select_sort(self):
        """测试选择排序"""
        my_sort.select_sort(self.test_nums)
        self.assertEqual(self.test_nums,self.nums)

    def test_my_radix_sort1(self):
        """测试基数排序1"""
        self.test_nums = my_sort.radix_sort1(self.test_nums)
        self.assertEqual(self.test_nums,self.nums)

    def test_my_radix_sort2(self):
        """测试基数排序2"""
        self.test_nums = my_sort.radix_sort2(self.test_nums)
        self.assertEqual(self.test_nums,self.nums)

if __name__ == "__main__":
    unittest.main()

