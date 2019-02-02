#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
 @author:qcymkxyc
 @email:qcymkxyc@163.com
 @software: PyCharm
 @file: book2.py
 @time: 2019/2/2 15:43

"""
from main1.question9 import book1


class Stack:
    def __init__(self):
        self.queue1 = book1.Queue1()
        self.queue2 = book1.Queue1()

    def push(self, val):
        empty_queue = self.queue1 if len(self.queue1) == 0 else self.queue2
        other_queue = self.queue1 if empty_queue == self.queue2 else self.queue1

        other_queue.append_tail(val)

    def pop(self):
        if len(self.queue1) == 0 and len(self.queue2) == 0:
            raise ValueError("栈为空")

        empty_queue = self.queue1 if len(self.queue1) == 0 else self.queue2
        other_queue = self.queue1 if empty_queue == self.queue2 else self.queue2

        while len(other_queue) > 1:
            empty_queue.append_tail(other_queue.delete_head())

        return other_queue.delete_head()

    def __len__(self):
        return len(self.queue1) + len(self.queue2)
