#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 18-10-22 下午12:00
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : ms19_test.py
@Software: PyCharm
    
"""
import unittest

from main.question19 import my1


class MSTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_my1_regex_match(self):
        self.assertTrue(my1.regex_match("ab", "abcd"))
        self.assertTrue(my1.regex_match("bc", "abcd"))
        self.assertTrue(my1.regex_match("cd", "abcd"))

        self.assertFalse(my1.regex_match("ac", "abcd"))
        self.assertFalse(my1.regex_match("be", "abcd"))
        self.assertFalse(my1.regex_match("ce", "abcd"))


if __name__ == "__main__":
    unittest.main()