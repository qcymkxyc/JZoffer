#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
    @Time :    19-1-12 上午11:35
    @Author:  qcymkxyc
    @File: DP_test.py
    @Software: PyCharm


"""
import unittest
from main.other.DP import question1, question2


class DPTestCase(unittest.TestCase):
    def test_question1_walk_way1(self):
        self.assertEqual(3,question1.walk_way1(3))
        self.assertEqual(21,question1.walk_way1(7))

    def test_question1_walk_way2(self):
        self.assertEqual(3, question1.walk_way2(3))
        self.assertEqual(21, question1.walk_way1(7))

    def test_question2_min_path(self):
        self.assertEqual(12, question2.min_path(question2.m))


if __name__ == '__main__':
    unittest.main()
