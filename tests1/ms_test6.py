#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
    @Time :    19-1-29 上午11:26
    @Author:  qcymkxyc
    @File: ms_test6.py
    @Software: PyCharm


"""
import unittest
from main1.question6 import my1


class MSTestCase(unittest.TestCase):

    def setUp(self):
        self.create_LinkList()

    def create_LinkList(self):
        nums = list(range(5))
        self.linklist = my1.LinkList.create_link(nums)

    def test_reverse_display(self):
        self.assertEqual([4, 3, 2, 1, 0], my1.reverse_display(self.linklist))

        head = my1.LinkList.create_link([0])
        self.assertEqual([0], my1.reverse_display(head))

        self.assertEqual([], my1.reverse_display(None))


if __name__ == '__main__':
    unittest.main()
