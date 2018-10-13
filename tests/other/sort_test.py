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

from main.other.sort import book_sort, my_sort1,my_sort2


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
        my_sort1.bubble_sort(self.test_nums)
        self.assertEqual(self.test_nums,self.nums)

    def test_my_insert_sort(self):
        """测试插入排序"""
        my_sort1.insert_sort(self.test_nums)
        self.assertEqual(self.test_nums,self.nums)

    def test_my_binary_search_sort(self):
        """测试二分插入排序"""
        my_sort1.binary_insert_sort(self.test_nums)
        self.assertEqual(self.test_nums,self.nums)

    def test_my_merge_sort(self):
        """测试归并排序"""
        self.test_nums = my_sort1.merge_sort(self.test_nums)
        self.assertEqual(self.test_nums,self.nums)

    def test_my_select_sort(self):
        """测试选择排序"""
        my_sort1.select_sort(self.test_nums)
        self.assertEqual(self.test_nums,self.nums)

    def test_my_radix_sort1(self):
        """测试基数排序1"""
        self.test_nums = my_sort1.radix_sort1(self.test_nums)
        self.assertEqual(self.test_nums,self.nums)

    def test_my_radix_sort2(self):
        """测试基数排序2（链表实现）"""
        self.test_nums = my_sort1.radix_sort2(self.test_nums)
        self.assertEqual(self.test_nums,self.nums)

    def test_my_shell_sort(self):
        """测试希尔排序"""
        my_sort1.shell_sort(self.test_nums)
        self.assertEqual(self.test_nums,self.nums)

##########################################################################
#   第二次训练
##########################################################################
    def test_my2_insert_sort(self):
        """测试直接插入排序"""
        my_sort2.insert_sort(self.test_nums)
        self.assertEqual(self.nums, self.test_nums)

        # 本来就有序的情况
        nums = [1, 2, 3]
        my_sort2.insert_sort(nums)
        self.assertEqual([1, 2, 3], nums)

        # 需要插入到第一个元素之前的情况
        nums = [3, 2, 1]
        my_sort2.insert_sort(nums)
        self.assertEqual([1, 2, 3], nums)

    def test_my2_binary_sort(self):
        """测试二分插入排序"""
        my_sort2.binary_insert_sort(self.test_nums)
        self.assertEqual(self.test_nums, self.nums)


if __name__ == "__main__":
    unittest.main()

