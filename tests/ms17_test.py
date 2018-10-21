#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 18-10-20 上午10:49
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : ms17_test.py
@Software: PyCharm
    
"""
import unittest

from main.question17 import my1, book1, book2


class MSTest(unittest.TestCase):

    def test_my1_order_display(self):
        # 功能
        self.assertEqual(my1.order_display(2), [i for i in range(1, 100)])

        # 负数情况
        self.assertEqual(my1.order_display(-2), [])
        # 0
        self.assertEqual(my1.order_display(0), [])

    def test_book1_increment(self):
        nums = ["006"]
        self.assertFalse(book1.increment(nums, 3))
        self.assertEqual(nums[-1], "007")

        nums = ["017"]
        self.assertFalse(book1.increment(nums, 3))
        self.assertEqual(nums[-1], "018")

        nums = ["99"]
        self.assertTrue(book1.increment(nums, 2))
        nums = ["39"]
        self.assertFalse(book1.increment(nums, 2))
        self.assertEqual(nums[-1], "40")

    def test_book1_order_display(self):
        self.assertEqual(book1.order_display(1), [str(i) for i in range(1, 10)])
        self.assertEqual(book1.order_display(2), [str(i) for i in range(1, 100)])

    def test_book2_order_display(self):
        self.assertEqual([str(i) for i in range(1, 10)], book2.order_display(1))
        self.assertEqual([str(i) for i in range(1, 100)], book2.order_display(2))


if __name__ == "__main__":
    unittest.main()
