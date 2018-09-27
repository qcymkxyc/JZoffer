#!/usr/bin/python3
# coding=utf-8
"""

 @Time    : 18-9-27 上午10:39
 @Author  : qcymkxyc
 @Email   : qcymkxyc@163.com
 @File    : ms9_test.py
 @Software: PyCharm
    
"""
import unittest
from main.面试题9 import my1

class MSTest(unittest.TestCase):

    def setUp(self):
        self.queue = my1.Queue()

    def tearDown(self):
        pass

    def test_add_element(self):
        """测试往队列中添加元素"""
        self.queue.push(1)
        self.queue.push(2)

        self.assertEqual(1,self.queue.pop())
        self.assertEqual(2,self.queue.pop())

    def test_pop_empty_element(self):
        """测试pop空的队列"""
        with self.assertRaises(IndexError):
            self.queue.pop()

