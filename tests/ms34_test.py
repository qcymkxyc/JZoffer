#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 上午11:43
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : ms34_test.py
@Software: PyCharm

"""
import unittest
from main.question34 import my1
from main.question26 import my1 as q26


class MSTestCase(unittest.TestCase):
    def setUp(self):
        pre_order = [10, 5, 4, 7, 12]
        in_order = [4, 5, 7, 10, 12]

        self.root = q26.create_binary_tree(pre_order, in_order)

    def test_my1_sum_display_path(self):
        sum_path = [
            [10, 5, 7],
            [10, 12]
        ]
        self.assertEqual(sum_path, my1.sum_display_path(self.root, 22))
        self.assertEqual([], my1.sum_display_path(self.root, 23))


if __name__ == "__main__":
    unittest.main()
