#!usr/bin/env python 
# -*- coding:utf-8 _*-  
""" 
 @author:qcymkxyc
 @email:qcymkxyc@163.com
 @software: PyCharm
 @file: ms.py
 @time: 2019/2/1 15:15
 
"""
import unittest
from main1.question8 import my1


class MSTestCase(unittest.TestCase):
    def setUp(self):
        self.pre_seq = [1,2,4,8,9,5,11,3,6,7]
        self.in_seq = [8,4,9,2,5,11,1,6,3,7]

        self.root = my1.create_binary_tree(self.pre_seq,self.in_seq)

    def test_display(self):
        self.assertEqual(self.pre_seq, my1.pre_display(self.root))
        self.assertEqual(self.in_seq, my1.in_display(self.root))

    def test_my1_in_order_next_node(self):
        next_node = my1.in_order_next_node(self.root)
        self.assertEqual(next_node.val, 3)

        c_node = self.root.left_child
        n_node = my1.in_order_next_node(c_node)
        self.assertEqual(5, n_node.val)

        c_node = self.root.left_child
        c_node = c_node.right_child
        c_node = c_node.right_child
        n_node = my1.in_order_next_node(c_node)
        self.assertEqual(1, n_node.val)

if __name__ == '__main__':
    unittest.main()
