#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
 @author:qcymkxyc
 @email:qcymkxyc@163.com
 @software: PyCharm
 @file: book1.py
 @time: 2019/2/2 15:11

"""
from main1.question9 import my1


class Queue1(my1.Queue):
    def append_tail(self, val):
        self.stack1.push(val)

    def delete_head(self):
        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                val = self.stack1.pop()
                self.stack2.push(val)

        return self.stack2.pop()
