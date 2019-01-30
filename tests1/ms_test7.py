#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
 @author:qcymkxyc
 @email:qcymkxyc@163.com
 @software: PyCharm
 @file: ms_test7.py
 @time: 2019/1/30 15:16

"""
import unittest
from main1.question7 import my1


class MSTestCase(unittest.TestCase):
    def test_my1_build_tree(self):
        pre_order = [1, 2, 4, 7, 3, 5, 6, 8]
        in_order = [4, 7, 2, 1, 5, 3, 6, 8]

        root = my1.build_tree(pre_order, in_order)
        self.assertEqual(pre_order, my1.pre_display(root))

        self.assertIsNone(my1.build_tree([], []))

        with self.assertRaises(ValueError):
            my1.build_tree([1, 2, 3], [])
            my1.build_tree(([1, 2, 3], [3, 4, 5]))


if __name__ == '__main__':
    unittest.main()
