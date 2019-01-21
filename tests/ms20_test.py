#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 18-10-23 上午11:04
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : ms20_test.py
@Software: PyCharm
    
"""
import unittest

from main.question20 import my1


class MSTestCase(unittest.TestCase):

    def test_my1_is_num(self):
        self.assertTrue(my1.is_num("+100"))
        self.assertTrue(my1.is_num("5e2"))
        self.assertTrue(my1.is_num("3.1416"))
        self.assertTrue(my1.is_num("-1E-16"))

        self.assertFalse(my1.is_num("12e"))
        self.assertFalse(my1.is_num("1a3.14"))
        self.assertFalse(my1.is_num("+-5"))
        self.assertFalse(my1.is_num("12e+5.4"))


if __name__ == "__main__":
    unittest.main()
