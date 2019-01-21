#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 18-10-8 下午12:18
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : ms12_test.py
@Software: PyCharm
    
"""
import unittest

from main.question12 import my1

class MSTest(unittest.TestCase):
    def setUp(self):
        self.matrix = [
            "abtg",
            "cfcs",
            "jdeh"
        ]
        self.s = "abfd"


    def tearDown(self):
        pass

    def test_my_find_ch(self):
        str_path = my1.find_ch(self.matrix,0,self.s,(0,0))
        self.assertEqual([(0, 0), (1,0), (1, 1), (1, 2)], str_path)

    def test_my_find_path1(self):
        #能找到的情况
        str_path = my1.find_path1(self.matrix,self.s)
        self.assertEqual([(0, 0), (1, 0), (1, 1), (1, 2)], str_path)

        #不能找到的情况
        str_path = my1.find_path1(self.matrix,"abfe")
        self.assertEqual(None,str_path)

        #多个选择的情况
        str_path = my1.find_path1(self.matrix,"abfc")
        self.assertEqual([(0, 0), (1, 0), (1, 1), (0, 1)], str_path)

        #会路过已经走过的路
        str_path = my1.find_path1(self.matrix,"abfb")
        self.assertEqual(None,str_path)



if __name__ == "__main__":
    unittest.main()