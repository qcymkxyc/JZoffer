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
from main.question9 import my1
from main.question9 import my2

class MSTest(unittest.TestCase):

    def setUp(self):
        self.queue = my1.Queue()
        self.stack = my2.Stack()

    def tearDown(self):
        pass

    def test_my1_add_element(self):
        """测试往队列中添加元素"""
        self.queue.push(1)
        self.queue.push(2)

        self.assertEqual(1,self.queue.pop())
        self.assertEqual(2,self.queue.pop())

    def test_my1_pop_empty_element(self):
        """测试pop空的队列"""
        with self.assertRaises(IndexError):
            self.queue.pop()

    ####################################################################
    #   以下为相关题目测试用例
    ####################################################################
    def test_my2_add_element(self):
        self.stack.push(1)
        self.stack.push(2)

        self.assertEqual(2,self.stack.pop())
        self.assertEqual(1,self.stack.pop())

    def test_my2_pop_empty_elment(self):

        print(my2.__doc__)
        with self.assertRaises(IndexError):
            self.stack.pop()

