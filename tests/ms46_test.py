#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
    @Time :    19-1-23 上午10:58
    @Author:  qcymkxyc
    @File: ms46_test.py
    @Software: PyCharm


"""
import unittest
from main.question46 import my1


class MSTestCase(unittest.TestCase):

    def test_my1_translate(self):
        count = my1.translate(12258)
        self.assertEqual(5, count)


if __name__ == '__main__':
    unittest.main()
