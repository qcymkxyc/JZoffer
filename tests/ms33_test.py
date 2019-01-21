#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 上午11:37
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : ms33_test.py
@Software: PyCharm

"""
import unittest
from main.question26 import my1 as q26
from main.question33 import my1, book1


class MSTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_post_display(self):
        pre_order = [8, 6, 5, 7, 10, 9, 11]
        in_order = [5, 6, 7, 8, 9, 10, 11]

        root = q26.create_binary_tree(pre_order, in_order)
        self.assertEqual([5, 7, 6, 9, 11, 10, 8], my1._post_display(root))

    def test_is_post_order(self):
        """判断是否是后序遍历"""
        pre_order = [8, 6, 5, 7, 10, 9, 11]
        in_order = [5, 6, 7, 8, 9, 10, 11]

        root = q26.create_binary_tree(pre_order, in_order)
        self.assertTrue(my1.is_post_order(root, [5, 7, 6, 9, 11, 10, 8]))

        # 仅有左子树
        pre_order = [1, 2, 3, 4, 5]
        in_order = [5, 4, 3, 2, 1]

        root = q26.create_binary_tree(pre_order, in_order)
        self.assertTrue(my1.is_post_order(root, [5, 4, 3, 2, 1]))

        # 仅有右子树
        pre_order = [1, 2, 3, 4, 5]
        in_order = [1, 2, 3, 4, 5]

        root = q26.create_binary_tree(pre_order, in_order)
        self.assertTrue(my1.is_post_order(root, [5, 4, 3, 2, 1]))

        # 根结点为空
        self.assertTrue(my1.is_post_order(None, []))

    def test_is_bst_post_seq(self):
        self.assertTrue(book1.is_bst_post_seq([5,7,6,9,11,10,8]))
        self.assertFalse(book1.is_bst_post_seq([7,4,6,5]))

        self.assertTrue(book1.is_bst_post_seq([]))


if __name__ == "__main__":
    unittest.main()
